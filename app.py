from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "study_assistant_secret_key"


# ---------------- DATABASE SETUP ----------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Study plans table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            subject TEXT,
            hours TEXT,
            weakness TEXT,
            plan TEXT
        )
    ''')

    conn.commit()
    conn.close()


init_db()


# ---------------- STUDY PLAN LOGIC ----------------
def generate_plan(subject, hours, weakness):
    plan = []

    hours = int(hours)

    if "math" in subject.lower():
        plan.append("Revise formulas")
        plan.append("Practice problems")

    if "calculus" in weakness.lower():
        plan.append("Focus on derivatives")
        plan.append("Solve 5 questions")

    if "physics" in subject.lower():
        plan.append("Revise formulas and core concepts")
        plan.append("Practice numerical problems")

    if "chemistry" in subject.lower():
        plan.append("Revise chemical equations")
        plan.append("Practice reaction mechanisms")

    if "programming" in subject.lower():
        plan.append("Practice coding exercises")
        plan.append("Build small projects")

    plan.append(f"Study for {hours} hours with breaks")

    return plan


# ---------------- HOME ----------------
@app.route('/')
def home():
    if 'user' in session:
        return render_template("index.html", username=session['user'])
    return redirect(url_for('login'))


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()

        except:
            conn.close()
            return "Username already exists!"

        conn.close()
        return redirect(url_for('login'))

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials!"

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ---------------- STUDY PLAN ----------------
@app.route('/plan', methods=['POST'])
def plan():
    data = request.json

    subject = data['subject']
    hours = data['hours']
    weakness = data['weakness']

    generated_plan = generate_plan(subject, hours, weakness)

    # Save study plan to database
    if 'user' in session:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            '''
            INSERT INTO study_plans
            (username, subject, hours, weakness, plan)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                session['user'],
                subject,
                hours,
                weakness,
                ", ".join(generated_plan)
            )
        )

        conn.commit()
        conn.close()

    return jsonify({"plan": generated_plan})


# ---------------- ADVANCED CHATBOT ----------------
@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message'].lower()

    try:
        # Basic calculator
        if any(op in user_msg for op in ['+', '-', '*', '/']):
            answer = eval(user_msg)
            reply = f"The answer is {answer}"

        elif "derivative" in user_msg:
            reply = "Derivative is the rate of change of a function."

        elif "integration" in user_msg:
            reply = "Integration helps calculate area under a curve."

        elif "calculus" in user_msg:
            reply = "Focus on limits, differentiation, and integration."

        elif "physics" in user_msg:
            reply = "Study formulas, laws, and solve numerical problems."

        elif "chemistry" in user_msg:
            reply = "Focus on reactions, equations, and conceptual understanding."

        elif "programming" in user_msg:
            reply = "Practice coding daily and strengthen logic-building."

        elif "exam tips" in user_msg or "exam" in user_msg:
            reply = "Revise weak topics first, solve past papers, and manage time effectively."

        elif "motivation" in user_msg:
            reply = "Consistency beats intensity. Study daily and trust progress."

        elif "time management" in user_msg:
            reply = "Use focused sessions like 50 mins study + 10 mins break."

        elif "study plan" in user_msg:
            reply = "Enter your subject, hours, and weak topics above to generate a personalized study plan."

        else:
            reply = "I can help with academics, study plans, exams, and motivation!"

    except:
        reply = "I couldn't understand that. Try asking differently."

    return jsonify({"reply": reply})


# ---------------- STUDY HISTORY ----------------
@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT subject, hours, weakness, plan FROM study_plans WHERE username=?",
        (session['user'],)
    )

    plans = cursor.fetchall()
    conn.close()

    return render_template("history.html", plans=plans)


# ---------------- PROGRESS DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Total study plans
    cursor.execute(
        "SELECT COUNT(*) FROM study_plans WHERE username=?",
        (session['user'],)
    )
    total_plans = cursor.fetchone()[0]

    # Unique subjects
    cursor.execute(
        "SELECT DISTINCT subject FROM study_plans WHERE username=?",
        (session['user'],)
    )
    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_plans=total_plans,
        subjects=subjects
    )


# ---------------- MAIN ----------------
if __name__ == '__main__':
    app.run(debug=True)