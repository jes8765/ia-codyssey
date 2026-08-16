import os

from flask import Flask, request, jsonify
from openai import OpenAI

from openai_service import generate_game_plan, ask_game_mentor


app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return jsonify({
        "status": "ok",
        "message": "GameForge AI API is running"
    })


# =========================
# Planner API
# =========================

@app.route("/planner", methods=["POST"])
def planner():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request data is required"
            }), 400

        result = generate_game_plan(data)

        return jsonify({
            "result": result
        })

    except Exception as e:

        print("Planner API Error:", e)

        return jsonify({
            "error": "Failed to generate game plan"
        }), 500


# =========================
# Mentor API
# =========================

@app.route("/mentor", methods=["POST"])
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
