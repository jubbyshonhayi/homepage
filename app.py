from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
import os
from psycopg_pool import ConnectionPool

app = Flask(__name__, static_folder="public")
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")
database_url = os.getenv("DATABASE_URL")

# Database connection
db = ConnectionPool(database_url)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        # Get the information entered by the user
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Ensure user fills all the fields in the form
        if not name or not email or not message:
            flash("All fields are required.", "danger")
            return redirect(url_for("contact"))

        # Insert the form details in the database
        with db.connection() as connection:
            connection.execute(
                """
                INSERT INTO messages (name, email, message)
                VALUES (%s, %s, %s)
                """,
                (name, email, message)
            )

        flash("Thanks! Your message has bezf sen submitted.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404