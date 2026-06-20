#!/usr/bin/env python3
"""Monta uma homepage única a partir das seções, escopando o CSS de cada uma
e embutindo as imagens em base64. Saída: index.html (portátil, 1 arquivo)."""
import re, base64, pathlib

SITE = pathlib.Path(__file__).resolve().parent

# (scope-name, arquivo, id-âncora, rótulo-nav)
SECTIONS = [
    ("hero",    "hero-section.html",          "top",         None),
    ("hiw",     "how-it-works-section.html",  "how-it-works","How it works"),
    ("ing",     "ingredients-section.html",   "ingredients", "Ingredients"),
    ("story",   "our-story-section.html",     "story",       "Our Story"),
    ("reviews", "reviews-section.html",        "reviews",     "Reviews"),
    ("footer",  "footer-section.html",        "footer",      None),
]

GLOBAL_SELECTORS = {":root", "*", "body", "html", "a", "body::before"}


def read(p):
    return (SITE / p).read_text()


def extract(html):
    style = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.S).group(1)
    return style, body


def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def parse_blocks(css):
    """Divide CSS em [(prelude, inner)] respeitando chaves aninhadas."""
    blocks, i, n, prelude = [], 0, len(css), ""
    while i < n:
        c = css[i]
        if c == "{":
            depth, j = 1, i + 1
            while j < n and depth > 0:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                j += 1
            blocks.append((prelude.strip(), css[i + 1:j - 1]))
            prelude, i = "", j
        else:
            prelude += c
            i += 1
    return blocks


def is_global(pre):
    parts = [p.strip() for p in pre.split(",")]
    return all(p in GLOBAL_SELECTORS for p in parts)


def prefix(pre, scope):
    parts = [p.strip() for p in pre.split(",") if p.strip()]
    return ", ".join(f"{scope} {p}" for p in parts)


def scope_css(css, scope, store):
    css = strip_comments(css)
    out = []
    for pre, inner in parse_blocks(css):
        if not pre:
            continue
        if pre.startswith("@keyframes") or pre.startswith("@font-face"):
            store.setdefault("at", {})[pre] = f"{pre}{{{inner}}}"
        elif pre.startswith("@media") or pre.startswith("@supports"):
            inner_out = []
            for p2, i2 in parse_blocks(inner):
                if not p2:
                    continue
                if p2.startswith("@"):
                    inner_out.append(f"{p2}{{{i2}}}")
                else:
                    inner_out.append(f"{prefix(p2, scope)}{{{i2}}}")
            out.append(f"{pre}{{{''.join(inner_out)}}}")
        elif is_global(pre):
            store.setdefault("base", {}).setdefault(pre, inner)  # mantém o 1º
        else:
            out.append(f"{prefix(pre, scope)}{{{inner}}}")
    return "\n".join(out)


def inline_images(body):
    def repl(m):
        f = SITE / m.group(1)
        if f.exists():
            data = base64.b64encode(f.read_bytes()).decode()
            ext = f.suffix.lstrip(".").lower().replace("jpg", "jpeg")
            return f'src="data:image/{ext};base64,{data}"'
        return m.group(0)
    return re.sub(r'src="(assets/[^"]+)"', repl, body)


def strip_hero_chrome(body):
    body = re.sub(r'<div class="announce">.*?</div>', "", body, count=1, flags=re.S)
    body = re.sub(r"<header>.*?</header>", "", body, count=1, flags=re.S)
    return body


store = {}
sec_css, sec_html, nav_links = [], [], []
for name, fn, anchor, label in SECTIONS:
    style, body = extract(read(fn))
    if name == "hero":
        body = strip_hero_chrome(body)
    # remove o <script> interno de cada seção (evita redeclaração de const no escopo
    # global); um único JS global no fim cuida de reveal + parallax de toda a página
    body = re.sub(r"<script[^>]*>.*?</script>", "", body, flags=re.S)
    body = inline_images(body)
    sec_css.append(f"/* ===== {name} ===== */\n" + scope_css(style, f".scope-{name}", store))
    sec_html.append(f'<section id="{anchor}" class="liv-sec scope-{name}">{body}</section>')
    if label:
        nav_links.append(f'<a href="#{anchor}">{label}</a>')

# CSS global (dedup de :root, *, body, html, a, body::before + keyframes)
base = "\n".join(f"{pre}{{{inner}}}" for pre, inner in store.get("base", {}).items())
at = "\n".join(store.get("at", {}).values())

GLOBAL_CHROME = """
html{scroll-behavior:smooth;scroll-padding-top:84px;}
.liv-sec{position:relative;}
.site-announce{background:var(--green-800);color:var(--cream);text-align:center;font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:10px 16px;font-weight:500;}
.site-announce b{color:var(--gold-soft);font-weight:600;}
.site-announce .dot{color:var(--gold);margin:0 12px;}
.site-header{position:sticky;top:0;z-index:200;background:rgba(244,238,224,.86);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);}
.site-nav{max-width:1280px;margin:0 auto;padding:0 clamp(20px,4vw,48px);height:72px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;}
.site-links{display:flex;gap:28px;font-size:13.5px;font-weight:500;color:var(--green-700);}
.site-links a{position:relative;padding:4px 0;transition:color .3s var(--ease);}
.site-links a::after{content:"";position:absolute;left:0;right:100%;bottom:-2px;height:1.5px;background:var(--gold);transition:right .35s var(--ease);}
.site-links a:hover{color:var(--green-900);}
.site-links a:hover::after{right:0;}
.site-brand{text-align:center;line-height:1;}
.site-brand .w{display:block;color:var(--gold);font-size:11px;margin-bottom:3px;}
.site-brand .m{font-family:var(--serif);font-weight:500;font-size:24px;letter-spacing:.34em;color:var(--green-700);padding-left:.34em;}
.site-brand .s{display:block;font-size:8.5px;letter-spacing:.46em;color:var(--gold);margin-top:5px;padding-left:.46em;}
.site-actions{display:flex;gap:20px;justify-content:flex-end;align-items:center;color:var(--green-700);}
.site-actions svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:1.6;}
.site-cart{position:relative;}
.site-cart .count{position:absolute;top:-7px;right:-9px;background:var(--green-600);color:var(--cream);font-size:10px;font-weight:600;width:16px;height:16px;border-radius:50%;display:grid;place-items:center;}
.site-menu{display:none;background:none;border:none;cursor:pointer;color:var(--green-700);}
@media (max-width:880px){
  .site-nav{grid-template-columns:auto 1fr auto;}
  .site-links{display:none;}
  .site-brand{text-align:left;}
  .site-menu{display:flex;}
  .site-menu svg{width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.7;}
}
"""

HEADER_HTML = f"""
<div class="site-announce">Free shipping over $59 <span class="dot">·</span> <b>Naturally gluten-free</b>, made with real ingredients</div>
<header class="site-header">
  <div class="site-nav">
    <div class="site-links">{''.join(nav_links)}</div>
    <a href="#top" class="site-brand"><span class="w">✦</span><span class="m">LIVV BITES</span><span class="s">GOURMET</span></a>
    <div class="site-actions">
      <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
      <svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>
      <span class="site-cart"><svg viewBox="0 0 24 24"><path d="M6 7h12l-1 13H7L6 7Z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg><span class="count">0</span></span>
      <button class="site-menu" aria-label="Menu"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </div>
</header>
"""

JS = """
const els=[...document.querySelectorAll(".reveal:not(.in)")];
const show=el=>{el.classList.add("in");io.unobserve(el);};
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting)show(e.target);});},{threshold:.12,rootMargin:"0px 0px -8% 0px"});
els.forEach(el=>io.observe(el));
// robustez: revela o que já está na viewport no load, e um fallback final para nada ficar invisível
const revealInView=()=>{const vh=innerHeight||document.documentElement.clientHeight;els.forEach(el=>{if(el.classList.contains("in"))return;const r=el.getBoundingClientRect();if(r.top<vh&&r.bottom>0)show(el);});};
revealInView();  // síncrono: revela já o que está na viewport, sem esperar evento
addEventListener("load",revealInView);document.addEventListener("DOMContentLoaded",revealInView);
addEventListener("scroll",revealInView,{passive:true});
setTimeout(()=>els.forEach(el=>{if(!el.classList.contains("in"))show(el);}),4000);
if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
  const layers=[...document.querySelectorAll(".plate img, .closing img, .story-media img")];
  let t=false;
  const f=()=>{if(t)return;t=true;requestAnimationFrame(()=>{const vh=innerHeight;layers.forEach(img=>{const r=img.getBoundingClientRect();if(r.bottom>0&&r.top<vh){const p=(r.top+r.height/2-vh/2)/vh;img.style.transform=`translateY(${p*-24}px)`;}});t=false;});};
  addEventListener("scroll",f,{passive:true});addEventListener("resize",f);f();
}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>LIVV BITES — Comfort food, thoughtfully made.</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
<style>
/* ============ GLOBAL ============ */
{base}
{at}
{GLOBAL_CHROME}
/* ============ SECTIONS (scoped) ============ */
{chr(10).join(sec_css)}
</style>
</head>
<body>
<span id="top"></span>
{HEADER_HTML}
{chr(10).join(sec_html)}
<script>{JS}</script>
</body>
</html>
"""

out = SITE / "index.html"
out.write_text(html)
# também na raiz do projeto, que é o que o GitHub Pages serve
root_out = SITE.parent / "index.html"
root_out.write_text(html)
kb = len(html.encode()) / 1024
print(f"OK -> {out}  e  {root_out}  ({kb:.0f} KB)")
