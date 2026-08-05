import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Define dynamic absolute path for SQLite database file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "comments.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database Model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment_content = request.form.get("content")
        if comment_content and comment_content.strip():
            new_comment = Comment(content=comment_content.strip())
            db.session.add(new_comment)
            db.session.commit()
        return redirect(url_for("index"))

    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)