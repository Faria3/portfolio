"""
Faria Nafees — Portfolio
A small Flask app that serves a one-page developer portfolio, a
lightweight JSON API describing the same content, and a contact
endpoint that emails you when someone submits the form.
"""

import os
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ----------------------------------------------------------------------
# Content — edit these to update the site
# ----------------------------------------------------------------------

PROFILE = {
    "name": "Faria Nafees",
    "title": "Junior Software Developer — AI-Assisted Development",
    "location": "Lahore, Pakistan",
    "phone": "0324-0220542",
    "email": "farianafees803@gmail.com",
    "linkedin": "https://linkedin.com/in/faria-nafees",
    "github": "https://github.com/Faria3",
    "summary": (
        "Computer Science graduate with hands-on programming experience across "
        "JavaScript, Python, PHP, and C#, and a strong foundation in object-oriented "
        "programming and web development. Built an independent Final Year Project and "
        "an Online Academy web application to strengthen practical software development "
        "skills. Currently expanding my Python and JavaScript skills and learning "
        "AI-assisted development workflows with Cursor and Claude."
    ),
}

SKILLS = {
    "Programming": ["JavaScript", "Python", "PHP", "C#", "OOP"],
    "Web Development": ["HTML5", "CSS3", "React.js", "Node.js", "MySQL", "Flexbox", "CSS Grid"],
    "AI-Assisted Development": ["Cursor", "Claude", "AI-assisted debugging", "AI-assisted research"],
    "Tools & Frameworks": ["Git", "GitHub", ".NET", "VS Code", "WordPress"],
    "Design": ["Figma", "Adobe XD", "Canva"],
}

EXPERIENCE = [
    {
        "role": "Business Development Associate",
        "place": "Lahore, Pakistan",
        "period": "July 2026 — Present",
        "points": [
            "Communicate with clients to understand requirements and business needs.",
            "Support client coordination and professional workplace communication.",
        ],
    },
    {
        "role": "Freelance Web Developer & Designer",
        "place": "Remote",
        "period": "2023 — Present",
        "points": [
            "Develop websites, forms, and application interfaces for academic and small-business clients.",
            "Create professional visual and branding designs using Canva.",
        ],
    },
    {
        "role": "Frontend Developer Intern",
        "place": "Invexic Software House & ZombsTech, Lahore",
        "period": "2022 — 2023",
        "points": [
            "Built web interfaces using HTML, CSS, and JavaScript with responsive layouts via Flexbox and CSS Grid.",
            "Created UI/UX wireframes in Figma and Adobe XD, and assisted with .NET/C# development tasks.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Online Academy Web Application",
        "stack": ["React", "Node.js", "MySQL"],
        "description": "Independently built a web app for managing students, tutors, courses, and demo requests, with an admin dashboard.",
        "kind": "featured",
    },
    {
        "name": "E-Healthcare Web Application",
        "stack": ["HTML", "CSS", "JavaScript", "PHP"],
        "description": "Appointment booking and patient management app with a JavaScript frontend and PHP backend.",
        "kind": "standard",
    },
    {
        "name": "Final Year Project",
        "stack": ["Independent build"],
        "description": "Planned and developed end-to-end at Islamia University of Bahawalpur, applying programming, problem-solving, and project management skills.",
        "kind": "standard",
    },
    {
        "name": "Python / OOP Playground",
        "stack": ["Python", "OOP"],
        "description": "A coffee machine, a calculator, blackjack, and a password generator — small apps built to master Python fundamentals.",
        "kind": "standard",
    },
]

EDUCATION = [
    {
        "degree": "BS Computer Science",
        "school": "Islamia University of Bahawalpur",
        "period": "Sep 2024 — Jan 2026",
        "detail": "CGPA 3.39",
    },
    {
        "degree": "Biotechnology (2 years of study)",
        "school": "University of Lahore",
        "period": "Feb 2021 — Aug 2023",
        "detail": "CGPA 3.6",
    },
]

CERTIFICATIONS = [
    "Web Development — Programming Hub / Coursera",
    "Frontend Development — ZombsTech",
    "Python Intermediate — Udemy",
]

# ----------------------------------------------------------------------
# Email — reads credentials from environment variables, never hard-coded.
# See README.md for how to set these on your machine / host.
# ----------------------------------------------------------------------

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")            # the email account that sends the message
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")    # an app password, not your normal login password
CONTACT_RECEIVER = os.environ.get("CONTACT_RECEIVER", PROFILE["email"])


def send_contact_email(name: str, email: str, message: str) -> bool:
    """
    Sends the contact-form submission to CONTACT_RECEIVER by email.
    Returns True on success, False if email isn't configured or sending
    failed (in which case the submission is still logged server-side).
    """
    if not SMTP_USER or not SMTP_PASSWORD:
        print("[contact] Email not configured — set SMTP_USER / SMTP_PASSWORD. Logging only.")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio contact — {name}"
    msg["From"] = SMTP_USER
    msg["To"] = CONTACT_RECEIVER
    msg["Reply-To"] = email
    msg.set_content(
        f"New message from your portfolio site:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Message:\n{message}\n"
    )

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as exc:  # noqa: BLE001 — we want to log and degrade gracefully either way
        print(f"[contact] Email send failed: {exc}")
        return False


# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
        education=EDUCATION,
        certifications=CERTIFICATIONS,
        year=datetime.now().year,
    )


@app.route("/api/profile")
def api_profile():
    """A tiny JSON API — proof the site is Python-backed, not just styled to look like it."""
    return jsonify(
        {
            "profile": PROFILE,
            "skills": SKILLS,
            "experience": EXPERIENCE,
            "projects": PROJECTS,
            "education": EDUCATION,
            "certifications": CERTIFICATIONS,
        }
    )


@app.route("/api/contact", methods=["POST"])
def api_contact():
    """Validates the contact form, emails it to CONTACT_RECEIVER, and logs it either way."""
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "error": "Please fill in name, email, and message."}), 400

    print(f"[contact] {datetime.now().isoformat()} — {name} <{email}>: {message}")
    send_contact_email(name, email, message)

    return jsonify({"ok": True, "message": "Thanks — message received. I'll reply by email soon."})


if __name__ == "__main__":
    app.run(debug=True)
