# ATS Resume Screening Web Application

A Flask-based ATS (Applicant Tracking System) Resume Screening Web Application that analyzes PDF resumes against predefined job roles or custom job descriptions. The application extracts resume text, performs weighted skill matching, calculates an ATS score, stores analysis history in SQLite, and generates downloadable PDF reports.

---

## Features

* Upload resumes in PDF format
* Analyze resumes against predefined job roles
* Compare resumes with custom job descriptions
* Weighted ATS skill matching
* Resume match score calculation
* Display matched and missing skills
* Personalized improvement recommendations
* Generate downloadable PDF analysis reports
* Store resume analysis history using SQLite
* Responsive and modern user interface

---

## Tech Stack

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Flask

**Database**

* SQLite

**Libraries**

* PyPDF2
* ReportLab

---

## Project Structure

```text
ATS-Resume-Screening-Web-App/
│
├── app.py
├── database.py
├── requirements.txt
├── data/
├── reports/
├── resumes/
├── static/
├── templates/
└── utils/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Abinisha59/ATS-Resume-Screening-Web-App.git
```

Move into the project folder:

```bash
cd ATS-Resume-Screening-Web-App
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

* User authentication
* Resume ranking for multiple candidates
* NLP-based skill extraction
* PostgreSQL integration
* Email report delivery
* Dashboard with analytics

---

## Author

Abinisha G

GitHub: https://github.com/Abinisha59
