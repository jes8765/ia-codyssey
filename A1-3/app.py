from flask import Flask, request
from flask_cors import CORS
from openai_service import generate_game_plan

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "GameForge AI Backend Running!"


@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    result = generate_game_plan(data)

    return {
        "result": result
    }

@app.route("/mentor", methods=["POST"])
def mentor():

    data = request.json

    question = data.get("question", "")

    result = ask_game_mentor(question)

    return jsonify({
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)