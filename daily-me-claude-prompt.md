# Daily Me - פרומפט לקלוד קוד

## הוראות לבנייה

אתה הולך לבנות את **Daily Me** - דשבורד חדשות אישי שמתעדכן פעמיים ביום.

קרא את קובץ האפיון המלא `daily-me-spec.md` לפני שאתה מתחיל.

---

## שלב 1: מבנה הפרויקט

צור את מבנה הפרויקט הבא:

```
daily-me/
├── README.md
├── config.yaml
├── .github/
│   └── workflows/         # GitHub Actions (אם נצטרך)
├── .claude/
│   └── scheduled-tasks/
├── src/
│   ├── template.html      # תבנית HTML ראשית
│   ├── article-template.html  # תבנית לעמוד סיכום כתבה
│   ├── styles.css
│   └── script.js
├── docs/
│   ├── index.html
│   └── articles/
└── assets/
    ├── logo.svg
    └── icons/
```

## שלב 2: קובץ קונפיגורציה

צור `config.yaml` עם כל ההגדרות האישיות. ראה את האפיון לדוגמה מלאה.

## שלב 3: תבנית HTML

בנה תבנית HTML מודרנית ופרימיום:

### דרישות עיצוב:
- **RTL מלא** - כל הטקסט בעברית, direction: rtl
- **דארק/לייט מוד** - toggle ב-header, שמירה ב-localStorage
- **רספונסיבי** - grid שמתאים ל-3 עמודות (דסקטופ) → 2 (טאבלט) → 1 (מובייל)
- **פונט:** Heebo מ-Google Fonts
- **אנימציות:** fade-in staggered לכל card, transitions חלקים
- **נראה מיליון דולר** - whitespace נדיב, border-radius, shadows עדינים, gradients

### מבנה הדף:
1. **Header:** לוגו Daily Me + "מהדורת בוקר/ערב" + תאריך עברי + toggle דארק/לייט
2. **Hero:** ברכה אישית + הפתעה יומית (ציטוט/בדיחה/טריוויה - מתחלף כל יום)
3. **סקשנים ב-cards:**
   - מזג אוויר + המלצת לבוש (עם אייקון מונפש)
   - לוח שנה: חגים + פגישות
   - שער דולר + sparkline שבועי
   - חדשות AI (3-5 חדשות)
   - פוליטיקה ישראלית (3-5 חדשות)
   - ספורט: דני אבדיה / מסי (רק אם יש - אחרת לא מוצג)
   - סדרות (רק אם יש - אחרת לא מוצג)
   - גל גדות (רק אם יש - אחרת לא מוצג)
4. **Footer:** "Powered by Daily Me" + GitHub link

### Cards של חדשות - מבנה:
```html
<div class="news-card">
  <img src="[og:image מהכתבה]" alt="..." class="card-image" />
  <div class="card-content">
    <span class="card-category">חדשות AI</span>
    <h3 class="card-title">כותרת חדה</h3>
    <p class="card-summary">2-3 משפטי סיכום בעברית</p>
    <a href="articles/[article-id].html" class="read-more">קרא עוד ←</a>
  </div>
</div>
```

### עמוד סיכום כתבה (article page):
- כותרת
- תמונה (og:image)
- סיכום מלא בעברית (~1 דקה קריאה)
- קישור "למקור המלא →" לכתבה המקורית
- כפתור "חזרה לדשבורד"
- אותו עיצוב (דארק/לייט, פונט, סגנון)

## שלב 4: Scheduled Tasks

צור שני scheduled tasks:

### מהדורת בוקר (06:00):
```
כל יום ב-06:00 - מהדורת בוקר של Daily Me:

1. קרא את config.yaml
2. אסוף מידע:
   - מזג אוויר ברעננה (API) + המלצת לבוש
   - שער דולר (API) + שינוי מאתמול
   - חדשות AI מהלילה (web search) - 3-5 חדשות משמעותיות
   - חדשות פוליטיקה ישראלית (web search) - 3-5 חדשות
   - דני אבדיה + מסי (web search) - רק אם יש חדשות
   - סדרות מהרשימה (web search) - רק אם יש חדשות
   - גל גדות (web search) - רק אם יש
   - פגישות היום מ-Google Calendar
   - חגים/אירועים ישראליים (Hebcal API)
   - הפתעה יומית (ציטוט/בדיחה/טריוויה - סוג שונה כל יום)
3. לכל חדשה:
   - כתוב כותרת חדה בעברית
   - כתוב 2-3 משפטי סיכום בעברית (גם אם המקור באנגלית)
   - שלוף og:image מהמקור
   - צור עמוד סיכום מלא בעברית (article page)
   - שמור קישור למקור המלא
4. מלא את template.html עם כל המידע
5. שמור כ-docs/index.html
6. Git commit + push
```

### מהדורת ערב (18:00):
```
אותו דבר אבל:
- ברכת ערב במקום בוקר
- סיכום חדשות היום (לא הלילה)
- פגישות מחר במקום היום
- תחזית מזג אוויר למחר
- הפתעה שונה מהבוקר
```

## שלב 5: עיצוב CSS

### צבעוניות:
- לייט: רקע #FAFAFA, כרטיסים #FFFFFF, טקסט #1A1A1A
- דארק: רקע #0F0F0F, כרטיסים #1A1A1A, טקסט #E5E5E5
- אקסנט: gradient עדין (בחר צבעים מודרניים שעובדים בשני המצבים)
- ירוק לשינוי חיובי (דולר), אדום לשלילי

### אנימציות:
```css
/* Staggered fade-in */
.card { animation: fadeInUp 0.6s ease forwards; opacity: 0; }
.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
/* ... */

/* Dark mode transition */
body { transition: background-color 0.3s, color 0.3s; }
```

## שלב 6: JavaScript

- Toggle דארק/לייט מוד + שמירה ב-localStorage
- Sparkline לשער הדולר (canvas או SVG)
- Skeleton loading
- Smooth scroll
- אנימציות hover על cards

## שלב 7: README

README מרשים עם:
- Screenshots (דסקטופ + מובייל, דארק + לייט)
- "What is Daily Me?" - הסבר קצר
- Quick Start ב-3 שלבים
- הסבר config.yaml
- Contributing guidelines
- License: MIT

---

## עקרונות חשובים:
1. **הכל בעברית** - כל הממשק, כל הסיכומים, כל ההמלצות
2. **תמציתי** - כותרת + 2-3 משפטים ב-dashboard, סיכום מלא בעמוד נפרד, מקור בקישור
3. **רק מה שרלוונטי** - אם אין חדשות על מסי, לא מציגים את הסקשן
4. **נראה מיליון דולר** - כל פיקסל חשוב
5. **Fork-friendly** - הכל דרך config.yaml, אין hardcoded values
