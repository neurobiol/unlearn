#!/usr/bin/env python3
"""
Build docs/*.html from docs/content/*.md.

- Source Markdown links stay as *.md so GitHub browsing works.
- During HTML generation, links like:
    docs/content/foo.md   or   content/foo.md   or   foo.md
  are rewritten to:
    foo.html
"""

from pathlib import Path
import re

import markdown


ROOT = Path(__file__).resolve().parents[1]   # repo root (tools/..)
CONTENT_DIR = ROOT / "docs" / "content"
OUT_DIR = ROOT / "docs"

NAV = """
<nav class="nav">
  <a href="index.html">Home</a>
  <a href="poster_overview.html">Overview</a>
  <a href="poster_guide.html">Poster guide</a>
  <a href="core_question.html">Core question</a>
  <a href="methods_summary.html">Methods</a>
  <a href="two_timescale_model.html">Two timescale model</a>
  <a href="parkinsons_wearables.html">Parkinson wearables</a>
  <a href="discussion_future_work.html">Discussion</a>
  <a href="glossary.html">Glossary</a>
  <a href="references.html">References</a>
  <a href="further_reading.html">Further reading</a>
</nav>
""".strip()

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#111111">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="styles.css">
<title>{title}</title>
</head>
<body>
<header>
  <div class="brand">UNLEARN</div>
  {nav}
</header>

<main>
  <article class="content">
{body}
  </article>
</main>

<footer>
  <div class="foot">Poster companion text only</div>
</footer>

<script>
if ('serviceWorker' in navigator) {{
  navigator.serviceWorker.register('sw.js');
}}
</script>
<script>
window.MathJax = {
  tex: { inlineMath: [['$', '$'], ['\\(', '\\)']], displayMath: [['$$','$$'], ['\\[','\\]']] }
};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
"""


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def rewrite_md_links_for_site(md_text: str) -> str:
    """
    Rewrite markdown links that point to markdown pages into .html for the site build.

    Converts any of these to foo.html:
      (docs/content/foo.md)
      (content/foo.md)
      (foo.md)

    Keeps anchors if present:
      (docs/content/foo.md#section) -> (foo.html#section)
    """

    # 1) docs/content/foo.md or content/foo.md -> foo.html
    md_text = re.sub(
        r"\((?:docs/)?content/([A-Za-z0-9_\-]+)\.md(#[^)]+)?\)",
        r"(\1.html\2)",
        md_text,
    )

    # 2) foo.md -> foo.html  (only for “known pages” that exist in docs/content)
    known = {p.stem for p in CONTENT_DIR.glob("*.md")}

    def repl(m: re.Match) -> str:
        name = m.group(1)
        anchor = m.group(2) or ""
        if name in known:
            return f"({name}.html{anchor})"
        return m.group(0)

    md_text = re.sub(r"\(([A-Za-z0-9_\-]+)\.md(#[^)]+)?\)", repl, md_text)

    return md_text


def md_to_html(md_text: str) -> str:
    md_text = rewrite_md_links_for_site(md_text)
    html = markdown.markdown(
        md_text,
        extensions=["extra", "toc", "sane_lists"],
        output_format="html5",
    )
    # indent for template readability
    return "\n".join("    " + line for line in html.splitlines())


def main() -> None:
    if not CONTENT_DIR.exists():
        raise SystemExit(f"Missing folder: {CONTENT_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for md_path in sorted(CONTENT_DIR.glob("*.md")):
        md_text = md_path.read_text(encoding="utf-8")
        title = extract_title(md_text, md_path.stem.replace("_", " ").title())
        body = md_to_html(md_text)

        out_path = OUT_DIR / f"{md_path.stem}.html"
        out_path.write_text(
            TEMPLATE.format(title=title, nav=NAV, body=body),
            encoding="utf-8",
        )
        print(f"Wrote {out_path.relative_to(ROOT)}")

    # Build docs/index.html from docs/content/index.md (if present)
    index_md = CONTENT_DIR / "index.md"
    if index_md.exists():
        md_text = index_md.read_text(encoding="utf-8")
        title = extract_title(md_text, "UNLEARN")
        body = md_to_html(md_text)
        (OUT_DIR / "index.html").write_text(
            TEMPLATE.format(title=title, nav=NAV, body=body),
            encoding="utf-8",
        )
        print("Wrote docs/index.html")

if __name__ == "__main__":
    main()
