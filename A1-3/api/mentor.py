import os

from flask import Flask, request, jsonify
from openai import OpenAI


app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")


def ask_game_mentor(question):

    system_prompt = """
You are a senior game development mentor with expertise in:

- Game Design
- Unity
- Unreal Engine
- Programming
- Debugging
- Performance Optimization
- UI/UX
- Steam Publishing
- Marketing
- Multiplayer
- Indie Game Development

Provide practical, detailed and constructive advice.

Analyze the user's question from the perspective of
game development and give advice that can actually be applied.

Always answer in the same language as the user's question.

Do not add unnecessary greetings or introductions.
"""

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.output_text


@app.route("/", methods=["POST"])
def mentor():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request data is required"
            }), 400

        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "error": "Question is required"
            }), 400

        result = ask_game_mentor(question)

        return jsonify({
            "result": result
        })

    except Exception as e:

        print("Mentor API Error:", e)

        return jsonify({
            "error": "Failed to generate mentor response"
        }), 500