/* ============================================
   Daily Me - JavaScript v2.0
   Rating system, animations, sparkline
   ============================================ */

(function() {
    'use strict';

    // ---- Theme Toggle ----
    var themeToggle = document.getElementById('themeToggle');
    var themeIcon = document.getElementById('themeIcon');
    var body = document.body;

    function setTheme(theme) {
        body.setAttribute('data-theme', theme);
        localStorage.setItem('dailyme-theme', theme);
        if (themeIcon) themeIcon.textContent = theme === 'dark' ? '🌙' : '☀️';
    }
    setTheme(localStorage.getItem('dailyme-theme') || 'light');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            setTheme(body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
        });
    }

    // ---- Sparkline Chart ----
    function drawSparkline(canvasId, data, color) {
        var canvas = document.getElementById(canvasId);
        if (!canvas || !data || data.length < 2) return;
        var ctx = canvas.getContext('2d');
        var w = canvas.width, h = canvas.height, pad = 4;
        ctx.clearRect(0, 0, w, h);
        var min = Math.min.apply(null, data), max = Math.max.apply(null, data);
        var range = max - min || 1;

        ctx.beginPath();
        ctx.strokeStyle = color || '#6C5CE7';
        ctx.lineWidth = 2;
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        data.forEach(function(val, i) {
            var x = pad + (i / (data.length - 1)) * (w - pad * 2);
            var y = h - pad - ((val - min) / range) * (h - pad * 2);
            i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
        });
        ctx.stroke();

        ctx.lineTo(w - pad, h - pad);
        ctx.lineTo(pad, h - pad);
        ctx.closePath();
        var grad = ctx.createLinearGradient(0, 0, 0, h);
        grad.addColorStop(0, (color || '#6C5CE7') + '30');
        grad.addColorStop(1, (color || '#6C5CE7') + '05');
        ctx.fillStyle = grad;
        ctx.fill();

        var lastX = w - pad;
        var lastY = h - pad - ((data[data.length - 1] - min) / range) * (h - pad * 2);
        ctx.beginPath();
        ctx.arc(lastX, lastY, 3, 0, Math.PI * 2);
        ctx.fillStyle = color || '#6C5CE7';
        ctx.fill();
    }

    if (typeof dollarHistory !== 'undefined' && dollarHistory.length > 0) {
        var isPos = dollarHistory[dollarHistory.length - 1] >= dollarHistory[dollarHistory.length - 2];
        drawSparkline('dollarSparkline', dollarHistory, isPos ? '#00B894' : '#E17055');
    }

    // ---- Count-Up Animation ----
    function animateCountUp(el) {
        var text = el.textContent;
        var match = text.match(/(\d+\.?\d*)/);
        if (!match) return;
        var target = parseFloat(match[0]);
        var prefix = text.substring(0, text.indexOf(match[0]));
        var suffix = text.substring(text.indexOf(match[0]) + match[0].length);
        var duration = 1200;
        var start = performance.now();
        var decimals = match[0].includes('.') ? match[0].split('.')[1].length : 0;

        function step(now) {
            var progress = Math.min((now - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
            var current = (target * eased).toFixed(decimals);
            el.textContent = prefix + current + suffix;
            if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }

    // ---- Intersection Observer ----
    var animatedEls = document.querySelectorAll('.news-card');
    var countUpEls = document.querySelectorAll('.count-up');

    if ('IntersectionObserver' in window) {
        var cardObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    cardObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.05, rootMargin: '0px 0px 50px 0px' });

        animatedEls.forEach(function(el) { cardObserver.observe(el); });

        var countObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    animateCountUp(entry.target);
                    countObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        countUpEls.forEach(function(el) { countObserver.observe(el); });

        // Safety fallback
        setTimeout(function() {
            animatedEls.forEach(function(el) { el.classList.add('visible'); });
        }, 2000);
    } else {
        animatedEls.forEach(function(el) { el.classList.add('visible'); });
    }

    // ---- Parallax Hero ----
    var hero = document.querySelector('.hero');
    if (hero && window.innerWidth > 767) {
        window.addEventListener('scroll', function() {
            var scrolled = window.scrollY;
            if (scrolled < 600) {
                hero.style.transform = 'translateY(' + (scrolled * 0.3) + 'px)';
                hero.style.opacity = 1 - (scrolled / 600);
            }
        }, { passive: true });
    }

    // ---- Hero Image Rotation ----
    var heroEl = document.querySelector('.hero-bg');
    if (heroEl) {
        var HERO_COUNT = 23;
        var now = new Date();
        var dayOfYear = Math.floor((now - new Date(now.getFullYear(), 0, 0)) / 86400000);
        var editionIndex = dayOfYear * 2 + (now.getHours() >= 14 ? 1 : 0);
        var heroNum = (editionIndex % HERO_COUNT) + 1;
        heroEl.style.backgroundImage = "url('assets/hero/hero-" + heroNum + ".png')";
    }

    // ---- Edition Archive Navigation ----
    var editionNav = document.querySelector('.edition-nav');
    if (editionNav && !window.location.pathname.includes('/archive/')) {
        fetch('archive/editions.json')
            .then(function(r) { return r.json(); })
            .then(function(editions) {
                if (!editions || editions.length < 2) return;
                // Clear existing nav
                editionNav.innerHTML = '';
                // Add "current" link
                var currentLink = document.createElement('a');
                currentLink.href = 'index.html';
                currentLink.className = 'edition-link active';
                currentLink.textContent = '📰 עכשיו';
                editionNav.appendChild(currentLink);
                // Add last few editions (up to 5)
                var shown = Math.min(editions.length, 5);
                for (var i = 0; i < shown; i++) {
                    var ed = editions[i];
                    var link = document.createElement('a');
                    link.href = 'archive/' + ed.file;
                    link.className = 'edition-link';
                    link.textContent = ed.label || (ed.date + ' ' + (ed.edition === 'morning' ? '☀️' : '🌙'));
                    editionNav.appendChild(link);
                }
            })
            .catch(function() {}); // Silent fail if no archive yet
    }

    // ---- Scroll Position Memory ----
    // Restore scroll position when coming back from article
    var savedScroll = sessionStorage.getItem('dailyme-scroll');
    if (savedScroll && document.querySelector('.news-grid')) {
        setTimeout(function() {
            window.scrollTo(0, parseInt(savedScroll));
            sessionStorage.removeItem('dailyme-scroll');
        }, 100);
    }

    // Save scroll position when clicking "read more"
    document.querySelectorAll('.read-more').forEach(function(link) {
        link.addEventListener('click', function() {
            sessionStorage.setItem('dailyme-scroll', window.scrollY.toString());
        });
    });

    // ---- Rating System ----
    var RATINGS_KEY = 'dailyme-ratings';

    function getRatings() {
        try { return JSON.parse(localStorage.getItem(RATINGS_KEY)) || {}; }
        catch(e) { return {}; }
    }

    function saveRating(articleId, rating) {
        var ratings = getRatings();
        ratings[articleId] = {
            rating: rating, // 'up' or 'down'
            timestamp: new Date().toISOString(),
            category: document.querySelector('[data-article-id="' + articleId + '"]')
                ? document.querySelector('[data-article-id="' + articleId + '"]').getAttribute('data-category')
                : ''
        };
        localStorage.setItem(RATINGS_KEY, JSON.stringify(ratings));
    }

    function initRatings() {
        var ratings = getRatings();
        document.querySelectorAll('.rating-btn').forEach(function(btn) {
            var articleId = btn.getAttribute('data-article-id');
            var type = btn.getAttribute('data-rating');

            // Restore previous ratings
            if (ratings[articleId]) {
                var card = btn.closest('.news-card') || btn.closest('.article');
                if (card) {
                    var btns = card.querySelectorAll('.rating-btn');
                    btns.forEach(function(b) {
                        if (b.getAttribute('data-rating') === ratings[articleId].rating) {
                            b.classList.add('rated-' + ratings[articleId].rating);
                        }
                    });
                }
            }

            btn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                var card = btn.closest('.news-card') || btn.closest('.article');
                if (!card) return;

                // Clear previous
                card.querySelectorAll('.rating-btn').forEach(function(b) {
                    b.classList.remove('rated-up', 'rated-down');
                });

                // Set new
                btn.classList.add('rated-' + type);
                saveRating(articleId, type);

                // Visual feedback
                btn.style.transform = 'scale(1.3)';
                setTimeout(function() { btn.style.transform = ''; }, 200);
            });
        });
    }

    initRatings();

    // ---- Preferences Profile from Ratings ----
    function buildPreferences() {
        var ratings = getRatings();
        var prefs = {}; // category -> {up: count, down: count, score: number}

        Object.keys(ratings).forEach(function(key) {
            var r = ratings[key];
            var cat = r.category || 'unknown';
            if (!prefs[cat]) prefs[cat] = { up: 0, down: 0, score: 0 };
            if (r.rating === 'up') prefs[cat].up++;
            else prefs[cat].down++;
            prefs[cat].score = prefs[cat].up - prefs[cat].down;
        });

        return prefs;
    }

    // Export for scheduled task to read
    window.dailyMeGetRatings = function() { return getRatings(); };
    window.dailyMeGetPreferences = function() { return buildPreferences(); };

    // Save preferences to a visible element so the task can scrape it
    var prefsData = buildPreferences();
    if (Object.keys(prefsData).length > 0) {
        var prefsEl = document.createElement('script');
        prefsEl.type = 'application/json';
        prefsEl.id = 'dailyme-preferences';
        prefsEl.textContent = JSON.stringify(prefsData);
        document.head.appendChild(prefsEl);
    }

})();
