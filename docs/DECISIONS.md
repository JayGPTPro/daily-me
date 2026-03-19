# Decisions Log

## Architecture
- **Static HTML over Next.js** — GitHub Pages hosting, no server needed, scheduled task generates HTML directly. Simpler = better for this use case.
- **Vanilla CSS over Tailwind** — Single CSS file with CSS variables for theming. No build step.

## Design
- **Single column layout** — Jay found side-by-side categories confusing. One column, clear reading order.
- **og:images from real articles only** — Never use placeholder/stock photos. No image is better than a fake image.
- **"מעניין/פחות" not "👍/👎"** — Rating is about interest level, not opinion on the news. "Like" on bad news felt wrong.
- **Gal Gadot inside Entertainment** — Not a separate category. Same logic as Messi inside Sports.
- **23 rotating hero images** — One per edition, not random. ~1 month without repeats.
- **RTL ticker direction** — Hebrew reads right-to-left, ticker scrolls accordingly.

## Content
- **Strictly today's news** — Jay caught a 6-month old article. Trust = everything.
- **Three-level content** — Card → Hebrew summary → Original source. Never skip the middle step.
- **Jay's actual wardrobe** — Only suggest clothes he owns.
- **Viral exception** — If the whole world talks about something, include it even outside configured interests.
