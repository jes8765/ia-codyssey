console.log("Resources Loaded");

let resourcesData = {};

// =========================
// Load JSON
// =========================

async function loadResources() {

    const response = await fetch("data/sites.json");

    resourcesData = await response.json();

    console.log(resourcesData);

    createMainCategories();

}

loadResources();

const displayNames = {

    AI: "AI",

    GameAsset: "Assets",

    Fonts: "Fonts",

    Image: "Images",

    OutSource: "Outsource",

    Funding: "Funding",

    SNS: "Community",

    Learn: "Learning",

    GameDownloadPlatform: "Platforms",

    "Contest/Jam": "Contest"

};

function createMainCategories(){

    const container =
        document.getElementById("category-container");

    container.innerHTML = "";

    for(const category in resourcesData){

        const button =
            document.createElement("button");

        button.className = "category-btn";

        button.textContent =
            displayNames[category] || category;

        button.addEventListener("click", () => {

    document
        .querySelectorAll(".category-btn")
        .forEach(btn => btn.classList.remove("selected"));

    button.classList.add("selected");

    createSubCategories(category);

    createResourceCards(category);

});

        container.appendChild(button);

    }

}

function createSubCategories(category){

    const container =
        document.getElementById("subcategory-container");

    container.innerHTML = "";

    const data = resourcesData[category];

    if(!data){
        return;
    }

    // All 버튼

    const allButton =
        document.createElement("button");

    allButton.className = "category-btn selected";

    allButton.textContent = "All";
allButton.addEventListener("click",()=>{

    document
    .querySelectorAll("#subcategory-container .category-btn")
    .forEach(btn=>btn.classList.remove("selected"));

    allButton.classList.add("selected");

    createResourceCards(category);

});

    container.appendChild(allButton);

    for(const subCategory in data){

        const button =
            document.createElement("button");

        button.className = "category-btn";

        button.textContent = subCategory;

        button.addEventListener("click",()=>{

            document
.querySelectorAll("#subcategory-container .category-btn")
.forEach(btn=>btn.classList.remove("selected"));

button.classList.add("selected");

createResourceCards(category, subCategory);

        });

        container.appendChild(button);

    }

}

function createResourceCards(category, subCategory = "All"){

    const container =
        document.getElementById("resource-container");

    container.innerHTML = "";

    const categoryData =
        resourcesData[category];

    if(!categoryData) return;

    // All이면 모든 사이트 출력
    if(subCategory === "All"){

        for(const key in categoryData){

            createCards(categoryData[key], container);

        }

        return;

    }

    createCards(categoryData[subCategory], container);

}

function createCards(data, container){

    if(!Array.isArray(data)) return;

    data.forEach(site=>{

        const card =
            document.createElement("div");

        card.className = "resource-card";

        card.innerHTML = `

            <h3>${site.name}</h3>

            <p class="resource-price">
                ${site.price}
            </p>

            <p class="resource-description">
                ${site.description}
            </p>

            <a
                href="${site.url}"
                target="_blank"
                class="visit-btn">

                Visit

            </a>

        `;

        container.appendChild(card);

    });

}