from flask import Flask, render_template, request, jsonify
import json
import os
from chatbot import AetherBot

app = Flask(__name__)

bot = AetherBot()

NOTES_FILE = "notes.json"


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Chat API
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "reply": "Please enter a message."
            })

        response = bot.get_response(user_message)

        return jsonify({
            "reply": response
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        })


# -----------------------------
# Save Notes
# -----------------------------
@app.route("/save_note", methods=["POST"])
def save_note():

    try:

        data = request.get_json()

        note = data.get("note", "").strip()

        if not note:
            return jsonify({
                "success": False,
                "message": "Note cannot be empty."
            })

        notes = []

        if os.path.exists(NOTES_FILE):

            with open(
                    NOTES_FILE,
                    "r",
                    encoding="utf-8"
            ) as file:

                try:
                    notes = json.load(file)
                except:
                    notes = []

        notes.append(note)

        with open(
                NOTES_FILE,
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                notes,
                file,
                indent=4
            )

        return jsonify({
            "success": True,
            "message": "Note saved successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# -----------------------------
# Load Notes
# -----------------------------
@app.route("/get_notes", methods=["GET"])
def get_notes():

    try:

        if not os.path.exists(NOTES_FILE):

            return jsonify([])

        with open(
                NOTES_FILE,
                "r",
                encoding="utf-8"
        ) as file:

            notes = json.load(file)

        return jsonify(notes)

    except Exception:

        return jsonify([])


# -----------------------------
# Delete Note
# -----------------------------
@app.route("/delete_note", methods=["POST"])
def delete_note():

    try:

        data = request.get_json()

        index = data.get("index")

        if not os.path.exists(NOTES_FILE):

            return jsonify({
                "success": False
            })

        with open(
                NOTES_FILE,
                "r",
                encoding="utf-8"
        ) as file:

            notes = json.load(file)

        if index is not None and 0 <= index < len(notes):

            notes.pop(index)

            with open(
                    NOTES_FILE,
                    "w",
                    encoding="utf-8"
            ) as file:

                json.dump(
                    notes,
                    file,
                    indent=4
                )

        return jsonify({
            "success": True
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# -----------------------------
# Health Check
# -----------------------------
@app.route("/status")
def status():

    return jsonify({
        "app": "Aether AI",
        "status": "running",
        "mode": "offline"
    })


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )