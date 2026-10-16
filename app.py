import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import random
import math
import datetime

# ==========================================
# 0. رسوم الأشجار الاحترافية (SVG + CSS)
# ==========================================
CSS = """<style>
svg{display:block}
.sw,.sh{animation:sw var(--d,6s) ease-in-out infinite;animation-delay:var(--l,0s);transform-box:fill-box;transform-origin:50% 100%}
.sh{transform-origin:50% 0}
@keyframes sw{0%,100%{transform:rotate(-1.4deg) skewX(.8deg)}50%{transform:rotate(1.4deg) skewX(-.8deg)}}
.fl{animation:fl var(--d,8s) linear infinite;animation-delay:var(--l,0s);transform-box:fill-box;transform-origin:center}
@keyframes fl{0%{transform:translate(0,0) rotate(0);opacity:0}10%{opacity:1}50%{transform:translate(calc(var(--x,40px)*.5),200px) rotate(200deg)}90%{opacity:1}100%{transform:translate(var(--x,40px),400px) rotate(420deg);opacity:0}}
.tw{animation:tw var(--d,3s) ease-in-out infinite;animation-delay:var(--l,0s)}
@keyframes tw{0%,100%{opacity:.3}50%{opacity:1}}
.dr{animation:dr 16s ease-in-out infinite alternate}
@keyframes dr{to{transform:translateX(45px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""

DEFS = """<defs>
<filter id="bark" x="-10%" y="-5%" width="120%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".04 .6" numOctaves="3" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6" result="d"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.2 .75" result="m"/><feComposite in="m" in2="d" operator="in" result="s"/><feMerge><feMergeNode in="d"/><feMergeNode in="s"/></feMerge></filter>
<filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="glow" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="vig" cx="50%" cy="45%" r="75%"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".3"/></radialGradient>
</defs>"""


def _scene(sky, gnd, body, sun="#fff", bark=("#2a1608", "#6b3f1f", "#24120a"), sx=470, sy=95):
    rays = "".join(f'<polygon points="{x},0 {x+40},0 {x-60},470 {x-130},470" fill="#fff" opacity=".14"/>' for x in (360, 430, 500))
    return CSS + f'''<svg viewBox="0 0 600 500" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">{DEFS}
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky[0]}"/><stop offset="1" stop-color="{sky[1]}"/></linearGradient>
<linearGradient id="bk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{bark[0]}"/><stop offset=".45" stop-color="{bark[1]}"/><stop offset="1" stop-color="{bark[2]}"/></linearGradient>
<radialGradient id="sun"><stop offset="0" stop-color="{sun}" stop-opacity=".9"/><stop offset="1" stop-color="{sun}" stop-opacity="0"/></radialGradient>
<linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{gnd[0]}"/><stop offset="1" stop-color="{gnd[1]}"/></linearGradient></defs>
<rect width="600" height="500" fill="url(#sky)"/>
<circle cx="{sx}" cy="{sy}" r="150" fill="url(#sun)"/>
<g class="dr" opacity=".5"><ellipse cx="120" cy="80" rx="70" ry="16" fill="#fff" filter="url(#soft)"/><ellipse cx="190" cy="100" rx="50" ry="12" fill="#fff" filter="url(#soft)"/></g>
<g class="tw" style="--d:7s" filter="url(#soft)">{rays}</g>
<path d="M0 440Q150 415 300 435T600 430V500H0Z" fill="url(#gd)"/>
<ellipse cx="300" cy="462" rx="150" ry="14" fill="#000" opacity=".22" filter="url(#soft)"/>
{body}
<rect width="600" height="500" fill="url(#vig)"/></svg>'''


def _fall(rng, n, cols, sz=(3, 6), y=(40, 240)):
    o = []
    for _ in range(n):
        s = rng.uniform(*sz)
        o.append(f'<ellipse class="fl" cx="{rng.uniform(60, 540):.0f}" cy="{rng.uniform(*y):.0f}" rx="{s:.1f}" ry="{s*.55:.1f}" '
                 f'fill="{rng.choice(cols)}" style="--d:{rng.uniform(6, 11):.1f}s;--l:-{rng.uniform(0, 10):.1f}s;--x:{rng.uniform(-90, 90):.0f}px"/>')
    return "".join(o)


def _tree(rng, x, y, a, ln, w, d, sp, paths, tips):
    """فروع متفرعة بشكل عضوي مع تناقص السماكة."""
    if d == 0:
        tips.append((x, y))
        return
    b = a + rng.uniform(-.2, .2)
    x2, y2 = x + ln * math.sin(b), y - ln * math.cos(b)
    mx, my = x + ln * .5 * math.sin(a), y - ln * .5 * math.cos(a)
    w2, c, s = w * .7, math.cos(a), math.sin(a)
    paths.append(f'M{x-c*w/2:.1f} {y-s*w/2:.1f}Q{mx-c*w*.4:.1f} {my-s*w*.4:.1f} {x2-c*w2/2:.1f} {y2-s*w2/2:.1f}'
                 f'L{x2+c*w2/2:.1f} {y2+s*w2/2:.1f}Q{mx+c*w*.4:.1f} {my+s*w*.4:.1f} {x+c*w/2:.1f} {y+s*w/2:.1f}Z')
    k = 1 if w > 28 else rng.choice((2, 2, 3))
    offs = [0] if k == 1 else [sp * (i / (k - 1) * 2 - 1) for i in range(k)]
    for o in offs:
        _tree(rng, x2, y2, a + o + rng.uniform(-.12, .12), ln * rng.uniform(.7, .82), w2, d - 1, sp, paths, tips)


def _leaves(rng, tips, pal, r=(24, 38), n=2):
    """أوراق بثلاث طبقات (ظل/لون/إضاءة) في ثلاث مناطق تتحرك بإيقاعات مختلفة."""
    dk, mids, lt = pal
    reg = [[], [], []]
    for x, y in tips:
        k = 0 if x < 255 else 1 if x < 345 else 2
        for _ in range(n):
            reg[k].append((x + rng.uniform(-20, 20), y + rng.uniform(-20, 16), rng.uniform(*r), rng.choice(mids)))
    o = []
    for k, bl in enumerate(reg):
        if not bl:
            continue
        s1 = "".join(f'<circle cx="{x:.0f}" cy="{y+r*.12:.0f}" r="{r:.0f}" fill="{dk}"/>' for x, y, r, _ in bl)
        s2 = "".join(f'<circle cx="{x-r*.1:.0f}" cy="{y-r*.1:.0f}" r="{r*.88:.0f}" fill="{c}"/>' for x, y, r, c in bl)
        s3 = "".join(f'<circle cx="{x-r*.3:.0f}" cy="{y-r*.35:.0f}" r="{r*.38:.0f}" fill="{lt}" opacity=".5"/>' for x, y, r, _ in bl)
        o.append(f'<g class="sw" style="--d:{5+k*1.3:.1f}s;--l:-{k*1.7:.1f}s">{s1}{s2}{s3}</g>')
    return "".join(o)


def _hang(rng, tips, cols):
    o = []
    for i, (x, y) in enumerate(t for t in tips if rng.random() < .55):
        c = "".join(f'<circle cx="{x+math.sin(k*.7+i)*3:.0f}" cy="{y+14+k*13:.0f}" r="{max(3, 10-k*.9):.1f}" fill="{cols[k % len(cols)]}"/>' for k in range(8))
        o.append(f'<g class="sh" style="--d:{4+i%4}s;--l:-{i%5}s">{c}</g>')
    return "".join(o)


def _wrap(paths, tips, inner, m=38):
    """يضبط حجم الشجرة تلقائياً لتبقى داخل الإطار."""
    xs, ys = [t[0] for t in tips], [t[1] for t in tips]
    hs = max(abs(min(xs) - 300), abs(max(xs) - 300)) + m
    s = min(1.2, 235 / hs, 380 / (452 - min(ys) + 30))
    d = "".join(paths)
    return (f'<g transform="translate(300 452) scale({s:.3f}) translate(-300 -452)">'
            f'<path d="{d}" fill="url(#bk)" filter="url(#bark)"/>{inner}</g>')


def _decid(seed, pal, sky, gnd, bark, fc=None, sun="#fff", sx=470, glow=False, sz=(3, 6), hang=None, fn=22):
    rng = random.Random(seed)
    paths, tips = [], []
    _tree(rng, 300, 452, 0, 105, 36, 6, .5, paths, tips)
    lv = _leaves(rng, tips, pal)
    if hang:
        lv += _hang(rng, tips, hang)
    if glow:
        lv = f'<g filter="url(#glow)">{lv}</g>'
    body = _wrap(paths, tips, lv) + (_fall(rng, fn, fc, sz) if fc else "")
    return _scene(sky, gnd, body, sun, bark, sx)


# ---------- شجرة الساكورا الجديدة ----------
FL = ('<defs><g id="f5">' + "".join(f'<ellipse cx="0" cy="-9" rx="5.5" ry="9" transform="rotate({a})"/>' for a in range(0, 360, 72)) + '<circle r="2.6" fill="#e0457b"/></g></defs>')


def _limb(p0, c1, c2, p1, w0, w1, n=18):
    L, R, pts = [], [], []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p1[0]
        y = u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p1[1]
        dx = 3 * u * u * (c1[0] - p0[0]) + 6 * u * t * (c2[0] - c1[0]) + 3 * t * t * (p1[0] - c2[0])
        dy = 3 * u * u * (c1[1] - p0[1]) + 6 * u * t * (c2[1] - c1[1]) + 3 * t * t * (p1[1] - c2[1])
        m = math.hypot(dx, dy) or 1
        w = (w0 + (w1 - w0) * t) / 2
        L.append((x - dy / m * w, y + dx / m * w))
        R.append((x + dy / m * w, y - dx / m * w))
        pts.append((x, y, math.atan2(dy, dx)))
    return "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in L + R[::-1]) + "Z", pts


def _sakura():
    rng = random.Random(12)
    limbs = [((280, 458), (268, 385), (322, 340), (296, 268), 46, 26),
             ((296, 292), (268, 255), (205, 246), (148, 192), 22, 7),
             ((298, 300), (340, 252), (412, 262), (462, 198), 22, 7),
             ((297, 272), (296, 222), (326, 182), (312, 118), 17, 6),
             ((288, 352), (250, 336), (198, 348), (146, 322), 14, 6),
             ((300, 342), (352, 330), (402, 342), (446, 308), 14, 6)]
    trunk, ticks, crown, anchors = "", "", "", []
    for k, (p0, c1, c2, p1, w0, w1) in enumerate(limbs):
        d, pts = _limb(p0, c1, c2, p1, w0, w1)
        if k == 0:
            trunk = d
            ticks = "".join(f"M{x-7:.0f} {y:.0f}q6 -3 13 0" for x, y, _ in pts[2:-2:2])
            continue
        crown += f'<path d="{d}"/>'
        anchors += [pts[-1][:2], pts[9][:2]]
        for j in (7, 10, 13):
            bx, by, a = pts[j]
            for sg in (-1, 1):
                ta, ln = a + sg * rng.uniform(.5, 1.0), rng.uniform(30, 55)
                ca, sa = math.cos(ta), math.sin(ta)
                dd, pp = _limb((bx, by), (bx + ln * .3 * ca, by + ln * .3 * sa - 6), (bx + ln * .7 * ca, by + ln * .7 * sa - 10),
                               (bx + ln * ca, by + ln * sa - 8), 5, 1.5, 8)
                crown += f'<path d="{dd}"/>'
                anchors.append(pp[-1][:2])
    reg = [([], [], []) for _ in range(3)]
    for x, y in anchors:
        B, M, F = reg[0 if x < 250 else 1 if x < 350 else 2]
        for _ in range(3):
            B.append(f'<circle cx="{x+rng.uniform(-24, 24):.0f}" cy="{y+rng.uniform(-22, 18):.0f}" r="{rng.uniform(16, 28):.0f}" fill="#f06aa4" opacity=".4"/>')
        for _ in range(5):
            M.append(f'<circle cx="{x+rng.uniform(-28, 28):.0f}" cy="{y+rng.uniform(-26, 22):.0f}" r="{rng.uniform(9, 16):.0f}" '
                     f'fill="{rng.choice(["#f9a8d4", "#fbcfe8", "#f472b6", "#fda4cf"])}" opacity=".92"/>')
        for _ in range(3):
            F.append(f'<use href="#f5" fill="{rng.choice(["#fff1f6", "#ffe0ec", "#ffc2dc"])}" '
                     f'transform="translate({x+rng.uniform(-30, 30):.0f} {y+rng.uniform(-28, 24):.0f}) rotate({rng.uniform(0, 72):.0f}) scale({rng.uniform(.5, .8):.2f})"/>')
    blossoms = "".join(f'<g class="sw" style="--d:{5+k*1.3:.1f}s;--l:-{k*1.7:.1f}s">{"".join(B)}{"".join(M)}{"".join(F)}</g>' for k, (B, M, F) in enumerate(reg))
    bokeh = '<g class="tw" filter="url(#soft)">' + "".join(
        f'<circle cx="{rng.uniform(40, 560):.0f}" cy="{rng.uniform(40, 300):.0f}" r="{rng.uniform(8, 22):.0f}" fill="#ffc2dc" opacity=".5"/>' for _ in range(9)) + "</g>"
    ground = "".join(
        f'<ellipse cx="{rng.uniform(150, 450):.0f}" cy="{rng.uniform(450, 478):.0f}" rx="{rng.uniform(2.5, 5):.1f}" ry="2" fill="{rng.choice(["#fbcfe8", "#f9a8d4", "#fff1f6"])}" opacity=".85"/>' for _ in range(45))
    body = (FL + bokeh + ground + f'<path d="{trunk}" fill="url(#bk)" filter="url(#bark)"/>'
            f'<path d="{ticks}" stroke="#e8d6cf" stroke-opacity=".45" stroke-width="1.6" fill="none" stroke-linecap="round"/>'
            f'<g class="sw" style="--d:8s;transform-box:view-box;transform-origin:300px 300px"><g fill="url(#bk)">{crown}</g>{blossoms}</g>'
            + _fall(rng, 26, ["#fbcfe8", "#f9a8d4", "#fff1f6"], (3.5, 7), (40, 300)))
    return _scene(("#ffe1ea", "#fff8fa"), ("#cfeacb", "#9fd193"), body, "#ffd6e3", ("#3a2a28", "#7a5a52", "#2a1c1a"))


# ---------- باقي الأشجار ----------
def _pine():
    rng = random.Random(5)
    o = '<rect x="288" y="350" width="26" height="112" fill="url(#bk)" filter="url(#bark)"/>'
    for i in range(5, -1, -1):
        t, w = 70 + i * 55, 48 + i * 27
        b = t + 100
        z = [(300 + w - 2 * w * k / 6, b - (14 if k % 2 else 0)) for k in range(1, 6)]
        full = " ".join(f"{x:.0f},{y:.0f}" for x, y in [(300, t), (300 + w, b)] + z + [(300 - w, b)])
        left = f"300,{t} {300-w},{b} 300,{b-8}"
        sn = " ".join(f"{300+u*w:.0f},{t+v}" for u, v in [(0, 0), (.52, 52), (.3, 42), (.15, 56), (0, 44), (-.15, 56), (-.3, 42), (-.52, 52)])
        o += (f'<g class="sw" style="--d:{5+i*.4:.1f}s;--l:-{i*.8:.1f}s"><polygon points="{full}" fill="hsl(162,58%,{13+(5-i)*1.6}%)"/>'
              f'<polygon points="{left}" fill="hsl(158,50%,{27+(5-i)*1.6}%)"/><polygon points="{sn}" fill="#f1f8ff" opacity=".93"/></g>')
    return _scene(("#9db4cf", "#e8f1fa"), ("#f4f8fc", "#cfdbe8"), o + _fall(rng, 28, ["#fff", "#e6f2ff"], (1.5, 3), (0, 300)),
                  "#fff", ("#2a1c14", "#5c4030", "#1d130e"))


def _frond(cx, cy, deg, L, c1, c2):
    th = math.radians(deg)
    p0 = (cx, cy)
    p1 = (cx + .5 * L * math.cos(th), cy + .5 * L * math.sin(th) - 45)
    p2 = (cx + L * math.cos(th), cy + L * math.sin(th) + 55)
    lf = []
    for j in range(2, 19):
        t = j / 18
        x = (1 - t) ** 2 * p0[0] + 2 * t * (1 - t) * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * t * (1 - t) * p1[1] + t * t * p2[1]
        tx = 2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        ty = 2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        ln = 44 * (1 - .55 * t)
        for s in (1, -1):
            g = math.atan2(ty, tx) + s * 1.0
            lf.append(f"M{x:.0f} {y:.0f}L{x+ln*math.cos(g):.0f} {y+ln*math.sin(g)+10:.0f}")
    rib = f"M{cx} {cy}Q{p1[0]:.0f} {p1[1]:.0f} {p2[0]:.0f} {p2[1]:.0f}"
    return (f'<path d="{"".join(lf)}" stroke="{c1}" stroke-width="3.4" stroke-linecap="round" fill="none"/>'
            f'<path d="{rib}" stroke="{c2}" stroke-width="4" stroke-linecap="round" fill="none"/>')


def _palm():
    cx, cy = 300, 160
    tr = f"M250 458Q335 300 {cx} {cy}"
    o = (f'<path d="{tr}" stroke="#6e4524" stroke-width="26" fill="none" stroke-linecap="round" filter="url(#bark)"/>'
         f'<path d="{tr}" stroke="#a87444" stroke-opacity=".55" stroke-width="8" fill="none"/>'
         f'<path d="{tr}" stroke="#25140a" stroke-opacity=".5" stroke-width="27" fill="none" stroke-dasharray="2 11"/>')
    for i, d in enumerate([-168, -142, -114, -66, -38, -12, 12, 168]):
        c1 = "#1f8a3c" if i % 2 else "#2fae4f"
        o += (f'<g class="sw" style="--d:{4+i%3}s;--l:-{i*.7:.1f}s;transform-box:view-box;transform-origin:{cx}px {cy}px">'
              f'{_frond(cx, cy, d, 165, c1, "#14532d")}</g>')
    o += "".join(f'<circle cx="{cx+u}" cy="{cy+14+v}" r="9" fill="#4a2c12"/>' for u, v in [(-12, 0), (8, 4), (-2, 14)])
    return _scene(("#ff9a5a", "#ffe3b3"), ("#f3d9a0", "#d9b36a"), o, "#fff2b0", ("#3a2210", "#7a4a28", "#24120a"), 430, 150)


def _m(x, s, spots=True):
    sp = "".join(f'<ellipse cx="{u}" cy="{v}" rx="{r}" ry="{r*.7:.0f}" fill="#fff" opacity=".92"/>'
                 for u, v, r in [(-80, -262, 20), (50, -288, 26), (0, -232, 13), (-115, -226, 14), (105, -236, 16)]) if spots else ""
    return (f'<g transform="translate({x} 462) scale({s})">'
            '<path d="M-38 0C-32 -80 -30 -140 -24 -200L24 -200C30 -140 32 -80 38 0Z" fill="url(#st)"/>'
            '<path d="M-30 -170Q0 -150 30 -170Q0 -132 -30 -170Z" fill="#efe9ff"/>'
            '<ellipse cx="0" cy="-204" rx="152" ry="26" fill="#cdb9ee"/>'
            f'<g class="sw" style="--d:6s"><path d="M-160 -200C-160 -352 160 -352 160 -200C100 -176 -100 -176 -160 -200Z" fill="url(#cap)"/>{sp}'
            '<path d="M-120 -270Q-60 -330 20 -325" stroke="#fff" stroke-opacity=".35" stroke-width="8" fill="none" stroke-linecap="round"/></g></g>')


def _shroom():
    rng = random.Random(4)
    o = ('<defs><radialGradient id="cap" cx=".4" cy=".25" r=".9"><stop offset="0" stop-color="#ff7a7a"/><stop offset=".6" stop-color="#e11d2e"/><stop offset="1" stop-color="#7f0f1d"/></radialGradient>'
         '<linearGradient id="st"><stop offset="0" stop-color="#e9e4ff"/><stop offset=".5" stop-color="#cfc6f2"/><stop offset="1" stop-color="#8f84c9"/></linearGradient></defs>'
         '<ellipse cx="300" cy="462" rx="200" ry="26" fill="#6d5dfc" opacity=".4" filter="url(#soft)"/>')
    o += _m(300, 1) + _m(110, .38) + _m(500, .3)
    o += '<g class="dr" filter="url(#glow)">' + "".join(
        f'<circle class="tw" cx="{rng.uniform(40, 560):.0f}" cy="{rng.uniform(90, 440):.0f}" r="{rng.uniform(1.5, 3.2):.1f}" fill="#fde68a" style="--d:{rng.uniform(2, 5):.1f}s;--l:-{rng.uniform(0, 4):.1f}s"/>'
        for _ in range(26)) + "</g>"
    return _scene(("#0d0b2e", "#2e2a78"), ("#1c1a4d", "#0e0c2c"), o, "#8b7bff", sx=120, sy=90)


def _gem(x, y, w, h, c):
    p = lambda *a: " ".join(f"{x+u*w:.1f},{y+v*h:.1f}" for u, v in a)
    T, UL, UR, LL, LR, B, C = (0, -1), (-.9, -.4), (.9, -.4), (-.9, .4), (.9, .4), (0, 1), (0, -.4)
    return (f'<polygon points="{p(T, UL, C)}" fill="{c[0]}"/><polygon points="{p(UL, C, B, LL)}" fill="{c[1]}"/>'
            f'<polygon points="{p(UR, C, B, LR)}" fill="{c[2]}"/><polygon points="{p(T, UR, C)}" fill="{c[3]}"/>')


def _crystal():
    rng = random.Random(21)
    paths, tips = [], []
    _tree(rng, 300, 452, 0, 95, 30, 5, .55, paths, tips)
    cry = [("#bff0ff", "#38bdf8", "#0369a1", "#e0faff"), ("#d6ccff", "#818cf8", "#4338ca", "#eef0ff"), ("#b6fff0", "#2dd4bf", "#0f766e", "#dffff9")]
    g = ""
    for i, (x, y) in enumerate(tips):
        w = rng.uniform(9, 17)
        g += f'<g class="tw" style="--d:{2+i%4}s;--l:-{i%7*.6:.1f}s">{_gem(x, y, w, w*rng.uniform(1.5, 2.2), rng.choice(cry))}</g>'
    sp = "".join(f'<path class="tw" d="M0-7L2-2L7 0L2 2L0 7L-2 2L-7 0L-2-2Z" transform="translate({rng.uniform(70, 530):.0f} {rng.uniform(60, 420):.0f}) scale({rng.uniform(.5, 1.1):.2f})" fill="#fff" style="--d:{rng.uniform(2, 4):.1f}s;--l:-{rng.uniform(0, 3):.1f}s"/>' for _ in range(16))
    return _scene(("#0b1224", "#1d2b4d"), ("#26364f", "#101a2e"), _wrap(paths, tips, f'<g filter="url(#glow)">{g}</g>', 24) + sp,
                  "#38bdf8", ("#0b1226", "#27406b", "#070c1a"), 120, 90)


def _bonsai():
    rng = random.Random(9)
    br = "M300 440C230 400 350 340 285 285C235 242 330 205 300 150"
    o = (f'<path d="{br}" stroke="url(#bk)" stroke-width="34" fill="none" stroke-linecap="round" filter="url(#bark)"/>'
         f'<path d="{br}" stroke="#000" stroke-opacity=".18" stroke-width="3" fill="none" stroke-dasharray="14 9"/>')
    for d, w in [("M292 300C250 285 215 270 205 235", 14), ("M300 215C350 205 390 215 400 185", 12), ("M288 345C340 335 380 340 395 310", 12)]:
        o += f'<path d="{d}" stroke="url(#bk)" stroke-width="{w}" fill="none" stroke-linecap="round" filter="url(#bark)"/>'
    o += _leaves(rng, [(300, 140), (205, 228), (400, 178), (392, 304)], ("#14532d", ["#15803d", "#16a34a", "#22c55e", "#4ade80"], "#bbf7d0"), (20, 30), 4)
    o += ('<path d="M190 432H410L392 470Q390 480 380 480H220Q210 480 208 470Z" fill="#8a5a44"/><rect x="182" y="424" width="236" height="14" rx="5" fill="#a56a50"/>'
          '<ellipse cx="300" cy="428" rx="108" ry="6" fill="#3b2a1e"/>') + _fall(rng, 6, ["#22c55e", "#4ade80"], (3, 5), (60, 200))
    return _scene(("#eef2e6", "#faf7ef"), ("#e8dfcf", "#cbbfa6"), o, "#fff4d6", ("#241812", "#5a4030", "#1a110c"))


def _bamboo():
    rng = random.Random(2)
    o = ('<defs><linearGradient id="bam"><stop offset="0" stop-color="#9be08a"/><stop offset=".35" stop-color="#46a84f"/><stop offset="1" stop-color="#1d6b30"/></linearGradient></defs>'
         '<g class="dr" opacity=".4"><ellipse cx="200" cy="400" rx="190" ry="26" fill="#fff" filter="url(#soft)"/><ellipse cx="420" cy="340" rx="170" ry="22" fill="#fff" filter="url(#soft)"/></g>')
    for i, (x, w, h) in enumerate([(150, 26, 430), (235, 32, 470), (330, 38, 490), (430, 30, 450), (505, 22, 400)]):
        top, ny, segs, lvs = 462 - h, 462, "", ""
        while ny > top + 20:
            y2 = max(top, ny - 92 + rng.uniform(-8, 8))
            segs += (f'<rect x="{x-w/2:.0f}" y="{y2:.0f}" width="{w}" height="{ny-y2:.0f}" rx="4" fill="url(#bam)"/>'
                     f'<rect x="{x-w/2-2:.0f}" y="{y2-3:.0f}" width="{w+4}" height="7" rx="3" fill="#1d5c2a"/>')
            if y2 < 380:
                for side in (1, -1):
                    for _ in range(2):
                        a = rng.uniform(-35, 20) if side == 1 else rng.uniform(160, 215)
                        lvs += (f'<path d="M0 0Q18 -9 46 3Q20 10 0 0Z" fill="{rng.choice(["#3f9b4a", "#5cb35e", "#2f8a3e"])}" '
                                f'transform="translate({x} {y2:.0f}) rotate({a:.0f}) scale({rng.uniform(.8, 1.3):.2f})"/>')
            ny = y2
        o += f'<g class="sw" style="--d:{5+i}s;--l:-{i*1.3:.1f}s">{segs}{lvs}</g>'
    o += _fall(rng, 10, ["#4aa650", "#86d27a"], (4, 7), (40, 300))
    return _scene(("#d9f2dc", "#f4fbf1"), ("#b5d9a3", "#7fb36d"), o, "#fff6c2")


def get_tree_svg(active):
    """يعيد كود SVG + CSS كاملاً للشجرة المفعّلة."""
    a = active
    if "الساكورا" in a:
        return _sakura()
    if "الصنوبر" in a:
        return _pine()
    if "الفطر" in a:
        return _shroom()
    if "النخيل" in a:
        return _palm()
    if "القيقب" in a:
        return _decid(5, ("#8f2a07", ["#ea580c", "#dc2626", "#f59e0b", "#f97316"], "#fde68a"), ("#ffd9a8", "#fff0dc"), ("#e6c58a", "#b8863e"),
                      ("#24120a", "#5a3320", "#1a0d06"), ["#ea580c", "#dc2626", "#f59e0b"], "#ffd27a", sz=(4, 8))
    if "الويسترليا" in a:
        return _decid(8, ("#5b21b6", ["#a855f7", "#c084fc", "#d8b4fe", "#8b5cf6"], "#f5e8ff"), ("#ede4ff", "#fbf7ff"), ("#dcefd5", "#a6cf9b"),
                      ("#2a1030", "#5e3a4e", "#1e0c24"), ["#e9d5ff", "#c084fc"], "#e9d5ff", hang=["#a855f7", "#c084fc", "#d8b4fe"], fn=10)
    if "الكريستال" in a:
        return _crystal()
    if "البنساي" in a:
        return _bonsai()
    if "البامبو" in a:
        return _bamboo()
    return _decid(3, ("#7f1d1d", ["#ef4444", "#f97316", "#fb923c", "#facc15"], "#fef08a"), ("#140a0a", "#4a1208"), ("#2a1210", "#14090a"),
                  ("#0c0606", "#3a1a14", "#050303"), ["#fde047", "#fb923c", "#ef4444"], "#ff7a1a", glow=True, sz=(2, 4))


# ==========================================
# 0.5 محرك التحليل الدقيق والمهام
# ==========================================
SNACK_OPTS = [
    "🍏 وجبة ذكية خفيفة (مكسرات، فواكه، زبادي)",
    "🥩 وجبة غنية بالبروتين (بيض، دجاج، أسماك)",
    "🍝 وجبة غداء ثقيلة/كاربوهيدرات (رز، معكرونة، وجبات سريعة)",
    "🍩 سكريات ومشروبات طاقة (حلويات، عصائر مصنعة)",
    "☕ معتمدة على الكافيين فقط (قهوة/شاي بدون طعام)",
    "🌙 صائم / لم أتناول وجبة"
]
METHOD_OPTS = [
    "التسجيل النشط والخرائط الذهنية",
    "حل المسائل والتطبيقات العملية",
    "القراءة التكرارية الصامتة"
]
PHONE_OPTS = [
    "مفصول تماماً في غرفة ثانية",
    "قريب بصامت ومقلوب",
    "في اليد أو بجانب الكتاب"
]
SNACK = [90, 95, 45, 35, 40, 30]
METHOD = [100, 95, 60]
PHONE = [100, 60, 20]


def _c(v):
    return max(0.0, min(100.0, v))


def analyze(sh, sq, scr, ts, df, temp, ot, stress, mo, hy, snack, method, phone):
    dur = 100 if 7 <= sh <= 9 else 100 - (7 - sh if sh < 7 else sh - 9) * 25
    sleep = _c(.55 * dur + .45 * sq / 15 * 100)
    df = min(df, ts)
    focus = _c(.6 * df / ts * 100 + .4 * min(df / 4, 1) * 100)
    eyes = _c(100 - max(0, scr - 2) * 9)
    tmp = _c(100 if 21 <= temp <= 24 else 100 - (21 - temp if temp < 21 else temp - 24) * 12)
    ph = PHONE[PHONE_OPTS.index(phone)]
    env = _c(.4 * tmp + .4 * ph + .2 * eyes)
    mind = _c(100 - ot / 120 * 55 - (stress - 1) / 14 * 45)
    sn = SNACK[SNACK_OPTS.index(snack)]
    energy = _c(.4 * (mo - 1) / 14 * 100 + .25 * (hy - 1) / 14 * 100 + .35 * sn)
    meth = METHOD[METHOD_OPTS.index(method)]
    total = (.25 * sleep + .25 * focus + .15 * energy + .15 * mind + .10 * env + .10 * meth) * 5
    goals = [
        ("😴 نوم 7 ساعات أو أكثر", sh >= 7),
        ("🎯 تركيز نقي 3 ساعات أو أكثر", df >= 3),
        ("📵 الهاتف مفصول تماماً", ph == 100),
        ("💧 ترطيب 10 من 15 أو أكثر", hy >= 10),
        ("🌀 تفكير زائد 30 دقيقة أو أقل", ot <= 30),
        ("📱 شاشة 5 ساعات أو أقل", scr <= 5),
    ]
    return dict(sleep=sleep, focus=focus, eyes=eyes, temp=tmp, phone=ph, env=env, mind=mind,
                energy=energy, snack=sn, method=meth, total=total, goals=goals)


def grade(v):
    return "ممتاز 🌟" if v >= 85 else "جيد جداً ✅" if v >= 70 else "متوسط ⚠️" if v >= 55 else "يحتاج تحسين 🔴"


def show_metrics(items, ncols=2):
    cols = st.columns(ncols)
    for i, (name, v) in enumerate(items):
        cols[i % ncols].metric(name, f"{v:.1f}%")
        cols[i % ncols].progress(int(round(v)))


def show_tips(tips, ok_msg):
    if tips:
        for t in tips:
            st.warning(t)
    else:
        st.success(ok_msg)


# ==========================================
# 1. إعدادات الصفحة والتصميم العصري
# ==========================================
st.set_page_config(
    page_title="وعلم الإنسان ما لم يعلم | النظام التحليلي المتطور",
    page_icon="🎓",
    layout="wide"
)

# تهيئة ذاكرة الجلسة
if "history" not in st.session_state:
    st.session_state.history = []

if "mind_dump" not in st.session_state:
    st.session_state.mind_dump = []

if "user_points" not in st.session_state:
    st.session_state.user_points = 100

if "last_sig" not in st.session_state:
    st.session_state.last_sig = None

if "unlocked_trees" not in st.session_state:
    st.session_state.unlocked_trees = ["🌸 شجرة الساكورا اليابانية الساحرة"]

if "active_tree" not in st.session_state:
    st.session_state.active_tree = "🌸 شجرة الساكورا اليابانية الساحرة"

# CSS العام للتصميم النظيف
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    .main {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #6366f1;
        border-right: 6px solid #f97316;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);
    }

    .hero-verse {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f97316;
        margin-bottom: 5px;
    }

    .hero-title {
        font-weight: 900;
        font-size: 1.75rem;
        color: #ffffff;
    }

    .clean-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #10b981;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }

    .stButton>button {
        background: #10b981;
        color: white;
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #059669;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر
st.markdown("""
    <div class="hero-container">
        <div class="hero-verse">✨ « وَعَلَّمَ الإِنْسَانَ مَا لَمْ يَعْلَمْ » 🧠</div>
        <div class="hero-title">🚀 متجر الأشجار الواقعية الفخمة والأنيميشن السينمائي المتقدم</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. اللوحة الجانبية: نموذج الإدخال (Form)
# ==========================================
with st.sidebar.form(key="main_form"):
    st.markdown("### 🎛️ لوحة القياسات الحيوية")
    st.caption("أدخل بياناتك ثم اضغط (إرسال وتحليل) للحفظ والتقييم")

    sleep_hours = st.slider("🌙 ساعات النوم اليومية", 3.0, 12.0, 7.5, 0.25)
    sleep_quality = st.slider("✨ جودة النوم الاستشفائي (1-15)", 1, 15, 12)
    screen_hours = st.slider("📱/🖥️ ساعات الشاشة (الإجهاد البصري)", 1.0, 14.0, 4.5, 0.25)

    total_study = st.slider("⏱️ إجمالي ساعات التواجد الدراسي", 1.0, 12.0, 4.0, 0.25)
    deep_focus = st.slider("🎯 ساعات التركيز النقي الصافي", 0.5, 12.0, 3.5, 0.25)

    room_temp = st.slider("🌡️ حرارة الغرفة (مئوية)", 16.0, 32.0, 23.0, 0.5)
    overthinking_mins = st.slider("🌀 دقائق التفكير الزائد والقلق", 0, 120, 20, 1)

    stress_level = st.slider("⚠️ مستوى التوتر العصبي (1-15)", 1, 15, 5)
    motivation_level = st.slider("🔥 الدافعية والحماس (1-15)", 1, 15, 12)
    hydration_level = st.slider("💧 مستوى ترطيب الجسم (1-15)", 1, 15, 11)

    snack_type = st.selectbox("🍱 نوع الوجبة الخفيفة قبل المذاكرة", SNACK_OPTS)
    study_method = st.selectbox("📚 أسلوب المذاكرة الأساسي", METHOD_OPTS)
    phone_isolation = st.selectbox("📵 عزل الهاتف الخلوي", PHONE_OPTS)

    submit_btn = st.form_submit_button(label="🚀 إرسال وتحليل البيانات")

# التحليل الدقيق للقيم الحالية
R = analyze(sleep_hours, sleep_quality, screen_hours, total_study, deep_focus, room_temp,
            overthinking_mins, stress_level, motivation_level, hydration_level,
            snack_type, study_method, phone_isolation)

if submit_btn:
    sig = (sleep_hours, sleep_quality, screen_hours, total_study, deep_focus, room_temp,
           overthinking_mins, stress_level, motivation_level, hydration_level,
           snack_type, study_method, phone_isolation)
    if deep_focus > total_study:
        st.warning("⚠️ ساعات التركيز النقي لا يمكن أن تزيد عن إجمالي ساعات التواجد الدراسي. صحّح القيم ثم أعد الإرسال.")
    elif sig == st.session_state.last_sig:
        st.info("ℹ️ هذه نفس البيانات السابقة. غيّر بعض القيم لتحصل على نقاط جديدة.")
    else:
        done = sum(1 for _, ok in R["goals"] if ok)
        base = round(R["total"] / 500 * 60)
        perfect = 40 if done == len(R["goals"]) else 0
        gain = base + 15 * done + perfect
        st.session_state.user_points += gain
        st.session_state.last_sig = sig
        st.session_state.history.append({"الدرجة": round(R["total"], 1), "النقاط": gain})
        msg = f"✅ تم حفظ التحليل واكتسبت +{gain} نقطة (التحليل {base} + المهام {done}×15"
        msg += f" + مكافأة اليوم المثالي {perfect})" if perfect else ")"
        st.success(msg)

# ==========================================
# 3. التبويبات الرئيسية
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 المؤشرات والموجز",
    "🌿 البيئة والاستشفاء",
    "⚡ الطاقة والتحفيز",
    "🧠 التحليل والتفريغ",
    "🌳 معارض الأشجار الواقعية",
    "🏛️ منصة الحكام والاستثمار"
])

# --- TAB 1: المؤشرات والموجز ---
with tab1:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🎯 مؤشر التحصيل المعرفي الحالي")
    st.metric("النتيجة المعيارية الإجمالية", f"{R['total']:.1f} / 500 نقطة", delta=grade(R["total"]), delta_color="off")
    st.progress(int(round(R["total"] / 5)))
    show_metrics([
        ("😴 النوم", R["sleep"]), ("🎯 التركيز", R["focus"]), ("⚡ الطاقة", R["energy"]),
        ("🧠 الصفاء الذهني", R["mind"]), ("🌿 البيئة", R["env"]), ("📚 أسلوب المذاكرة", R["method"])
    ], 3)
    st.markdown("#### 🎯 مهام اليوم (كل مهمة منجزة = +15 نقطة)")
    for name, ok in R["goals"]:
        st.write(("✅ " if ok else "⬜ ") + name)
    if len(st.session_state.history) > 1:
        st.markdown("#### 📈 تطور درجتك مع كل تحليل")
        st.line_chart(pd.DataFrame(st.session_state.history)["الدرجة"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: البيئة والاستشفاء ---
with tab2:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌿 تحليل البيئة العصبية")
    show_metrics([
        ("😴 جودة الاستشفاء (النوم)", R["sleep"]), ("🌡️ ملاءمة حرارة الغرفة", R["temp"]),
        ("📵 عزل الهاتف", R["phone"]), ("👁️ راحة العين", R["eyes"])
    ])
    tips = []
    if sleep_hours < 7 or sleep_hours > 9:
        tips.append(f"😴 نومك {sleep_hours:g} ساعة، والمدى المثالي من 7 إلى 9 ساعات.")
    if not 21 <= room_temp <= 24:
        tips.append(f"🌡️ حرارة الغرفة {room_temp:g}°م، والمثالي بين 21 و24°م.")
    if phone_isolation != PHONE_OPTS[0]:
        tips.append("📵 الهاتف قريب منك، وفصله في غرفة ثانية يرفع التركيز بوضوح.")
    if screen_hours > 5:
        tips.append(f"📱 ساعات الشاشة {screen_hours:g}، حاول خفضها إلى 5 ساعات أو أقل مع استراحات للعين.")
    show_tips(tips, "🍃 ظروف النوم والإضاءة والحرارة والتهوية ضمن المدى المثالي للتركيز.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: الطاقة والتحفيز ---
with tab3:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("⚡ محرك الطاقة المعرفية")
    show_metrics([
        ("⚡ مؤشر الطاقة الكلي", R["energy"]), ("🔥 الدافعية", (motivation_level - 1) / 14 * 100),
        ("💧 الترطيب", (hydration_level - 1) / 14 * 100), ("🍱 جودة الوجبة", R["snack"])
    ])
    tips = []
    if hydration_level < 8:
        tips.append("💧 مستوى الترطيب منخفض، اشرب كوب ماء قبل المذاكرة وخلالها.")
    if motivation_level < 8:
        tips.append("🔥 الدافعية منخفضة، ابدأ بمهمة صغيرة سهلة لتكسر الجمود.")
    if R["snack"] < 50:
        tips.append("🍱 وجبتك الحالية ضعيفة للتركيز، استبدلها بمكسرات أو فواكه أو بروتين.")
    show_tips(tips, "⚡ طاقتك وترطيبك ودافعيتك في مستوى ممتاز.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 4: التحليل والتفريغ ---
with tab4:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🧠 التفريغ الذهني")
    show_metrics([
        ("🧠 الصفاء الذهني الكلي", R["mind"]),
        ("🌀 هدوء التفكير", 100 - overthinking_mins / 120 * 100),
        ("⚠️ استقرار الأعصاب", 100 - (stress_level - 1) / 14 * 100),
        ("🎯 كفاءة التركيز", R["focus"])
    ])
    tips = []
    if overthinking_mins > 30:
        tips.append(f"🌀 {overthinking_mins} دقيقة من التفكير الزائد، دوّن أفكارك على ورقة لتفرغها من ذهنك.")
    if stress_level > 8:
        tips.append("⚠️ التوتر مرتفع، جرّب تنفساً عميقاً لدقيقتين قبل المذاكرة.")
    show_tips(tips, "🗑️ الذاكرة المؤقتة منقّاة والتفكير الزائد ضمن الحدود الطبيعية.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 5: معرض الأشجار ---
# ==========================================
with tab5:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🌳 المعرض الفني للأشجار الواقعية المتقدمة والأنيميشن")
    st.write("تصاميم فنية عضوية متكاملة ومتحركة (تتضمن تدرجات لونية، لحاء أشجار مفصل، وتساقط بتلات وأوراق حية):")

    active = st.session_state.active_tree
    svg_tree_render = get_tree_svg(active)

    components.html(f"""
    <div style="width: 100%; height: 480px; border-radius: 20px; overflow: hidden; border: 3px solid #334155; box-shadow: 0 15px 30px rgba(0,0,0,0.2); background: #fff;">
        {svg_tree_render}
    </div>
    """, height=490)

    st.markdown(f"### 🌲 الشجرة النشطة حالياً: **{active}**")
    st.info("✨ هذه الشجرة مصممة برسم هندسي عضوي وأنيميشن سينمائي عالي الجودة.")

    st.markdown("---")
    st.markdown("### 🛒 متجر الـ 10 أشجار الواقعية والأيقونية")
    st.write(f"رصيد نقاطك الحالي: **{st.session_state.user_points} نقطة** 🪙")
    st.caption("💡 تكسب في كل تحليل جديد حتى 60 نقطة حسب درجتك، و15 نقطة لكل مهمة منجزة، و40 نقطة مكافأة اليوم المثالي.")

    trees_catalog = [
        {"name": "🌸 شجرة الساكورا اليابانية الساحرة", "price": 0, "env": "بيئة ربيعية زهرية"},
        {"name": "🌲 شجرة الصنوبر الثلجية", "price": 250, "env": "بيئة جبلية شتوية"},
        {"name": "🍄 شجرة الفطر الساحرة", "price": 500, "env": "بيئة غامضة مضيئة"},
        {"name": "🌴 شجرة النخيل الاستوائية", "price": 800, "env": "بيئة واحة مشمسة"},
        {"name": "🍁 شجرة القيقب الخريفية", "price": 1200, "env": "بيئة خريفية دافئة"},
        {"name": "🔮 شجرة الويسترليا البنفسجية", "price": 1700, "env": "بيئة أرجوانية ساحرة"},
        {"name": "💎 شجرة الكريستال البلورية", "price": 2300, "env": "بيئة جليدية مشعة"},
        {"name": "🌿 شجرة البنساي العتيقة", "price": 3000, "env": "بيئة صخرية يابانية"},
        {"name": "🎋 غابة البامبو الآسيوية", "price": 3800, "env": "بيئة غابة هادئة"},
        {"name": "🔥 شجرة العنقاء النارية", "price": 5000, "env": "بيئة طاقة أسطورية"}
    ]

    cols_shop = st.columns(3)
    for idx, t in enumerate(trees_catalog):
        with cols_shop[idx % 3]:
            st.markdown(f"**{t['name']}**")
            st.caption(f"🌍 {t['env']}")

            is_unlocked = t['name'] in st.session_state.unlocked_trees
            if is_unlocked:
                if active == t['name']:
                    st.success("✅ المفعلة حالياً")
                else:
                    if st.button("تفعيل", key=f"act_{idx}"):
                        st.session_state.active_tree = t['name']
                        st.rerun()
            else:
                missing = max(0, t['price'] - st.session_state.user_points)
                st.caption(f"🔒 تحتاج {missing} نقطة إضافية" if missing else "🔓 رصيدك يكفي لشرائها")
                if st.button(f"شراء ({t['price']} ن)", key=f"buy_{idx}"):
                    if st.session_state.user_points >= t['price']:
                        st.session_state.user_points -= t['price']
                        st.session_state.unlocked_trees.append(t['name'])
                        st.session_state.active_tree = t['name']
                        st.success("🎉 مبروك! تم التفعيل بنجاح!")
                        st.rerun()
                    else:
                        st.error("❌ النقاط غير كافية!")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# --- TAB 6: منصة الحكام والاستثمار ---
# ==========================================
with tab6:
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)
    st.subheader("🏛️ منطقة الحكام والاستثمار")

    st.markdown("""
    ### 📌 نبذة سريعة عن المشروع:
    نظام ذكي متكامل لقياس وتحليل الأنماط المعرفية والبيئية للطلاب، يدمج بين علم النفس العصبي والتفاعل البصري المتقدم لتعزيز التحصيل الدراسي.

    ---
    ### 💡 رؤية التطوير والاستثمار (لماذا هذا المشروع واعد؟):
    * **قابلية التخصيص الكامل:** المنصة مصممة بهندسة مرنة تتيح لكل مستخدم أو مؤسسة تخصيص بيئتها وتجربتها بالكامل.
    * **مرتكز للمطورين (Extensibility):** البنية البرمجية قابلة للدمج والتطوير المستمر بسهولة تامة.
    * **الفرصة الاستثمارية:** يمثل المنتج حلاً حقيقياً لأسواق التعليم الرقمي (EdTech) والصحة العقلية، بطلب استهلاكي مرتفع وقابلية توسع تجاري ضخمة (SaaS).
    """)
    st.success("✨ مشروع يعكس رؤية تقنية واستثمارية مستقبلية مستدامة.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("النظام التحليلي المتطور — نسخة المعارض العلمية المتقدمة.")
