# Daily Me - Project Instructions

## What is this?
Personal AI news dashboard. Updates twice daily (6AM, 6PM) via Claude Code scheduled tasks. Static HTML → GitHub Pages.

## Key Rules
- **Hebrew only** - All content, summaries, UI
- **Only today's news** - Last 24h. Never pad with old stories. Verify every article date.
- **Every item needs a source** - No exceptions. og:image from real articles only, never placeholders.
- **Jay's wardrobe** - Only: חולצה קצרה, סוודר, ג'קט, מעיל, מעיל גשם
- **Viral exception** - If EVERYONE is talking about something, include it even outside configured interests
- **Up to 10 items per category** - Pick most interesting if more exist
- **Search shows individually** - Loop each show/celeb name separately in Google News

## Architecture
- `config.yaml` - All user preferences
- `scripts/generate-edition.md` - Full instructions for scheduled task
- `src/` - Templates (HTML, CSS, JS)
- `docs/` - Generated output (GitHub Pages)
- `docs/archive/` - Past editions
- `docs/assets/hero/` - 23 rotating hero images
- `docs/assets/icons/` - Nano Banana generated section icons

## Categories
War & Security, AI, Politics, World News, Amazon Seller, Tech Gadgets, Sports (Avdija + Messi), Entertainment (shows + Gal Gadot)

## Google Calendar
Check both: `primary` (info@jaygptpro.com) AND `jmargaliot@gmail.com` AND holidays calendar.

## Live at
https://jaygptpro.github.io/daily-me/
