"""Build article pages from a JSON data file."""
import json
import os
import sys

TEMPLATE = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Daily Me</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/svg+xml" href="../assets/logo.svg">
</head>
<body data-theme="light">
    <header class="header">
        <div class="header-inner">
            <div class="header-right">
                <a href="../index.html" class="back-link">→ חזרה לדשבורד</a>
            </div>
            <div class="header-left">
                <button class="theme-toggle" id="themeToggle" aria-label="החלף ערכת נושא">
                    <span class="theme-toggle-icon" id="themeIcon">☀️</span>
                </button>
            </div>
        </div>
    </header>

    <main class="article-main">
        <article class="article">
            <div class="article-meta">
                <span class="article-category">{category}</span>
                <span class="article-date">יום רביעי, 13 במאי 2026</span>
            </div>
            <h1 class="article-title">{title}</h1>

            <div class="article-body">
{body_html}
            </div>
            <div class="article-rating" style="margin-top: 32px; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 0.95rem; color: var(--text-secondary); font-weight: 600;">עניין אותך?</span>
                <div class="rating-buttons">
                    <button class="rating-btn" data-article-id="{aid}" data-rating="up" data-category="{category}" title="מעניין">✨ מעניין</button>
                    <button class="rating-btn" data-article-id="{aid}" data-rating="down" data-category="{category}" title="פחות מעניין">💤 פחות</button>
                </div>
            </div>
            <div class="article-source">
                <a href="{source}" target="_blank" rel="noopener" class="source-link">למקור המלא ↗</a>
            </div>
            <div class="article-back">
                <a href="../index.html" class="back-button">← חזרה לדשבורד</a>
            </div>
        </article>
    </main>

    <footer class="footer">
        <div class="footer-inner">
            <p class="footer-text">Daily Me · My world, every day.</p>
        </div>
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
"""

def build_article(data, out_dir):
    body_html = "\n".join(f"                <p>{p}</p>" for p in data["body"])
    html = TEMPLATE.format(
        title=data["title"],
        category=data["category"],
        body_html=body_html,
        aid=data["id"],
        source=data["source"],
    )
    path = os.path.join(out_dir, f"{data['id']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path

def main():
    json_path = sys.argv[1]
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    with open(json_path, "r", encoding="utf-8") as f:
        articles = json.load(f)
    for art in articles:
        path = build_article(art, out_dir)
        print(f"wrote {path}")

if __name__ == "__main__":
    main()
