#!/usr/bin/env python3
"""Headless QA for the built site: console errors, layout overflow, search, dark mode, screenshots.

Usage: python3 scripts/qa.py [base_url]   (default http://localhost:8080)
Requires: pip install playwright && python -m playwright install chromium
Screenshots go to /tmp/qa/*.png (throwaway).
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
OUT = Path("/tmp/qa")
OUT.mkdir(exist_ok=True)


def main() -> int:
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, vp in [("desktop", (1400, 900)), ("mobile", (390, 844))]:
            page = browser.new_page(viewport={"width": vp[0], "height": vp[1]})
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(BASE + "/", wait_until="load")
            page.wait_for_selector("#toc a")

            overflow = page.evaluate(
                "document.documentElement.scrollWidth > document.documentElement.clientWidth + 1"
            )
            if overflow:
                failures.append(f"[{name}] horizontal overflow")

            n_toc = page.evaluate("document.querySelectorAll('#toc a').length")
            missing = page.evaluate(
                "Array.from(document.querySelectorAll('#toc a')).map(a=>a.dataset.target)"
                ".filter(id=>!document.getElementById(id))"
            )
            if n_toc < 50:
                failures.append(f"[{name}] toc too small: {n_toc}")
            if missing:
                failures.append(f"[{name}] toc targets missing: {missing[:5]}")

            page.fill("#searchInput", "rust embedded")
            page.wait_for_timeout(300)
            hits = page.evaluate("document.querySelectorAll('#searchResults a').length")
            if hits == 0:
                failures.append(f"[{name}] search returned 0 results")
            page.screenshot(path=str(OUT / f"{name}-search.png"))
            page.keyboard.press("Escape")

            page.click("#themeBtn")
            dark = page.evaluate("document.documentElement.classList.contains('dark')")
            if not dark:
                failures.append(f"[{name}] dark mode toggle failed")
            page.screenshot(path=str(OUT / f"{name}-dark.png"))
            page.click("#themeBtn")

            if name == "mobile":
                page.click("#menuBtn")
                page.wait_for_timeout(300)
                if not page.evaluate("document.body.classList.contains('nav-open')"):
                    failures.append("[mobile] nav drawer did not open")
                page.screenshot(path=str(OUT / "mobile-nav.png"))
                page.click("#scrim")

            page.goto(BASE + "/#39-machine-learning-ai-and-llm-applications", wait_until="load")
            page.wait_for_timeout(600)
            active = page.evaluate("document.querySelector('#toc a.active')?.dataset.target || ''")
            page.screenshot(path=str(OUT / f"{name}-section.png"))

            if errors:
                failures.append(f"[{name}] console errors: {errors[:3]}")
            print(f"{name}: toc={n_toc} search_hits={hits} active_after_jump={active!r} errors={len(errors)}")
            page.close()
        browser.close()

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(" -", f)
        return 1
    print("\nQA passed. Screenshots in", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
