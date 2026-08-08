import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Secret key required by Flask to encrypt session cookies
app.secret_key = "super-secret-key-change-this-in-production"

# Database Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "comments.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

# --- Main Portfolio Route ---
@app.route("/")
def portfolio():
    return render_template("portfolio.html")

# --- Project 1 Standalone Page (TBA) ---
@app.route("/Project1")
def project1():
    return render_template("project1.html")

# --- Project 2 Standalone Page (TBA) ---
@app.route("/Project2")
def project2():
    return render_template("project2.html")

# --- Interactive Scratchpad & Comment Wall Route ---
@app.route("/scratchpad", methods=["GET", "POST"])
def scratchpad():
    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect(url_for("login"))

        comment_content = request.form.get("content")
        if comment_content and comment_content.strip():
            new_comment = Comment(content=comment_content.strip())
            db.session.add(new_comment)
            db.session.commit()
        return redirect(url_for("scratchpad"))

    comments = Comment.query.all()
    return render_template("main_page.html", comments=comments)

# --- Authentication Routes ---
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password123":
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("scratchpad"))
        else:
            error = "Invalid credentials. Please try again."

    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("scratchpad"))

if __name__ == "__main__":
    app.run(debug=True)