from flask import Flask, render_template, request, session, redirect, url_for
import time
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
failed_attempts = {}

def init_db():
    connection = sqlite3.connect("database.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return "Authentication System"


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Basic input validation
        if not username or not password:
         return render_template(
          "register.html",
          error="Username and password are required."
        ) 
        
        if len(username) < 3 or len(username) > 30:
         return render_template(
          "register.html",
          error="Username must be between 3 and 30 characters."
        )

        if len(password) < 8:
         return render_template(
          "register.html",
          error="Password must be at least 8 characters long."
        )

        # Hash the password before storing it
        password_hash = generate_password_hash(password)

        connection = sqlite3.connect("database.db")

        try:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )

            connection.commit()

        except sqlite3.IntegrityError:
            connection.close()
            return render_template(
             "register.html",
             error="Username already exists."
            )
        
        connection.close()

        return redirect(url_for("login", registered="1"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    registered = request.args.get("registered")
    
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        current_time = time.time()

        # Check whether this username is temporarily blocked
        if username in failed_attempts:
            attempts, blocked_until = failed_attempts[username]

            if current_time < blocked_until:
                remaining = int(blocked_until - current_time)

                return render_template(
                    "login.html",
                    error=f"Too many failed attempts. Try again in {remaining} seconds."
                )

        connection = sqlite3.connect("database.db")
        connection.row_factory = sqlite3.Row

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(
            user["password_hash"],
            password
        ):

            failed_attempts.pop(username, None)

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        # Login failed
        attempts = failed_attempts.get(username, (0, 0))[0] + 1

        if attempts >= 5:

            failed_attempts[username] = (
                attempts,
                current_time + 60
            )

            return render_template(
                "login.html",
                error="Too many failed attempts. Please try again in 60 seconds."
            )

        failed_attempts[username] = (attempts, 0)

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)