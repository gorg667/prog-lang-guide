# PROGRESS.md — agent memory

## 2026-09-11
- Task: MD guide (DONE, ~22k words, PROGRAMMING_LANGUAGE_GUIDE.md on main) + website adaptation.
- Branch policy: push straight to main.
- Website plan: docs/ static site (GitHub Pages). docs/index.html loads docs/guide.md via fetch, renders with marked.js (CDN), builds sidebar TOC from headings, client-side search, dark mode, mobile drawer. scripts/build.py copies guide -> docs/guide.md and validates headings/anchors. Preview: python3 -m http.server 8080 in docs/.
- NEXT: write docs/index.html, docs/style.css, docs/app.js, scripts/build.py, README.md. Commit each. Then start server + GetServiceUrl + Playwright check.
