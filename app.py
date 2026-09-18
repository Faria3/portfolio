"""
Faria Nafees — Portfolio
A small Flask app that serves a one-page developer portfolio and a
lightweight JSON API describing the same content (because a Python
portfolio should have at least one working endpoint).
"""

from datetime import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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
    """
    Receives the contact form. On a free host with no database/email
    service configured, we just validate and echo back a confirmation —
    swap this for a real email send (see README) once you add one.
    """
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "error": "Please fill in name, email, and message."}), 400

    print(f"[contact] {datetime.now().isoformat()} — {name} <{email}>: {message}")
    return jsonify({"ok": True, "message": "Thanks — message received. I'll reply by email soon."})


if __name__ == "__main__":
    app.run(debug=True)
