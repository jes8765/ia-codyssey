const selectedOptions = {};
console.log("NEW planner.js loaded");

// ===============================
// Load Planner Options
// ===============================

async function loadPlannerOptions() {

    const response = await fetch("data/planner-options.json");
    const data = await response.json();

    createOptionSection(data);

}

loadPlannerOptions();

// ===============================
// Create Option Buttons
// ===============================

function createOptionSection(data) {

    const container = document.getElementById("planner-container");

    container.innerHTML = "";

    for (const category in data) {

        const section = document.createElement("div");
        section.className = "option-group";

        const title = document.createElement("h2");
        title.textContent = formatTitle(category);

        const buttonContainer = document.createElement("div");
        buttonContainer.className = "option-buttons";

        data[category].forEach(option => {

            const button = document.createElement("button");

            button.className = "option-btn";
            button.textContent = option;

            button.addEventListener("click", () => {

                button.classList.toggle("selected");

                updateSelection(category, option);

            });

            buttonContainer.appendChild(button);

        });

        section.appendChild(title);
        section.appendChild(buttonContainer);

        container.appendChild(section);

    }

}

// ===============================
// Title Format
// ===============================

function formatTitle(text) {

    return text
        .replace(/([A-Z])/g, " $1")
        .replace(/^./, char => char.toUpperCase());

}

// ===============================
// Save Selected Options
// ===============================

function updateSelection(category, option) {

    if (!selectedOptions[category]) {

        selectedOptions[category] = [];

    }

    const index = selectedOptions[category].indexOf(option);

    if (index === -1) {

        selectedOptions[category].push(option);

    } else {

        selectedOptions[category].splice(index, 1);

    }

    console.log(selectedOptions);

}

// ===============================
// Collect Textarea Data
// ===============================

function collectPlannerData() {

    selectedOptions.concept =
        document.getElementById("concept").value;

    selectedOptions.story =
        document.getElementById("story").value;

    selectedOptions.reference =
        document.getElementById("reference").value;

    selectedOptions.request =
        document.getElementById("request").value;

}

// ===============================
// Preview
// ===============================

document
    .getElementById("preview-btn")
    .addEventListener("click", () => {

        collectPlannerData();

        renderPreview();

    });

// ===============================
// Generate AI
// ===============================

document
.getElementById("generate-btn")
.addEventListener("click", async () => {

    collectPlannerData();

    setGenerating(true);

    // AI 호출 예정
    try {

    const response = await fetch("http://127.0.0.1:5000/generate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(selectedOptions)

    });

    const result = await response.json();

const container = document.getElementById("ai-result-container");
const content = document.getElementById("ai-result-content");

console.log(container);
console.log(content);

container.classList.remove("hidden");

content.innerHTML = `
<div class="ai-result">
<pre>${result.result}</pre>
</div>
`;

}
catch(error){

    console.error(error);

    alert("AI 호출에 실패했습니다.");

}
finally{

    setGenerating(false);

}

});

// ===============================
// Render Preview
// ===============================

function renderPreview() {

    const container = document.getElementById("result-container");
    const content = document.getElementById("result-content");

    container.classList.remove("hidden");

    content.innerHTML = `

        ${createSection("Genre", selectedOptions.genre)}
        ${createSection("Game Features", selectedOptions.features)}
        ${createSection("Game Mode", selectedOptions.mode)}
        ${createSection("Perspective", selectedOptions.perspective)}
        ${createSection("Mood", selectedOptions.mood)}
        ${createSection("Art Style", selectedOptions.artStyle)}
        ${createSection("Platform", selectedOptions.platform)}
        ${createSection("Core Mechanics", selectedOptions.mechanics)}

        ${createTextSection("Game Concept", selectedOptions.concept)}
        ${createTextSection("Story / Background", selectedOptions.story)}
        ${createTextSection("Reference Games", selectedOptions.reference)}
        ${createTextSection("Additional Requests", selectedOptions.request)}

    `;

}

// ===============================
// Helpers
// ===============================

function createSection(title, values) {

    if (!values || values.length === 0) {

        return "";

    }

    return `

        <div class="result-content-section">

            <h3>${title}</h3>

            <p>${values.join(", ")}</p>

        </div>

    `;

}

function createTextSection(title, text) {

    if (!text || text.trim() === "") {

        return "";

    }

    return `

        <div class="result-content-section">

            <h3>${title}</h3>

            <p>${text}</p>

        </div>

    `;

}


function setGenerating(isGenerating) {

    const button = document.getElementById("generate-btn");
    const loading = document.getElementById("loading-message");

    if (isGenerating) {

        button.disabled = true;
        button.textContent = "Generating...";

        if (loading) {
            loading.classList.remove("hidden");
        }

    } else {

        button.disabled = false;
        button.textContent = "Generate with AI";

        if (loading) {
            loading.classList.add("hidden");
        }

    }

}