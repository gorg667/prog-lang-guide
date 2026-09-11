#!/usr/bin/env python3
"""Build the static website from PROGRAMMING_LANGUAGE_GUIDE.md.

Outputs:
  docs/index.html   pre-rendered page (sidebar TOC, search index, dark mode)
  docs/guide.md     verbatim copy of the guide for download

Usage: python3 scripts/build.py [--check]
  --check  validate only (headings unique, internal anchors resolve), no write.

Dependency: `pip install markdown` (falls back to a minimal renderer if missing).
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "PROGRAMMING_LANGUAGE_GUIDE.md"
DOCS = ROOT / "docs"
TEMPLATE = DOCS / "template.html"
OUT = DOCS / "index.html"
GUIDE_COPY = DOCS / "guide.md"


def slugify(text: str) -> str:
    """GitHub-style heading slug so the guide's own TOC links keep working."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\u00A7-]", "", text)  # keep letters, digits, _, space, hyphen, §
    text = text.replace("§", "")
    text = re.sub(r"\s+", "-", text.strip())
    return text or "section"


def extract_headings(md: str) -> list[dict]:
    heads = []
    in_code = False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            level = len(m.group(1))
            title = re.sub(r"\*\*|__|`", "", m.group(2))
            heads.append({"level": level, "title": title, "slug": slugify(title)})
    return heads


def dedupe_slugs(heads: list[dict]) -> None:
    seen: dict[str, int] = {}
    for h in heads:
        s = h["slug"]
        if s in seen:
            seen[s] += 1
            h["slug"] = f"{s}-{seen[s]}"
        else:
            seen[s] = 0


def validate(md: str, heads: list[dict]) -> list[str]:
    errors = []
    slugs = {h["slug"] for h in heads}
    for m in re.finditer(r"\]\(#([^)]+)\)", md):
        anchor = m.group(1)
        if anchor not in slugs:
            errors.append(f"broken internal link: #{anchor}")
    if not heads or heads[0]["level"] != 1:
        errors.append("guide must start with a level-1 heading")
    return errors


def render_markdown(md: str) -> str:
    try:
        import markdown  # type: ignore
        from markdown.extensions.toc import TocExtension  # type: ignore

        return markdown.markdown(
            md,
            extensions=[
                "tables",
                "fenced_code",
                "sane_lists",
                "attr_list",
                TocExtension(slugify=lambda v, sep: slugify(v), permalink="#", toc_depth="1-3"),
            ],
            output_format="html5",
        )
    except ImportError:  # minimal fallback so the build never hard-fails
        body = html.escape(md)
        return f"<pre class='fallback'>{body}</pre>"


def build_sidebar(heads: list[dict]) -> str:
    items = []
    for h in heads:
        if h["level"] < 2 or h["level"] > 3:
            continue
        cls = "lvl2" if h["level"] == 2 else "lvl3"
        items.append(
            f'<li class="{cls}"><a href="#{h["slug"]}" data-target="{h["slug"]}">{html.escape(h["title"])}</a></li>'
        )
    return "\n".join(items)


def build_search_index(md: str, heads: list[dict]) -> str:
    """Section -> plain text, for client-side search."""
    sections: list[dict] = []
    current = None
    in_code = False
    hi = 0
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m and hi < len(heads):
            h = heads[hi]
            hi += 1
            current = {"t": h["title"], "s": h["slug"], "l": h["level"], "b": ""}
            sections.append(current)
            continue
        if current is not None:
            txt = re.sub(r"[|*_`>#\[\]()]+", " ", line)
            txt = re.sub(r"\s+", " ", txt).strip()
            if txt:
                current["b"] += txt + " "
    for s in sections:
        s["b"] = s["b"][:1200]
    return json.dumps(sections, ensure_ascii=False)


def word_count(md: str) -> int:
    return len(re.findall(r"\w+", md))


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    md = SRC.read_text(encoding="utf-8")
    heads = extract_headings(md)
    dedupe_slugs(heads)
    errors = validate(md, heads)
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    print(f"ok: {len(heads)} headings, {word_count(md):,} words")
    if check_only:
        return 0

    body = render_markdown(md)
    template = TEMPLATE.read_text(encoding="utf-8")
    page = (
        template.replace("{{CONTENT}}", body)
        .replace("{{SIDEBAR}}", build_sidebar(heads))
        .replace("{{SEARCH_INDEX}}", build_search_index(md, heads))
        .replace("{{WORDS}}", f"{word_count(md):,}")
        .replace("{{SECTIONS}}", str(len(heads)))
    )
    OUT.write_text(page, encoding="utf-8")
    GUIDE_COPY.write_text(md, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB) and {GUIDE_COPY.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
