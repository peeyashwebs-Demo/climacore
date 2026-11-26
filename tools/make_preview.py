#!/usr/bin/env python3
"""Single-file homepage preview (CSS, JS, images inlined). Output: /mnt/user-data/outputs/climacore-home-preview.html"""
import re, base64
h = open("index.html", encoding="utf-8").read()
h = h.replace('<link rel="stylesheet" href="css/home.css">', "<style>" + open("css/home.css", encoding="utf-8").read() + "</style>")
h = h.replace('<script src="js/main.js"></script><script src="js/home.js"></script>', "<script>" + open("js/main.js", encoding="utf-8").read() + open("js/home.js", encoding="utf-8").read() + "</script>")
h = re.sub(r'(src|data-fb)="(assets/images/[a-z0-9-]+\.svg)"', lambda m: f'{m.group(1)}="data:image/svg+xml;base64,' + base64.b64encode(open(m.group(2), "rb").read()).decode() + '"', h)
h = re.sub(r'href="(?:services/)?[a-z-]+\.html"', 'href="#contact"', h)
open("/mnt/user-data/outputs/climacore-home-preview.html", "w", encoding="utf-8").write(h); print("preview", len(h) // 1024, "KB")
