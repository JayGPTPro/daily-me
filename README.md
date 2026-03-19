# Daily Me

### *My world, every day.*

> Your personal AI-powered daily newspaper. Fresh twice a day. Learns what you like.

![Daily Me Hero](docs/assets/hero/hero-1.png)

---

## What is Daily Me?

Daily Me is a personalized news dashboard that updates every morning and evening with exactly the news **you** care about. Built with Claude Code, hosted on GitHub Pages, completely customizable.

**No algorithms you can't control. No noise. Just your world, every day.**

### Features

| Feature | Description |
|---------|-------------|
| **Twice-daily editions** | Morning (what happened overnight) + Evening (day recap + tomorrow preview) |
| **Your topics** | War & security, AI, politics, world news, Amazon seller, gadgets, sports, entertainment |
| **Your calendar** | Real Google Calendar meetings + Israeli holidays |
| **Your weather** | Local forecast + personalized clothing recommendation |
| **Dollar rate** | Live USD/ILS with weekly sparkline |
| **Learns from you** | Rate articles (interesting/less) and the dashboard adapts over time |
| **Breaking news ticker** | Scrolling headlines at the top |
| **Three-level content** | Headline → Hebrew summary → Original source |
| **Every item sourced** | Nothing without a link to verify |
| **Edition archive** | Browse past editions (morning/evening/yesterday) |
| **23 hero images** | Different background every edition |
| **Dark/Light mode** | One tap toggle |
| **Mobile-first** | Responsive design, PWA-ready |
| **Fork-friendly** | Everything in `config.yaml` |

---

## Quick Start

### 1. Fork this repo

### 2. Edit `config.yaml`

```yaml
name: "Your Name"
weather:
  city: "Your City"
  country: "IL"
sections:
  ai_news: true
  israel_politics: true
  war_security: true
  world_news: true
  amazon_seller: true
  tech_gadgets: true
  sports:
    players:
      - "Your Player"
  shows:
    list:
      - "Your Show"
  celebrities:
    list:
      - "Celebrity"
```

### 3. Set up Claude Code scheduled tasks

Two tasks run automatically:
- **Morning** (06:00) — overnight news + today's schedule
- **Evening** (18:00) — day summary + tomorrow preview

Both read `scripts/generate-edition.md` for instructions.

---

## How It Works

```
Claude Code scheduled task (6AM / 6PM)
├── Reads config.yaml for your preferences
├── Reads your rating history to prioritize content
├── Searches web for fresh news (last 24h only)
├── Fetches real images from articles (og:image)
├── Translates & summarizes everything to Hebrew
├── Pulls meetings from Google Calendar
├── Generates static HTML + article pages
├── Archives previous edition
└── Git push → GitHub Pages updates
```

## Rating System

Every article has **✨ מעניין** (interesting) and **💤 פחות** (less) buttons. Your ratings:
- Persist across sessions (localStorage)
- Build a preference profile over time
- Influence which categories get more coverage
- Help the AI learn what matters to you

## Project Structure

```
daily-me/
├── config.yaml              # Your preferences
├── scripts/
│   └── generate-edition.md  # AI generation instructions
├── src/                     # Source templates
│   ├── template.html
│   ├── article-template.html
│   ├── styles.css
│   └── script.js
├── docs/                    # GitHub Pages (auto-generated)
│   ├── index.html           # Current edition
│   ├── archive/             # Past editions
│   ├── articles/            # Hebrew article summaries
│   ├── assets/
│   │   ├── hero/            # 23 rotating hero images
│   │   ├── icons/           # Section icons
│   │   └── logo.svg
│   ├── css/style.css
│   └── js/script.js
└── README.md
```

## Tech Stack

- **Static HTML/CSS/JS** — No framework, no build step
- **Claude Code** — AI-powered content generation
- **GitHub Pages** — Free hosting
- **Google Calendar MCP** — Real meeting data
- **Heebo font** — Premium Hebrew typography
- **CSS Variables** — Dark/light theming
- **localStorage** — Ratings persistence
- **PWA manifest** — Add to home screen

## License

MIT — Fork it, customize it, make it yours.

---

**Daily Me** — *My world, every day.* ☀️🌙
