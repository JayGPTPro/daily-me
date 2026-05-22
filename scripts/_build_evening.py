#!/usr/bin/env python3
"""Build evening edition of Daily Me - 2026-05-17."""
import os, json, shutil, re
from pathlib import Path

BASE = Path("/Users/jacobmargaliot/Downloads/Claude/הדיילי מי")
DOCS = BASE / "docs"
SRC = BASE / "src"
ARTICLES = DOCS / "articles"
ARCHIVE = DOCS / "archive"

DATE = "2026-05-17"
EDITION = "evening"
DATE_HEBREW = "יום ראשון, 17 במאי 2026"
UPDATE_TIME = "18:15"

NEWS = {
    "aiNews": [
        ("חדשות AI", "aiNews",
         "Google משיקה את Gemini 3.1 Ultra עם חלון של 2 מיליון טוקנים",
         "Google שחררה השבוע את Gemini 3.1 Ultra, מודל מולטימודלי שמטפל בטקסט, תמונה, אודיו ווידאו ללא תמלול ביניים. החלון תופח ל-2 מיליון טוקנים ויש שיפור בכלי הרצת הקוד והפחתת הזיות.",
         "https://blog.google/technology/google-deepmind/", "ai-gemini-3-1-ultra"),
        ("חדשות AI", "aiNews",
         "OpenAI שחררה את GPT-5.5 - המודל הכי חכם והכי אינטואיטיבי שלהם",
         "GPT-5.5 שוחרר ב-23 באפריל ומגיע עם 1 מיליון טוקנים, מצטיין בקידוד אגנטי, שימוש במחשב ועבודת ידע. תמחור: 5$ למיליון input ו-30$ למיליון output. OpenAI מתמקדת באוטומציה של עבודה מקצועית.",
         "https://openai.com/news/", "ai-gpt-5-5-launch"),
        ("חדשות AI", "aiNews",
         "Anthropic משיקה את Project Glasswing עם Claude Mythos Preview",
         "Anthropic נתנה גישה ל-Claude Mythos Preview לארגונים נבחרים כולל AWS, Apple, Cisco, Google, JPMorgan ו-Microsoft. המטרה: לאתר ולתקן פגיעויות אבטחה קריטיות בקוד מקור. בנוסף, זיכרון אישי נפרס לכל משתמשי Claude.",
         "https://www.anthropic.com/news", "ai-anthropic-glasswing"),
        ("חדשות AI", "aiNews",
         "Meta חושפת את Muse Spark - מודל הדגל הראשון של Superintelligence Labs",
         "Meta חשפה את Muse Spark, מודל שפה גדול שנבנה תחת מנהל ה-AI אלכסנדר ואנג. הוא מציג ביצועים מולטימודליים תחרותיים בעלויות חישוב נמוכות יותר, וקפיטל ה-AI ל-2026 צפוי לעמוד על 115-135 מיליארד דולר - כמעט כפול מ-2025.",
         "https://about.fb.com/news/", "ai-meta-muse-spark"),
        ("חדשות AI", "aiNews",
         'ממשלת ארה"ב תוכל לבצע הערכות אבטחה למודלים מתקדמים',
         'Microsoft, Google ו-xAI חתמו על הסכם שמאפשר לממשלת ארה"ב להעריך את האבטחה של מודלים מתקדמים לפני השקה ציבורית. הצעד נועד להתמודד עם חששות לאומיים סביב יכולות AI גנרטיבי.',
         "https://www.reuters.com/technology/", "ai-us-security-assessment"),
        ("חדשות AI", "aiNews",
         "Google I/O 2026 בשבוע הבא: ציפיות לאנדרואיד 17 והכרזות AI",
         "אירוע Google I/O 2026 צפוי להיפתח בשבוע הבא, עם הכרזות מרכזיות על Android 17, יכולות AI חדשות ב-Workspace ושילובי Gemini במוצרי הצרכן של Google. צפויה גם הכרזה על שותפויות חדשות עם יצרני סמארטפונים.",
         "https://tech.yahoo.com/general/article/google-io-2026-what-to-expect-next-week-including-android-17-ai-announcements-and-more-131200995.html", "ai-google-io-2026"),
    ],
    "politics": [
        ("פוליטיקה", "politics",
         'ישיבת ממשלה: יחידה ייעודית לחיילים עולים תוקם',
         'ראש הממשלה נתניהו הוביל את ישיבת הקבינט השבועית והממשלה אישרה תוכנית להקמת יחידה ייעודית לסיוע לעולים המשרתים בצה"ל, עם דגש על חיילים בודדים. שר הקליטה אופיר סופר יעמוד בראש המהלך יחד עם שר הביטחון כ"ץ ושר תפוצות חיקלי.',
         "https://www.timesofisrael.com/liveblog-may-17-2026/", "politics-immigrant-soldiers-unit"),
        ("פוליטיקה", "politics",
         "נועם בטן חוזר ארצה אחרי הזכייה במקום השני באירוויזיון",
         'נועם בטן נחת בנמל התעופה בן גוריון לאחר ביצוע מצוין שזיכה אותו במקום השני באירוויזיון. "היו לנו אתגרים, אבל תודה לכל מי שתמך", אמר. נשיא המדינה הרצוג כינה את הביצוע "מושלם".',
         "https://www.timesofisrael.com/liveblog-may-16-2026/", "politics-bettan-eurovision"),
        ("פוליטיקה", "politics",
         "בחירות לכנסת ה-26 ייערכו עד 27 באוקטובר 2026",
         "על פי לוח הזמנים החוקי, ישראל תקיים בחירות לכנסת ה-26 עד 27 באוקטובר 2026. במפלגות החל מירוץ אסטרטגי לקראת המערכה, כאשר האופוזיציה הצהירה כי מטרתה למנוע מנתניהו, בן גביר וסמוטריץ' קדנציה נוספת.",
         "https://en.wikipedia.org/wiki/2026_Israeli_legislative_election", "politics-elections-2026"),
        ("פוליטיקה", "politics",
         "דיווח: שרי הקבינט מחלקים משרות לקראת הבחירות",
         'לפי Times of Israel, מספר שרים בקבינט מחלקים תפקידים למקורבים ולפעילי מפלגה ערב הבחירות. הצעדים מעוררים ביקורת באופוזיציה, שמכנה את התופעה "שלל מקצועי על חשבון הציבור".',
         "https://www.timesofisrael.com/liveblog-may-13-2026/", "politics-cabinet-jobs"),
        ("פוליטיקה", "politics",
         'האופוזיציה מתאחדת: "לא ניתן לממשלה הזו עוד קדנציה"',
         'ראשי האופוזיציה הצהירו כי נכונים לשתף פעולה כדי למנוע מהקואליציה הנוכחית להמשיך. נושאים מרכזיים: הסכם בני ערובה, החזרת התקציב למסלול, ושיקום היחסים עם ארה"ב.',
         "https://www.jpost.com/israel-news", "politics-opposition-unite"),
    ],
    "warSecurity": [
        ("מלחמה וביטחון", "warSecurity",
         'צה"ל חיסל את עיז א-דין אל-חדאד, מפקד הזרוע הצבאית של חמאס בעזה',
         'צה"ל חיסל בעזה את עיז א-דין אל-חדאד, שתואר ע"י ישראל כאחד האחרונים מבין אדריכלי מתקפת 7 באוקטובר 2023. הוא היה מפקד מרכזי בחמאס במשך עשרות שנים, החזיק חטופים כמגן אנושי, והוביל בחודשים האחרונים את בניית הכוח של הארגון.',
         "https://www.timesofisrael.com/liveblog-may-15-2026/", "war-haddad-eliminated"),
        ("מלחמה וביטחון", "warSecurity",
         "חיזבאללה תקף בסבך רחפנים את צפון ישראל",
         'חיזבאללה הודיע כי תקף יעד צבאי בצפון ישראל באמצעות "להקת רחפנים" וכי ביצע יותר מתריסר תקיפות נוספות. צה"ל יירט חלק מהרחפנים, וכפרים בגליל קיבלו אזעקות. בעקבות התקיפה, צה"ל הגביר תקיפות באזורים בדרום לבנון.',
         "https://www.timesofisrael.com/", "war-hezbollah-drones"),
        ("מלחמה וביטחון", "warSecurity",
         "הפסקת האש מול חיזבאללה הוארכה ב-45 ימים",
         'ארה"ב הודיעה על הארכת הפסקת האש ה"נקבובית" בין ישראל לחיזבאללה ב-45 יום, אחרי שהסבב השלישי של השיחות בוושינגטון הסתיים. במקביל, ישראל מקבלת אישור אמריקאי להמשיך לתקוף פעילי חיזבאללה שמוגדרים כאיום מיידי - תקיפות שמתרחשות באופן יום-יומי.',
         "https://www.israelhayom.com/2026/05/17/as-iran-standoff-nears-breaking-point-gaza-war-could-reignite/", "war-ceasefire-extension"),
        ("מלחמה וביטחון", "warSecurity",
         'דיווח: ישראל וארה"ב נערכות לחדש את העימות מול איראן בשבוע הבא',
         'לפי גורמים אמריקאים, ארה"ב וישראל נערכות לחדש פעילות צבאית מול איראן כבר בשבוע הקרוב. בין ההצעות: שיגור כוחות קומנדו לקרקע איראנית כדי להוציא חומר גרעיני. השיחות מתואמות גם עם בעלות ברית אירופאיות.',
         "https://www.israelhayom.com/2026/05/17/as-iran-standoff-nears-breaking-point-gaza-war-could-reignite/", "war-iran-renewed"),
        ("מלחמה וביטחון", "warSecurity",
         'מצר הורמוז נפתח מחדש לאחר הסכם ארה"ב-סין',
         'טראמפ ושי הסכימו בפסגת בייג\'ין שמצר הורמוז - שנסגר באופן אפקטיבי מאז העימות מול איראן - חייב להיפתח מחדש לתמיכה בביקוש האנרגיה העולמי. ההסכם משפיע ישירות על מחירי הנפט וההזרמה לכלכלות אירופה.',
         "https://www.euronews.com/2026/05/15/china-offers-us-to-help-open-strait-of-hormuz-but-warns-trump-over-taiwan", "war-hormuz-reopen"),
    ],
    "worldNews": [
        ("חדשות העולם", "worldNews",
         "טראמפ ושי סיכמו פסגת ענק בבייג'ין",
         'נשיא ארה"ב טראמפ ונשיא סין שי ג\'ינפינג סיימו פסגת ענק בבייג\'ין. טראמפ אמר ש"פתרנו הרבה בעיות" ושי כינה את הביקור "אבן דרך". במהלכים הפנימיים שי הזהיר כי נושא טייוואן עלול להוביל ל"התנגשויות וקונפליקטים".',
         "https://www.euronews.com/2026/05/15/china-offers-us-to-help-open-strait-of-hormuz-but-warns-trump-over-taiwan", "world-trump-xi-summit"),
        ("חדשות העולם", "worldNews",
         'צבא ארה"ב וניגריה חיסלו את ראש דאע"ש אבו-בילאל אל-מאינוקי',
         'טראמפ הודיע במאוחר בלילה בפוסט ברשת החברתית שלו על פעולה משותפת של צבא ארה"ב וניגריה שחיסלה את אבו-בילאל אל-מאינוקי, ראש ארגון דאע"ש באזור. הפעולה נחשבת מכה משמעותית למבנה המפקדה של הארגון באפריקה.',
         "https://www.golocalprov.com/news/5-big-news-stories-overnight-sunday-may-17-2026", "world-isis-leader"),
        ("חדשות העולם", "worldNews",
         "צרפת תחקור את ההתנקשות בעיתונאי הסעודי ג'מאל קשוקג'י",
         "שופט פריזאי החליט לפתוח חקירה רשמית להתנקשות בעיתונאי ג'מאל קשוקג'י ב-2018, בעקבות תלונה שהוגשה על ידי ארגוני זכויות אדם נגד יורש העצר הסעודי MBS. החקירה צפויה ליצור משבר דיפלומטי נוסף בין צרפת לסעודיה.",
         "https://www.cnn.com/world", "world-khashoggi-investigation"),
        ("חדשות העולם", "worldNews",
         "ניגריה: ממשלת לאגוס מפקיעה אדמות מאזרחים עניים לטובת דירות יוקרה",
         "ממשלת לאגוס מפקיעה אדמות ממשפחות אזרחים עניים שגרים בהם דורות, כדי לבנות מתחמי יוקרה. הסיפור מעורר מהומה בינלאומית והפגנות מקומיות. ארגונים בינלאומיים קוראים למימשל להפסיק את ההפקעות.",
         "https://www.npr.org/sections/news", "world-lagos-evictions"),
        ("חדשות העולם", "worldNews",
         "טראמפ שוקל חבילת נשק לטייוואן אחרי הפסגה",
         'אחרי שובו מהפסגה עם שי, הבית הלבן שוקל לאשר חבילת נשק חדשה לטייוואן. המהלך עלול להוות בדיקת מאמץ ראשונה ליחסי ארה"ב-סין החדשים, ועלול לקעקע את ההסכמות שגובשו השבוע.',
         "https://spectrumlocalnews.com/us/snplus/international/2026/05/15/trump-xi-visit-china-beijing-trade-talks-taiwan-relationship-differences-", "world-taiwan-arms"),
    ],
    "amazon": [
        ("אמזון למוכרים", "amazon",
         "תוספת דלק של 3.5% הוטלה על כל עמלות FBA",
         'החל מ-17 באפריל 2026 אמזון מטילה תוספת דלק של 3.5% על כל עמלות FBA בארה"ב ובקנדה. ההחלטה צפויה להעלות עלויות למוכרים, במיוחד באזורים עם משלוחים תכופים. מומלץ לעדכן מחירונים בהתאם.',
         "https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026", "amazon-fuel-surcharge"),
        ("אמזון למוכרים", "amazon",
         "תוספת הדלק התרחבה גם ל-MCF ול-Buy with Prime",
         "החל מ-2 במאי 2026, תוספת הדלק של 3.5% מורחבת גם לשירות Multi-Channel Fulfillment (MCF) ו-Buy with Prime. מוכרים שמשתמשים ב-Amazon לוגיסטיקה למשלוחים ישירים מאתרי החברה ירגישו את ההשפעה בעמלות.",
         "https://sellercentral.amazon.com/help/hub/reference/external/G201411300?locale=en-US", "amazon-mcf-fuel"),
        ("אמזון למוכרים", "amazon",
         "תוספות לאחסון מלאי מיושן עכשיו מ-181 ימים במקום 271",
         "אמזון הקדימה את תוספות האחסון למלאי מיושן ב-90 יום. במקום החל מ-271 ימים, התוספות יחולו כבר אחרי 181 יום. מומלץ למוכרים לבצע ניקיון מלאי ולהריץ מבצעים על SKUs איטיים לפני שיוצרים עלויות נוספות.",
         "https://3plcenter.com/amazon-fba-fee-changes-2026/", "amazon-aged-inventory"),
        ("אמזון למוכרים", "amazon",
         "פיצול Large Bulky ל-Small Bulky ו-Large Bulky עם שינוי עמלות",
         "אמזון מפצלת את קטגוריית Large Bulky לשתי קטגוריות: Small Bulky עם הורדת עמלה של $2.06 ליחידה, ו-Large Bulky עם הורדה של $0.26 ליחידה. שינוי משמעותי למוכרים עם פריטים גדולים, וצפוי להגביר תחרות בחללי המוצרים הגדולים.",
         "https://www.efulfillmentservice.com/2026/04/amazon-2026-fba-fee-changes-what-sellers-need-to-know/", "amazon-bulky-split"),
    ],
    "gadgets": [
        ("טכנולוגיה", "gadgets",
         "Nova Flip של Ai+ - הפלאפון המתקפל הזול ביותר בעולם",
         "Nova Flip של Ai+ הושק בהודו במחיר של 29,999 רופי (כ-$320), מה שהופך אותו לפלאפון המתקפל הזול בעולם. המכשיר כולל מסך פנימי AMOLED 6.9 אינץ', מסך חיצוני 3.1 אינץ', מעבד MediaTek Dimensity 7300 ומצלמה ראשית 50 מגה.",
         "https://easternherald.com/2026/05/04/best-new-gadgets-may-2026/", "gadgets-nova-flip"),
        ("טכנולוגיה", "gadgets",
         "Pebble Round 2: שעון חכם עם מסך e-paper לשבועיים סוללה ב-$199",
         "Pebble חוזרת עם Round 2 - שעון חכם עגול עם מסך e-paper צבעוני בגודל 1.3 אינץ' ובטריה שנמשכת מעל שבועיים. השעון מגיע במאי במחיר של 199$ ומשתלב עם אנדרואיד ו-iOS. נחשב לאלטרנטיבה לאפל ווצ' עם דגש על סוללה ופשטות.",
         "https://www.tomsguide.com/wellness/smartwatches/these-are-the-5-coolest-wearable-tech-gadgets-i-tried-at-ces-2026-so-far", "gadgets-pebble-round-2"),
        ("טכנולוגיה", "gadgets",
         "Pebble Index 01: טבעת חכמה עם AI מבוססת Claude",
         "Pebble משיקה גם את Index 01 - טבעת חכמה עם כפתור שמאפשר לדבר עם AI מבוסס Claude של Anthropic כדי לזכור דברים. הטבעת מתרכזת בעוזר אישי, מעקב פעילות בסיסי וחיבור לסמארטפון. נחשבת לחלק מטרנד ה-AI Wearables.",
         "https://www.tomsguide.com/wellness/smartwatches/5-biggest-wearable-tech-predictions-for-2026-from-new-fitbits-to-the-ever-elusive-apple-ring", "gadgets-pebble-index-01"),
        ("טכנולוגיה", "gadgets",
         "StillFrame: אוזניות שקטות ופתוחות עם ANC",
         'StillFrame הציגה אוזניות פתוחות שמשקלן רק 103 גרם, עם נהגי 40 מ"מ שמתוכננים לסאונד פתוח ורחב, ANC ו-Transparency Mode. האוזניות נועדו למאזינים שמחפשים נוחות שעות ארוכות ללא הפרעה לסביבה.',
         "https://www.yankodesign.com/2026/05/12/the-5-best-tech-gadgets-of-may-2026/", "gadgets-stillframe"),
    ],
    "sports": [
        ("ספורט", "sports",
         "מסי הבקיע hat-trick נגד סינסינטי, שני בטבלת מבקיעים MLS",
         "מסי הוביל את אינטר מיאמי לניצחון 5-3 על סינסינטי עם 2 גולים, בישול וגול עצמי שאילץ. עם 12 שערים בעונה, מסי במקום השני בטבלת המבקיעים של MLS. שיא שמתחזק עם התקרבות גביע העולם 2026.",
         "https://www.mlssoccer.com/news/lionel-messi-s-scorching-pre-world-cup-form-leads-inter-miami-to-big-win-vs-cincy", "sports-messi-hat-trick"),
        ("ספורט", "sports",
         "אינטר מיאמי מארחת את פורטלנד טימברס - מסי צפוי לפתוח",
         'אינטר מיאמי תארח הערב את פורטלנד טימברס במשחק חשוב בליגת MLS. מסי צפוי לפתוח, עם המאמן מסקרנו שמדגיש שהקפטן "בכושר מלא". המשחק יוצג ב-Apple TV ב-1:00 בלילה בארץ.',
         "https://worldsoccertalk.com/news/when-is-lionel-messi-next-game/", "sports-miami-portland"),
        ("ספורט", "sports",
         "דני אבדיה: שיאי קריירה אישיים, פורטלנד בעיצומה של עונת המעבר",
         "דני אבדיה סיים את העונה עם שיאי קריירה: 24.2 נקודות, 6.9 ריבאונדים ו-6.7 אסיסטים בממוצע ב-66 משחקים. אחרי שיצא בסיבוב הראשון של הפלייאוף נגד סן אנטוניו ספרס, אבדיה צפוי להישאר כעיקרון של פורטלנד בעונת המעבר.",
         "https://www.espn.com/nba/player/_/id/4683021/deni-avdija", "sports-avdija-season"),
    ],
    "shows": [
        ("בידור", "shows",
         'גל גדות בכנס הנשיא: "אנחנו בונים בית חדש בישראל"',
         'גל גדות נשאה דברים בכנס הנשיא לעתיד ישראלי משותף בירושלים והודיעה שמשפחתה בונה בית חדש בישראל. בנוסף, הודיעה שתתרום את מלוא פרס בראשית שלה לארגונים שעובדים על איחוי הקרעים בחברה. "קשה להיות ישראלית בחו"ל בימים אלה".',
         "https://www.jns.org/feature/gal-gadot-reveals-her-family-is-building-a-new-home-in-israel", "shows-gal-gadot-conference"),
        ("בידור", "shows",
         "Beast Games עונה 3: עסקה עם IATSE, מאבק חדש עם Teamsters",
         "MrBeast הגיע להסכם עם איגוד IATSE שמכסה כ-500 אנשי צוות לעונה 3 של Beast Games. ימים בלבד לאחר מכן, איגוד ה-Teamsters איים בשביתה אחרי משא ומתן מתוח. אמזון פריים עדיין לא אישרה עונות מעבר ל-3.",
         "https://deadline.com/2026/05/mrbeast-strike-teamsters-beast-games-1236905514/", "shows-beast-games-teamsters"),
        ("בידור", "shows",
         "הישרדות חוזרת: 18 שורדים אנונימיים על אי באוקיינוס",
         'תוכנית הריאליטי "הישרדות" של רשת 13 חוזרת עם עונה חדשה ומפתיעה: 18 שורדים אנונימיים יגיעו לאי מבודד וייאבקו על מיליון שקלים ועל התואר "השורד הטוב ביותר". גיא זוארץ ימשיך להנחות. צילומים בעיצומם.',
         "https://13tv.co.il/mood/survivor/", "shows-survivor-new-season"),
    ],
}

article_template = (SRC / "article-template.html").read_text(encoding="utf-8")

article_files = {}

for cat, stories in NEWS.items():
    for i, (cat_name, cat_filter, title, summary, source, slug) in enumerate(stories):
        filename = f"{DATE}-{slug}.html"
        article_id = f"{DATE}-{slug}"
        body_html = ""
        body_html += f"<p>{summary}</p>\n"
        body_html += f"<p>הסיפור הזה הוא חלק מסיקור Daily Me ליום {DATE_HEBREW}. הנושאים מהבחירה של ג'יי מתעדכנים פעמיים ביום, בוקר וערב.</p>\n"
        body_html += '<p>הכתבה המקורית באנגלית או בעברית זמינה במקור (לינק בתחתית). אם הנושא מעניין אותך, סמנו "✨ מעניין" כדי שניתן עדיפות לסיפורים דומים בעתיד.</p>\n'

        html_out = article_template
        html_out = html_out.replace("{{ARTICLE_TITLE}}", title)
        html_out = html_out.replace("{{ARTICLE_CATEGORY}}", cat_name)
        html_out = html_out.replace("{{ARTICLE_DATE}}", DATE_HEBREW)
        html_out = html_out.replace("{{ARTICLE_ID}}", article_id)
        html_out = html_out.replace("{{ARTICLE_BODY}}", body_html)
        html_out = html_out.replace("{{SOURCE_URL}}", source)
        html_out = re.sub(r'\{\{#ARTICLE_IMAGE\}\}.*?\{\{/ARTICLE_IMAGE\}\}', '', html_out, flags=re.DOTALL)

        (ARTICLES / filename).write_text(html_out, encoding="utf-8")
        article_files[(cat, i)] = (filename, article_id, cat_filter)

print(f"Created {sum(len(v) for v in NEWS.values())} article pages")

def make_card(cat, i, story):
    cat_name, cat_filter, title, summary, source, slug = story
    filename, article_id, cf = article_files[(cat, i)]
    return f'''<div class="news-card" data-article-id="{article_id}" data-category="{cat_filter}">
    <div class="card-content">
        <span class="card-category">{cat_name}</span>
        <h3 class="card-title">{title}</h3>
        <p class="card-summary">{summary}</p>
        <div class="card-footer">
            <a href="articles/{filename}" class="read-more">קרא עוד ←</a>
            <div class="rating-buttons">
                <button class="rating-btn" data-article-id="{article_id}" data-rating="up">👍</button>
                <button class="rating-btn" data-article-id="{article_id}" data-rating="down">👎</button>
            </div>
        </div>
    </div>
</div>'''

cards = {}
for cat, stories in NEWS.items():
    cards[cat] = "\n".join(make_card(cat, i, s) for i, s in enumerate(stories))

calendar_html = '''<div class="calendar-event"><span class="event-time">כל היום</span><span class="event-title">🚀 Challenge EN - Round 4 (סבב חדש)</span></div>
<div class="calendar-event"><span class="event-time">כל היום</span><span class="event-title">🏢 יום שלם עבודה מהמשרד</span></div>'''

surprise_label = "📜 היום בהיסטוריה"
surprise_content = 'ב-17 במאי 1954 בית המשפט העליון של ארה"ב הוציא פסיקה פה אחד בתיק Brown v. Board of Education, שאסרה הפרדה גזעית בבתי ספר ציבוריים. ב-17 במאי 1792 נחתם הסכם Buttonwood על ידי 24 ברוקרים בניו יורק - האירוע המכונן של בורסת ניו יורק (NYSE). ב-17 במאי 1990 ארגון הבריאות העולמי הסיר את ההומוסקסואליות מרשימת המחלות הנפשיות. <a href="https://www.history.com/this-day-in-history/may-17" target="_blank" style="color: var(--text-secondary); font-size: 0.85em;">(מקור: History.com)</a>'

daily_quote = '"היופי, בעיני, טמון בפשטות" — מארק היימן, רופא וסופר'
quote_source = '<a href="https://positivity.org/quotes/daily-quotes" target="_blank">Positivity.org</a>'

podcast_rec = '<strong>עושים היסטוריה</strong> - פודקאסט בעברית מהפופולריים בארץ עם רן לוי. פרקים שבועיים על היסטוריה, מדע וטכנולוגיה. אפיזודות חדשות יוצאות באופן קבוע.'
podcast_source = '<a href="https://osimhistoria.com/" target="_blank">osimhistoria.com</a>'

english_word = '<strong>Serendipity</strong> (סֶרֶנדִיפִּיטִי) — גילוי מקרי ומשמח של דבר שלא חיפשת. דוגמה: "I found this amazing restaurant by pure serendipity."'

daily_riddle = '<strong>חידה:</strong> מי הולך על ארבע בבוקר, על שתיים בצהריים ועל שלוש בערב?<br><br><details><summary style="cursor: pointer; color: var(--brand);">הצג תשובה</summary><p style="margin-top: 8px;"><strong>תשובה:</strong> האדם. זוחל על ארבע בילדותו, הולך על שתיים בבגרותו, ונשען על מקל בזקנתו (חידת הספינקס).</p></details>'

viral_tweet = '<strong>פוסט ויראלי:</strong> "2023: Corona ended. 2026: Hantavirus." הפוסט הישן של משתמש X שצפה לכאורה התפרצות של הנטה-וירוס ב-2026 חזר לטרנדינג עם 255 אלף לייקים, 100 אלף שיתופים ו-21 אלף תגובות, אחרי שמספר נוסעים על ספינת נופש מתו בעקבות התפרצות אמיתית של הוירוס.'
tweet_source = '<a href="https://www.newsweek.com/years-old-x-post-appearing-to-predict-hantavirus-in-2026-goes-viral-11925318" target="_blank">Newsweek</a>'

template = (SRC / "template.html").read_text(encoding="utf-8")

template = re.sub(r'\{\{#SPORTS\}\}|\{\{/SPORTS\}\}', '', template)
template = re.sub(r'\{\{#ENTERTAINMENT\}\}|\{\{/ENTERTAINMENT\}\}', '', template)
template = re.sub(r'\{\{#HOLIDAY\}\}.*?\{\{/HOLIDAY\}\}', '', template, flags=re.DOTALL)

dollar_rate = "2.92"
dollar_change = "↓ 0.8%"
dollar_direction = "negative"
dollar_history = [2.9071, 2.9027, 2.9158, 2.9011, 2.9197, 2.9066, 2.9384, 2.9162]

replacements = {
    "{{EDITION_TITLE}}": "מהדורת ערב · 17 במאי 2026",
    "{{EDITION_LABEL}}": "מהדורת ערב 🌙",
    "{{DATE_HEBREW}}": DATE_HEBREW,
    "{{UPDATE_TIME}}": UPDATE_TIME,
    "{{GREETING}}": "ערב טוב, ג'יי! 🌙",
    "{{SURPRISE_LABEL}}": surprise_label,
    "{{SURPRISE_CONTENT}}": surprise_content,
    "{{WEATHER_ICON}}": "☀️",
    "{{TEMPERATURE}}": "25",
    "{{WEATHER_DESC}}": '<a href="https://www.weather-forecast.com/locations/Ra-anana/forecasts/latest" target="_blank" style="color: inherit; text-decoration: none;">בהיר וחם, 19°-30°</a>',
    "{{CLOTHING_REC}}": "👕 חולצה קצרה (קריר בערב)",
    "{{DOLLAR_RATE}}": f'<a href="https://www.boi.org.il/roles/markets/exchangerates/" target="_blank" style="color: inherit; text-decoration: none;">{dollar_rate}</a>',
    "{{DOLLAR_CHANGE}}": dollar_change,
    "{{DOLLAR_DIRECTION}}": dollar_direction,
    "{{DOLLAR_HISTORY_JSON}}": json.dumps(dollar_history),
    "{{CALENDAR_TITLE}}": "פגישות מחר (יום שני)",
    "{{CALENDAR_EVENTS}}": calendar_html,
    "{{AI_NEWS_CARDS}}": cards["aiNews"],
    "{{POLITICS_CARDS}}": cards["politics"],
    "{{WAR_SECURITY_CARDS}}": cards["warSecurity"],
    "{{WORLD_NEWS_CARDS}}": cards["worldNews"],
    "{{AMAZON_CARDS}}": cards["amazon"],
    "{{GADGETS_CARDS}}": cards["gadgets"],
    "{{SPORTS_CARDS}}": cards["sports"],
    "{{ENTERTAINMENT_CARDS}}": cards["shows"],
    "{{DAILY_QUOTE}}": daily_quote,
    "{{QUOTE_SOURCE}}": quote_source,
    "{{PODCAST_REC}}": podcast_rec,
    "{{PODCAST_SOURCE}}": podcast_source,
    "{{ENGLISH_WORD}}": english_word,
    "{{DAILY_RIDDLE}}": daily_riddle,
    "{{VIRAL_TWEET}}": viral_tweet,
    "{{TWEET_SOURCE}}": tweet_source,
}

for k, v in replacements.items():
    template = template.replace(k, v)

morning_today = ARCHIVE / "2026-05-17-morning.html"
morning_link = "archive/2026-05-17-morning.html" if morning_today.exists() else "archive/2026-05-16-morning.html"

edition_nav = f'''
<div class="edition-nav" style="text-align: center; padding: 12px; background: var(--bg-secondary); font-size: 0.9em;">
    <a href="{morning_link}" style="margin: 0 8px; color: var(--text-secondary);">☀️ בוקר</a>
    <span style="color: var(--brand);">·</span>
    <a href="#" style="margin: 0 8px; color: var(--brand); font-weight: 600;">🌙 ערב</a>
    <span style="color: var(--brand);">·</span>
    <a href="archive/2026-05-16-evening.html" style="margin: 0 8px; color: var(--text-secondary);">📅 אתמול</a>
    <span style="color: var(--brand);">·</span>
    <a href="archive/" style="margin: 0 8px; color: var(--text-secondary);">📚 ארכיון</a>
</div>
'''

template = template.replace("</header>", "</header>\n" + edition_nav)

category_filter = '''        <!-- Category Filter Bar -->
        <div class="category-filter">
            <button class="filter-btn active" data-filter="all">הכל</button>
            <button class="filter-btn" data-filter="warSecurity">⚔️ מלחמה</button>
            <button class="filter-btn" data-filter="politics">🏛️ פוליטיקה</button>
            <button class="filter-btn" data-filter="aiNews">🤖 AI</button>
            <button class="filter-btn" data-filter="worldNews">🌍 עולם</button>
            <button class="filter-btn" data-filter="amazon">📦 אמזון</button>
            <button class="filter-btn" data-filter="gadgets">📱 גאדג'טים</button>
            <button class="filter-btn" data-filter="sports">⚽ ספורט</button>
            <button class="filter-btn" data-filter="shows">📺 בידור</button>
        </div>

'''
template = template.replace('        <!-- News Grid -->\n        <div class="news-grid">', category_filter + '        <!-- News Grid -->\n        <div class="news-grid">')

(DOCS / "index.html").write_text(template, encoding="utf-8")
print("Wrote docs/index.html")

archive_html = template
path_fixes = [
    ('href="css/', 'href="../css/'),
    ('href="js/', 'href="../js/'),
    ('src="js/', 'src="../js/'),
    ('href="assets/', 'href="../assets/'),
    ('src="assets/', 'src="../assets/'),
    ('href="articles/', 'href="../articles/'),
    ('href="archive/', 'href="../archive/'),
    ('href="manifest.json"', 'href="../manifest.json"'),
    ('href="index.html"', 'href="../index.html"'),
]
for old, new in path_fixes:
    archive_html = archive_html.replace(old, new)

archive_file = ARCHIVE / f"{DATE}-{EDITION}.html"
archive_file.write_text(archive_html, encoding="utf-8")
print(f"Wrote archive {archive_file.name}")

editions_path = ARCHIVE / "editions.json"
editions = json.loads(editions_path.read_text(encoding="utf-8"))
editions = [e for e in editions if not (e["date"] == DATE and e["edition"] == EDITION)]
editions.insert(0, {"date": DATE, "edition": EDITION, "file": f"{DATE}-{EDITION}.html"})
editions_path.write_text(json.dumps(editions, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated editions.json ({len(editions)} entries)")

print("Done!")
