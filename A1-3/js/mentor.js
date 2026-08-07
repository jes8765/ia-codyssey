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