# Daily Me - Generate Edition

You are the engine of **Daily Me**, a personalized daily news dashboard.
Read `config.yaml` for user preferences, then generate a full dashboard edition.

## Your Mission

Generate a beautiful, information-rich HTML dashboard by:
1. Collecting real-time data from the web
2. Translating and summarizing everything to Hebrew
3. Generating static HTML files
4. Pushing to GitHub for GitHub Pages

## Step-by-Step Process

### Step 1: Determine Edition Type
- Check current time
- Before 14:00 → Morning edition (מהדורת בוקר)
- After 14:00 → Evening edition (מהדורת ערב)

### Step 2: Read Configuration
- Read `config.yaml` for user name, city, topics, shows, players, etc.

### Step 3: Collect Data

For EACH data source below, use web search to find the latest information:

#### 3.1 Weather (always)
- Search: "weather in Ra'anana Israel today"
- Extract: temperature, conditions, min/max, rain chance
- Generate clothing recommendation in Hebrew based on conditions:
  - Hot (>28°): "חולצה קצרה ומשקפי שמש"
  - Warm (22-28°): "חולצה קלה, אפשר שרוול קצר"
  - Mild (16-22°): "סוודר קל או חולצה ארוכה"
  - Cool (10-16°): "מעיל קל וסוודר"
  - Cold (<10°): "מעיל חורף וצעיף"
  - Rain: add "לקחת מטריה!"

#### 3.2 Dollar Rate (always)
- Search: "dollar shekel exchange rate today"
- Get current rate and yesterday's rate
- Calculate change percentage
- Try to find last 7 days rates for sparkline

#### 3.3 AI News (always)
- Search: "biggest AI news today" and "AI announcements today"
- Find UP TO 10 significant stories (new models, major launches, acquisitions, breakthroughs)
- Pick the 10 most interesting if there are more
- Skip minor blog posts or opinion pieces
- For each story: title, 2-3 sentence summary IN HEBREW, source URL, og:image URL
- Sources: TechCrunch, The Verge, Ars Technica, Hacker News, Wired, MIT Technology Review, Reuters Tech

#### 3.4 Israel Politics (always)
- Search: "חדשות פוליטיקה ישראל היום" and "Israeli politics news today"
- Find UP TO 10 significant political stories
- Pick the 10 most interesting if there are more
- For each: title, 2-3 sentence summary IN HEBREW, source URL, og:image URL
- Israeli sources: mako.co.il, walla.co.il, ynet.co.il, kan.org.il, haaretz.co.il, israelhayom.co.il, maariv.co.il
- International sources: Times of Israel, Reuters, BBC, AP News, CNN

#### 3.4b War & Security - Iran/US/Israel (always)
- Search: "Iran Israel war news today" and "מלחמה איראן ישראל חדשות" and "US Iran military" and "Middle East conflict today"
- Find UP TO 10 significant stories about the Iran-US-Israel conflict, military operations, diplomacy, ceasefire talks, hostages, Hezbollah, Hamas, regional security
- Pick the 10 most interesting if there are more
- For each: title, 2-3 sentence summary IN HEBREW, source URL, og:image URL
- Sources: Reuters, BBC, CNN, Times of Israel, ynet, kan.org.il, Al Jazeera, AP News

#### 3.4c World News (always)
- Search: "world news today" and "breaking news today" and "חדשות העולם היום"
- Find UP TO 10 significant world news stories (wars, diplomacy, natural disasters, economy, science, major events)
- Pick the 10 most interesting if there are more
- For each: title, 2-3 sentence summary IN HEBREW, source URL, og:image URL
- Sources: Reuters, BBC, AP News, CNN, Al Jazeera, The Guardian, NY Times

#### 3.5 Sports (only if news exists)
- Search: "Danny Avdia NBA news today" and "Lionel Messi news today"
- Only include if there are actual news/games/stats
- If nothing significant, skip this section entirely

#### 3.6 Shows & Entertainment (only if news exists)
- IMPORTANT: Search EACH show and celebrity INDIVIDUALLY by name
- Loop through every item in config.yaml shows list:
  - Search: "{show name} news today" (in Hebrew for Israeli shows, English for international)
  - Example searches: "הישרדות פרק חדש", "Beast Games news today", "Squid Game season 3 news", "בריג'רטון עונה חדשה"
- Also search Google News for each show
- Only include shows with actual fresh news (new episodes, eliminations, renewals, viral moments, actor news)
- Skip shows with no news from last 24 hours
- Also search for celebrity gossip related to actors from these shows

#### 3.7 Gal Gadot (only if news exists)
- Search: "Gal Gadot news today"
- Only include if actual news exists

#### 3.8 Calendar
- Search: "Jewish holidays today Israel" and "Israeli national events today"
- Check Hebrew calendar for holidays/events
- Morning: Today's events. Evening: Tomorrow's events too.
- Note: Google Calendar integration requires API key in config

#### 3.9 Daily Surprise
- Rotate type each day (use day-of-year % 6):
  - 0: Inspirational quote (ציטוט מעורר השראה)
  - 1: Joke (בדיחה)
  - 2: Trivia (טריוויה)
  - 3: Interesting fact (עובדה מעניינת)
  - 4: Today in history (היום בהיסטוריה)
  - 5: Riddle (חידה)
- All in Hebrew!

### Step 4: Generate Article Pages

For each news story, create a separate article HTML page in `docs/articles/`:
- Filename: `YYYY-MM-DD-slug.html` (slug from title)
- Use `src/article-template.html` as base
- Fill in: title, category, date, image, full Hebrew summary (5-8 paragraphs, ~1 minute read), source URL
- The summary should be MUCH more detailed than the dashboard card
- Replace template CSS/JS paths to use `../css/style.css` and `../js/script.js`

### Step 4b: Check for Breaking News

If there is a MAJOR ongoing event (war, natural disaster, huge announcement):
- Add a breaking news banner at the top of the page (before header)
- HTML: `<div class="breaking-banner"><span class="breaking-label">🔴 מבזק</span> TEXT HERE</div>`
- Keep it to one line, punchy, with key facts

### Step 4c: Rating System

Every news card must include rating buttons:
```html
<div class="card-footer">
    <a href="articles/..." class="read-more">קרא עוד ←</a>
    <div class="rating-buttons">
        <button class="rating-btn" data-article-id="UNIQUE_ID" data-rating="up">👍</button>
        <button class="rating-btn" data-article-id="UNIQUE_ID" data-rating="down">👎</button>
    </div>
</div>
```
Also add `data-article-id` and `data-category` attributes to the `.news-card` div.

Before generating, read localStorage ratings (if accessible) from `docs/ratings.json` to understand user preferences and prioritize similar content.

### Step 5: Generate Main Dashboard HTML

Read `src/template.html` and replace all `{{PLACEHOLDERS}}`:

- `{{EDITION_TITLE}}`: "מהדורת בוקר" or "מהדורת ערב" + date
- `{{EDITION_LABEL}}`: "מהדורת בוקר ☀️" or "מהדורת ערב 🌙"
- `{{DATE_HEBREW}}`: Today's date in Hebrew (e.g., "יום רביעי, 19 במרץ 2026")
- `{{UPDATE_TIME}}`: Current time (e.g., "06:15")
- `{{GREETING}}`: Morning → "בוקר טוב, ג'יי! ☀️" / Evening → "ערב טוב, ג'יי! 🌙"
- `{{SURPRISE_LABEL}}`: Type label (e.g., "💡 עובדה מעניינת", "😂 בדיחה", "📜 ציטוט")
- `{{SURPRISE_CONTENT}}`: The surprise content in Hebrew
- `{{WEATHER_ICON}}`: Emoji matching weather (☀️/⛅/🌧️/❄️)
- `{{TEMPERATURE}}`: Current temp number
- `{{WEATHER_DESC}}`: Hebrew description (e.g., "עננות חלקית, 18°-24°")
- `{{CLOTHING_REC}}`: Hebrew recommendation
- `{{DOLLAR_RATE}}`: Rate (e.g., "3.62")
- `{{DOLLAR_CHANGE}}`: Change with arrow (e.g., "↑ 0.3%" or "↓ 0.5%")
- `{{DOLLAR_DIRECTION}}`: "positive" or "negative" CSS class
- `{{DOLLAR_HISTORY_JSON}}`: JSON array of 7 numbers for sparkline
- `{{CALENDAR_TITLE}}`: Morning → "פגישות היום" / Evening → "פגישות מחר"
- `{{HOLIDAY}}` section: Show if holiday exists, hide otherwise
- `{{CALENDAR_EVENTS}}`: HTML for calendar events

For news cards, generate this HTML for each story:
```html
<div class="news-card">
    <img src="OG_IMAGE_URL" alt="" class="card-image" loading="lazy"
         onerror="this.style.display='none'">
    <div class="card-content">
        <span class="card-category">CATEGORY</span>
        <h3 class="card-title">HEBREW_TITLE</h3>
        <p class="card-summary">HEBREW_SUMMARY</p>
        <a href="articles/ARTICLE_FILE.html" class="read-more">קרא עוד ←</a>
    </div>
</div>
```

For conditional sections (sports, shows, gadot), if no news:
- Remove the entire `{{#SECTION}}...{{/SECTION}}` block

### Step 6: Copy Assets

Copy to `docs/`:
- `src/styles.css` → `docs/css/style.css`
- `src/script.js` → `docs/js/script.js`
- `assets/logo.svg` → `docs/assets/logo.svg`
- `assets/icons/` → `docs/assets/icons/`

### Step 7: Save & Push

1. Save generated HTML as `docs/index.html`
2. Save article pages in `docs/articles/`
3. Git add all changes in `docs/`
4. Git commit with message: "📰 Daily Me - מהדורת [בוקר/ערב] [DATE]"
5. Git push to origin

## Important Rules

1. **Everything in Hebrew** - All summaries, titles, recommendations, greetings
2. **Concise** - Dashboard cards: title + 2-3 sentences max. Article pages: fuller summary.
3. **Only relevant** - Skip sections with no news (sports, shows, gadot)
4. **Quality over quantity** - 3 great stories > 5 mediocre ones
5. **Premium feel** - Every detail matters, proper formatting
6. **Real data only** - Don't make up news, quotes, or stats
7. **OG Images** - Try to get og:image from source articles for visual richness
8. **Translate, don't transliterate** - Natural Hebrew, not word-by-word translation
9. **ONLY TODAY'S NEWS** - Only include news from the last 24 hours. Never pad with old stories. If there's lots of news, the dashboard can be longer. If there's nothing, that section should be shorter or hidden. Don't force old content. CRITICAL: Always verify the publish date of every article. If the article is older than 24 hours, DO NOT include it. Check the URL, the page date, and any timestamps. When in doubt, skip it.
10. **Dynamic length** - The dashboard length should reflect how much actually happened. Busy news day = more cards. Quiet day = fewer cards. Never add filler.
11. **EVERY ITEM MUST HAVE A SOURCE** - Every single piece of information must link to its original source. No exceptions. News cards must have "קרא עוד" linking to an article page, and every article page must have "למקור המלא" linking to the original source URL. Weather must link to the weather service. Dollar rate must link to the exchange rate source. Even the daily surprise should cite its source. The user needs to be able to verify everything.
12. **No unverifiable claims** - If you can't find a source URL for a piece of information, don't include it. Credibility is everything.
