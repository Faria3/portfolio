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

## The contact form — now emails you

`POST /api/contact` validates the submission, logs it to the server
console, **and emails it to you** via SMTP (using only Python's
built-in `smtplib` — no extra dependency). If email isn't configured
yet, it just logs and still shows the visitor a normal success message
— nothing breaks, you just won't get the email until you set this up.

### Set it up with Gmail (free, ~5 minutes)

1. Turn on 2-Step Verification on the Gmail account you want to send
   from: myaccount.google.com/security.
2. Create an **App Password**: myaccount.google.com/apppasswords →
   name it "portfolio" → copy the 16-character password it gives you.
   (This is *not* your normal Gmail password — Google blocks normal
   passwords for this.)
3. Set three environment variables wherever you run the app:

   | Variable | Value |
   |---|---|
   | `SMTP_USER` | the Gmail address you're sending **from** |
   | `SMTP_PASSWORD` | the 16-character app password from step 2 |
   | `CONTACT_RECEIVER` | the address you want messages sent **to** (can be the same Gmail, or `farianafees803@gmail.com`) |

   **Running locally (PowerShell):**
   ```powershell
   $env:SMTP_USER="youraddress@gmail.com"
   $env:SMTP_PASSWORD="your16charapppassword"
   $env:CONTACT_RECEIVER="farianafees803@gmail.com"
   python app.py
   ```
   (These only last for that terminal session — set them again next
   time, or use a `.env` file with `python-dotenv` if you want them to
   persist.)

   **On PythonAnywhere:** open your WSGI configuration file and add
   these three lines *before* the `from app import app as application`
   line:
   ```python
   os.environ['SMTP_USER'] = 'youraddress@gmail.com'
   os.environ['SMTP_PASSWORD'] = 'your16charapppassword'
   os.environ['CONTACT_RECEIVER'] = 'farianafees803@gmail.com'
   ```
   (add `import os` near the top if it's not already there), then
   Save and Reload.

   **On Render:** dashboard → your service → **Environment** tab → add
   the three variables there. Render keeps them secret and out of your
   GitHub repo automatically.

4. Test it: submit the contact form on your live site and check the
   inbox at `CONTACT_RECEIVER`.

⚠️ Never commit real credentials into `app.py` or push them to GitHub.
Environment variables keep them out of your repo entirely — that's
the whole reason `app.py` reads them with `os.environ.get(...)`
instead of having them typed in directly.

### Alternative: Formspree / Web3Forms

If you'd rather not deal with SMTP at all, a hosted form service works
too — point the `fetch()` call in `static/js/script.js` at your
Formspree/Web3Forms endpoint instead of `/api/contact`. Less setup,
but your submissions live on a third party's service instead of
going straight to your inbox.

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
