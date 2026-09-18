// Scrollspy: highlight the active file/tab as the user scrolls through sections
(function () {
  const sections = Array.from(document.querySelectorAll(".pane[id]"));
  const fileLinks = Array.from(document.querySelectorAll(".filetree__item"));
  const tabs = Array.from(document.querySelectorAll(".tab"));

  function setActive(id) {
    fileLinks.forEach((el) => el.classList.toggle("is-active", el.dataset.target === id));
    tabs.forEach((el) => el.classList.toggle("tab--active", el.dataset.tab === id));
  }

  if ("IntersectionObserver" in window && sections.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) setActive(entry.target.id);
        });
      },
      { rootMargin: "-40% 0px -55% 0px", threshold: 0 }
    );
    sections.forEach((s) => observer.observe(s));
  }
})();

// Contact form: POST to /api/contact, show inline status
(function () {
  const form = document.getElementById("contact-form");
  const status = document.getElementById("contact-status");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());
    const submitBtn = form.querySelector("button[type=submit]");

    submitBtn.disabled = true;
    status.textContent = "Sending…";
    status.classList.remove("is-error");

    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();

      if (data.ok) {
        status.textContent = data.message;
        form.reset();
      } else {
        status.textContent = data.error || "Something went wrong. Please try again.";
        status.classList.add("is-error");
      }
    } catch (err) {
      status.textContent = "Network error — email me directly instead.";
      status.classList.add("is-error");
    } finally {
      submitBtn.disabled = false;
    }
  });
})();
