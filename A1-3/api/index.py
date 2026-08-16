import os

from flask import Flask, request, jsonify
from openai import OpenAI

from openai_service import generate_game_plan, ask_game_mentor


app = Flask(__name__)


# =========================
# Planner API
# =========================

@app.route("/api/planner", methods=["POST"])
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

@app.route("/api/mentor", methods=["POST"])
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
