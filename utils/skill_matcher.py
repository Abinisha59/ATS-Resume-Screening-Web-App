import json
import re


# -----------------------------
# Load predefined job roles
# -----------------------------

def load_skills():

    with open("data/skills.json", "r") as file:

        return json.load(file)


# -----------------------------
# Skill aliases
# -----------------------------

SKILL_ALIASES = {

    "Python": ["python"],

    "JavaScript": [
        "javascript",
        "js"
    ],

    "HTML": [
        "html",
        "html5"
    ],

    "CSS": [
        "css",
        "css3"
    ],

    "SQL": [
        "sql",
        "mysql",
        "postgresql",
        "postgres"
    ],

    "Git": [
        "git",
        "github"
    ],

    "Flask": [
        "flask"
    ],

    "Docker": [
        "docker"
    ],

    "REST API": [
        "rest api",
        "restful api",
        "api"
    ],

    "PostgreSQL": [
        "postgresql",
        "postgres"
    ],

    "React": [
        "react",
        "reactjs"
    ],

    "Bootstrap": [
        "bootstrap"
    ],

    "Power BI": [
        "power bi",
        "powerbi"
    ],

    "Excel": [
        "excel"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy"
    ],

    "Matplotlib": [
        "matplotlib"
    ]
}


# -----------------------------
# Check if a skill exists
# -----------------------------

def skill_found(text, skill):

    aliases = SKILL_ALIASES.get(skill, [skill.lower()])

    for word in aliases:

        if re.search(r"\b" + re.escape(word) + r"\b", text):

            return True

    return False


# -----------------------------
# ATS Matching
# -----------------------------

def match_skills(resume_text, job_input):

    resume_text = resume_text.lower()

    all_roles = load_skills()

    # -------------------------
    # Case 1 : Dropdown selected
    # -------------------------

    if job_input in all_roles:

        required = all_roles[job_input]

    # -------------------------
    # Case 2 : Custom JD
    # -------------------------

    else:

        required = {}

        jd = job_input.lower()

        for skill in SKILL_ALIASES:

            if skill_found(jd, skill):

                required[skill] = 1

    matched = []

    missing = []

    earned = 0

    total = sum(required.values())

    for skill, weight in required.items():

        if skill_found(resume_text, skill):

            matched.append(skill)

            earned += weight

        else:

            missing.append(skill)

    if total == 0:

        percentage = 0

    else:

        percentage = round((earned / total) * 100)

    return matched, missing, percentage