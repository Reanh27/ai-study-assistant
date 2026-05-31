from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_file
import sqlite3
import os
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = "study_assistant_secret_key"

# ---------------- CONFIG ----------------
DATABASE = "users.db"
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------- DATABASE HELPERS ----------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            subject TEXT NOT NULL,
            hours TEXT NOT NULL,
            weakness TEXT NOT NULL,
            plan TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            filename TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- STUDY PLAN ENGINE ----------------
def generate_plan(subject, hours, weakness):
    steps = []

    try:
        hours = int(hours)
    except (ValueError, TypeError):
        hours = 2

    subject = subject.lower()
    weakness = weakness.lower()

    if "math" in subject:
        steps.extend([
            "Revise formulas",
            "Practice problems"
        ])

    if "calculus" in weakness:
        steps.extend([
            "Focus on derivatives",
            "Solve 5 questions"
        ])

    if "physics" in subject:
        steps.extend([
            "Revise formulas and concepts",
            "Solve numericals"
        ])

    if "chemistry" in subject:
        steps.extend([
            "Study equations and reactions",
            "Practice core concepts"
        ])

    if "programming" in subject:
        steps.extend([
            "Practice coding exercises",
            "Build mini projects"
        ])

    if not steps:
        steps.extend([
            "Revise important concepts",
            "Practice weak topics"
        ])

    steps.append(f"Study for {hours} hours with breaks")

    return steps


# ---------------- AUTH ----------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["user"])


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists!"

        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("home"))

        return "Invalid credentials!"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ---------------- STUDY PLAN API ----------------
@app.route("/plan", methods=["POST"])
def create_plan():
    data = request.get_json()

    subject = data.get("subject", "")
    hours = data.get("hours", 2)
    weakness = data.get("weakness", "")

    plan = generate_plan(subject, hours, weakness)

    if "user" in session:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO study_plans (username, subject, hours, weakness, plan)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                session["user"],
                subject,
                str(hours),
                weakness,
                ", ".join(plan)
            )
        )

        conn.commit()
        conn.close()

    return jsonify({"plan": plan})


# ---------------- CHATBOT ----------------
@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()

    try:
        if any(op in message for op in ["+", "-", "*", "/"]):
            reply = f"The answer is {eval(message)}"
        elif "derivative" in message:
            reply = "Derivative measures the rate of change of a function."
        elif "integration" in message:
            reply = "Integration calculates area under a curve."
        elif "physics" in message:
            reply = "Focus on formulas, concepts, and numerical practice."
        elif "chemistry" in message:
            reply = "Revise reactions, equations, and theory."
        elif "programming" in message:
            reply = "Practice logic-building and coding projects daily."
        elif "exam" in message:
            reply = "Prioritize weak topics and solve previous papers."
        elif "motivation" in message:
            reply = "Consistency creates success—study daily."
        else:
            reply = "I can help with academics, study plans, and exam preparation!"
    except Exception:
        reply = "I couldn't understand that."

    return jsonify({"reply": reply})


# ---------------- HISTORY ----------------
@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, subject, hours, weakness, plan FROM study_plans WHERE username = ?",
        (session["user"],)
    )

    plans = cursor.fetchall()
    conn.close()

    return render_template("history.html", plans=plans)


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM study_plans WHERE username = ?",
        (session["user"],)
    )
    total_plans = cursor.fetchone()[0]

    cursor.execute(
        "SELECT DISTINCT subject FROM study_plans WHERE username = ?",
        (session["user"],)
    )
    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_plans=total_plans,
        subjects=subjects
    )


# ---------------- PDF DOWNLOAD ----------------
@app.route("/download_plan/<int:plan_id>")
def download_plan(plan_id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT subject, hours, weakness, plan FROM study_plans WHERE id = ? AND username = ?",
        (plan_id, session["user"])
    )

    plan = cursor.fetchone()
    conn.close()

    if not plan:
        return "Plan not found"

    pdf_path = f"study_plan_{plan_id}.pdf"
    pdf = canvas.Canvas(pdf_path)
    pdf.setFont("Helvetica", 14)

    pdf.drawString(100, 800, "AI Study Assistant - Study Plan Report")
    pdf.drawString(100, 760, f"Subject: {plan[0]}")
    pdf.drawString(100, 730, f"Hours: {plan[1]}")
    pdf.drawString(100, 700, f"Weakness: {plan[2]}")
    pdf.drawString(100, 670, "Generated Plan:")

    y = 640
    for line in plan[3].split(", "):
        pdf.drawString(120, y, f"- {line}")
        y -= 25

    pdf.save()

    return send_file(pdf_path, as_attachment=True)


# ---------------- DOCUMENT UPLOAD ----------------
@app.route("/upload", methods=["GET", "POST"])
def upload_document():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        file = request.files.get("document")

        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO documents (username, filename) VALUES (?, ?)",
                (session["user"], filename)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("upload_document"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT filename FROM documents WHERE username = ?",
        (session["user"],)
    )

    documents = cursor.fetchall()
    conn.close()

    return render_template("upload.html", documents=documents)

@app.route("/ai_tutor")
def ai_tutor():
    return render_template("ai_tutor.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/progress")
def progress():
    return render_template("progress.html")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "profile.html",
        username=session["user"]
    )


@app.route("/save_note", methods=["POST"])
def save_note():
    if "user" not in session:
        return jsonify({"status":"error"})
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes(username,title,content) VALUES(?,?,?)",
        (session["user"], data.get("title",""), data.get("content",""))
    )
    conn.commit()
    conn.close()
    return jsonify({"status":"success"})


@app.route("/get_notes")
def get_notes():
    if "user" not in session:
        return jsonify([])
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id,title,content FROM notes WHERE username=? ORDER BY id DESC",
        (session["user"],)
    )
    notes = cursor.fetchall()
    conn.close()
    return jsonify(notes)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)