document
.getElementById("mentor-btn")
.addEventListener("click", async () => {

    const question =
        document.getElementById("mentor-question").value;

    if(question.trim()===""){

        alert("Please enter a question.");
        return;

    }

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/mentor",
            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    question:question

                })

            }

        );

        const result =
            await response.json();

        document
            .getElementById("mentor-result")
            .classList.remove("hidden");

        document
            .getElementById("mentor-answer")
            .innerHTML =

`<pre>${result.result}</pre>`;

    }

    catch(error){

        console.error(error);

        alert("Mentor request failed.");

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
// Save Mentor Answer
// =========================

document
    .getElementById("save-btn")
    .addEventListener("click", () => {

        const question =
            document.getElementById("mentor-question").value.trim();

        const answer =
            document.getElementById("mentor-answer").innerText.trim();

        if (!answer) {

            alert("저장할 답변이 없습니다.");

            return;

        }

        const savedAdvice =
            JSON.parse(
                localStorage.getItem("savedAdvice") || "[]"
            );

        savedAdvice.push({

            question: question,

            answer: answer,

            date: new Date().toLocaleString()

        });

        localStorage.setItem(
            "savedAdvice",
            JSON.stringify(savedAdvice)
        );

        alert("답변이 저장되었습니다.");

    });

// =========================
// Saved Advice
// =========================

function loadSavedAdvice() {

    const savedAdviceList =
        document.getElementById("saved-advice-list");

    const savedAdvice =
        JSON.parse(
            localStorage.getItem("savedAdvice") || "[]"
        );

    if (savedAdvice.length === 0) {

        savedAdviceList.innerHTML = `
            <div class="empty-advice">
                아직 저장된 조언이 없습니다.
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

        card.innerHTML = `

            <div class="saved-advice-question">
                ${escapeHtml(advice.question)}
            </div>

            <div class="saved-advice-date">
                ${advice.date}
            </div>

            <div class="saved-advice-answer">
                ${escapeHtml(advice.answer)}
            </div>

            <div class="saved-advice-actions">

                <button
                    class="delete-advice-btn"
                    data-index="${index}">
                    Delete
                </button>

            </div>

        `;

        savedAdviceList.appendChild(card);

    });


    // 답변 클릭 → 펼치기 / 접기

    document
        .querySelectorAll(".saved-advice-answer")
        .forEach(answer => {

            answer.addEventListener("click", () => {

                answer.classList.toggle("expanded");

            });

        });


    // 삭제

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
// Delete Saved Advice
// =========================

function deleteSavedAdvice(index) {

    const savedAdvice =
        JSON.parse(
            localStorage.getItem("savedAdvice") || "[]"
        );

    savedAdvice.splice(index, 1);

    localStorage.setItem(
        "savedAdvice",
        JSON.stringify(savedAdvice)
    );

    loadSavedAdvice();

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


// 처음 페이지에 들어왔을 때 저장된 답변 불러오기

loadSavedAdvice();    