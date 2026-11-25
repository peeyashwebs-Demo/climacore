#!/usr/bin/env python3
"""Builds a single-file homepage preview (CSS, JS and images inlined). Output: /mnt/user-data/outputs/hvac-home-preview.html"""
import re, base64
h = open("index.html", encoding="utf-8").read()
h = h.replace('<link rel="stylesheet" href="css/home.css">', "<style>" + open("css/home.css", encoding="utf-8").read() + "</style>")
h = h.replace('<script src="js/main.js"></script><script src="js/home.js"></script>', "<script>" + open("js/main.js", encoding="utf-8").read() + open("js/home.js", encoding="utf-8").read() + "</script>")
h = re.sub(r'src="(assets/images/[a-z0-9-]+\.svg)"', lambda m: 'src="data:image/svg+xml;base64,' + base64.b64encode(open(m.group(1), "rb").read()).decode() + '"', h)
h = re.sub(r'href="(?:services/)?[a-z-]+\.html"', 'href="#contact"', h)
a, b = h.split("<script>", 1)
a = re.sub(r">([^<>]+)<", lambda m: ">" + m.group(1).replace("'", "\u2019") + "<", a)
open("/mnt/user-data/outputs/hvac-home-preview.html", "w", encoding="utf-8").write(a + "<script>" + b)
print("preview", len(a + b) // 1024, "KB")
