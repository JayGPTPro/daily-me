"""One-shot generator for 2026-05-16 morning edition. Reads article specs and writes HTML."""
import json, os, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART_TPL = (ROOT / "src/article-template.html").read_text(encoding="utf-8")
DOCS = ROOT / "docs"
ART_DIR = DOCS / "articles"
ART_DIR.mkdir(parents=True, exist_ok=True)

DATE_HE = "שבת, 16 במאי 2026"

ARTICLES = json.loads((ROOT / "scripts/_today_data.json").read_text(encoding="utf-8"))["articles"]

def render_article(a):
    body_html = "\n".join(f"<p>{html.escape(p)}</p>" for p in a["body"])
    out = ART_TPL
    out = out.replace("{{ARTICLE_TITLE}}", html.escape(a["title"]))
    out = out.replace("{{ARTICLE_CATEGORY}}", html.escape(a["category"]))
    out = out.replace("{{ARTICLE_DATE}}", DATE_HE)
    out = out.replace("{{ARTICLE_BODY}}", body_html)
    out = out.replace("{{ARTICLE_ID}}", a["id"])
    out = out.replace("{{SOURCE_URL}}", a["source"])
    img = a.get("image", "").strip()
    if img:
        out = re.sub(r"\{\{#ARTICLE_IMAGE\}\}|\{\{/ARTICLE_IMAGE\}\}", "", out)
        out = out.replace("{{ARTICLE_IMAGE}}", html.escape(img))
    else:
        out = re.sub(r"\{\{#ARTICLE_IMAGE\}\}.*?\{\{/ARTICLE_IMAGE\}\}", "", out, flags=re.S)
    return out

count = 0
for a in ARTICLES:
    fp = ART_DIR / a["file"]
    fp.write_text(render_article(a), encoding="utf-8")
    count += 1
print(f"Wrote {count} articles")
