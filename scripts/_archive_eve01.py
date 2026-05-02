#!/usr/bin/env python3
"""Archive the May 1 evening edition with fixed relative paths and update editions.json."""
import pathlib, json, re

ROOT = pathlib.Path("/Users/jacobmargaliot/Downloads/Claude/הדיילי מי")
src = (ROOT / "docs/index.html").read_text(encoding="utf-8")

# Fix paths for archive subdir
fixes = [
    ('href="css/', 'href="../css/'),
    ('src="js/', 'src="../js/'),
    ('href="assets/', 'href="../assets/'),
    ('src="assets/', 'src="../assets/'),
    ('href="articles/', 'href="../articles/'),
    ('href="archive/', 'href="../archive/'),
    ('href="manifest.json"', 'href="../manifest.json"'),
]
out = src
for a, b in fixes:
    out = out.replace(a, b)

# Mark "ערב" link as the active archive page (current viewer is in archive now)
out = out.replace('<a href="#" class="footer-link active">ערב</a>',
                  '<a href="../index.html" class="footer-link">חזור לדשבורד</a>')

archive_path = ROOT / "docs/archive/2026-05-01-evening.html"
archive_path.write_text(out, encoding="utf-8")
print(f"Archived to {archive_path.name}")

# Update editions.json - prepend new entry
editions_file = ROOT / "docs/archive/editions.json"
editions = json.loads(editions_file.read_text(encoding="utf-8"))
new_entry = {
    "date": "2026-05-01",
    "edition": "evening",
    "file": "2026-05-01-evening.html",
    "label": "יום שישי 1.5 · ערב"
}
# Remove any existing matching entry, then insert at start
editions = [e for e in editions if not (e.get("date") == "2026-05-01" and e.get("edition") == "evening")]
editions.insert(0, new_entry)
editions_file.write_text(json.dumps(editions, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated editions.json: {len(editions)} entries, newest = {editions[0]['label']}")
