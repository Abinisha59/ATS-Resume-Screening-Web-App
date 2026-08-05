
from flask import Flask, render_template, request
from utils.file_reader import read_pdf
from utils.skill_matcher import match_skills

from flask import send_file
from utils.report_generator import generate_report
from utils.database_helper import save_result
import database
import sqlite3
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    uploaded_file = request.files["resume"]

    job_role = request.form["job_role"]

    job_description = request.form["job_description"]

    file_path = "resumes/" + uploaded_file.filename

    uploaded_file.save(file_path)

    resume_text = read_pdf(file_path)

    # Use custom Job Description
    if job_description.strip():

        matched, missing, percentage = match_skills(
            resume_text,
            job_description
        )

        role = "Custom Job Description"

    # Use selected Job Role
    else:

        matched, missing, percentage = match_skills(
            resume_text,
            job_role
        )

        role = job_role

    # Generate PDF
    generate_report(
        "reports/report.pdf",
        role,
        percentage,
        matched,
        missing
    )
    save_result(
    uploaded_file.filename,
    role,
    percentage,
    matched,
    missing
    )

    return render_template(
        "report.html",
        role=role,
        matched=matched,
        missing=missing,
        percentage=percentage
    )
@app.route("/download")

def download():

    return send_file(

        "reports/report.pdf",

        as_attachment=True

    )



@app.route("/history")
def history():

    conn = sqlite3.connect("resume.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT filename,
               role,
               score,
               created_at
        FROM resume_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        history=rows
    )

if __name__ == "__main__":
    app.run(debug=True)