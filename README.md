# Faria Nafees — Portfolio (Flask)

A one-page developer portfolio built with **Python (Flask)**, styled as a
dark code-editor UI (file sidebar, open tabs, syntax-highlighted intro)
to match an AI-assisted / Cursor-and-Claude workflow. All content lives
in `app.py` as plain Python data, rendered through Jinja templates —
edit one file to update the whole site.

## Run it locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000**.

## Project structure

```
portfolio/
├── app.py                 # Flask routes + all your content (edit here)
├── requirements.txt
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/style.css      # editor-theme styling
    └── js/script.js       # scrollspy nav + contact form
```

## Editing your content

Everything — name, summary, skills, experience, projects, education,
certifications — is defined as Python dictionaries/lists near the top
of `app.py` (`PROFILE`, `SKILLS`, `EXPERIENCE`, `PROJECTS`, `EDUCATION`,
`CERTIFICATIONS`). Change the values there; the template updates
automatically.

## The contact form

`POST /api/contact` currently validates the submission and logs it to
the server console — it does **not** send you an email yet, because
free hosts don't include an email service by default. Two easy ways to
make it real:

- **Formspree / Web3Forms** (no backend changes): point the form's
  `fetch` call in `static/js/script.js` at your Formspree/Web3Forms
  endpoint instead of `/api/contact`.
- **SMTP from Flask**: install `Flask-Mail`, add your Gmail/Outlook
  SMTP credentials as environment variables (never hard-code them),
  and send the message inside `api_contact()` in `app.py`.

## Deploying for free

Because this is a real Flask app (not static HTML), it needs a host
that runs Python — GitHub Pages/Netlify alone won't work. Good free
options, easiest first:

1. **Render** (render.com) — free "Web Service": connect your GitHub
   repo, set build command `pip install -r requirements.txt`, start
   command `gunicorn app:app`. Free tier sleeps after inactivity and
   wakes on the next visit (~30s cold start) — fine for a portfolio.
2. **PythonAnywhere** (pythonanywhere.com) — free tier built
   specifically for small Flask/Django apps, always-on, no sleep.
   Upload your files or pull from GitHub, point the WSGI file at
   `app`.
3. **Railway** / **Fly.io** — also support free/low-cost Flask
   deploys, good next step once you outgrow Render's free tier.

Recommended path to look professional fast:
1. Push this folder to a public GitHub repo (`github.com/Faria3`).
2. Deploy it on **Render** — you get a live `https://your-name.onrender.com` URL.
3. (Optional, later) Point a custom domain like `farianafees.dev` at it —
   Namecheap/Porkbun domains are ~$8–12/year, and Render supports custom
   domains free.
4. Put the live link at the top of your GitHub profile, your resume, and
   your LinkedIn "Featured" section — that's what clients and recruiters
   click first.

## Stack

Python · Flask · Jinja2 · vanilla JS · vanilla CSS (no framework —
keeps it fast and dependency-free to host anywhere).
