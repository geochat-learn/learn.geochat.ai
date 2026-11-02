#!/usr/bin/env python3
"""Build the GeoChat AI content site (learn.geochat.ai) as plain static HTML.

Every page is complete HTML on arrival, so crawlers that do not run JavaScript
(GPTBot, OAI-SearchBot, ClaudeBot, Claude-SearchBot, Bingbot) read the full text.

Usage: python3 build.py            -> writes ./dist
       SITE_URL=https://... python3 build.py
"""
import datetime as dt
import html
import json
import os
import re
import shutil
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
SITE_URL = os.environ.get("SITE_URL", "https://learn.geochat.ai").rstrip("/")
APP_URL = "https://atlas.geochat.ai"
HOME_URL = "https://geochat.ai"
CONTACT_URL = "https://geochat.ai/about#contact"
ORG_NAME = "GeoChat AI"
REVIEWER = "GeoChat AI"  # change to "GeoChat AI research team" once a named review step is confirmed

TYPE_LABELS = {
    "guide": "Guide",
    "data": "Data brief",
    "roundup": "Roundup",
    "comparison": "Comparison",
    "glossary": "Glossary",
    "page": "",
}
SECTION_ORDER = [
    ("data", "Data briefs"),
    ("guide", "Guides"),
    ("roundup", "Tool roundups"),
    ("comparison", "Comparisons"),
    ("glossary", "Glossary"),
]

CSS = """
:root{--ink:#14202b;--muted:#4a5a68;--line:#d9e0e6;--bg:#ffffff;--soft:#f4f7f9;--accent:#b8461b;--link:#0b5c8a}
@media (prefers-color-scheme:dark){:root{--ink:#e8eef3;--muted:#a9b6c1;--line:#2c3a46;--bg:#0f171e;--soft:#16222c;--accent:#f08a5d;--link:#7cc4f0}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--link)}a:hover{text-decoration-thickness:2px}
.wrap{max-width:760px;margin:0 auto;padding:0 16px}
header.site{border-bottom:1px solid var(--line);background:var(--soft)}
header.site .wrap{max-width:1040px;display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center;justify-content:space-between;padding-top:12px;padding-bottom:12px}
.brand{font-weight:700;color:var(--ink);text-decoration:none;font-size:18px}
nav.top a{margin-right:14px;font-size:15px;color:var(--ink);text-decoration:none}
nav.top a:hover{text-decoration:underline}
.cta-btn{display:inline-block;background:var(--accent);color:#fff;padding:8px 14px;border-radius:6px;text-decoration:none;font-weight:600;font-size:15px}
main{padding:28px 0 40px}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:6px}.crumbs a{color:var(--muted)}
h1{font-size:34px;line-height:1.2;margin:4px 0 10px}
h2{font-size:24px;line-height:1.3;margin:36px 0 10px}
h3{font-size:19px;margin:24px 0 6px}
.meta{font-size:14px;color:var(--muted);margin-bottom:22px}
.lede{font-size:19px;color:var(--ink)}
table{border-collapse:collapse;width:100%;font-size:15px;margin:16px 0;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--soft)}
code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:15px}
blockquote{margin:16px 0;padding:4px 16px;border-left:4px solid var(--line);color:var(--muted)}
.faq h3{margin-top:18px}
.sources{font-size:15px}.sources li{margin:4px 0;word-break:break-word}
.box{background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:16px 18px;margin:32px 0}
.box p{margin:0 0 10px}
.cards{list-style:none;padding:0;margin:0}
.cards li{border-bottom:1px solid var(--line);padding:12px 0}
.cards a{font-weight:600}.cards p{margin:4px 0 0;color:var(--muted);font-size:15px}
footer.site{border-top:1px solid var(--line);font-size:14px;color:var(--muted);padding:18px 0 40px}
footer.site a{color:var(--muted)}
"""


def load_pages():
    pages = []
    for path in sorted(CONTENT.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
        if not m:
            raise SystemExit(f"Missing front matter: {path}")
        meta = yaml.safe_load(m.group(1)) or {}
        body = m.group(2).strip()
        rel = path.relative_to(CONTENT).with_suffix("")
        slug = str(meta.get("slug") or rel).strip("/")
        meta["slug"] = slug
        meta["type"] = meta.get("type", "page")
        meta["updated"] = str(meta.get("updated", dt.date.today().isoformat()))
        for key in ("title", "description"):
            if not meta.get(key):
                raise SystemExit(f"{path}: missing {key}")
        if len(meta["title"]) > 70:
            print(f"warn: long title ({len(meta['title'])}): {slug}")
        if len(meta["description"]) > 170:
            print(f"warn: long description ({len(meta['description'])}): {slug}")
        meta["body_md"] = body
        pages.append(meta)
    slugs = [p["slug"] for p in pages]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    if dupes:
        raise SystemExit(f"Duplicate slugs: {dupes}")
    return pages


def url_for(slug):
    return f"{SITE_URL}/" if slug in ("", "index") else f"{SITE_URL}/{slug}/"


def md_to_html(text):
    out = markdown.markdown(text, extensions=["tables", "sane_lists", "attr_list"])
    # open external links in same tab but mark them for crawlers as normal links
    return out


def org_ld():
    return {
        "@type": "Organization",
        "@id": f"{HOME_URL}/#organization",
        "name": ORG_NAME,
        "url": HOME_URL,
        "sameAs": ["https://www.youtube.com/@geochatai"],
    }


def app_ld():
    return {
        "@type": "SoftwareApplication",
        "@id": f"{APP_URL}/#app",
        "name": "GeoChat Atlas",
        "alternateName": "GeoChat AI",
        "url": APP_URL,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web browser",
        "softwareVersion": "2",
        "description": "Free AI-powered mapping platform for community health assessments, needs assessments and healthcare supply-demand studies.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@id": f"{HOME_URL}/#organization"},
    }


def plain(text):
    """Markdown -> plain text for structured data (no raw [link](url) syntax)."""
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(text))
    t = re.sub(r"[*_`]{1,2}([^*_`]+)[*_`]{1,2}", r"\1", t)
    return t.strip()


def page_ld(p):
    graph = [org_ld(), app_ld()]
    url = url_for(p["slug"])
    crumbs = [{"@type": "ListItem", "position": 1, "name": "GeoChat AI Learn", "item": url_for("")}]
    if p["type"] == "glossary" and p["slug"] != "glossary":
        crumbs.append({"@type": "ListItem", "position": 2, "name": "Glossary", "item": url_for("glossary")})
    crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": p["title"], "item": url})
    graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if p["type"] == "glossary" and p["slug"] != "glossary":
        graph.append({
            "@type": "DefinedTerm",
            "name": p.get("term", p["title"]),
            "description": p["description"],
            "url": url,
            "inDefinedTermSet": url_for("glossary"),
        })
    if p.get("dataset"):
        d = p["dataset"]
        graph.append({
            "@type": "Dataset",
            "name": d.get("name", p["title"]),
            "description": p["description"],
            "url": url,
            "creator": {"@id": f"{HOME_URL}/#organization"},
            "dateModified": p["updated"],
            "spatialCoverage": d.get("spatial"),
            "temporalCoverage": d.get("temporal"),
            "variableMeasured": d.get("variables", []),
            "isBasedOn": d.get("based_on", []),
            "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv",
                              "contentUrl": f"{SITE_URL}{d['csv']}"}] if d.get("csv") else [],
        })
    if p["type"] in ("guide", "data", "roundup", "comparison", "glossary", "page") and p["slug"] not in ("", "index"):
        graph.append({
            "@type": "Article",
            "headline": p["title"],
            "description": p["description"],
            "url": url,
            "mainEntityOfPage": url,
            "dateModified": p["updated"],
            "datePublished": str(p.get("published", p["updated"])),
            "author": {"@type": "Organization", "name": REVIEWER, "url": HOME_URL},
            "publisher": {"@id": f"{HOME_URL}/#organization"},
            "inLanguage": "en-US",
        })
    if p.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": plain(f["q"]),
                 "acceptedAnswer": {"@type": "Answer", "text": plain(f["a"])}}
                for f in p["faq"]
            ],
        })
    return {"@context": "https://schema.org", "@graph": graph}


def esc(s):
    return html.escape(str(s), quote=True)


def fmt_date(iso):
    try:
        d = dt.date.fromisoformat(iso)
        return d.strftime("%B %-d, %Y")
    except ValueError:
        return iso


def layout(p, inner_html):
    url = url_for(p["slug"])
    ld = json.dumps(page_ld(p), ensure_ascii=False, indent=1)
    crumbs = '<a href="/">Learn</a>'
    if p["type"] == "glossary" and p["slug"] != "glossary":
        crumbs += ' / <a href="/glossary/">Glossary</a>'
    label = TYPE_LABELS.get(p["type"], "")
    meta_line = []
    if label:
        meta_line.append(label)
    meta_line.append(f"Updated {fmt_date(p['updated'])}")
    meta_line.append("Sources listed below")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}{'' if 'GeoChat AI' in p['title'] else ' | GeoChat AI'}</title>
<meta name="description" content="{esc(p['description'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-snippet:-1">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="GeoChat AI">
<meta property="article:modified_time" content="{esc(p['updated'])}">
<script type="application/ld+json">
{ld}
</script>
<style>{CSS}</style>
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="/">GeoChat AI <span style="font-weight:400">Learn</span></a>
<nav class="top" aria-label="Main"><a href="/#data">Data</a><a href="/#guides">Guides</a><a href="/#comparisons">Comparisons</a><a href="/glossary/">Glossary</a><a href="/methods/">Methods</a><a href="/faq/">FAQ</a></nav>
<a class="cta-btn" href="{APP_URL}">Try GeoChat AI free</a>
</div></header>
<main><div class="wrap">
<div class="crumbs">{crumbs}</div>
<h1>{esc(p['title'])}</h1>
<div class="meta">{' · '.join(esc(x) for x in meta_line)}</div>
{inner_html}
</div></main>
<footer class="site"><div class="wrap">
<p>GeoChat AI is a free, AI-powered mapping platform for community health assessments, needs assessments and healthcare supply-demand studies. <a href="{APP_URL}">Start a free analysis</a> · <a href="{CONTACT_URL}">Contact</a> · <a href="{HOME_URL}">geochat.ai</a></p>
<p>Published by {REVIEWER}. Spot an error? <a href="{CONTACT_URL}">Tell us</a> and we will correct it.</p>
</div></footer>
</body>
</html>
"""


def render_page(p):
    body = md_to_html(p["body_md"])
    parts = [body]
    if p.get("faq"):
        faq = ['<section class="faq"><h2>Frequently asked questions</h2>']
        for f in p["faq"]:
            faq.append(f"<h3>{esc(f['q'])}</h3>{md_to_html(str(f['a']))}")
        faq.append("</section>")
        parts.append("".join(faq))
    if p["type"] != "page" or p.get("show_cta"):
        parts.append(
            f'<div class="box"><p><strong>Map access gaps for your community.</strong> '
            f'GeoChat AI is free to use, with no credit card required. Ask questions in plain language, drill into ZIP codes and compare regions.</p>'
            f'<p><a class="cta-btn" href="{APP_URL}">Start a free analysis</a></p></div>'
        )
    if p.get("sources"):
        items = []
        for s in p["sources"]:
            acc = f" (accessed {fmt_date(str(s['accessed']))})" if s.get("accessed") else ""
            items.append(f'<li><a href="{esc(s["url"])}">{esc(s["title"])}</a>{esc(acc)}</li>')
        parts.append(f'<section class="sources"><h2>Sources</h2><ol>{"".join(items)}</ol></section>')
    return layout(p, "\n".join(parts))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def card_list(items):
    return '<ul class="cards">' + "".join(
        f'<li><a href="/{esc(i["slug"])}/">{esc(i["title"])}</a><p>{esc(i["description"])}</p></li>' for i in items
    ) + "</ul>"


def build():
    pages = load_pages()
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    for p in pages:
        if p["slug"] in ("", "index"):
            continue
        write(DIST / p["slug"] / "index.html", render_page(p))

    today = max((p["updated"] for p in pages), default=dt.date.today().isoformat())

    # Glossary hub
    gloss = sorted([p for p in pages if p["type"] == "glossary"], key=lambda x: x["title"].lower())
    hub_g = {"slug": "glossary", "type": "page", "title": "Glossary of Healthcare Access Terms",
             "description": "Plain-language definitions of the shortage designations, data sources and access measures used in needs assessments.",
             "updated": today, "body_md": ""}
    write(DIST / "glossary" / "index.html", layout(hub_g,
          '<p class="lede">Definitions of the terms that come up when you map healthcare access: shortage designations, census geographies, provider data and access measures.</p>'
          + card_list(gloss)))

    # Home hub
    home_parts = ['<p class="lede">Practical guides, tool comparisons and definitions for mapping healthcare access gaps in community health needs assessments, health department assessments and aging-services planning.</p>']
    for t, label in SECTION_ORDER:
        items = [p for p in pages if p["type"] == t]
        if not items:
            continue
        anchor = {"guide": "guides", "comparison": "comparisons", "data": "data"}.get(t, t)
        home_parts.append(f'<h2 id="{anchor}">{label}</h2>' + card_list(items))
    others = [p for p in pages if p["type"] == "page" and p["slug"] not in ("", "index")]
    if others:
        home_parts.append('<h2 id="about">About these pages</h2>' + card_list(others))
    hub_h = {"slug": "", "type": "page", "title": "GeoChat AI Learn: Mapping Healthcare Access",
             "description": "Guides, tool comparisons and definitions for mapping healthcare access gaps in needs assessments.",
             "updated": today, "body_md": ""}
    write(DIST / "index.html", layout(hub_h, "\n".join(home_parts)))

    # sitemap.xml
    urls = [("", today), ("glossary", today)] + [(p["slug"], p["updated"]) for p in pages if p["slug"] not in ("", "index")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, upd in urls:
        sm.append(f"  <url><loc>{url_for(slug)}</loc><lastmod>{upd}</lastmod></url>")
    sm.append("</urlset>")
    write(DIST / "sitemap.xml", "\n".join(sm) + "\n")

    # robots.txt: allow everything, including AI search and training crawlers
    write(DIST / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    # llms.txt: plain-text map for AI assistants
    ll = [f"# GeoChat AI Learn", "",
          "> Guides, tool comparisons and definitions for mapping healthcare access gaps, from GeoChat AI, a free AI-powered mapping platform for community health assessments and needs assessments. Its current version is GeoChat Atlas (https://atlas.geochat.ai), which replaces app.geochat.ai.", ""]
    for t, label in SECTION_ORDER + [("page", "About these pages")]:
        items = [p for p in pages if p["type"] == t and p["slug"] not in ("", "index")]
        if not items:
            continue
        ll.append(f"## {label}")
        ll += [f"- [{p['title']}]({url_for(p['slug'])}): {p['description']}" for p in items]
        ll.append("")
    write(DIST / "llms.txt", "\n".join(ll))

    # IndexNow key file (lets Bing accept instant "this page changed" pings)
    key_file = ROOT / "indexnow.key"
    if key_file.exists():
        key = key_file.read_text().strip()
        write(DIST / f"{key}.txt", key + "\n")
    # Static files (data downloads) served as-is, e.g. static/data/x.csv -> /data/x.csv
    static = ROOT / "static"
    if static.exists():
        shutil.copytree(static, DIST, dirs_exist_ok=True)
    # Custom domain for GitHub Pages
    if (ROOT / "CNAME").exists():
        shutil.copy(ROOT / "CNAME", DIST / "CNAME")
    write(DIST / ".nojekyll", "")

    write(DIST / "404.html", layout({"slug": "404", "type": "page", "title": "Page not found", "description": "This page does not exist.", "updated": today, "body_md": ""},
                                    '<p>That page does not exist. <a href="/">Browse all guides</a>.</p>'))
    print(f"Built {len(pages)} content pages + hubs into {DIST}")


if __name__ == "__main__":
    build()
