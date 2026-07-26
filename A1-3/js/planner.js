const selectedOptions = {};
async function loadPlannerOptions() {

    const response = await fetch("data/planner-options.json");

    const data = await response.json();

    createOptionSection(data);

}

loadPlannerOptions();

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

function formatTitle(text) {

    return text
        .replace(/([A-Z])/g, " $1")
        .replace(/^./, char => char.toUpperCase());

}

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

function collectPlannerData(){

    selectedOptions.concept =
        document.getElementById("concept").value;

    selectedOptions.story =
        document.getElementById("story").value;

    selectedOptions.reference =
        document.getElementById("reference").value;

    selectedOptions.request =
        document.getElementById("request").value;

}


document
.getElementById("generate-btn")
.addEventListener("click", () => {

    collectPlannerData();

    renderPreview();

});

function renderPreview() {

    const container = document.getElementById("result-container");
    const content = document.getElementById("result-content");

    container.classList.remove("hidden");

    const prompt = buildPrompt();

    content.innerHTML = `
        <div class="result-content-section">
            <h3>Prompt Preview</h3>
            <pre>${prompt}</pre>
        </div>
    `;
}


function buildPrompt() {

    return `
Create a detailed game design document based on the following requirements.

Genre:
${selectedOptions.genre?.join(", ") || "None"}

Game Features:
${selectedOptions.features?.join(", ") || "None"}

Game Mode:
${selectedOptions.mode?.join(", ") || "None"}

Perspective:
${selectedOptions.perspective?.join(", ") || "None"}

Mood:
${selectedOptions.mood?.join(", ") || "None"}

Art Style:
${selectedOptions.artStyle?.join(", ") || "None"}

Platform:
${selectedOptions.platform?.join(", ") || "None"}

Core Mechanics:
${selectedOptions.mechanics?.join(", ") || "None"}

Game Concept:
${selectedOptions.concept || ""}

Story / Background:
${selectedOptions.story || ""}

Reference Games:
${selectedOptions.reference || ""}

Additional Requests:
${selectedOptions.request || ""}
`;
}