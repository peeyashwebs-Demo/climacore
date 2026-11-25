#!/usr/bin/env python3
"""Generates the demo illustrations (original vector art) into assets/images/. Run from project root."""
import os, math
O = "assets/images"; os.makedirs(O, exist_ok=True)
def svg(w, h, body, c1="#12395a", c2="#06101C", bg=True):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><defs>'
      '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
      '<linearGradient id="wh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7F9FC"/><stop offset="1" stop-color="#BFCBD8"/></linearGradient>'
      '<radialGradient id="gl"><stop offset="0" stop-color="#38C6D8" stop-opacity=".6"/><stop offset="1" stop-color="#38C6D8" stop-opacity="0"/></radialGradient>'
      '<radialGradient id="sun"><stop offset="0" stop-color="#F5B04C" stop-opacity=".9"/><stop offset="1" stop-color="#F5B04C" stop-opacity="0"/></radialGradient></defs>'
      + (f'<rect width="{w}" height="{h}" fill="url(#bg)"/>' if bg else "") + body + "</svg>")
R = lambda x, y, w, h, f, rx=0, o=1: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" opacity="{o}"/>'
C = lambda x, y, r, f, o=1: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" opacity="{o}"/>'
F = lambda d, f, o=1: f'<path d="{d}" fill="{f}" opacity="{o}"/>'
L = lambda d, s, sw=3, o=1: f'<path d="{d}" fill="none" stroke="{s}" stroke-width="{sw}" opacity="{o}" stroke-linecap="round" stroke-linejoin="round"/>'
T = lambda x, y, t, sz, f="#38C6D8", a="middle": f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{sz}" font-weight="700" fill="{f}" text-anchor="{a}">{t}</text>'
def ac(x, y, w, t="24°"):
    h = w * .3
    return R(x, y, w, h, "url(#wh)", h * .2) + R(x + w * .06, y + h * .76, w * .88, h * .09, "#8d9db0", h * .05) + R(x + w * .37, y + h * .18, w * .26, h * .32, "#08121e", h * .07) + T(x + w / 2, y + h * .42, t, h * .21)
def cool(x, y, w, n=7, c="#38C6D8"):
    return "".join(L(f"M{x + w * i / n:.0f} {y} q {18 * (-1) ** i} 45 0 90 t 0 90", c, 3, .3) for i in range(n + 1))
def fan(x, y, r):
    return C(x, y, r, "#16283C") + C(x, y, r * .92, "#0B1726") + "".join(f'<rect x="{x}" y="{y - r * .13}" width="{r * .82}" height="{r * .26}" rx="{r * .12}" fill="#9FB0C3" transform="rotate({a} {x} {y})"/>' for a in range(0, 360, 72)) + C(x, y, r * .16, "#38C6D8")
def person(x, y, s=1, shirt="#1F6FB2", hat="#F5B04C", skin="#D9A07A", arm=(40, -120), flip=False):
    g = f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    g += R(-22, -72, 17, 72, "#16283C", 6) + R(5, -72, 17, 72, "#16283C", 6) + R(-30, -152, 60, 90, shirt, 16)
    g += L("M-22 -138 L-32 -92", skin, 11) + L(f"M22 -138 L{arm[0]} {arm[1]}", skin, 11) + C(arm[0], arm[1], 7, skin)
    g += C(0, -176, 19, skin) + F("M-21 -178 a21 21 0 0 1 42 0 z", hat) + R(-25, -180, 50, 6, hat, 3) + "</g>"
    return g
def building(x, y, w, h, c="#102A43", lit=.35, seed=1):
    g = R(x, y, w, h, c, 4)
    cols, rows = max(2, int(w // 34)), max(2, int(h // 38))
    for i in range(cols):
        for j in range(rows):
            on = ((i * 7 + j * 13 + seed) % 10) / 10 < lit
            g += R(x + 12 + i * ((w - 24) / cols), y + 14 + j * ((h - 20) / rows), (w - 24) / cols - 8, (h - 20) / rows - 12, "#F5B04C" if on else "#1B3A58", 2, .9 if on else .8)
    return g
def box_unit(x, y, w, h): return R(x, y, w, h, "url(#wh)", 10) + fan(x + w / 2, y + h * .5, min(w, h) * .36) + R(x + 8, y + h - 14, w - 16, 6, "#8d9db0", 3)
def person_head(cx, cy, skin): return f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="92" fill="{skin}"/>'
def w(name, s): open(f"{O}/{name}.svg", "w", encoding="utf-8").write(s)
SK = ["#F1C9A5", "#D9A07A", "#B97A56", "#8A5A3C", "#F5D5BD"]

# ---------- hero room backdrop (1600x700) ----------
b = R(0, 0, 1600, 700, "url(#bg)") + R(1020, 110, 420, 360, "#0A1D31", 8) + R(1036, 126, 388, 328, "#1B4C77", 4)
b += "".join(R(1036 + i * 52, 454 - (60 + (i * 37) % 150), 40, 60 + (i * 37) % 150, "#0E2A44") for i in range(8)) + R(1226, 126, 6, 328, "#0A1D31") + R(1036, 286, 388, 6, "#0A1D31")
b += R(0, 520, 1600, 180, "#071524") + R(120, 430, 420, 110, "#12304C", 30) + R(100, 400, 70, 140, "#173a5c", 28) + R(500, 400, 70, 140, "#173a5c", 28) + R(150, 380, 360, 80, "#194266", 30)
b += R(700, 220, 6, 320, "#2a4a68") + F("M660 230 L746 230 L726 180 L680 180 Z", "#F5B04C", .85) + C(700, 190, 140, "url(#sun)", .35)
b += R(1280, 480, 50, 60, "#0f2a43", 6) + "".join(F(f"M1305 480 Q{1305 + dx} 420 1305 {380 - k * 12}", "#1d6b5b", .9) for k, dx in enumerate([-60, -30, 0, 30, 60]))
b += R(240, 130, 250, 160, "#0E263D", 6, .8) + R(256, 146, 218, 128, "#14385a", 4, .8) + L("M280 250 L340 200 L390 230 L450 170", "#38C6D8", 3, .7)
w("hero-room", svg(1600, 700, b, bg=False))

# ---------- service cards (800x500) ----------
b = R(0, 430, 800, 70, "#0A1B2D") + ac(140, 70, 520) + cool(180, 232, 440) + R(60, 280, 14, 160, "#9FB0C3", 4) + R(130, 280, 14, 160, "#9FB0C3", 4) + "".join(R(60, 300 + i * 40, 84, 7, "#9FB0C3", 3) for i in range(4))
b += person(640, 440, 1.5, arm=(55, -150), flip=True) + R(520, 410, 70, 32, "#F5B04C", 6) + R(535, 402, 40, 10, "#8a5a1c", 4)
w("svc-repair", svg(800, 500, b))
b = R(0, 400, 800, 100, "#0A1B2D") + building(40, 120, 220, 290, "#0F2740", .3, 2) + R(300, 250, 300, 160, "#0E2740", 8) + box_unit(340, 270, 180, 130) + L("M520 330 C600 330 620 300 660 300 L700 300", "#B87333", 6) + L("M520 350 C610 350 620 330 660 330 L700 330", "#9FB0C3", 6)
b += person(660, 430, 1.35, arm=(38, -110)) + R(560, 372, 50, 40, "#F5F8FC", 4) + R(570, 380, 30, 5, "#8d9db0") + C(150, 70, 110, "url(#sun)", .4)
w("svc-maintenance", svg(800, 500, b, "#1b4a73", "#081626"))
b = R(0, 430, 800, 70, "#0A1B2D") + building(60, 90, 360, 340, "#0F2740", .4, 5) + building(450, 190, 260, 240, "#0D2238", .3, 3) + R(90, 62, 90, 30, "#E8EEF5", 4) + R(210, 62, 90, 30, "#E8EEF5", 4) + R(320, 62, 70, 30, "#E8EEF5", 4)
b += "".join(C(135 + i * 120 if i < 2 else 355, 77, 9, "#9FB0C3") for i in range(3)) + R(480, 160, 100, 30, "#E8EEF5", 4) + C(530, 175, 9, "#9FB0C3") + cool(90, 36, 300, 8)
w("svc-commercial", svg(800, 500, b, "#173f66", "#071524"))
b = ""
for cx, col in ((260, "#1688E8"), (540, "#E5484D")):
    b += C(cx, 230, 118, "#16283C") + C(cx, 230, 104, "#F5F8FC") + C(cx, 230, 96, "#0B1726") + "".join(L(f"M{cx + 84 * math.cos(math.radians(a)):.1f} {230 + 84 * math.sin(math.radians(a)):.1f} L{cx + 94 * math.cos(math.radians(a)):.1f} {230 + 94 * math.sin(math.radians(a)):.1f}", "#9FB0C3", 3) for a in range(135, 406, 18))
    b += L(f"M{cx} 230 L{cx + 66 * math.cos(math.radians(300 if col == '#1688E8' else 340)):.1f} {230 + 66 * math.sin(math.radians(300 if col == '#1688E8' else 340)):.1f}", "#F5B04C", 5) + C(cx, 230, 9, "#F5B04C") + R(cx - 44, 346, 88, 40, col, 8)
b += R(380, 330, 40, 60, "#F5B04C", 6) + L("M260 386 C260 460 150 440 120 500", "#1688E8", 12) + L("M540 386 C540 460 650 440 680 500", "#E5484D", 12) + L("M400 390 C400 450 400 470 400 500", "#9FB0C3", 12)
w("svc-refrigerant", svg(800, 500, b, "#10304e", "#06101C"))
b = R(0, 440, 800, 60, "#0A1B2D") + R(80, 80, 230, 230, "url(#wh)", 28) + R(110, 110, 170, 110, "#08121e", 16) + T(195, 190, "74°", 64) + C(195, 262, 22, "#C3CFDC") + C(195, 262, 14, "#8d9db0") + F("M0 0", "#000")
b += R(380, 130, 360, 220, "#16283C", 12) + R(396, 146, 328, 180, "#08121e", 6) + L("M416 300 L470 250 L520 280 L580 200 L640 235 L700 170", "#38C6D8", 5) + R(350, 350, 420, 18, "#C3CFDC", 8) + C(560, 160, 8, "#F5B04C")
b += cool(70, 330, 250, 6) + C(195, 195, 190, "url(#gl)", .35)
w("svc-diagnosis", svg(800, 500, b))

# ---------- project cards (800x500) ----------
b = R(0, 400, 800, 100, "#0A1B2D") + R(80, 140, 640, 260, "#12304C", 6) + "".join(R(80 + i * 64, 140, 64, 54, "#E8EEF5" if i % 2 else "#1688E8") for i in range(10)) + R(130, 230, 250, 170, "#0B1A2A") + R(135, 235, 240, 160, "#1B4C77", 4, .8) + R(430, 230, 90, 170, "#0B1A2A") + R(450, 250, 60, 60, "#F5B04C", 4, .8)
b += R(560, 250, 130, 80, "#F5F8FC", 6) + fan(625, 290, 28) + R(300, 96, 200, 36, "#38C6D8", 6) + T(400, 122, "STORE", 24, "#06101C") + cool(120, 200, 240, 5)
w("proj-store", svg(800, 500, b, "#173f66", "#071524"))
b = R(0, 410, 800, 90, "#0A1B2D") + R(200, 190, 330, 220, "#E8EEF5", 4) + F("M170 195 L365 70 L560 195Z", "#2a4a68") + "".join(R(x, y, 70, 60, "#F5B04C", 3, .9) for x, y in ((230, 230), (440, 230), (230, 320), (440, 320))) + R(335, 310, 60, 100, "#16283C", 3)
b += R(580, 330, 130, 80, "#F5F8FC", 8) + fan(645, 370, 30) + C(645, 370, 120, "url(#gl)", .5) + C(90, 100, 70, "url(#sun)", .5)
w("proj-house", svg(800, 500, b, "#1b4a73", "#081626"))
b = R(0, 0, 800, 70, "#0B1A2A") + "".join(R(60 + i * 250, 14, 190, 46, "#E8EEF5", 6) + R(100 + i * 250, 24, 110, 8, "#8d9db0", 3) for i in range(3)) + "".join(cool(70 + i * 250, 70, 170, 4) for i in range(3))
b += R(0, 400, 800, 100, "#0A1B2D") + "".join(R(80 + i * 220, 300, 160, 14, "#2a4a68", 4) + R(90 + i * 220, 314, 8, 90, "#2a4a68") + R(142 + i * 220, 314, 8, 90, "#2a4a68") + R(110 + i * 220, 262, 70, 40, "#16283C", 4) for i in range(3)) + person(700, 420, 1.1, shirt="#2a4a68", hat="#2a4a68", skin="#B97A56", arm=(-5, -90))
w("proj-office", svg(800, 500, b, "#14385a", "#071524"))
b = R(0, 440, 800, 60, "#0A1B2D")
for i in range(4):
    x = 60 + i * 180
    b += R(x, 70, 140, 370, "#0E1D2E", 6) + "".join(R(x + 12, 86 + j * 44, 116, 34, "#16283C", 4) + C(x + 28, 103 + j * 44, 4, "#38C6D8" if (i + j) % 3 else "#F5B04C") + R(x + 70, 98 + j * 44, 48, 10, "#2a4a68", 2) for j in range(8))
b += cool(60, 40, 700, 12) + C(400, 450, 360, "url(#gl)", .25)
w("proj-server", svg(800, 500, b, "#0c2038", "#050d17"))
b = C(660, 110, 150, "url(#sun)") + C(660, 110, 58, "#F5B04C") + R(0, 410, 800, 90, "#0A1B2D") + R(130, 210, 310, 200, "#E8EEF5", 4) + F("M100 215 L285 90 L470 215Z", "#2a4a68") + R(150, 250, 90, 70, "#F5B04C", 3) + R(330, 250, 90, 70, "#F5B04C", 3) + R(240, 330, 50, 80, "#16283C", 3)
b += R(500, 330, 140, 80, "#F5F8FC", 8) + fan(570, 370, 32) + C(570, 370, 120, "url(#gl)", .5) + "".join(L(f"M{40 + i * 90} 440 q 20 -16 40 0 t 40 0", "#F5B04C", 3, .5) for i in range(8))
w("proj-heat", svg(800, 500, b, "#5a3a22", "#1a1020"))

# ---------- blog (800x500) ----------
b = R(250, 60, 300, 300, "url(#wh)", 150) + C(400, 210, 118, "#0B1726") + T(400, 232, "72°", 72) + L("M310 270 A 100 100 0 0 0 490 270", "#38C6D8", 6) + R(0, 430, 800, 70, "#0A1B2D") + C(400, 210, 250, "url(#gl)", .3)
w("blog-thermostat", svg(800, 500, b))
b = R(0, 430, 800, 70, "#0A1B2D") + R(200, 90, 400, 300, "#9FB0C3", 10) + R(222, 112, 356, 256, "#E8EEF5", 4) + L("".join(f"M{222 + i * 22} 112 L{233 + i * 22} 368 L{244 + i * 22} 112 " for i in range(16)), "#8d9db0", 2) + cool(180, 40, 440, 8)
w("blog-filter", svg(800, 500, b))
b = R(0, 430, 800, 70, "#0A1B2D") + R(60, 190, 460, 90, "url(#wh)", 12) + R(500, 190, 90, 240, "url(#wh)", 12) + "".join(R(90 + i * 90, 186, 8, 98, "#8d9db0") for i in range(5)) + R(520, 120, 150, 40, "#8d9db0", 8) + R(560, 150, 70, 50, "#8d9db0") + cool(520, 160, 150, 3) + R(40, 200, 24, 70, "#38C6D8", 6)
w("blog-ducts", svg(800, 500, b))

# ---------- portraits (400x500) ----------
def avatar(name, skin, hair, style, shirt, bg, glasses=False, beard=False, tie=False):
    b = R(0, 0, 400, 500, "url(#bg)") + F("M30 500 Q40 385 200 362 Q360 385 370 500Z", shirt) + R(170, 300, 60, 80, skin, 20) + person_head(200, 225, skin)
    b += f'<ellipse cx="122" cy="232" rx="12" ry="20" fill="{skin}"/><ellipse cx="278" cy="232" rx="12" ry="20" fill="{skin}"/>'
    if style == "short": b += F("M120 218 Q116 118 200 114 Q284 118 280 218 Q256 166 200 164 Q144 166 120 218Z", hair)
    if style == "curly": b += "".join(C(130 + i * 28, 150 + 10 * ((i % 2) * 2 - 1) * -1 + abs(i - 3) * 8, 30, hair) for i in range(7))
    if style == "bob": b += F("M112 260 Q96 110 200 106 Q304 110 288 260 L262 260 Q268 170 200 164 Q132 170 138 260Z", hair)
    if style == "buzz": b += F("M124 205 Q124 130 200 128 Q276 130 276 205 Q250 172 200 172 Q150 172 124 205Z", hair, .85)
    if beard: b += F("M126 240 Q130 330 200 332 Q270 330 274 240 Q250 300 200 300 Q150 300 126 240Z", hair)
    b += C(168, 228, 6, "#1a1a1a") + C(232, 228, 6, "#1a1a1a") + L("M150 208 Q168 200 186 208", hair, 5) + L("M214 208 Q232 200 250 208", hair, 5) + L("M172 280 Q200 298 228 280", "#7a3b3b" if not beard else "#2a1a1a", 5)
    if glasses: b += f'<circle cx="168" cy="228" r="22" fill="none" stroke="#0B1726" stroke-width="4"/><circle cx="232" cy="228" r="22" fill="none" stroke="#0B1726" stroke-width="4"/>' + L("M190 228 L210 228", "#0B1726", 4)
    b += F("M165 362 L200 412 L235 362Z", "#E8EEF5") if not tie else F("M180 362 L200 372 L220 362 L214 500 L186 500Z", "#1688E8") + F("M165 362 L200 400 L235 362 L200 376Z", "#F7F9FC")
    if not tie: b += C(290, 440, 14, "#38C6D8")
    w(name, svg(400, 500, b, *bg))
A = [("t-1", SK[0], "#4a4a4a", "short", "#101f33", ("#2a5a85", "#0c2238"), True, False), ("t-2", SK[1], "#1a1a1a", "short", "#101f33", ("#256178", "#0b2230"), False, True),
     ("t-3", SK[3], "#0d0d0d", "curly", "#101f33", ("#3a4a85", "#0c1630"), False, False), ("t-4", SK[2], "#2b1a10", "buzz", "#101f33", ("#2a6a6a", "#0b2226"), False, True),
     ("r-1", SK[4], "#6b4a2b", "short", "#2a3b52", ("#3a5a7a", "#0f2236"), False, False), ("r-2", SK[2], "#1a1010", "bob", "#3a2a52", ("#5a3a7a", "#1a1030"), False, False), ("r-3", SK[1], "#222", "short", "#1d2d44", ("#2a5a85", "#0c2238"), True, False)]
for n, s, h, st, sh, bg, g, bd in A: avatar(n, s, h, st, sh, bg, g, bd, tie=n.startswith("r-"))
# enterprise building (220x260, transparent)
w("enterprise", svg(220, 260, building(20, 30, 90, 220, "#0E2A44", .3, 1) + building(110, 90, 90, 160, "#12395a", .4, 2) + R(40, 12, 50, 18, "#9FB0C3", 3) + cool(30, 8, 60, 3), bg=False))
print("images:", len(os.listdir(O)))
