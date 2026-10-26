# Landing multilingüe del teclado: una página por idioma con hreflang, datos estructurados
# (app y preguntas frecuentes), Open Graph y sitemap. La llama build.py.
import html
import json
import os

from PIL import Image, ImageDraw, ImageFont

BASE = "https://sherpamiguel.github.io/teclado-traductor"
APP_ID = "6822189721"
# El inglés va en la raíz y es la versión por defecto (x-default).
PATHS = {"en": "", "es": "es/", "fr": "fr/", "de": "de/", "it": "it/", "pt": "pt/",
         "nl": "nl/", "zh": "zh/"}
HREFLANG = {"zh": "zh-Hans"}
SHOTS = ["incoming", "outgoing", "templates", "languages"]
APP_FONTS = os.path.expanduser("~/Documents/GitHub/teclado-traductor-chat-ia/App/Fonts")

CSS = """
/* Paleta de la app (Shared/Palette.swift): laguna, menta, tinta y niebla. */
:root{--bg:#F4F8F7;--card:#ffffff;--ink:#13253A;--soft:#5F6F82;--line:#DDE7E5;
--primary:#0E8F80;--primary-strong:#0B7468;--on-primary:#ffffff;--chip:#DDF4EF}
@media (prefers-color-scheme:dark){:root{--bg:#0C1620;--card:#13212E;--ink:#EAF1F7;
--soft:#9AA9BA;--line:#22323F;--primary:#2BC4AE;--primary-strong:#2BC4AE;
--on-primary:#0C1620;--chip:#133D37}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Manrope,system-ui,sans-serif}
a{color:var(--primary-strong)}img{max-width:100%;height:auto}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}
.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:12px;min-height:60px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;color:var(--ink);
text-decoration:none;margin-right:auto}.brand img{width:36px;height:36px;border-radius:9px}
.links{display:none;gap:18px}.links a{color:var(--ink);text-decoration:none;font-weight:600}
details.lang{position:relative}details.lang summary{list-style:none;cursor:pointer;
padding:6px 12px;border:1px solid var(--line);border-radius:999px;font-weight:600}
details.lang summary::-webkit-details-marker{display:none}
details.lang ul{position:absolute;right:0;top:44px;margin:0;padding:8px;list-style:none;
background:var(--card);border:1px solid var(--line);border-radius:14px;min-width:170px}
details.lang li a{display:block;padding:6px 10px;border-radius:8px;color:var(--ink);
text-decoration:none}details.lang li a[aria-current]{background:var(--chip);font-weight:800}
.hero{display:grid;gap:32px;align-items:center;padding:40px 0 24px}
h1{font-size:clamp(32px,6vw,54px);line-height:1.08;margin:0 0 16px;letter-spacing:-.02em}
h1,h2{text-wrap:balance}
.lead{font-size:clamp(18px,2.4vw,21px);color:var(--soft);margin:0 0 24px}
.badge img{height:56px;width:auto}.trial{margin:12px 0 0;color:var(--soft);font-size:15px}
.phone{justify-self:center;max-width:340px;filter:drop-shadow(0 18px 40px rgba(0,0,0,.18))}
.phone img{border-radius:28px}
section{padding:48px 0}h2{font-size:clamp(26px,4vw,36px);line-height:1.15;margin:0 0 24px}
.gallery{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px}
.gallery figure{margin:0;flex:0 0 220px;scroll-snap-align:start}
.gallery img{border-radius:22px}
.steps,.cards,.plans{display:grid;gap:16px}
.step,.card,.plan{background:var(--card);border:1px solid var(--line);border-radius:20px;
padding:22px}.step b,.card b{display:block;font-size:19px;margin-bottom:6px}
.num{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;
background:var(--primary);color:var(--on-primary);font-weight:800;margin-bottom:12px}
.card p,.step p{margin:0;color:var(--soft)}
.plan{font-size:20px;font-weight:800;text-align:center}
.plan:first-child{background:var(--primary);color:var(--on-primary);border-color:var(--primary)}
.note{color:var(--soft);margin-top:16px}
.langs{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px;
margin:0;color:var(--soft)}
details.q{background:var(--card);border:1px solid var(--line);border-radius:16px;
padding:16px 20px;margin-bottom:10px}details.q summary{cursor:pointer;font-weight:800}
details.q p{margin:10px 0 0;color:var(--soft)}
ol.help{padding-left:22px}ol.help li{margin-bottom:6px}
.cta{text-align:center;background:var(--card);border:1px solid var(--line);border-radius:28px;
padding:40px 16px;margin:24px 0 48px}.cta h2{margin-bottom:20px}
footer{border-top:1px solid var(--line);padding:24px 0 40px;font-size:14px;color:var(--soft)}
footer .wrap{display:flex;flex-wrap:wrap;gap:8px 20px}footer a{color:var(--soft)}
@media (min-width:760px){.hero{grid-template-columns:1.15fr .85fr;padding:64px 0 32px}
.links{display:flex}.steps{grid-template-columns:repeat(3,1fr)}
.cards{grid-template-columns:repeat(3,1fr)}.plans{grid-template-columns:repeat(4,1fr)}
.gallery figure{flex-basis:240px}}
"""


def esc(text):
    return html.escape(text, quote=True)


def url(lang):
    return f"{BASE}/{PATHS[lang]}"


def store_url(c):
    return f"https://apps.apple.com/{c['store']}/app/id{APP_ID}"


def og_image(lang, c):
    """Tarjeta de 1200 × 630 para compartir: titular a la izquierda y captura a la derecha."""
    card = Image.new("RGB", (1200, 630), "#F4F8F7")
    draw = ImageDraw.Draw(card)
    draw.rectangle((0, 600, 1200, 630), fill="#0E8F80")
    shot = Image.open(f"img/{lang}/incoming.webp").convert("RGB")
    shot = shot.resize((int(shot.width * 560 / shot.height), 560), Image.LANCZOS)
    card.paste(shot, (1200 - shot.width - 70, 20))
    icon = Image.open("icon.png").convert("RGBA").resize((96, 96), Image.LANCZOS)
    card.paste(icon, (70, 70), icon)
    if lang == "zh":
        path = next(p for p in __import__("glob").glob(
            "/System/Library/AssetsV2/com_apple_MobileAsset_Font*/*/AssetData/PingFang.ttc"))
        font = ImageFont.truetype(path, 54, index=11)
    else:
        font = ImageFont.truetype(f"{APP_FONTS}/Manrope-Bold.ttf", 54)
    words, lines, line = c["h1"], [], ""
    tokens = list(words) if lang == "zh" else words.split()
    for token in tokens:
        test = line + token if lang == "zh" else (line + " " + token).strip()
        if draw.textlength(test, font=font) > 620 and line:
            lines.append(line)
            line = token
        else:
            line = test
    lines.append(line)
    y = 200
    for text in lines[:5]:
        draw.text((70, y), text, font=font, fill="#13253A")
        y += 68
    card.save(f"img/og-{lang}.jpg", quality=86)


def structured_data(lang, c):
    app = {
        "@context": "https://schema.org", "@type": "MobileApplication",
        "name": c["name"], "operatingSystem": "iOS 26",
        "applicationCategory": "UtilitiesApplication", "inLanguage": HREFLANG.get(lang, lang),
        "description": c["description"], "url": url(lang), "downloadUrl": store_url(c),
        "image": f"{BASE}/icon.png",
        "screenshot": [f"{BASE}/img/{lang}/{name}.webp" for name in SHOTS],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "publisher": {"@type": "Organization", "name": "Sherpas Time Consulting S.L."},
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]
        ],
    }
    return "".join(
        f'<script type="application/ld+json">{json.dumps(item, ensure_ascii=False)}</script>'
        for item in (app, faq)
    )


def page(lang, content, help_steps, email):
    c = content[lang]
    root = "../" if PATHS[lang] else ""
    alternates = "".join(
        f'<link rel="alternate" hreflang="{HREFLANG.get(code, code)}" href="{url(code)}">'
        for code in PATHS
    ) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    og_locales = "".join(
        f'<meta property="og:locale:alternate" content="{content[code]["locale"]}">'
        for code in PATHS if code != lang
    )
    current = ' aria-current="page"'
    menu = "".join(
        f'<li><a href="{root}{PATHS[code]}" hreflang="{HREFLANG.get(code, code)}"'
        f'{current if code == lang else ""}>{esc(content[code]["label"])}</a></li>'
        for code in PATHS
    )
    badge = (f'<a class="badge" href="{store_url(c)}"><img src="{root}img/badge-{lang}.svg" '
             f'alt="{esc(c["badge_alt"])}" width="168" height="56"></a>')
    gallery = "".join(
        f'<figure><img src="{root}img/{lang}/{name}.webp" alt="{esc(caption)}" width="600" '
        f'height="1304" loading="lazy"></figure>'
        for name, caption in zip(SHOTS, c["shots"])
    )
    steps = "".join(
        f'<div class="step"><span class="num">{i}</span><b>{esc(t)}</b><p>{esc(x)}</p></div>'
        for i, (t, x) in enumerate(c["how"], 1)
    )
    cards = "".join(f'<div class="card"><b>{esc(t)}</b><p>{esc(x)}</p></div>'
                    for t, x in c["features"])
    plans = "".join(f'<div class="plan">{esc(p)}</div>' for p in c["pricing"])
    faq = "".join(f'<details class="q"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
                  for q, a in c["faq"])
    help_list = "".join(f"<li>{esc(s)}</li>" for s in help_steps)
    nav = "".join(f'<a href="#{anchor}">{esc(label)}</a>'
                  for anchor, label in zip(["how", "features", "pricing", "faq"], c["nav"]))
    privacy = f'{root}privacy.html#{HREFLANG.get(lang, lang)}'
    return f"""<!doctype html>
<html lang="{HREFLANG.get(lang, lang)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(c["title"])}</title><meta name="description" content="{esc(c["description"])}">
<link rel="canonical" href="{url(lang)}">{alternates}
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta name="theme-color" content="#0E8F80"><link rel="icon" href="{root}icon.png">
<link rel="apple-touch-icon" href="{root}icon.png">
<meta property="og:type" content="website"><meta property="og:url" content="{url(lang)}">
<meta property="og:title" content="{esc(c["title"])}">
<meta property="og:description" content="{esc(c["description"])}">
<meta property="og:image" content="{BASE}/img/og-{lang}.jpg">
<meta property="og:locale" content="{c["locale"]}">{og_locales}
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&display=swap"
rel="stylesheet"><style>{CSS}</style>{structured_data(lang, c)}</head><body>
<header class="top"><div class="wrap"><a class="brand" href="{root}{PATHS[lang]}">
<img src="{root}icon.png" alt="" width="36" height="36">{esc(c["name"])}</a>
<nav class="links">{nav}</nav><details class="lang"><summary>{esc(c["label"])}</summary>
<ul aria-label="{esc(c["lang_label"])}">{menu}</ul></details></div></header>
<main class="wrap">
<div class="hero"><div><h1>{esc(c["h1"])}</h1><p class="lead">{esc(c["lead"])}</p>{badge}
<p class="trial">{esc(c["trial"])}</p></div>
<div class="phone"><img src="{root}img/{lang}/incoming.webp" alt="{esc(c["shots"][0])}"
width="600" height="1304" fetchpriority="high"></div></div>
<section id="how"><h2>{esc(c["how_title"])}</h2><div class="steps">{steps}</div></section>
<section aria-label="{esc(c["name"])}"><div class="gallery">{gallery}</div></section>
<section id="features"><h2>{esc(c["features_title"])}</h2><div class="cards">{cards}</div>
</section>
<section><h2>{esc(c["langs_title"])}</h2><p class="langs">{esc(c["langs"])}</p></section>
<section id="pricing"><h2>{esc(c["pricing_title"])}</h2><div class="plans">{plans}</div>
<p class="note">{esc(c["pricing_note"])}</p></section>
<section id="faq"><h2>{esc(c["faq_title"])}</h2>{faq}</section>
<section id="help"><h2>{esc(c["help_title"])}</h2><ol class="help">{help_list}</ol>
<p>{esc(c["help_contact"])} <a href="mailto:{email}">{email}</a>.</p></section>
<div class="cta"><h2>{esc(c["cta"])}</h2>{badge}</div>
</main>
<footer><div class="wrap"><span>© 2026 Sherpas Time Consulting S.L.</span>
<a href="{privacy}">{esc(c["privacy"])}</a><a href="mailto:{email}">{esc(c["support"])}</a>
</div></footer></body></html>"""


def sitemap():
    links = "".join(
        f'<xhtml:link rel="alternate" hreflang="{HREFLANG.get(code, code)}" href="{url(code)}"/>'
        for code in PATHS
    ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en")}"/>'
    entries = "".join(f"<url><loc>{url(code)}</loc>{links}</url>" for code in PATHS)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            f"{entries}<url><loc>{BASE}/privacy.html</loc></url></urlset>\n")


def build(help_steps, email):
    """help_steps: pasos de puesta en marcha por idioma (los de la página de soporte)."""
    content = json.load(open("content/landing.json"))
    for lang in PATHS:
        os.makedirs(PATHS[lang] or ".", exist_ok=True)
        og_image(lang, content[lang])
        with open(f"{PATHS[lang]}index.html", "w") as out:
            out.write(page(lang, content, help_steps[lang], email))
    with open("sitemap.xml", "w") as out:
        out.write(sitemap())
    with open("robots.txt", "w") as out:
        out.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
