document.addEventListener("DOMContentLoaded", () => {
    const navItems = document.querySelectorAll(".nav-links li");
    const sections = document.querySelectorAll(".page-section");

    // 탭 클릭 이벤트 리스너
    navItems.forEach(item => {
        item.addEventListener("click", () => {
            // 1. 모든 메뉴의 active 클래스 제거
            navItems.forEach(nav => nav.classList.remove("active"));
            // 2. 모든 섹션 숨기기
            sections.forEach(sec => sec.classList.remove("active"));
            
            // 3. 클릭한 메뉴 활성화
            item.classList.add("active");
            
            // 4. 클릭한 메뉴의 data-target과 일치하는 ID를 가진 섹션 활성화
            const targetId = item.getAttribute("data-target");
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.classList.add("active");
            }
        });
    });
    // Summary API 호출 및 데이터 주입 로직
    async function loadSummaryData() {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/data/summary");
            const data = await response.json();

            if (data.metrics) {
                document.getElementById("summary-avg").textContent = `$${data.metrics.average}`;
                document.getElementById("summary-max").textContent = `$${data.metrics.max}`;
                document.getElementById("summary-min").textContent = `$${data.metrics.min}`;
            }
        } catch (error) {
            console.error("데이터 로드 실패:", error);
        }
    }

    // 앱 로드 시 최초 1회 실행
    loadSummaryData();
});

// --- Data 탭 관리 로직 ---
const dataListContainer = document.getElementById("data-list");
const modalOverlay = document.getElementById("add-modal");
const openModalBtn = document.getElementById("open-modal-btn");
const closeModalBtn = document.getElementById("close-modal-btn");
const cancelBtn = document.getElementById("cancel-btn");
const addDataForm = document.getElementById("add-data-form");

// 1. Data 목록 불러오기 및 렌더링
async function loadPriceData() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/data");
        const items = await response.json();

        dataListContainer.innerHTML = "";

        items.forEach(item => {
            const row = document.createElement("div");
            row.className = "data-row";
            
            row.innerHTML = `
                <div class="data-summary-bar">
                    <span>${item.date || "날짜 없음"}</span>
                    <span style="color: var(--accent-color); font-weight: bold;">$${item.value}</span>
                    <span style="color: var(--text-secondary);">${item.memo || "NVIDIA"}</span>
                </div>
                <div class="data-details">
                    <p><strong>Volume:</strong> ${item.volume || 0}</p>
                    <p><strong>Open:</strong> $${item.open || 0} | <strong>High:</strong> $${item.high || 0} | <strong>Low:</strong> $${item.low || 0}</p>
                    <div style="display: flex; gap: 8px; margin-top: 12px;">
                        <button class="delete-btn" data-id="${item.id}" style="background-color: #ff4444; color: white;">Delete</button>
                    </div>
                </div>
            `;

            // 아코디언 토글 기능 (상세 바 클릭 시 열림/닫힘)
            const summaryBar = row.querySelector(".data-summary-bar");
            summaryBar.addEventListener("click", () => {
                row.classList.toggle("active");
            });

            // 삭제 버튼 기능
            const deleteBtn = row.querySelector(".delete-btn");
            deleteBtn.addEventListener("click", async (e) => {
                e.stopPropagation(); // 아코디언 열림 방지
                if (confirm("정말 이 데이터를 삭제하시겠습니까?")) {
                    await deleteData(item.id);
                }
            });

            dataListContainer.appendChild(row);
        });
    } catch (error) {
        console.error("데이터 목록 로드 실패:", error);
    }
}

// 2. 데이터 삭제 함수
async function deleteData(id) {
    try {
        await fetch(`http://127.0.0.1:8000/api/data/${id}`, {
            method: "DELETE"
        });
        loadPriceData(); // 목록 새로고침
    } catch (error) {
        console.error("삭제 실패:", error);
    }
}

// 3. 모달 제어 (열기/닫기)
openModalBtn.addEventListener("click", () => modalOverlay.classList.add("active"));
closeModalBtn.addEventListener("click", () => modalOverlay.classList.remove("active"));
cancelBtn.addEventListener("click", () => modalOverlay.classList.remove("active"));

// 4. 새 데이터 추가 (POST) 폼 제출
addDataForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const newData = {
        date: document.getElementById("input-date").value,
        value: parseFloat(document.getElementById("input-value").value),
        volume: 1000000, // 기본값 설정
        open: parseFloat(document.getElementById("input-value").value),
        high: parseFloat(document.getElementById("input-value").value),
        low: parseFloat(document.getElementById("input-value").value),
        memo: document.getElementById("input-memo").value || "사용자 추가 데이터"
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/data", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newData)
        });

        if (response.ok) {
            modalOverlay.classList.remove("active");
            addDataForm.reset();
            loadPriceData(); // 목록 갱신
        } else {
            alert("데이터 추가에 실패했습니다.");
        }
    } catch (error) {
        console.error("추가 요청 에러:", error);
    }
});

// 페이지 진입 시 Data 목록 로드 함수 호출 연결
document.querySelector('[data-target="data"]').addEventListener("click", () => {
    loadPriceData();
});

// --- AI Chat 탭 관리 로직 ---
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatMessages = document.getElementById("chat-messages");
const chatLoading = document.getElementById("chat-loading");

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const userText = chatInput.value.trim();
    if (!userText) return;

    // 1. 사용자 메시지 화면에 추가
    appendMessage(userText, "user-message", "You");
    chatInput.value = "";
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // 2. 로딩 표시 켜기
    chatLoading.style.display = "block";

    try {
        // 3. 백엔드 /api/chat 호출
        const response = await fetch("http://127.0.0.1:8000/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userText })
        });

        const data = await response.json();

        // 4. 로딩 표시 끄기 및 AI 답변 추가
        chatLoading.style.display = "none";
        if (data.reply) {
            appendMessage(data.reply, "ai-message", "✦ StockMate AI");
        } else {
            appendMessage("답변을 불러오지 못했습니다.", "ai-message", "✦ StockMate AI");
        }
    } catch (error) {
        chatLoading.style.display = "none";
        console.error("채팅 통신 에러:", error);
        appendMessage("서버와의 통신 중 오류가 발생했습니다.", "ai-message", "✦ StockMate AI");
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
});

function appendMessage(text, className, senderName) {
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${className}`;
    
    msgDiv.innerHTML = `
        <div class="message-sender">${senderName}</div>
        <div class="message-bubble">${text.replace(/\n/g, '<br>')}</div>
    `;
    
    chatMessages.appendChild(msgDiv);
}

// --- History 탭 관리 로직 ---
const historyListContainer = document.getElementById("history-list");

async function loadConversations() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/conversations");
        const conversations = await response.json();

        historyListContainer.innerHTML = "";

        if (conversations.length === 0) {
            historyListContainer.innerHTML = `<p style="color: var(--text-secondary);">저장된 대화 기록이 없습니다.</p>`;
            return;
        }

        conversations.forEach((conv, index) => {
            const row = document.createElement("div");
            row.className = "data-row"; // 기존 Data 탭의 아코디언 스타일 재사용
            
            // 첫 번째 질문 내용을 제목으로 요약 사용
            const firstMsg = conv.messages && conv.messages.length > 0 ? conv.messages[0].content : "대화 내용";
            const msgCount = conv.messages ? conv.messages.length : 0;
            const timeStr = conv.timestamp ? conv.timestamp.replace("T", " ").substring(0, 16) : "";

            // 메시지 목록 HTML 생성
            let messagesHtml = "";
            if (conv.messages) {
                conv.messages.forEach(m => {
                    const isUser = m.role === "user";
                    messagesHtml = messagesHtml + `
                        <div style="margin-bottom: 12px; text-align: ${isUser ? 'right' : 'left'};">
                            <span style="font-size: 0.75rem; color: var(--text-secondary); display: block; margin-bottom: 2px;">${isUser ? 'You' : 'StockMate AI'}</span>
                            <div style="display: inline-block; padding: 10px 14px; border-radius: 10px; background-color: ${isUser ? 'var(--accent-color)' : ' var(--card-bg)'}; color: ${isUser ? '#000' : 'var(--text-main)'}; text-align: left; max-width: 85%; font-size: 0.9rem;">
                                ${m.content.replace(/\n/g, '<br>')}
                            </div>
                        </div>
                    `;
                });
            }

            row.innerHTML = `
                <div class="data-summary-bar">
                    <div>
                        <span style="font-weight: 500; color: var(--text-main);">✦ ${firstMsg}</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 4px;">${timeStr} · ${msgCount} messages</div>
                    </div>
                    <span style="color: var(--text-secondary);">›</span>
                </div>
                <div class="data-details">
                    ${messagesHtml}
                </div>
            `;

            // 아코디언 토글
            const summaryBar = row.querySelector(".data-summary-bar");
            summaryBar.addEventListener("click", () => {
                row.classList.toggle("active");
            });

            historyListContainer.appendChild(row);
        });
    } catch (error) {
        console.error("대화 기록 로드 실패:", error);
    }
}

// History 탭을 누를 때마다 목록 최신화
document.querySelector('[data-target="history"]').addEventListener("click", () => {
    loadConversations();
});