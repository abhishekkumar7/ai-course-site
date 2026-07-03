#!/usr/bin/env python3
"""Shared chrome for all page generators: slug, masthead, footer, page_shell."""
import html as _html

def slug(code):
    return code.lower().replace(".", "-")

def masthead(rel):
    items = [
        ("Foundation", rel + "foundation/index.html"),
        ("Research",   rel + "research/index.html"),
        ("Management", rel + "management/index.html"),
        ("All courses",rel + "courses/index.html"),
        ("Toolkit",    rel + "toolkit.html"),
        ("Library",    rel + "library.html"),
        ("About",      rel + "about.html"),
    ]
    links = "\n      ".join(f'<a href="{u}">{t}</a>' for t, u in items)
    return f'''<header class="masthead">
  <div class="wrap">
    <a class="brand" href="{rel}index.html">
      <span class="glyph">AI</span>
      <span class="bt"><b>AI for Management &amp; Research</b><span>Open Learning · SPJIMR</span></span>
    </a>
    <button class="menubtn" aria-label="Menu">☰</button>
    <nav class="nav" aria-label="Primary">
      {links}
      <a class="cta" href="{rel}foundation/index.html">Start free →</a>
    </nav>
  </div>
</header>'''

def footer(rel):
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div><h5>AI for Management &amp; Research</h5><p class="blurb">A free, public, hands-on curriculum teaching AI from a management and research perspective.</p></div>
      <div><h5>Tracks</h5><a href="{rel}foundation/index.html">AI Foundation</a><a href="{rel}research/index.html">AI for Research</a><a href="{rel}management/index.html">AI for Managers</a></div>
      <div><h5>Resources</h5><a href="{rel}toolkit.html">Free Tools Directory</a><a href="{rel}library.html">Reading Library</a><a href="{rel}courses/index.html">All courses</a></div>
      <div><h5>About</h5><a href="{rel}about.html">The instructor</a><a href="https://www.spjimr.org/faculty/abhishek-kumar-jha/">SPJIMR profile ↗</a></div>
    </div>
    <div class="base"><span>© 2026 · Prof. Abhishek Kumar Jha · SPJIMR Information Management</span><span>Open learning · Free to use</span></div>
  </div>
</footer>'''

def page_shell(rel, title, desc, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)}</title>
<meta name="description" content="{_html.escape(desc)}">
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{masthead(rel)}
<main id="main">
{body}
</main>
{footer(rel)}
<script src="{rel}assets/main.js"></script>
</body>
</html>'''
