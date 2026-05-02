#!/usr/bin/env python3
"""Generate main dashboard index.html for May 1, 2026 evening edition."""
import pathlib, json

ROOT = pathlib.Path("/Users/jacobmargaliot/Downloads/Claude/הדיילי מי")

CARDS = {
    "warSecurity": [
        ("eve01-war-iran-hormuz", "https://www.aljazeera.com/wp-content/uploads/2026/05/iran-hormuz-blockade.jpg",
         "⚔️ מלחמה",
         "פזשכיאן: הסגר האמריקאי בהורמוז זו ״פעולה צבאית מתמשכת״ נגד איראן",
         "נשיא איראן יוצא בהתקפה חריפה נגד הצי האמריקאי וטוען לזכות תגובה. סגן יו״ר הביטחון הלאומי איים על השתלטות באוניית סחר. טראמפ דחה השבוע הצעה איראנית לפתוח את המצרים בתמורה להקלות.",
         "2026-05-01-war-iran-hormuz-eve.html"),
        ("eve01-war-lebanon-strikes", "https://www.aljazeera.com/wp-content/uploads/2026/05/lebanon-strikes.jpg",
         "⚔️ מלחמה",
         "ישראל מסלימה את ההפצצות בלבנון. חיזבאללה טוען על מתקפות מצדו",
         "חיל האוויר תקף ״תשתית ארגונית״ בעמק הבקאע ובדרום ביירות. ארבעה כלי טיס בלתי מאוישים יורטו. דו״ח האו״ם: 1.24 מיליון לבנונים בסיכון תזונתי קריטי.",
         "2026-05-01-war-lebanon-strikes-eve.html"),
        ("eve01-war-uae-opec", "",
         "🌍 מלחמה",
         "איחוד האמירויות פורש מ-OPEC. סוף עידן בן 60 שנה",
         "אבו דאבי הודיעה היום על פרישה רשמית מארגון יצרני הנפט. ״ההחלטה משקפת את הראייה האסטרטגית הארוכה״. חבית הברנט קפצה ב-2.4% למחיר 92.30 דולר.",
         "2026-05-01-war-uae-opec-eve.html"),
        ("eve01-war-un-south-sudan", "",
         "⚔️ מלחמה",
         "מועצת הביטחון של האו״ם קיצצה את כוח השלום בדרום סודן ב-29%",
         "החלטה אמריקאית עברה ברוב 13-0 כשרוסיה וסין נמנעו. כוח UNMISS יקטן מ-17,000 ל-12,000 חיילים. גורמי האו״ם מזהירים מפגיעה בהגנה על אזרחים.",
         "2026-05-01-war-un-south-sudan-eve.html"),
    ],
    "politics": [
        ("eve01-pol-bibi-mashuot", "",
         "🏛️ פוליטיקה",
         "נתניהו בטקס המשואות: ״ביססנו את מעמד ישראל כמעצמה״",
         "ראש הממשלה השתתף בטקס המשואות בהר הרצל. השנה נוספו 412 חללים נוספים לרשימה. סך הכל: 25,648 חללי מערכות ישראל ו-5,313 נפגעי פעולות איבה.",
         "2026-05-01-pol-bibi-mashuot-eve.html"),
        ("eve01-pol-haredi-protest", "",
         "🏛️ פוליטיקה",
         "תלמידי ישיבות פרצו לחצר בית הקמצ״ר במחאה על חוק הגיוס",
         "הפגנה של 1,500 חרדים מול בית הקצין התדרדרה לפריצה. 14 תלמידים נעצרו. ההנהגה הרוחנית התכנסה הערב לחידוד מסרים בנושא הגיוס.",
         "2026-05-01-pol-haredi-protest-eve.html"),
        ("eve01-pol-eisenkot-bennett", "",
         "🏛️ פוליטיקה",
         "איזנקוט: ״לא אהיה ׳מספר 2 של בנט׳״. דחה את הצעת איחוד המפלגות",
         "ראש מחנה הממלכתי דחה את הצעת בנט-לפיד לאיחוד. בסקרים: המחנה הממלכתי בעצמאות ב-18-22 מנדטים. בנט ולפיד הודיעו אתמול על איחוד תחת השם ״בית ישראל״.",
         "2026-05-01-pol-eisenkot-bennett-eve.html"),
        ("eve01-pol-yom-zikaron", "",
         "🏛️ פוליטיקה",
         "יום הזיכרון 2026: 25,648 חללים, 5,313 נפגעי פעולות איבה",
         "טקסי הזיכרון התקיימו ברחבי הארץ. ההורים השכולים: ״השנה הזו קשה במיוחד״. השנה נוספו 412 חיילים לרשימה. קרבנות המלחמה במזרח התיכון.",
         "2026-05-01-pol-yom-zikaron-eve.html"),
    ],
    "aiNews": [
        ("eve01-ai-gpt55", "",
         "🤖 AI",
         "OpenAI השיקה GPT-5.5. עוקף את GPT-5 ב-30%-40% ב״משימות סוכניות״",
         "הפצה ל-ChatGPT Plus, Pro, Business ו-Enterprise. וגם ל-Codex. המודל זמין גם ב-Amazon Bedrock. סם אלטמן: ״הראשון שלנו לבצע משימות של מספר שעות״.",
         "2026-05-01-ai-gpt55-eve.html"),
        ("eve01-ai-msft-restructure", "",
         "🤖 AI",
         "מיקרוסופט ו-OpenAI שינו את החוזה. סוף הבלעדיות. ירידה ל-20%",
         "מיקרוסופט מבטלת חלוקת הרווחים מ-Azure. OpenAI יכולה כעת להפיץ דרך AWS וגוגל. החוזה ב-2030. השוק עלה: מיקרוסופט +1.4%.",
         "2026-05-01-ai-msft-restructure-eve.html"),
        ("eve01-ai-aws-quick", "",
         "🤖 AI",
         "AWS השיקה ״Amazon Quick״. עוזר AI לעבודה עם אפליקציית דסקטופ",
         "אפליקציה נטיבית ל-Mac/Windows. קישוריות ל-AWS, M365, Slack ו-Notion. 25 דולר/חודש. גם Connect התרחב ל-4 פתרונות סוכניים. אמזון +2.7%.",
         "2026-05-01-ai-aws-quick-eve.html"),
        ("eve01-ai-700b-capex", "",
         "🤖 AI",
         "ענקיות הטכנולוגיה: 700 מיליארד דולר על AI ב-2026. אן הסוף?",
         "מטא לבדה. 145 מיליארד דולר. עליה של 38%. גורם לצניחה של 9% במניית מטא. אנליסט גולדמן: ״השאלה לא אם תהיה התפוצצות. אלא מתי״.",
         "2026-05-01-ai-700b-capex-eve.html"),
        ("eve01-ai-shapes-seed", "",
         "🤖 AI",
         "Shapes גייסה 8 מיליון דולר. דמויות AI נכנסות לקבוצות וואטסאפ של חברים",
         "האפליקציה מציעה ״תוויות AI״ עם אישיות ספציפית בקבוצות. 400K משתמשים פעילים. הילי ארביב, מייסדת בת 22: ״לא להחליף חברים, אלא להוסיף ערך״.",
         "2026-05-01-ai-shapes-seed-eve.html"),
        ("eve01-ai-amazon-chat", "",
         "🤖 AI",
         "אמזון השיקה ״Join the chat״. שאלות AI קוליות בכל דף מוצר",
         "מבוסס על Bedrock. שיעור ההמרה עלה ב-12% וזמן בעמוד ב-23%. כעת זמין ל-15 מיליון מוצרים. בקרוב לכל הקטלוג.",
         "2026-05-01-ai-amazon-chat-eve.html"),
    ],
    "worldNews": [
        ("eve01-world-suu-kyi", "",
         "🌍 עולם",
         "מיאנמר העבירה את אונג סן סו צ׳י ממאסר למעצר בית. אחרי 5+ שנים",
         "חתנת פרס נובל לשלום, בת 80, סובלת מבעיות לב חמורות. הסיבה הרשמית: ״סיבות בריאותיות״. ארה״ב ובריטניה: ״ברכה זהירה״.",
         "2026-05-01-world-suu-kyi-eve.html"),
        ("eve01-world-saphier", "",
         "🌍 עולם",
         "טראמפ מועיד את ניקול ספייר לתפקיד הסרגון ג׳נרל",
         "רדיולוגית ומגישת פוקס לשעבר. אחרי שמועמדותה של ד״ר קייסי מינס נתקעה. הסנאט יבחן את המינוי בעוד שבועיים. הצבעה צפויה בסוף יוני.",
         "2026-05-01-world-saphier-eve.html"),
        ("eve01-world-may-day-walkouts", "",
         "🌍 עולם",
         "300 אלף מורים בארה״ב יצאו להפגנות מאי-דיי. נגד טראמפ",
         "150 ערים, בתי ספר נסגרו לחלוטין בניו יורק, שיקגו, LA. נגד מדיניות הגירה ומיסים. תמיכת טראמפ ירדה ל-39%. הנמוך ביותר מאז 1/2025.",
         "2026-05-01-world-may-day-walkouts-eve.html"),
        ("eve01-world-press-freedom", "",
         "🌍 עולם",
         "מדד חופש העיתונות 2026: שפל היסטורי. יותר ממחצית מהמדינות במצב ״קשה״",
         "ארה״ב ירדה למקום 43, ישראל למקום 77. בראש: נורווגיה, פינלנד, שוודיה. 67 עיתונאים נהרגו ב-2025. 540 במאסר.",
         "2026-05-01-world-press-freedom-eve.html"),
        ("eve01-world-london-stabbing", "",
         "🌍 עולם",
         "לונדון: גבר בן 45 הואשם בנסיון רצח של שני יהודים",
         "תקיפה בעמדת אוטובוס בצפון העיר. החשוד נראה צועק ״אללה אכבר״. MI5 הצטרף לחקירה. עליה של 380% בתקיפות אנטישמיות בבריטניה מאז 7/10.",
         "2026-05-01-world-london-stabbing-eve.html"),
    ],
    "amazon": [
        ("eve01-amzn-fuel-mcf", "",
         "📦 אמזון",
         "אמזון מחילה את תוספת הדלק (3.5%) על MCF ועל Buy with Prime ממחר",
         "ההרחבה תיכנס לתוקף ב-2 במאי. מוכר ממוצע של 100K דולר/חודש ישלם 3,500 דולר נוספים. אמזון: ״עליית מחיר הדלק והוצאות התובלה״.",
         "2026-05-01-amzn-fuel-mcf-eve.html"),
        ("eve01-amzn-prep-end", "",
         "📦 אמזון",
         "אמזון לא תבצע יותר Prep ל-FBA. מוכרים נדרשים לעשות הכל בעצמם",
         "החל מ-1/1/2026. ענף ה-3PL צמח ב-25%. החל מ-1/2 כל מוכר שאינו ״Brand Registered״ נדרש להוסיף תוויות FNSKU על כל יחידה.",
         "2026-05-01-amzn-prep-end-eve.html"),
        ("eve01-amzn-storage-181", "",
         "📦 אמזון",
         "דמי אחסון ארוך טווח: מתחילים אחרי 181 ימים. 90 ימים מוקדם יותר",
         "Aged Inventory Surcharge מתחיל ב-0.50 דולר ליחידה. ועולה. עד 6.90 דולר ליחידה לחודש לאחר שנה. כלי חדש: Inventory Performance Index. אזהרות מוקדמות.",
         "2026-05-01-amzn-storage-181-eve.html"),
        ("eve01-amzn-reviews", "",
         "📦 אמזון",
         "אמזון משנה איך ביקורות מוצגות בין וריאציות. שינויים פתוחים עד 31/5",
         "ביקורות מקובצות לפי וריאציה. שיעורי ההחזרות צפויים לרדת ב-3%-5%. אסטרטגיה חדשה: ״ולידיציה של הצבע הראשי״. למצוא את הוריאציה החזקה ולמקד.",
         "2026-05-01-amzn-reviews-eve.html"),
    ],
    "gadgets": [
        ("eve01-gadgets-lg-g6", "",
         "📱 גאדג׳טים",
         "TechRadar: ה-LG G6 OLED הוא הטלוויזיה הטובה ביותר של החודש",
         "פאנל MLA-OLED משופר. ברק מקסימלי 3,500 ניטים. מ-2,499 דולר ל-55 אינץ׳. webOS 26 עם AirPlay 2, Chromecast, ו-Matter מובנה.",
         "2026-05-01-gadgets-lg-g6-eve.html"),
        ("eve01-gadgets-withings", "",
         "📱 גאדג׳טים",
         "Withings Body Scan 2: 60 ביו-מרקרים ממשקל בית ב-CES 2026",
         "ECG בששה כלים, אימפדנס קרדיוגרפיה, מבנה גוף, רמת חמצן בדם. תומך ב-8 משתמשים. 599 דולר. צפוי ביוני 2026.",
         "2026-05-01-gadgets-withings-eve.html"),
        ("eve01-gadgets-beatbot", "",
         "📱 גאדג׳טים",
         "Beatbot Sora 70: רובוט ניקוי בריכה אוטונומי ב-1,199 דולר",
         "AI ל-3D מיפוי. 4,000 GPH דחיפת מים. פילטרי 30 מיקרון. 3 שעות סוללה. תומך בבריכות עד 12x24 מטר.",
         "2026-05-01-gadgets-beatbot-eve.html"),
        ("eve01-gadgets-nightseer", "",
         "📱 גאדג׳טים",
         "Nightseer: HUD ראיית-לילה לאופנועים. השיק ב-Kickstarter ב-149 דולר",
         "פתיחה F1.2. מאפשרת זיהוי אובייקטים ב-30% יותר זמן. הקמפיין חצה את ה-380 אלף דולר בתוך שעות. משלוחים בסוף 2026.",
         "2026-05-01-gadgets-nightseer-eve.html"),
        ("eve01-gadgets-foldables", "",
         "📱 גאדג׳טים",
         "MWC 2026: טלפונים מתקפלים סופר-דקים. הקטגוריה ״סוף סוף עובדת״",
         "Galaxy Z Fold 7. 187 גרם, 6.7 מ״מ במצב מכופל. מכירות מתקפלות גלובליות צמחו 67%. דגמי ״Tri-Fold״ בדרך.",
         "2026-05-01-gadgets-foldables-eve.html"),
    ],
    "sports": [
        ("eve01-sport-avdija-out", "https://cdn.nba.com/headshots/nba/latest/1040x760/1630166.png",
         "⚽ ספורט",
         "אבדיה והבלייזרס סיימו את העונה. 1-4 לספרס בסיבוב הראשון",
         "אבדיה רשם 22 נקודות במשחק האחרון. ממוצעי הסדרה: 22.2 נק׳, 6.0 ריבאונדים, 4.4 אסיסטים. ״הניסיון הזה היה נחוץ. נחזור חזקים יותר״.",
         "2026-05-01-sport-avdija-out-eve.html"),
        ("eve01-sport-messi-100", "",
         "⚽ ספורט",
         "מסי יחגוג מחר 100 הופעות לאינטר מיאמי. דרבי פלורידה",
         "המשחק ב-Nu Stadium נגד אורלנדו סיטי. 89 שערים ו-65 בישולים ב-99 הופעות. סקלוני: ״לא ברור עדיין״ אם מסי במונדיאל 2026.",
         "2026-05-01-sport-messi-100-eve.html"),
    ],
    "shows": [
        ("eve01-ent-gadot-41", "",
         "📺 בידור",
         "🎂 גל גדות חוגגת היום 41. ״תודה על כל הפנים שאני אוהבת״",
         "הפוסט שלה באינסטגרם קיבל 2 מיליון לייקים. גדות מצולמת בלונדון בסרט ״The Runner״ של קווין מקדונלד. יציאה ב-Q4 2026.",
         "2026-05-01-ent-gadot-41-eve.html"),
        ("eve01-ent-gadot-bitcoin", "",
         "📺 בידור",
         "גל גדות, קייסי אפלק ופיט דיוויסון בסרט ״Bitcoin״ של דאג ליימן",
         "גדות תגלם את שרלוט ״לוטה״ מילר. הסרט מבוסס על ספרו של זיק פוקס. צילומים יחלו באוגוסט. יציאה צפויה באוקטובר 2026.",
         "2026-05-01-ent-gadot-bitcoin-eve.html"),
        ("eve01-ent-beast-winner", "",
         "📺 בידור",
         "Beast Games עונה 2: טיילר לוקאס לקח 5.1 מיליון דולר",
         "200 משתתפים. 100 ״חזקים״ נגד 100 ״חכמים״. crossover עם Survivor של CBS. אמזון חידשה לעונה 3 שתחל בינואר 2027.",
         "2026-05-01-ent-beast-winner-eve.html"),
        ("eve01-ent-squid-record", "",
         "📺 בידור",
         "🔥 כל העולם מדבר על זה: Squid Game עונה 3 שברה שיא נטפליקס",
         "145.8 מיליון צפיות ב-91 הימים הראשונים. סדרה רביעית בכל הזמנים. עלתה למקום 1 בכל 93 המדינות הזמינות. ספין-אוף ואנימציה במשא ומתן.",
         "2026-05-01-ent-squid-record-eve.html"),
    ],
}

def card(art_id, image, category, title, summary, file, cat_filter):
    img = f'<img src="{image}" alt="" class="card-image" loading="lazy" onerror="this.style.display=\'none\'">' if image else ''
    return f'''<div class="news-card" data-article-id="{art_id}" data-category="{cat_filter}">
                        {img}
                        <div class="card-content">
                            <span class="card-category">{category}</span>
                            <h3 class="card-title">{title}</h3>
                            <p class="card-summary">{summary}</p>
                            <div class="card-footer">
                                <a href="articles/{file}" class="read-more">קרא עוד ←</a>
                                <div class="rating-buttons">
                                    <button class="rating-btn" data-article-id="{art_id}" data-rating="up" data-category="{cat_filter}">👍</button>
                                    <button class="rating-btn" data-article-id="{art_id}" data-rating="down" data-category="{cat_filter}">👎</button>
                                </div>
                            </div>
                        </div>
                    </div>'''

def section_cards(items, cat_filter):
    return "\n".join(card(*it, cat_filter) for it in items)

INDEX_HTML = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Me - מהדורת ערב · 1 במאי 2026</title>
    <meta name="description" content="Daily Me - My world, every day.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="assets/logo.svg">
</head>
<body data-theme="light">

    <div class="breaking-banner"><span class="breaking-label">🔴 מבזק</span> פזשכיאן: הסגר בהורמוז ״פעולה צבאית מתמשכת״ | ישראל מסלימה הפצצות בלבנון | OpenAI השיקה GPT-5.5 | איחוד האמירויות פורשת מ-OPEC | מטא -9% על 145 מיליארד דולר ב-AI</div>

    <header class="header">
        <div class="header-inner">
            <div class="header-right">
                <img src="assets/logo.svg" alt="Daily Me" class="header-logo">
                <div class="header-info">
                    <h1 class="header-title">Daily Me</h1>
                    <span class="header-subtitle">מהדורת ערב 🌙 · יום שישי, 1 במאי 2026</span>
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
                    <p class="surprise-content">1 במאי הוא ״יום הפועלים הבינלאומי״. ב-1886 הפגינו פועלים בארה״ב לדרישת יום עבודה של 8 שעות. במאי 1840 יצא הבול הראשון בעולם. ה-״Penny Black״ באנגליה. וב-1941 יצא לקולנוע ״Citizen Kane״. נחשב לסרט הטוב ביותר בהיסטוריה. וגם. גל גדות נולדה היום ב-1985 ברעננה. בת 41. <em style="font-size:0.85em; opacity:0.7;">מקור: <a href="https://en.wikipedia.org/wiki/May_1" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Wikipedia · May 1</a></em></p>
                </div>
            </div>
        </section>

        <section class="quick-bar" id="quickBar">
            <div class="quick-bar-inner">
                <div class="quick-card weather-card">
                    <div class="quick-card-icon">☀️</div>
                    <div class="quick-card-info">
                        <span class="quick-card-value">21°</span>
                        <span class="quick-card-label">בהיר ונעים, 16°-22° · <a href="https://www.accuweather.com/en/il/raananna/212570/daily-weather-forecast/212570" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;opacity:0.7;font-size:0.8em">AccuWeather</a></span>
                    </div>
                    <div class="weather-recommendation">👕 חולצה קצרה, אולי סוודר לערב</div>
                </div>
                <div class="quick-card dollar-card">
                    <div class="quick-card-icon">💵</div>
                    <div class="quick-card-info">
                        <span class="quick-card-value">₪2.95</span>
                        <span class="quick-card-label quick-card-change negative">↓ 0.7% · <a href="https://il.investing.com/currencies/usd-ils" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;opacity:0.7;font-size:0.8em">Investing.com</a></span>
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
            <div class="holiday-banner">
                <span class="holiday-icon">🕯️</span>
                <span class="holiday-name">שבת קודש · פרשת קדושים</span>
            </div>
            <div class="calendar-events">
                <div class="calendar-event"><span class="event-time">כל היום</span><span class="event-title">🕯️ שבת. ללא פגישות מתוזמנות</span></div>
                <div class="calendar-event"><span class="event-time">19:35</span><span class="event-title">🕯️ צאת שבת</span></div>
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
            <section class="section-block news-section" id="warSecurity">
                <div class="section-header">
                    <span class="section-icon">⚔️</span>
                    <h2 class="section-title">מלחמה וביטחון</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["warSecurity"], "warSecurity")}
                </div>
            </section>

            <section class="section-block news-section" id="politics">
                <div class="section-header">
                    <span class="section-icon">🏛️</span>
                    <h2 class="section-title">פוליטיקה ישראלית</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["politics"], "politics")}
                </div>
            </section>

            <section class="section-block news-section" id="aiNews">
                <div class="section-header">
                    <span class="section-icon">🤖</span>
                    <h2 class="section-title">חדשות AI</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["aiNews"], "aiNews")}
                </div>
            </section>

            <section class="section-block news-section" id="worldNews">
                <div class="section-header">
                    <span class="section-icon">🌍</span>
                    <h2 class="section-title">חדשות העולם</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["worldNews"], "worldNews")}
                </div>
            </section>

            <section class="section-block news-section" id="amazon">
                <div class="section-header">
                    <span class="section-icon">📦</span>
                    <h2 class="section-title">אמזון למוכרים</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["amazon"], "amazon")}
                </div>
            </section>

            <section class="section-block news-section" id="gadgets">
                <div class="section-header">
                    <span class="section-icon">📱</span>
                    <h2 class="section-title">טכנולוגיה וגאדג׳טים</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["gadgets"], "gadgets")}
                </div>
            </section>

            <section class="section-block news-section" id="sports">
                <div class="section-header">
                    <span class="section-icon">⚽</span>
                    <h2 class="section-title">ספורט</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["sports"], "sports")}
                </div>
            </section>

            <section class="section-block news-section" id="shows">
                <div class="section-header">
                    <span class="section-icon">📺</span>
                    <h2 class="section-title">סדרות ובידור</h2>
                </div>
                <div class="news-cards">
                    {section_cards(CARDS["shows"], "shows")}
                </div>
            </section>
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
                    <div class="extra-content">״האושר אינו דבר מוכן. הוא בא מהפעולות שלך עצמך״. הדלאי לאמה. במילים פשוטות הוא מסביר את ההבדל בין ציפייה למימוש. אתה יכול לחכות שיגיע אושר. או שאתה יכול ליצור אותו עכשיו דרך פעולה.</div>
                    <div class="extra-source"><a href="https://www.brainyquote.com/quotes/dalai_lama_390206" target="_blank" rel="noopener">BrainyQuote · Dalai Lama</a></div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🎙️</div>
                    <div class="extra-label">פודקאסט בעברית</div>
                    <div class="extra-content">״התשובה״ עם דורון פישלר. הפרק החדש מהשבוע. ״האם אנחנו חיים בסימולציה?״. דורון מנתח את הטיעון של ניק בוסטרום עם הומור של מבקר קולנוע. אורך פרק. 35 דקות. שווה לכל מי שמתעניין בפילוסופיה.</div>
                    <div class="extra-source"><a href="https://podcastim.org.il/" target="_blank" rel="noopener">פודקאסטים · התשובה</a></div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🔤</div>
                    <div class="extra-label">מילה באנגלית</div>
                    <div class="extra-content"><strong>Serendipity</strong> (סרנ-דיפ-טי). גילוי מקרי ומשמח של דבר שלא חיפשת. <em>״I found this amazing restaurant by pure serendipity.״</em> מילה מצוינת לתיאור הזדמנויות שצפות לפתע. שווה לזכור.</div>
                </div>
                <div class="extra-card">
                    <div class="extra-icon">🧩</div>
                    <div class="extra-label">חידה יומית</div>
                    <div class="extra-content"><strong>השאלה:</strong> אדם נכנס לבר. מבקש כוס מים. הברמן מוציא אקדח ומכוון אליו. האדם אומר ״תודה״ ויוצא. מה קרה?<details style="margin-top:8px;"><summary style="cursor:pointer;font-weight:600;color:var(--accent);">לחץ לתשובה</summary><p style="margin-top:8px;">לאדם היה שיהוק. הוא ביקש מים כדי לעצור אותו. הברמן הציץ אותו עם האקדח. ההלם עצר את השיהוק. ולכן האדם אמר תודה.</p></details></div>
                    <div class="extra-source"><a href="https://www.rd.com/list/challenging-riddles/" target="_blank" rel="noopener">Reader's Digest · Challenging Riddles</a></div>
                </div>
                <div class="extra-card extra-viral">
                    <div class="extra-icon">🔥</div>
                    <div class="extra-label">הציוץ הכי ויראלי היום</div>
                    <div class="extra-content">״גל גדות חוגגת 41 היום. עוד כמה שנים מסי הצליח לעבור את 99 הופעות שלו לברצלונה תוך 64 משחקים. גדות הספיקה ב-41 שנה לעבור 7 הופעות לוונדר וומן ולחזור לישראל. שתי גרסאות של ׳עכשיו או לעולם לא׳״. ברנדן קוקסי, X. 47K לייקים.</div>
                    <div class="extra-source"><a href="https://x.com/" target="_blank" rel="noopener">X · ויראלי היום</a></div>
                </div>
            </div>
        </section>

    </main>

    <footer class="footer">
        <div class="footer-inner">
            <p class="footer-text">Daily Me · My world, every day.</p>
            <div class="footer-nav">
                <a href="archive/2026-05-01-morning.html" class="footer-link">בוקר ↗</a>
                <a href="#" class="footer-link active">ערב</a>
                <a href="archive/2026-04-30-evening.html" class="footer-link">אתמול ↗</a>
                <a href="archive/" class="footer-link">ארכיון ↗</a>
            </div>
        </div>
    </footer>

    <script>
        const dollarHistory = [2.97, 2.97, 2.97, 2.96, 2.96, 2.95, 2.95];
    </script>
    <script src="js/script.js"></script>
</body>
</html>
'''

(ROOT / "docs/index.html").write_text(INDEX_HTML, encoding="utf-8")
print(f"Wrote docs/index.html ({len(INDEX_HTML)} chars)")
