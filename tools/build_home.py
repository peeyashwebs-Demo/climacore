#!/usr/bin/env python3
"""Generates index.html (demo content). Replace the DEMO data below with real details before launch."""
I = lambda n, alt, cls="pimg": f'<img class="{cls}" src="assets/images/{n}.svg" alt="{alt}" loading="lazy">'
NAME = "HVAC Demo"
svc = [("AC repair", "svc-repair", "Technician repairing a wall-mounted air conditioner"), ("AC service and maintenance", "svc-maintenance", "Technician servicing an outdoor condenser unit"),
       ("Commercial air conditioning", "svc-commercial", "Office buildings with rooftop cooling units"), ("Refrigerant service", "svc-refrigerant", "Manifold gauge set measuring refrigerant pressure"), ("AC problem diagnosis", "svc-diagnosis", "Thermostat and laptop showing system diagnostics")]
proj = [("proj-store", "Retail", "Minimized downtime across a busy store", "Cooling upgraded after hours so trading was never interrupted."), ("proj-house", "Residential", "Two-storey home returned to stable cooling", "Upstairs and downstairs balanced with a corrected duct layout."),
        ("proj-office", "Commercial", "Office comfort restored before the deadline", "Ceiling cassette units replaced over a single weekend."), ("proj-server", "Technical space", "Server room temperature stabilized overnight", "Airflow and cooling capacity corrected with no outage."),
        ("proj-heat", "Residential", "Cooling restored before a summer heatwave", "Failed system diagnosed and repaired the same week.")]
team = [("t-1", "Daniel Hart", "Lead service technician"), ("t-2", "Marcus Reed", "Installation specialist"), ("t-3", "Aisha Bello", "Diagnostics and repair"), ("t-4", "Luis Ortega", "Commercial systems technician")]
rev = [("r-1", "A cooling failure hit one evening in peak summer. The technician arrived promptly, explained the fault clearly, and had the system running again before we went to bed.", "Daniel R., homeowner"),
       ("r-2", "We manage a busy office with several tenants. The team planned the work around our schedule, kept us informed, and left everything tidy.", "Priya N., office manager"),
       ("r-3", "Clear options, a written quote and no pressure. Our replacement was installed on the day promised and the house has never been more comfortable.", "Marcus T., property owner")]
faq = [("How much will it cost before you know the fault?", "We charge a flat diagnostic fee, which is credited toward the repair if you go ahead. You will see the price before we start."),
       ("Can someone come out today if my system stops working?", "We keep same-day slots open for urgent no-cooling and no-heating calls. Call us and we will give you a realistic arrival time."),
       ("Will I be pushed into replacing the whole system?", "No. We explain what is wrong, what a repair costs, and what replacement would cost, then you decide."),
       ("What happens if the issue isn't fixed on the first visit?", "We return to finish the job at no extra call-out charge when the same fault is still present."),
       ("Do you offer after-hours or emergency callouts?", "Yes, for urgent problems. After-hours visits carry an emergency rate, which we confirm before dispatching."),
       ("How do payment and invoicing work?", "You receive a written invoice on completion and can pay by card, bank transfer or finance, depending on the job.")]
blog = [("blog-thermostat", "Guides · 4 min read", "Which thermostat setting is actually efficient?"), ("blog-filter", "Maintenance · 3 min read", "What a seasonal tune-up covers, and why it matters"), ("blog-ducts", "Guides · 5 min read", "Repair or replace: how to decide with confidence")]
areas = ["Downtown", "Northside", "Riverside", "Lakeview", "Westgate", "Oakridge", "Eastfield", "Harbor District"]
cards = "".join(f'<div class="sl" role="group" aria-label="{a}"><img src="assets/images/{n}.svg" alt="{al}" loading="lazy"><h3>{a}</h3></div>' for a, n, al in svc)
pj = "".join(f'<div>{I(n, t)}<small>{c}</small><h3>{t}</h3><p>{d}</p></div>' for n, c, t, d in proj)
tm = "".join(f'<div class="tm">{I(n, "Portrait of " + nm + " (illustration)")}<h3>{nm}</h3><p>{r}</p></div>' for n, nm, r in team)
rv = "".join(f'<figure>{I(n, "Illustrated portrait of " + w.split(", ")[0])}<div><p class="stars" aria-label="5 out of 5 stars">★★★★★</p><blockquote>“{q}”</blockquote><p style="margin-top:1rem"><b style="color:#fff">{w}</b> · sample review</p></div></figure>' for n, q, w in rev)
fq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
bl = "".join(f'<article>{I(n, t)}<small>{c}</small><h3>{t}</h3></article>' for n, c, t in blog)
ar = "".join(f'<div>{a}</div>' for a in areas)
av = "".join(f'<img src="assets/images/{n}.svg" alt="" loading="lazy">' for n in ("t-1", "t-2", "t-3", "t-4", "r-2"))
br = "".join(f'<div>{b}</div>' for b in ("Arctiva", "Zephra", "Kelvora", "Thermia"))
mq = "".join(f'<span>✻ {NAME}</span>' for _ in range(6))
def plan(t, price, inc, btn, hi=False):
    return f'<div class="plan{" hi" if hi else ""}"><h3>{t}</h3><p style="margin:0"><b style="color:#fff;font:700 1.9rem var(--fh)">{price}</b></p><ul>' + "".join(f"<li>{x}</li>" for x in inc) + f'</ul><a class="btn {"btn-p" if hi else "btn-g"}" href="#contact">{btn}</a></div>'
plans = (plan("Diagnostic visit", "From $89", ["Full system inspection", "Written findings", "Fee credited to any repair"], "Book a diagnostic")
         + plan("Standard repair", "From $179", ["Fault repair and testing", "Parts warranty explained", "Same-day slots when available"], "Request a repair", True)
         + plan("Installation", "From $2,900", ["Site assessment and sizing", "Installation and commissioning", "Handover and care guide"], "Get an installation quote"))
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{NAME} | HVAC &amp; Climate Engineering</title><meta name="description" content="Demo website for an HVAC and climate engineering company: heating, cooling and ventilation designed around comfort, efficiency and reliability.">
<meta property="og:title" content="{NAME} | HVAC &amp; Climate Engineering"><meta name="theme-color" content="#06101C">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap"><link rel="stylesheet" href="css/home.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="nav"><a class="logo" href="#top">✻ <span data-site="name">{NAME}</span></a><button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><a class="btn btn-p" href="#contact">Request a Quote</a>
<ul id="menu"><li><a href="about.html">About</a></li><li><a href="solutions.html">Solutions</a></li><li><a href="industries.html">Industries</a></li><li><a href="projects.html">Projects</a></li><li><a href="technology.html">Technology</a></li><li><a href="maintenance.html">Maintenance</a></li><li><a href="insights.html">Insights</a></li><li><a href="contact.html">Contact</a></li><li><a data-call href="#contact">Call <span data-site="phone">(212) 555-0100</span></a></li></ul></header>
<main id="main"><span id="top"></span>
<section class="hero"><div class="room" aria-hidden="true"><img src="assets/images/hero-room.svg" alt=""></div><div class="wrap"><span class="chip">★ 4.9 average rating · sample figure</span><h1>Comfort engineered. Performance perfected.</h1>
<p class="lead">Heating, cooling and ventilation designed around comfort, efficiency and reliability for homes and businesses across the Greater Demo City area.</p>
<a class="btn btn-p" href="#contact">Request a Quote</a> <a class="btn btn-g" data-call href="#contact">Call now</a>
<div class="stage"><button class="hot h1" data-k="filter" aria-pressed="false">Filtration</button><button class="hot h2" data-k="air" aria-pressed="false">Airflow</button><button class="hot h3" data-k="ctrl" aria-pressed="false">Controls</button>
<div class="ac"><div class="scr"><span id="scr" aria-live="polite">24°</span><div class="rows"><span>Cooling</span><span>Auto fan</span><span>Eco</span></div></div></div><div class="air" aria-hidden="true"></div></div>
<p class="cap" id="cap" role="status">Select a point on the unit to learn how it works.</p>
<div class="tmp" role="group" aria-label="Demo thermostat"><button data-t="-1" aria-label="Lower temperature">−</button><span>Try the control</span><button data-t="1" aria-label="Raise temperature">+</button></div>
<div class="facts"><div><b>15+ years</b>In business (sample)</div><div><b>Within 60 minutes</b>Emergency response (sample)</div><div><b>4.9 / 5</b>Customer rating (sample)</div></div></div></section>
<section><div class="wrap"><p class="stmt reveal" id="stmt">We combine responsive service and proven technical expertise to keep every property running comfortably.</p>
<div class="bento reveal"><div class="bc w2"><div class="av">{av}</div><div><h3>Our team</h3><p>12 certified technicians (sample)</p></div></div>
<div class="bc w2"><div><h3>Coverage</h3><p>Check your ZIP code. Try 10001.</p></div><div><form class="zip" id="zipForm" novalidate><input id="zip" inputmode="numeric" maxlength="5" placeholder="ZIP code" aria-label="ZIP code"><button class="btn btn-p" type="submit">Check</button></form><p class="msg" id="zipMsg" role="status"></p></div></div>
<div class="bc"><div class="cond" aria-hidden="true"></div><div><div class="num" id="units">8,400</div><h3>Systems serviced (sample)</h3></div></div>
<div class="bc"><div><h3>Brands we service</h3><p>Sample brand names.</p></div><div class="pt4">{br}</div></div>
<div class="bc w2" style="align-items:center;text-align:center"><div class="radar"><div class="shield">⛨</div></div><div><h3>Emergency support</h3><p>Typical response within 60 minutes (sample)</p></div><a class="btn btn-p" href="#contact">Get a fast response</a></div></div></div></section>
<div class="band" aria-hidden="true"><div>{mq}{mq}</div></div>
<section id="spaces" class="c"><div class="wrap"><h2>Support for every type of space</h2><p>Swipe, use the arrows, or press the left and right keys.</p>
<div class="cf" aria-roledescription="carousel" aria-label="Services">{cards}</div><div class="ctl"><button id="prev" aria-label="Previous">←</button><div class="dots" id="dots"></div><button id="next" aria-label="Next">→</button></div><p class="cap2" id="cfcap" aria-live="polite"></p></div></section>
<section id="projects" class="pin"><div class="sticky"><div class="wrap"><h2>See what we've delivered recently</h2><p>Sample projects shown for demonstration. Keep scrolling.</p></div><div class="snap" id="trk">{pj}</div></div></section>
<section class="c" id="process"><div class="wrap"><h2>Your visit planned from the start</h2><p>Select a step.</p><div class="wheel"><button class="n0" aria-pressed="true">01</button><button class="n1" aria-pressed="false">02</button><button class="n2" aria-pressed="false">03</button><button class="n3" aria-pressed="false">04</button><div class="wc" aria-live="polite"><h3 id="wt"></h3><p id="wd"></p></div></div></div></section>
<section class="c"><div class="wrap"><h2>Areas we serve</h2><p>Sample service areas.</p><div class="areas">{ar}</div><div class="acta"><div><h3>Not on the list?</h3><p>Ask us about your location.</p></div><a class="btn btn-p" href="#contact">Ask about your area</a></div></div></section>
<section class="c"><div class="wrap"><h2>See why customers leave great reviews</h2><p>Sample reviews for demonstration.</p><div class="rv">{rv}</div><div class="ctl"><button id="rprev" aria-label="Previous review">←</button><div class="dots num" id="rp"></div><button id="rnext" aria-label="Next review">→</button></div></div></section>
<section class="c" id="plans"><div class="wrap"><h2>Clear options, planned from the start</h2><p>Sample pricing for demonstration.</p><div class="plans">{plans}<div class="plan ent"><div><h3>For properties with bigger requirements</h3><p style="margin:0">Facilities, multifamily and commercial projects with custom proposals.</p><a class="btn btn-p" href="#contact" style="margin-top:1rem">Request a proposal</a></div><img class="bld" src="assets/images/enterprise.svg" alt="" loading="lazy"></div></div></div></section>
<section class="cta" id="contact"><div class="wrap g"><div><h2>One conversation clarifies everything.</h2><p>Tell us what's going on and how to reach you. For urgent problems, call <a data-call href="#contact"><span data-site="phone">(212) 555-0100</span></a>.</p><p>Email: hello@hvacdemo.example</p><a class="btn btn-g" data-text href="#contact">Text us</a></div>
<form id="quoteForm" novalidate><div class="hp" aria-hidden="true"><label>Leave blank<input name="website" tabindex="-1" autocomplete="off"></label></div><div class="row"><div><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div><div><label for="p">Phone</label><input id="p" name="phone" type="tel" autocomplete="tel" required></div><div><label for="z">ZIP code</label><input id="z" name="zip" inputmode="numeric" autocomplete="postal-code" required></div>
<div><label for="s">Service needed</label><select id="s" name="service"><option>Repair</option><option>Replacement</option><option>New installation</option><option>Maintenance</option><option>Commercial / facility</option></select></div><div><label for="d">Details</label><textarea id="d" name="details" rows="3"></textarea></div></div>
<button class="btn btn-p" type="submit">Send request</button><p class="note">By sending this you agree to our <a href="privacy.html">privacy policy</a> and <a href="terms.html">terms</a>.</p><p class="msg" id="quoteMsg" role="status"></p></form></div></section>
<section class="c"><div class="wrap"><h2>The reason customers keep calling back</h2><div class="team" id="team">{tm}</div><div class="ctl"><button id="tprev" aria-label="Previous">←</button><button id="tnext" aria-label="Next">→</button></div></div></section>
<section><div class="faqw"><div><h2>Answers that make the next step easier</h2></div><div><div class="faq">{fq}</div><div class="concern"><p>Still have a specific concern? We're happy to answer it directly.</p><a class="btn btn-g" href="#contact">Ask a question</a></div></div></div></section>
<section><div class="wrap"><div class="row2"><h2>Experience you can read before calling</h2><a class="btn btn-g" href="insights.html">View all</a></div><div class="blog">{bl}</div></div></section>
</main>
<footer><div class="wrap g"><div><a class="logo" href="#top">✻ {NAME}</a><p>HVAC and climate engineering for homes and businesses.</p><form class="nl" id="nl" novalidate><input name="email" type="email" autocomplete="email" placeholder="Email address" aria-label="Email address"><button class="btn btn-p" type="submit">Subscribe</button></form><p class="msg" id="nlMsg" role="status"></p><p style="font-size:.85rem">Unsubscribe anytime. {NAME}, 123 Demo Street, Demo City.</p><p>Instagram · LinkedIn · Facebook</p></div>
<div><h3>Navigation</h3><ul><li><a href="about.html">About</a></li><li><a href="projects.html">Projects</a></li><li><a href="insights.html">Insights</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h3>Services</h3><ul><li><a href="services/ac-repair.html">AC repair</a></li><li><a href="services/ac-installation.html">Installation</a></li><li><a href="services/hvac-maintenance.html">Maintenance</a></li><li><a href="services/ventilation.html">Ventilation</a></li></ul></div>
<div><h3>Legal</h3><ul><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li>License no. 000000 (demo)</li><li>© <span data-year></span> {NAME}</li></ul></div></div><div class="wrap wm" aria-hidden="true">✻ {NAME}</div></footer>
<div class="demo" role="note">Demo site · sample content</div>
<div class="bar"><a class="btn btn-p" data-call href="#contact">Call</a><a class="btn btn-g" data-text href="#contact">Text</a></div>
<script src="js/main.js"></script><script src="js/home.js"></script></body></html>'''
open("index.html", "w", encoding="utf-8").write(html); print("index.html", len(html) // 1024, "KB")
