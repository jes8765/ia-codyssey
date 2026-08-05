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

    // 기본 입력

    selectedOptions.concept =
        document.getElementById("concept").value;

    selectedOptions.story =
        document.getElementById("story").value;

    selectedOptions.reference =
        document.getElementById("reference").value;

    selectedOptions.request =
        document.getElementById("request").value;


    // Advanced Options

    selectedOptions.customGenre =
        document.getElementById("custom-genre").value;

    selectedOptions.customFeatures =
        document.getElementById("custom-features").value;

    selectedOptions.customMechanics =
        document.getElementById("custom-mechanics").value;

    selectedOptions.customMood =
        document.getElementById("custom-mood").value;

    selectedOptions.customArtStyle =
        document.getElementById("custom-artstyle").value;

    selectedOptions.customPlatform =
        document.getElementById("custom-platform").value;

    console.log(selectedOptions);

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

    ${createSection(
    "Genre",
    selectedOptions.genre,
    selectedOptions.customGenre
)}

${createSection(
    "Game Features",
    selectedOptions.features,
    selectedOptions.customFeatures
)}

${createSection(
    "Game Mode",
    selectedOptions.mode
)}

${createSection(
    "Perspective",
    selectedOptions.perspective
)}

${createSection(
    "Mood",
    selectedOptions.mood,
    selectedOptions.customMood
)}

${createSection(
    "Art Style",
    selectedOptions.artStyle,
    selectedOptions.customArtStyle
)}

${createSection(
    "Platform",
    selectedOptions.platform,
    selectedOptions.customPlatform
)}

${createSection(
    "Core Mechanics",
    selectedOptions.mechanics,
    selectedOptions.customMechanics
)}

${createTextSection("Game Concept", selectedOptions.concept)}
${createTextSection("Story / Background", selectedOptions.story)}
${createTextSection("Reference Games", selectedOptions.reference)}
${createTextSection("Additional Requests", selectedOptions.request)}

`;

}

// ===============================
// Helpers
// ===============================

function createSection(title, values, custom) {

    const items = [];

    if (values && values.length > 0) {
        items.push(...values);
    }

    if (custom && custom.trim() !== "") {
        items.push(custom);
    }

    if (items.length === 0) {
        return "";
    }

    return `
        <div class="result-content-section">
            <h3>${title}</h3>
            <p>${items.join(", ")}</p>
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

const toggle =
document.getElementById("advanced-toggle");

const advanced =
document.getElementById("advanced-options");

toggle.addEventListener("click",()=>{

    advanced.classList.toggle("hidden");

    if(advanced.classList.contains("hidden")){

        toggle.textContent="▼ Advanced Options";

    }

    else{

        toggle.textContent="▲ Advanced Options";

    }

});