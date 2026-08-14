// =========================
// Tag Detection
// =========================

function detectTags(question) {

    const tags = [];

    const tagKeywords = {

        "기획": [
            "기획",
            "게임 디자인",
            "게임디자인",
            "시스템",
            "컨셉",
            "콘텐츠"
        ],

        "Unity": [
            "unity",
            "유니티"
        ],

        "Unreal": [
            "unreal",
            "언리얼"
        ],

        "디버깅": [
            "버그",
            "오류",
            "에러",
            "debug",
            "디버깅",
            "exception",
            "error"
        ],

        "최적화": [
            "최적화",
            "optimization",
            "performance",
            "성능",
            "프레임",
            "fps"
        ],

        "밸런스": [
            "밸런스",
            "밸런싱",
            "balance",
            "난이도"
        ],

        "UI/UX": [
            "ui",
            "ux",
            "인터페이스",
            "사용자 경험"
        ],

        "Steam": [
            "steam",
            "스팀",
            "출시"
        ],

        "마케팅": [
            "마케팅",
            "홍보",
            "marketing",
            "광고"
        ],

        "멀티플레이": [
            "멀티",
            "멀티플레이",
            "multiplayer",
            "네트워크",
            "network"
        ],

        "아이디어": [
            "아이디어",
            "아이디어 보강",
            "추가",
            "개선",
            "발전"
        ]

    };

    const lowerQuestion = question.toLowerCase();

    for (const [tag, keywords] of Object.entries(tagKeywords)) {

        const matched = keywords.some(keyword =>
            lowerQuestion.includes(keyword.toLowerCase())
        );

        if (matched) {
            tags.push(tag);
        }

    }

    // 아무 태그도 찾지 못한 경우
    if (tags.length === 0) {
        tags.push("기타");
    }

    return tags;
}


// =========================
// Mentor
// =========================

document
    .getElementById("mentor-btn")
    .addEventListener("click", async () => {

        const question =
            document.getElementById("mentor-question").value.trim();

        const mentorButton =
            document.getElementById("mentor-btn");

        const mentorResult =
            document.getElementById("mentor-result");

        const mentorAnswer =
            document.getElementById("mentor-answer");


        if (question === "") {

            alert("Please enter a question.");
            return;

        }


        // 생성 중 상태
        mentorButton.disabled = true;
        mentorButton.textContent = "Generating...";


        try {

            const response = await fetch(
    "/api/mentor",
    {
        method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        question: question
                    })

                }
            );


            if (!response.ok) {
                throw new Error(
                    `Server error: ${response.status}`
                );
            }


            const result =
                await response.json();


            mentorResult.classList.remove("hidden");


            mentorAnswer.innerHTML =
                `<pre>${escapeHtml(result.result || "")}</pre>`;


        } catch (error) {

            console.error(error);

            alert("Mentor request failed.");

        } finally {

            // 버튼 원상복구
            mentorButton.disabled = false;
            mentorButton.textContent = "Ask Mentor";

        }

    });


// =========================
// Quick Questions
// =========================

const quickQuestionButtons =
    document.querySelectorAll(".quick-question-btn");

const mentorQuestion =
    document.getElementById("mentor-question");


quickQuestionButtons.forEach(button => {

    button.addEventListener("click", () => {

        mentorQuestion.value =
            button.dataset.question;

        mentorQuestion.focus();

    });

});


// =========================
// Copy Mentor Answer
// =========================

document
    .getElementById("copy-btn")
    .addEventListener("click", async () => {

        const answer =
            document
                .getElementById("mentor-answer")
                .innerText
                .trim();


        if (!answer) {

            alert("복사할 답변이 없습니다.");
            return;

        }


        try {

            await navigator.clipboard.writeText(answer);

            alert("답변이 복사되었습니다.");

        } catch (error) {

            console.error(error);

            // Clipboard API가 실패할 경우
            const textarea =
                document.createElement("textarea");

            textarea.value = answer;

            document.body.appendChild(textarea);

            textarea.select();

            document.execCommand("copy");

            textarea.remove();

            alert("답변이 복사되었습니다.");

        }

    });


// =========================
// Save Mentor Answer
// =========================

document
    .getElementById("save-btn")
    .addEventListener("click", () => {

        const question =
            document
                .getElementById("mentor-question")
                .value
                .trim();


        const answer =
            document
                .getElementById("mentor-answer")
                .innerText
                .trim();


        if (!question) {

            alert("저장할 질문이 없습니다.");
            return;

        }


        if (!answer) {

            alert("저장할 답변이 없습니다.");
            return;

        }


        const savedAdvice =
            JSON.parse(
                localStorage.getItem("savedAdvice") || "[]"
            );


        // 질문을 기준으로 태그 자동 생성
        const tags =
            detectTags(question);


        savedAdvice.push({

            question: question,

            answer: answer,

            tags: tags,

            date: new Date().toLocaleString()

        });


        localStorage.setItem(
            "savedAdvice",
            JSON.stringify(savedAdvice)
        );


        alert("답변이 저장되었습니다.");


        // 현재 선택된 필터 유지
        const activeFilter =
            document.querySelector(".tag-filter.active");


        const selectedTag =
            activeFilter
                ? activeFilter.dataset.tag
                : "all";


        renderFilteredAdvice(selectedTag);

    });


// =========================
// Render Saved Advice
// =========================

function renderSavedAdvice(savedAdvice, originalIndices = []) {

    const savedAdviceList =
        document.getElementById("saved-advice-list");


    if (savedAdvice.length === 0) {

        savedAdviceList.innerHTML = `
            <div class="empty-advice">
                해당 태그의 저장된 조언이 없습니다.
            </div>
        `;

        return;

    }


    savedAdviceList.innerHTML = "";


    savedAdvice.forEach((advice, index) => {

        const card =
            document.createElement("div");


        card.className =
            "saved-advice-card";


        const tags =
            advice.tags || ["기타"];


        const tagHTML =
            tags.map(tag => `
                <span class="saved-tag">
                    ${escapeHtml(tag)}
                </span>
            `).join("");


        // 필터링된 목록에서도 원래 localStorage의 index를 유지
        const actualIndex =
            originalIndices.length > 0
                ? originalIndices[index]
                : index;


        card.innerHTML = `

            <div class="saved-advice-question">
                ${escapeHtml(advice.question)}
            </div>

            <div class="saved-advice-date">
                ${escapeHtml(advice.date)}
            </div>

            <div class="saved-tags">
                ${tagHTML}
            </div>

            <div class="saved-advice-answer">
                ${escapeHtml(advice.answer)}
            </div>

            <div class="saved-advice-actions">

                <button
                    class="delete-advice-btn"
                    data-index="${actualIndex}">
                    Delete
                </button>

            </div>

        `;


        savedAdviceList.appendChild(card);

    });


    // =========================
    // 답변 펼치기 / 접기
    // =========================

    document
        .querySelectorAll(".saved-advice-answer")
        .forEach(answer => {

            answer.addEventListener("click", () => {

                answer.classList.toggle("expanded");

            });

        });


    // =========================
    // Delete
    // =========================

    document
        .querySelectorAll(".delete-advice-btn")
        .forEach(button => {

            button.addEventListener("click", () => {

                const index =
                    Number(button.dataset.index);

                deleteSavedAdvice(index);

            });

        });

}


// =========================
// Load Saved Advice
// =========================

function loadSavedAdvice() {

    renderFilteredAdvice("all");

}


// =========================
// Filter Saved Advice
// =========================

function renderFilteredAdvice(selectedTag) {

    const savedAdvice =
        JSON.parse(
            localStorage.getItem("savedAdvice") || "[]"
        );


    if (selectedTag === "all") {

        renderSavedAdvice(savedAdvice);

        return;

    }


    const filteredAdvice = [];

    const originalIndices = [];


    savedAdvice.forEach((advice, index) => {

        const tags =
            advice.tags || ["기타"];


        if (tags.includes(selectedTag)) {

            filteredAdvice.push(advice);

            originalIndices.push(index);

        }

    });


    renderSavedAdvice(
        filteredAdvice,
        originalIndices
    );

}


// =========================
// Tag Filter
// =========================

// HTML의 실제 클래스는 .tag-filter
const filterButtons =
    document.querySelectorAll(".tag-filter");


filterButtons.forEach(button => {

    button.addEventListener("click", () => {

        const selectedTag =
            button.dataset.tag;


        // 선택된 버튼 표시
        filterButtons.forEach(btn => {

            btn.classList.remove("active");

        });


        button.classList.add("active");


        renderFilteredAdvice(selectedTag);

    });

});


// =========================
// Delete Saved Advice
// =========================

function deleteSavedAdvice(index) {

    const savedAdvice =
        JSON.parse(
            localStorage.getItem("savedAdvice") || "[]"
        );


    if (
        index < 0 ||
        index >= savedAdvice.length
    ) {
        return;
    }


    savedAdvice.splice(index, 1);


    localStorage.setItem(
        "savedAdvice",
        JSON.stringify(savedAdvice)
    );


    // 현재 필터 유지
    const activeFilter =
        document.querySelector(".tag-filter.active");


    const selectedTag =
        activeFilter
            ? activeFilter.dataset.tag
            : "all";


    renderFilteredAdvice(selectedTag);

}


// =========================
// HTML Escape
// =========================

function escapeHtml(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}


// =========================
// Initial Load
// =========================

loadSavedAdvice();