# Daily Me - אפיון מלא

## My world, every day.

---

## 1. סקירה כללית

**Daily Me** הוא דשבורד חדשות אישי שמתעדכן פעמיים ביום (בוקר וערב), מציג למשתמש את כל מה שרלוונטי עבורו במקום אחד. הפרויקט בנוי כ-open source כך שכל אחד יכול לעשות fork ולהתאים לעצמו דרך קובץ קונפיגורציה.

**טכנולוגיה:** Claude Code scheduled task שמייצר HTML סטטי → מתארח ב-GitHub Pages.

**שפה:** עברית (RTL מלא).

**עיצוב:** מודרני, פרימיום, רספונסיבי (מובייל + דסקטופ), דארק מוד + לייט מוד.

**זמן קריאה:** כ-10 דקות למהדורה.

---

## 2. מהדורות

### מהדורת בוקר (06:00-07:00)
הדגש: מה קרה בלילה + מה מחכה לך היום.

**מבנה:**
1. ברכת בוקר אישית + הפתעה (ציטוט / בדיחה / טריוויה / עובדה מעניינת - כל יום משהו אחר)
2. מזג אוויר ברעננה + המלצת לבוש ("היום 18°, עננות חלקית - סוודר קל וג'קט לערב")
3. לוח שנה: פגישות היום מגוגל קלנדר + חגים/אירועים ארציים
4. שער הדולר (עדכני + שינוי מאתמול)
5. חדשות AI גדולות מהלילה
6. חדשות פוליטיות בישראל
7. ספורט: דני אבדיה / מסי (רק אם יש חדשות)
8. סדרות ורכילות רלוונטית
9. גל גדות (רק אם יש חדשות)

### מהדורת ערב (18:00-19:00)
הדגש: סיכום היום + הצצה למחר.

**מבנה:**
1. ברכת ערב + הפתעה (שונה מהבוקר)
2. סיכום מזג האוויר של היום + תחזית למחר
3. פגישות מחר + אירועים קרובים
4. שער הדולר (סגירה + שינוי יומי)
5. סיכום חדשות AI של היום
6. סיכום פוליטי של היום
7. ספורט: דני אבדיה / מסי (רק אם יש חדשות)
8. סדרות ורכילות רלוונטית
9. גל גדות (רק אם יש חדשות)

---

## 3. סקשנים - פירוט

### 3.1 ברכה + הפתעה יומית
- בוקר: "בוקר טוב!" / ערב: "ערב טוב!"
- כל יום הפתעה שונה מסוג אחר:
  - ציטוט מעורר השראה
  - בדיחה
  - טריוויה
  - עובדה מעניינת
  - "היום בהיסטוריה"
  - חידה
- הסוג מתחלף כדי שלא יהיה משעמם

### 3.2 מזג אוויר + המלצת לבוש
- **מקור:** API של מזג אוויר (OpenWeatherMap / WeatherAPI)
- **עיר:** רעננה (ניתן לשינוי בקונפיג)
- **תצוגה:** טמפרטורה נוכחית, מינימום/מקסימום, תחושת חום, לחות, סיכוי גשם
- **המלצת לבוש:** משפט טבעי בעברית:
  - "חולצה קצרה ומשקפי שמש"
  - "סוודר קל, לקחת מטריה ליתר ביטחון"
  - "קר! מעיל חורף וצעיף"
- **אייקונים:** שמש/עננים/גשם/ברד וכו'

### 3.3 לוח שנה
**חגים ואירועים ארציים:**
- חגים יהודיים / ישראליים
- ימי זיכרון ואירועים לאומיים
- אם יש חג - תצוגה בולטת עם אייקון מתאים

**פגישות אישיות:**
- שליפה מ-Google Calendar API
- תצוגה כרונולוגית: שעה, שם הפגישה, משתתפים
- בוקר: פגישות היום
- ערב: פגישות מחר

### 3.4 שער הדולר
- שער דולר-שקל עדכני
- שינוי באחוזים מאתמול (ירוק/אדום)
- גרף מיני של השבוע האחרון (sparkline)
- **מקור:** Bank of Israel API / Currency API

### 3.5 חדשות AI
- 3-5 חדשות AI משמעותיות
- **פורמט קצר ותמציתי:**
  - כותרת חדה (משפט אחד)
  - 2-3 משפטי סיכום בעברית, לא יותר
  - קישור "קרא עוד →" לכתבה המקורית
- **מקורות אפשריים:** חיפוש רשת עדכני, TechCrunch, The Verge, Hacker News, ArsTechnica
- **סינון:** רק חדשות משמעותיות, לא כל בלוג פוסט

### 3.6 פוליטיקה ישראלית
- 3-5 חדשות פוליטיות עיקריות
- **פורמט קצר ותמציתי:**
  - כותרת חדה (משפט אחד)
  - 2-3 משפטי סיכום, לא יותר
  - קישור "קרא עוד →" לכתבה המקורית
- **מקורות אפשריים:** חיפוש רשת עדכני, ynet, הארץ, וואלה, כאן
- **סגנון:** עובדתי, לא פרשני

### 3.7 ספורט
- **דני אבדיה בלבד:** סטטיסטיקות משחק אחרון, חדשות העברה, פציעות
- **מסי בלבד:** גולים, חדשות, שיאים
- **מוצג רק אם יש חדשות** - אם אין, הסקשן לא מופיע
- סטטיסטיקות בולטות עם מספרים גדולים

### 3.8 סדרות ורכילות
**סדרות שנעקבות:**
- הישרדות (ישראל)
- Survivor (US)
- Beast Games
- The Traitors
- Squid Game
- Squid Game: The Challenge
- Friends
- הכוכב הבא
- רוקדים עם כוכבים
- בריג'רטון

**סוג התוכן:**
- מי הודח / מי ניצח
- דירוגי צפייה
- עונות חדשות שהוכרזו
- קליפים ויראליים
- רכילות שחקנים
- **מוצג רק אם יש חדשות**

### 3.9 גל גדות
- חדשות, פרויקטים חדשים, ראיונות, פוסטים בולטים
- **מוצג רק אם יש חדשות**

---

## 4. עיצוב

### 4.1 עקרונות
- **פרימיום:** נראה כמו מוצר של חברה גדולה, לא פרויקט צד
- **נקי:** הרבה whitespace, טיפוגרפיה ברורה
- **תמציתי בשלושה שלבים:**
  1. **Dashboard:** כותרת + 2-3 משפטי סיכום
  2. **לחיצה על "קרא עוד →":** עמוד סיכום מלא בעברית (~1 דקה קריאה), מתורגם ומסוכם גם אם המקור באנגלית
  3. **בתוך הסיכום:** קישור "למקור המלא →" לכתבה המקורית בשפת המקור
- **אנימציות:** עדינות בטעינה, transitions חלקים בין סקשנים
- **צבעוניות:** מודרנית ונקייה, gradients עדינים

### 4.2 תמונות ואיורים

**תמונות מכתבות:**
- כל חדשה שולפת את ה-Open Graph image (og:image) מהכתבה המקורית
- התמונה מוצגת ב-card מעל הכותרת והסיכום
- אם אין og:image - מוצג fallback (איור Nano Banana לפי נושא הסקשן)
- תמונות ב-aspect ratio אחיד (16:9) עם object-fit: cover

**איורי Nano Banana (Google AI Studio API):**
- לוגו Daily Me
- איור header למהדורת בוקר (שמש, קפה, עיתון)
- איור header למהדורת ערב (ירח, ספה, נר)
- אייקוני סקשנים: מזג אוויר, דולר, AI, פוליטיקה, ספורט, סדרות, לוח שנה
- Fallback images לכתבות בלי תמונה (אייקון כללי לפי קטגוריה)

**פרומפטים ל-Nano Banana:**

1. **לוגו:**
   "Design a minimal, modern logo for 'Daily Me' - a personalized daily news dashboard. Clean lines, flat design, newspaper/digital feel. Hebrew-friendly. SVG style, white background."

2. **Header בוקר:**
   "Flat illustration, morning scene: steaming coffee cup next to a folded newspaper, warm sunrise colors, golden light, minimal style, no text, 16:9 aspect ratio."

3. **Header ערב:**
   "Flat illustration, evening scene: cozy reading nook with warm lamp light, city skyline at dusk through a window, calm purple and orange tones, minimal style, no text, 16:9 aspect ratio."

4. **אייקון מזג אוויר:**
   "Minimal flat icon: sun with a small cloud, warm colors, clean lines, SVG style, transparent background."

5. **אייקון שער דולר:**
   "Minimal flat icon: dollar sign with shekel sign, exchange arrows between them, clean lines, SVG style, transparent background."

6. **אייקון AI:**
   "Minimal flat icon: brain with circuit patterns, modern tech feel, clean lines, SVG style, transparent background."

7. **אייקון פוליטיקה:**
   "Minimal flat icon: Knesset building silhouette, clean lines, SVG style, transparent background."

8. **אייקון ספורט:**
   "Minimal flat icon: basketball and soccer ball side by side, clean lines, SVG style, transparent background."

9. **אייקון סדרות:**
   "Minimal flat icon: TV screen with play button, popcorn, clean lines, SVG style, transparent background."

10. **אייקון לוח שנה:**
    "Minimal flat icon: calendar page with Star of David, clean lines, SVG style, transparent background."

11. **Fallback תמונה - חדשות כלליות:**
    "Minimal flat illustration: stack of newspapers with a magnifying glass, neutral colors, clean lines, 16:9 aspect ratio."

### 4.3 Layout
- **Header:** לוגו Daily Me + תאריך + שעת עדכון + toggle דארק/לייט
- **Hero:** ברכה + הפתעה יומית
- **Grid:** סקשנים מסודרים ב-cards
  - דסקטופ: 2-3 עמודות
  - מובייל: עמודה אחת
- **Footer:** "Powered by Daily Me" + קישור ל-GitHub

### 4.3 Cards
- כל סקשן ב-card עם:
  - אייקון ייחודי לסקשן
  - כותרת הסקשן
  - תוכן
  - רקע עדין שונה לכל סקשן
- Hover effects בדסקטופ
- Border-radius מעוגל

### 4.4 טיפוגרפיה
- פונט עברי איכותי (Heebo / Assistant / Rubik)
- היררכיה ברורה: כותרת ראשית > כותרת סקשן > כותרת חדשה > תוכן
- גדלים נוחים לקריאה

### 4.5 דארק מוד / לייט מוד
- Toggle בולט ב-header
- שמירת העדפה ב-localStorage
- צבעים מותאמים לשני המצבים
- מעבר חלק עם transition

### 4.6 רספונסיבי
- **דסקטופ (1200px+):** 3 עמודות, layout מרווח
- **טאבלט (768-1199px):** 2 עמודות
- **מובייל (עד 767px):** עמודה אחת, כפתורים גדולים, touch-friendly

### 4.7 אנימציות
- Fade-in בטעינת הדף
- Staggered animation לכל card
- Sparkline מונפש לשער הדולר
- אייקון מזג אוויר מונפש (שמש זורחת, גשם יורד)
- Skeleton loading בזמן טעינה

---

## 5. ארכיטקטורה טכנית

### 5.1 תהליך עדכון
```
Scheduled Task (Claude Code)
    ├── אוסף מידע ממקורות שונים (APIs + web search)
    ├── מעבד ומסכם בעברית
    ├── מייצר קובץ HTML סטטי
    ├── Git commit + push ל-GitHub
    └── GitHub Pages מגיש את הדף
```

### 5.2 Scheduled Tasks
- **מהדורת בוקר:** כל יום ב-06:00
- **מהדורת ערב:** כל יום ב-18:00

### 5.3 מבנה הפרויקט
```
daily-me/
├── README.md              # תיעוד + screenshots
├── config.yaml            # קונפיגורציה אישית
├── .claude/
│   └── scheduled-tasks/   # Claude Code tasks
├── src/
│   ├── template.html      # תבנית HTML
│   ├── styles.css         # עיצוב
│   └── script.js          # דארק מוד, אנימציות
├── docs/                  # GitHub Pages root
│   ├── index.html         # הדף הנוכחי (מיוצר אוטומטית)
│   ├── articles/          # עמודי סיכום מלאים (מיוצרים אוטומטית)
│   │   └── 2026-03-19-openai-new-model.html  # דוגמה
│   └── archive/           # מהדורות קודמות
└── assets/
    ├── logo.svg
    └── icons/
```

### 5.4 קובץ קונפיגורציה (config.yaml)
```yaml
# Daily Me Configuration
name: "ג'יי"
language: "he"

# Location
weather:
  city: "Ra'anana"
  country: "IL"

# Content Sections
sections:
  weather: true
  dollar: true
  ai_news: true
  israel_politics: true
  calendar: true
  sports:
    enabled: true
    players:
      - "Danny Avdia"
      - "Lionel Messi"
  shows:
    enabled: true
    list:
      - "הישרדות"
      - "Survivor US"
      - "Beast Games"
      - "The Traitors"
      - "Squid Game"
      - "Squid Game: The Challenge"
      - "Friends"
      - "הכוכב הבא"
      - "רוקדים עם כוכבים"
      - "בריג'רטון"
  celebrities:
    enabled: true
    list:
      - "גל גדות"

# Google Calendar
google_calendar:
  enabled: true
  calendar_id: "primary"

# Display
theme:
  default: "light"  # light / dark

# Schedule
schedule:
  morning: "06:00"
  evening: "18:00"
```

### 5.5 APIs נדרשים
| שירות | API | שימוש |
|--------|-----|--------|
| מזג אוויר | OpenWeatherMap / WeatherAPI | תחזית + טמפרטורה |
| שער דולר | Bank of Israel / ExchangeRate API | שער + היסטוריה |
| חדשות | Claude web search | AI, פוליטיקה, ספורט, סדרות |
| לוח שנה | Google Calendar API | פגישות אישיות |
| חגים | Hebcal API | חגים ישראליים |

---

## 6. Open Source & Fork-ability

### 6.1 README.md
- Screenshots מרשימים (דסקטופ + מובייל, דארק + לייט)
- GIF של הדשבורד
- הוראות התקנה ב-3 שלבים
- הסבר על הקונפיגורציה
- Contributing guidelines

### 6.2 התאמה אישית
כל מה שמשתמש צריך לשנות נמצא ב-`config.yaml`:
- שם
- עיר
- סדרות
- ספורטאים
- סלבריטאים
- סקשנים מופעלים/מכובים

### 6.3 הרחבות עתידיות אפשריות
- סקשן מניות / קריפטו
- חדשות טכנולוגיה כללית
- מתכון יומי
- המלצת שיר / פודקאסט
- סקשן "היום בהיסטוריה"
- שליחה למייל / טלגרם
- PWA עם push notifications

---

## 7. מדדי הצלחה
- זמן טעינה: מתחת ל-2 שניות
- Lighthouse score: 95+
- קריא ונוח ב-10 דקות
- עובד מושלם במובייל
- מתעדכן בזמן ללא תקלות
