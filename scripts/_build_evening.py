#!/usr/bin/env python3
"""Build Daily Me Evening Edition - 2026-04-30."""
import os, json, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
ARTICLES_DIR = os.path.join(DOCS, 'articles')
ARCHIVE_DIR = os.path.join(DOCS, 'archive')
DATE_STR = '2026-04-30'
PREFIX = 'eve30-'

with open(os.path.join(os.path.dirname(__file__), '_evening_data_2026-04-30.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
items = data['items']

section_order = [
  ("warSecurity", "מלחמה וביטחון", "⚔️"),
  ("aiNews",       "חדשות AI",        "🤖"),
  ("politics",     "פוליטיקה ישראלית","🏛️"),
  ("worldNews",    "חדשות העולם",     "🌍"),
  ("amazon",       "אמזון למוכרים",   "📦"),
  ("gadgets",      "טכנולוגיה וגאדג׳טים","📱"),
  ("sports",       "ספורט",            "⚽"),
  ("shows",        "סדרות ובידור",    "📺"),
]

by_cat = {}
for it in items:
    by_cat.setdefault(it["cat"], []).append(it)

def card_html(it):
    uid = PREFIX + it["slug"]
    viral_tag = '<span class="viral-tag">🔥 כל העולם מדבר על זה</span>' if it.get("viral") else ''
    return f'''<div class="news-card" data-article-id="{uid}" data-category="{it['cat']}">
                        <img src="{it['image']}" alt="" class="card-image" loading="lazy" onerror="this.style.display='none'">
                        <div class="card-content">
                            {viral_tag}
                            <span class="card-category">{it['catLabel']}</span>
                            <h3 class="card-title">{it['title']}</h3>
                            <p class="card-summary">{it['summary']}</p>
                            <div class="card-footer">
                                <a href="articles/{DATE_STR}-{it['slug']}-eve.html" class="read-more">קרא עוד ←</a>
                                <div class="rating-buttons">
                                    <button class="rating-btn" data-article-id="{uid}" data-rating="up" data-category="{it['cat']}">👍</button>
                                    <button class="rating-btn" data-article-id="{uid}" data-rating="down" data-category="{it['cat']}">👎</button>
                                </div>
                            </div>
                        </div>
                    </div>'''

sections_html_parts = []
for cat_id, cat_title, icon in section_order:
    if cat_id not in by_cat: continue
    cards = "\n".join(card_html(it) for it in by_cat[cat_id])
    sections_html_parts.append(f'''<section class="section-block news-section" id="{cat_id}">
                <div class="section-header">
                    <span class="section-icon">{icon}</span>
                    <h2 class="section-title">{cat_title}</h2>
                </div>
                <div class="news-cards">
                    {cards}
                </div>
            </section>''')
news_grid_html = "\n            ".join(sections_html_parts)

calendar_events_html = '''<div class="calendar-event"><span class="event-time">כל היום</span><span class="event-title">🚀 Challenge EN - Round 2 (יום 5 - אחרון!)</span></div>
                <div class="calendar-event"><span class="event-time">כל היום</span><span class="event-title">🌍 May Day - יום הפועלים הבינלאומי</span></div>
                <div class="calendar-event"><span class="event-time">21:30-22:00</span><span class="event-title">פגישה עם Robin Lobo (Lumian) - Zoom</span></div>'''

breaking = '''<div class="breaking-banner"><span class="breaking-label">🔴 מבזק</span> טראמפ דחה את ההצעה האיראנית לפתוח את מצרי הורמוז | 14 הרוגים בגיחות חיל האוויר בלבנון | בנט-לפיד הודיעו על איחוד מפלגות | מטא צנחה 9% בשוק על העלאת תקציב ה-AI ל-145 מיליארד</div>'''

html_doc = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Me - מהדורת ערב · 30 באפריל 2026</title>
    <meta name="description" content="Daily Me - My world, every day.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="assets/logo.svg">
</head>
<body data-theme="light">

    {breaking}

    <header class="header">
        <div class="header-inner">
            <div class="header-right">
                <img src="assets/logo.svg" alt="Daily Me" class="header-logo">
                <div class="header-info">
                    <h1 class="header-title">Daily Me</h1>
                    <span class="header-subtitle">מהדורת ערב 🌙 · יום חמישי, 30 באפריל 2026</span>
                </div>
            </div>
            <div class="header-left">
                <span class="header-update-time">עודכן 18:15</span>
                <button class="theme-toggle" id="themeToggle" aria-label="החלף ערכת נושא">
                    <span class="theme-toggle-icon" id="themeIcon">☀️</span>
                </button>
            </div>
        </div>
    </header>

    <main class="main">
        <section class="hero" id="hero">
            <div class="hero-inner">
                <h2 class="hero-greeting">ערב טוב, ג'יי! 🌙</h2>
                <div class="hero-surprise">
                    <span class="surprise-label">📜 היום בהיסטוריה</span>
                    <p class="surprise-content">ב-30 באפריל 1993. לפני בדיוק 33 שנה. טים ברנרס-לי שיחרר את קוד המקור של דפדפן ה-Web הראשון בעולם. בחינם. לציבור. הוא יכול היה להיות מיליארדר. הוא העדיף לשנות את העולם. <em style="font-size:0.85em; opacity:0.7;">מקור: <a href="https://www.history.com/this-day-in-history/april-30" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">History.com · This Day in History</a></em></p>
                </div>
            </div>
        </section>

        <section class="quick-bar" id="quickBar">
            <div class="quick-bar-inner">
                <div class="quick-card weather-card">
                    <div class="quick-card-icon">🌙</div>
                    <div class="quick-card-info">
                        <span class="quick-card-value">22°</span>
                        <span class="quick-card-label">לילה צלול, 16°-25° · <a href="https://www.timeanddate.com/weather/israel/raanana/ext" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;opacity:0.7;font-size:0.8em">מקור</a></span>
                    </div>
                    <div class="weather-recommendation">👕 חולצה קצרה, סוודר ללילה</div>
                </div>
                <div class="quick-card dollar-card">
                    <div class="quick-card-icon">💵</div>
                    <div class="quick-card-info">
                        <span class="quick-card-value">₪2.97</span>
                        <span class="quick-card-label quick-card-change negative">↓ 1.0% · <a href="https://www.boi.org.il/roles/markets/exchangerates/" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;opacity:0.7;font-size:0.8em">בנק ישראל</a></span>
                    </div>
                    <canvas class="sparkline" id="dollarSparkline" width="100" height="40"></canvas>
                </div>
            </div>
        </section>

        <section class="section-block" id="calendar">
            <div class="section-header">
                <span class="section-icon">📅</span>
                <h2 class="section-title">פגישות מחר</h2>
            </div>
            <div class="calendar-events">
                {calendar_events_html}
            </div>
        </section>

        <div class="category-filter">
            <button class="filter-btn active" data-filter="all">הכל</button>
            <button class="filter-btn" data-filter="warSecurity">⚔️ מלחמה</button>
            <button class="filter-btn" data-filter="politics">🏛️ פוליטיקה</button>
            <button class="filter-btn" data-filter="aiNews">🤖 AI</button>
            <button class="filter-btn" data-filter="worldNews">🌍 עולם</button>
            <button class="filter-btn" data-filter="amazon">📦 אמזון</button>
            <button class="filter-btn" data-filter="gadgets">📱 גאדג׳טים</button>
            <button class="filter-btn" data-filter="sports">⚽ ספורט</button>
            <button class="filter-btn" data-filter="shows">📺 בידור</button>
        </div>

        <div class="news-grid">
            {news_grid_html}
        </div>

        <section class="section-block extras-section" id="extras">
            <div class="section-header">
                <span class="section-icon">💡</span>
                <h2 class="section-title">הפינות של ג'יי</h2>
            </div>
            <div class="extras-grid">
                <div class="extra-card">
                    <div class="extra-icon">💬</div>
                    <div class="extra-label">ציטוט השראה</div>
                    <div class="extra-content">״אם אתה לא יכול להסביר את זה בפשטות. אתה לא מבין את זה מספיק טוב״ - אלברט איינשטיין. הוא לא דיבר על תקשורת. הוא דיבר על ידע. אם אתה מסתבך במילים. כנראה שאתה עוד לא שולט בנושא.</div>
                    <div class="extra-source"><a href="https://www.brainyquote.com/quotes/albert_einstein_383803" target="_blank" rel="noopener">BrainyQuote · Albert Einstein</a></div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🎙️</div>
                    <div class="extra-label">פודקאסט בעברית</div>
                    <div class="extra-content">״מפתחים חסרי תרבות״. פודקאסט שבועי על חיי היומיום של צוותי פיתוח בישראל. בחור בערוץ הסטריימינג שלך. אורך פרק. 50-70 דקות. מומלץ למי שעוסק ב-AI ובפיתוח.</div>
                    <div class="extra-source"><a href="https://www.iheart.com/podcast/256--43071799/" target="_blank" rel="noopener">iHeart · מפתחים חסרי תרבות</a></div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🔤</div>
                    <div class="extra-label">מילה באנגלית</div>
                    <div class="extra-content"><strong>Quintessential</strong> (קווינטה-סנשל). הדוגמה הטהורה והמושלמת של משהו. <em>״Apple is the quintessential premium tech brand.״</em> מילה מעולה לתאר את ״האמא של ה-X״. שווה כפי שני מילים פשוטות.</div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🧩</div>
                    <div class="extra-label">חידה יומית</div>
                    <div class="extra-content"><strong>השאלה:</strong> אבא ובנו תאומים בני 30. אבל אבא נולד לפני הבן ב-30 שנה. איך זה אפשרי?<details style="margin-top:8px;"><summary style="cursor:pointer;font-weight:600;color:var(--accent);">לחץ לתשובה</summary><p style="margin-top:8px;">בעצם הם נולדו ב-29 בפברואר (יום 366 בשנה מעוברת). יש להם רק יום הולדת אחד כל 4 שנים. אבא נולד ב-1996. בנו נולד ב-2026. אבא חגג רק 7 ימי הולדת. בנו רק 0. אז שניהם בשנה זו ״תאומים״.</p></details></div>
                    <div class="extra-source"><a href="https://www.rd.com/list/challenging-riddles/" target="_blank" rel="noopener">Reader's Digest · Challenging Riddles</a></div>
                </div>
                <div class="extra-card extra-viral">
                    <div class="extra-icon">🔥</div>
                    <div class="extra-label">הציוץ הכי ויראלי היום</div>
                    <div class="extra-content">״Meta צנחה 9%. זוקרברג עוד אומר ש-AI הוא העתיד. אבל השוק כנראה לא הולך לעבוד עם ׳אם תבנה. הם יבואו׳״ - בלומברג. 87K לייקים בשעתיים. תגובה לעלאת תקציב ההון ל-145 מיליארד דולר.</div>
                    <div class="extra-source"><a href="https://www.cnbc.com/2026/04/29/stock-market-today-live-updates.html" target="_blank" rel="noopener">CNBC · Markets Today</a></div>
                </div>
            </div>
        </section>

    </main>

    <footer class="footer">
        <div class="footer-inner">
            <p class="footer-text">Daily Me · My world, every day.</p>
            <div class="footer-nav">
                <a href="archive/2026-04-30-morning.html" class="footer-link">בוקר ↗</a>
                <a href="#" class="footer-link active">ערב</a>
                <a href="archive/2026-04-29-evening.html" class="footer-link">אתמול ↗</a>
                <a href="archive/" class="footer-link">ארכיון ↗</a>
            </div>
        </div>
    </footer>

    <script>
        const dollarHistory = [3.02, 3.01, 2.999, 2.98, 2.97, 2.97, 2.97];
    </script>
    <script src="js/script.js"></script>
</body>
</html>
'''

index_path = os.path.join(DOCS, 'index.html')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_doc)
print(f"Wrote {index_path}")

article_template_path = os.path.join(ROOT, 'src', 'article-template.html')
with open(article_template_path, 'r', encoding='utf-8') as f:
    art_tpl = f.read()

for it in items:
    uid = PREFIX + it["slug"]
    body_html = it["body"]
    filename = f'{DATE_STR}-{it["slug"]}-eve.html'
    out_path = os.path.join(ARTICLES_DIR, filename)
    art = art_tpl
    art = art.replace('{{ARTICLE_TITLE}}', html.escape(it['title']))
    art = art.replace('{{ARTICLE_CATEGORY}}', it['catLabel'])
    art = art.replace('{{ARTICLE_DATE}}', '30 באפריל 2026 · ערב')
    if it.get('image'):
        art = art.replace('{{#ARTICLE_IMAGE}}', '').replace('{{/ARTICLE_IMAGE}}', '')
        art = art.replace('{{ARTICLE_IMAGE}}', it['image'])
    else:
        art = re.sub(r'\{\{#ARTICLE_IMAGE\}\}[\s\S]*?\{\{/ARTICLE_IMAGE\}\}', '', art)
    art = art.replace('{{ARTICLE_BODY}}', body_html)
    art = art.replace('{{ARTICLE_ID}}', uid)
    art = art.replace('{{SOURCE_URL}}', it['source'])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(art)
print(f"Wrote {len(items)} article pages")

archive_filename = f'{DATE_STR}-evening.html'
archive_path = os.path.join(ARCHIVE_DIR, archive_filename)
arch = html_doc
arch = arch.replace('href="css/', 'href="../css/')
arch = arch.replace('href="js/', 'href="../js/')
arch = arch.replace('src="js/', 'src="../js/')
arch = arch.replace('href="assets/', 'href="../assets/')
arch = arch.replace('src="assets/', 'src="../assets/')
arch = arch.replace('href="articles/', 'href="../articles/')
arch = arch.replace('href="archive/', 'href="../archive/')
arch = arch.replace('href="manifest.json"', 'href="../manifest.json"')
arch = arch.replace('href="../archive/2026-04-30-morning.html"', 'href="2026-04-30-morning.html"')
arch = arch.replace('href="../archive/2026-04-29-evening.html"', 'href="2026-04-29-evening.html"')
arch = arch.replace('href="../archive/"', 'href="./"')
with open(archive_path, 'w', encoding='utf-8') as f:
    f.write(arch)
print(f"Wrote archive {archive_path}")

editions_path = os.path.join(ARCHIVE_DIR, 'editions.json')
with open(editions_path, 'r', encoding='utf-8') as f:
    editions = json.load(f)

new_entry = {
    "date": DATE_STR,
    "edition": "evening",
    "file": archive_filename,
    "label": "יום חמישי 30.4 · ערב"
}
editions = [e for e in editions if not (e.get('date') == DATE_STR and e.get('edition') == 'evening')]
editions.insert(0, new_entry)
with open(editions_path, 'w', encoding='utf-8') as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)
print("Updated editions.json")
print("DONE")
