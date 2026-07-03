#!/usr/bin/env python3
"""Generate research and management track index pages."""
import os, html
from _common import slug, masthead, footer, page_shell

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def track_index(rel, kicker, h1, lede, start_code, modules, next_blurb, next_links):
    mod_html = ""
    for mi, (mcode, mtitle, msub, lessons) in enumerate(modules):
        op = " open" if mi == 0 else ""
        lh = "".join(
            f'<div class="lesson"><span class="lc">{c}</span><span class="lt"><a href="{slug(c)}.html">{html.escape(t)}</a></span></div>'
            for c, t in lessons)
        mod_html += f'''
      <details class="module"{op}>
        <summary>
          <span class="mcode">{mcode}</span>
          <span class="mttl"><b>{html.escape(mtitle)}</b><span>{html.escape(msub)}</span></span>
          <span class="chev">›</span>
        </summary>
        <div class="lessons">{lh}</div>
      </details>'''
    nl = "".join(f'<a class="btn btn-dark" href="{u}">{t} →</a>' for t, u in next_links)
    body = f'''<section class="hero">
  <div class="wrap" style="padding:64px 28px 56px">
    <p class="eyebrow">{kicker}</p>
    <h1>{html.escape(h1)}</h1>
    <p class="lede">{html.escape(lede)}</p>
    <div class="actions">
      <a class="btn btn-primary" href="{slug(start_code)}.html">Start with {start_code}</a>
      <a class="btn btn-ghost" href="#modules">Browse all mini-courses</a>
    </div>
  </div>
</section>
<section id="modules">
  <div class="wrap">
    <div class="section-head">
      <span class="tag">Curriculum map</span>
      <h2>Mini-courses you can stack.</h2>
      <p>Each mini-course is a set of self-contained lessons. Every lesson is one page with Objective, Key concepts, a Hands-on activity, free Tools, and Read / explore links.</p>
    </div>
    <div class="modgrid">{mod_html}
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="tag">Where to next</span>
      <h2>{html.escape(next_blurb)}</h2>
    </div>
    <div class="actions">{nl}</div>
  </div>
</section>'''
    return page_shell(rel, f"{h1} — Open Learning", lede, body)

# ===== RESEARCH INDEX =====
research_modules = [
 ("R1", "Opening to AI for Researchers", "Connecting the foundation to research realities",
  [("R1.1", "Why AI matters for research now"), ("R1.2", "The AI-augmented research workflow")]),
 ("R2", "Using GenAI in Practice", "The everyday work of research, with validation",
  [("R2.1", "Literature discovery and synthesis"), ("R2.2", "Reading & note-making at scale"), ("R2.3", "Writing, editing & communication")]),
 ("R3", "Connecting GenAI to Theory & Design", "From tasks to thinking — with scepticism",
  [("R3.1", "Theory development & hypothesis generation"), ("R3.2", "Research design & methods planning"), ("R3.3", "AI strategy for a research programme")]),
 ("R4", "Using GenAI as a Research Method", "GenAI as an instrument of measurement",
  [("R4.1", "Text annotation & classification"), ("R4.2", "Silicon samples & synthetic respondents"), ("R4.3", "Agent-based & simulation studies"), ("R4.4", "Building & sharing a research app"), ("R4.5", "Validity, reliability & reporting")]),
]
with open(os.path.join(ROOT, "research", "index.html"), "w", encoding="utf-8") as f:
    f.write(track_index("../", "Research Track · R1 – R4 + Capstone", "AI for Research",
        "Use AI across the whole research lifecycle and, ultimately, as a method in its own right — literature synthesis, qualitative coding, silicon sampling, and synthetic data. Throughout, the emphasis is on validity, transparency, and reproducibility.",
        "R1.1", research_modules,
        "Take the Foundation first, or branch to Management.",
        [("AI Foundation", "../foundation/index.html"), ("AI for Managers", "../management/index.html")]))

# ===== MANAGEMENT INDEX =====
mgmt_modules = [
 ("M1", "The AI-Literate Manager", "An accurate, hype-free model of AI",
  [("M1.1", "Intelligent systems: what AI is for business"), ("M1.2", "The AI revolution so far"), ("M1.3", "What comes next: models, workflows, agents")]),
 ("M2", "GenAI in Practice for Business", "Prompting, use cases, and prototyping",
  [("M2.1", "Prompting & productivity for managers"), ("M2.2", "GenAI across business functions"), ("M2.3", "Low-code prototyping for managers")]),
 ("M3", "Data, Decisions & Analytics", "Why data — not models — decides outcomes",
  [("M3.1", "Data before models"), ("M3.2", "Decision systems & managing risk"), ("M3.3", "From text & behaviour to intelligence")]),
 ("M4", "Agentic AI for Enterprise Workflows", "Agents that act, with oversight",
  [("M4.1", "Reasoning, memory & agents in the enterprise"), ("M4.2", "Multi-agent systems & orchestration")]),
 ("M5", "Strategy, Innovation & Advantage", "Where AI creates durable advantage",
  [("M5.1", "AI strategy & business models"), ("M5.2", "Innovation, disruption & the future of work")]),
 ("M6", "Governance, Ethics & Leading Change", "Govern AI and drive adoption",
  [("M6.1", "Governance, fairness & liability"), ("M6.2", "Implementing AI & leading change")]),
]
with open(os.path.join(ROOT, "management", "index.html"), "w", encoding="utf-8") as f:
    f.write(track_index("../", "Management Track · M1 – M6 + Capstone", "AI for Managers",
        "The strategic and applied literacy a leader, consultant, or transformation manager needs: to diagnose AI opportunities, evaluate vendor claims, manage implementation risk, and drive adoption. Case-led and decision-focused, grounded in Indian and global business contexts.",
        "M1.1", mgmt_modules,
        "Take the Foundation first, or branch to Research.",
        [("AI Foundation", "../foundation/index.html"), ("AI for Research", "../research/index.html")]))

print("track indexes done")
