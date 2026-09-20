from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
import os
from psycopg_pool import ConnectionPool
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

app = Flask(__name__, static_folder="public", static_url_path="")
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

        # Brevo email configuration
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key["api-key"] = os.getenv("BREVO_API_KEY")

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )

        sender = {
            "name": "Jubilant Shonhayi",
            "email": "jubilantjubby@gmail.com"
        }

        # Email notification for me
        notification_email = sib_api_v3_sdk.SendSmtpEmail(
            sender=sender,
            to=[
                {
                    "email": "jubilentshonhayi@gmail.com"
                }
            ],
            reply_to={
                "email": email,
                "name": name
            },
            subject="You received a new message",
            html_content=f"""
                <h2>New message from your portfolio</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong></p>
                <p>{message}</p>
            """
        )

        # Confirmation email for the visitor
        confirmation_email = sib_api_v3_sdk.SendSmtpEmail(
            sender=sender,
            to=[
                {
                    "email": email,
                    "name": name
                }
            ],
            subject="We've received your message",
            html_content=f"""
                <h2>Thanks for reaching out!</h2>
                <p>Hi {name},</p>
                <p>We've received your message and will get back to you soon.</p>
                <p>Thanks for contacting us.</p>
            """
        )

        try:
            api_instance.send_transac_email(notification_email)
            api_instance.send_transac_email(confirmation_email)

        except ApiException:
            flash(
                "Your message was submitted, but there was a problem sending the email.",
                "warning"
            )
            return redirect(url_for("contact"))

        flash("Thanks! Your message has been submitted.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

