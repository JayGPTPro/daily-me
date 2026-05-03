#!/usr/bin/env python3
"""Generate article HTML pages from articles JSON for Daily Me."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ARTICLES_DIR = ROOT / "docs" / "articles"
TEMPLATE = (ROOT / "src" / "article-template.html").read_text(encoding="utf-8")

DATE_HEBREW = "יום ראשון, 3 במאי 2026"


def build(article):
    body_html = "\n".join(f"<p>{p}</p>" for p in article["body"])
    image_block = ""
    if article.get("image"):
        image_block = (
            f'<div class="article-image-wrap">\n'
            f'    <img src="{article["image"]}" alt="{article["title"]}" '
            f'class="article-image" loading="lazy" '
            f'onerror="this.parentElement.style.display=\'none\'">\n'
            f'</div>'
        )
    out = TEMPLATE
    # Remove image block placeholder pattern
    import re
    out = re.sub(r"\{\{#ARTICLE_IMAGE\}\}.*?\{\{/ARTICLE_IMAGE\}\}", image_block, out, flags=re.DOTALL)
    out = out.replace("{{ARTICLE_TITLE}}", article["title"])
    out = out.replace("{{ARTICLE_CATEGORY}}", article["category_label"])
    out = out.replace("{{ARTICLE_DATE}}", DATE_HEBREW)
    out = out.replace("{{ARTICLE_BODY}}", body_html)
    out = out.replace("{{SOURCE_URL}}", article["source"])
    out = out.replace("{{ARTICLE_ID}}", article["id"])
    return out


def main():
    json_path = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "scripts" / "articles_2026-05-03.json")
    articles = json.loads(Path(json_path).read_text(encoding="utf-8"))
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    for art in articles:
        out_path = ARTICLES_DIR / art["filename"]
        out_path.write_text(build(art), encoding="utf-8")
        print(f"  ✓ {art['filename']}")
    print(f"\nTotal: {len(articles)} articles generated")


if __name__ == "__main__":
    main()
