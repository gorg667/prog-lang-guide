# Which Programming Language Should I Learn? — The 2026 Guide

A comprehensive, research-backed guide to choosing a programming language by goal, current as of **11 September 2026**.

- **Read it as Markdown:** [`PROGRAMMING_LANGUAGE_GUIDE.md`](PROGRAMMING_LANGUAGE_GUIDE.md) (~21,000 words)
- **Read it as a website:** the static site in [`docs/`](docs/) — enable GitHub Pages (Settings → Pages → Source: `main` / `docs`) and it's live at `https://gorg667.github.io/prog-lang-guide/`

## What's inside

| Part | Contents |
|---|---|
| §0 | 60-second decision table: 30+ goals → language |
| I | How to choose: the five-axis framework, seven myths, the AI factor (2024–26), paradigm families |
| II | The data: TIOBE Sep 2026, Stack Overflow 2025, GitHub Octoverse 2025, JetBrains 2025, IEEE 2025 — cross-index scoreboard, salary analysis and why it lies, momentum, the junior-market problem |
| III | 25 domains: web (frontend/backend/full-stack), mobile (iOS/Android/cross-platform), desktop, data, ML/AI, data engineering, systems, embedded, games, DevOps, security, HPC, finance, blockchain, automation, enterprise, legacy, compilers, hardware, education, enlightenment languages |
| IV | 30 language profiles + comparison matrix |
| V | Roadmaps for 8 learner profiles (beginner, career switcher, student, working dev, scientist, kid/teen, team lead, hobbyist) |
| VI | Sequencing your 2nd/3rd/4th language |
| VII | How to actually learn in 2026 (incl. using AI assistants well) and resources per language |
| VIII | Anti-recommendations |
| IX | FAQ |
| A, B | Sources & methodology; glossary |

Raw research notes with figures and sources: [`research/`](research/).

## Building the website

```bash
pip install -r requirements.txt          # markdown (+ playwright for QA)
python3 scripts/build.py                 # -> docs/index.html, docs/guide.md
python3 scripts/build.py --check         # validate headings/anchors only
cd docs && python3 -m http.server 8080   # preview

# optional headless QA (console errors, overflow, search, dark mode, mobile nav)
python3 -m playwright install chromium
python3 scripts/qa.py http://localhost:8080
```

`docs/template.html`, `docs/style.css`, and `docs/app.js` are hand-written; `docs/index.html` and `docs/guide.md` are generated — edit the Markdown, then rebuild.

## Updating the guide

See Appendix A.3 in the guide. Each autumn: refresh TIOBE, Stack Overflow (July), Octoverse (Oct/Nov), JetBrains (Oct), IEEE (Sep), State of Rust (Feb/Mar); update §2.2 and §2.4 first, then any Part III verdict whose numbers moved by more than a tier.

## License

Text: CC BY 4.0. Code (`scripts/`, `docs/*.js`, `docs/*.css`, `docs/template.html`): MIT.
