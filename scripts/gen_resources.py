#!/usr/bin/env python3
"""Generate toolkit.html and library.html."""
import os, html
from _common import page_shell

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def shell(title, desc, crumb, h1, sub, body):
    full_body = f'''<div class="lessonhead"><div class="wrap">
  <p class="crumb">{crumb}</p>
  <h1>{html.escape(h1)}</h1>
  <p class="lcode">{html.escape(sub)}</p>
</div></div>
<section><div class="wrap">{body}</div></section>'''
    return page_shell("", title, desc, full_body)

def deflist(rows):
    r = "".join(
        f'<div class="row"><b>{html.escape(n)}</b><span>{html.escape(d)}</span><span><a href="{html.escape(u)}">{html.escape(u.replace("https://","").replace("http://","").rstrip("/"))}</a></span></div>'
        for n, d, u in rows)
    return f'<div class="deflist">{r}</div>'

# ===== TOOLKIT =====
nocode = [
 ("ChatGPT", "General assistant, analysis, drafting; free tier", "https://chatgpt.com"),
 ("Claude", "Reasoning, long documents, careful writing", "https://claude.ai"),
 ("Gemini", "Google-integrated assistant, multimodal", "https://gemini.google.com"),
 ("Microsoft Copilot", "Assistant integrated with Microsoft 365", "https://copilot.microsoft.com"),
 ("Perplexity", "Search with citations; good for sourcing", "https://perplexity.ai"),
 ("NotebookLM", "Source-grounded notebook over your own files", "https://notebooklm.google.com"),
 ("Poe", "Many models in one interface", "https://poe.com"),
 ("Google AI Studio", "Free playground + API key + function calling", "https://aistudio.google.com"),
]
research = [
 ("Elicit", "AI literature review, screening, extraction", "https://elicit.com"),
 ("Consensus", "Evidence answers from papers", "https://consensus.app"),
 ("Connected Papers", "Citation-graph discovery", "https://www.connectedpapers.com"),
 ("Research Rabbit", "Citation explorer & alerts", "https://www.researchrabbit.ai"),
 ("Semantic Scholar", "Free scholarly search & API", "https://www.semanticscholar.org"),
 ("OpenAlex", "Open scholarly metadata", "https://openalex.org"),
 ("Scite", "Citation context (supporting/contrasting)", "https://scite.ai"),
 ("SciSpace", "Read & explain papers", "https://scispace.com"),
 ("Taguette", "Free, open-source qualitative coding", "https://www.taguette.org"),
 ("QualCoder", "Open-source CAQDAS for qualitative data", "https://github.com/ccbogel/QualCoder"),
]
build = [
 ("Google Colab", "Free notebooks in the browser (Python)", "https://colab.research.google.com"),
 ("Hugging Face", "Models, datasets, and free Spaces hosting", "https://huggingface.co"),
 ("Gradio", "Build simple AI web demos in Python", "https://gradio.app"),
 ("Ollama", "Run open models locally, free", "https://ollama.com"),
 ("LM Studio", "Desktop app to run local models", "https://lmstudio.ai"),
 ("LangGraph", "Open framework for agent workflows", "https://github.com/langchain-ai/langgraph"),
 ("GitHub Pages", "Free static website hosting", "https://pages.github.com"),
]
tk_body = f'''<div class="section-head" style="margin-bottom:26px">
  <span class="tag">Hands-on toolkit</span>
  <h2>Every tool here has a free tier.</h2>
  <p>Use these in the Hands-on box of each lesson. Verify the free tier before relying on it — terms change. Links open the official site.</p>
</div>
<p class="subh">No-code · chat &amp; general AI</p>{deflist(nocode)}
<p class="subh">Research-specific tools</p>{deflist(research)}
<p class="subh">Light coding · build &amp; deploy (free)</p>{deflist(build)}'''
with open(os.path.join(ROOT, "toolkit.html"), "w", encoding="utf-8") as f:
    f.write(shell("Free Tools Directory — Toolkit",
                  "Every tool with a usable free tier, for the hands-on activities.",
                  "Resources", "Free Tools Directory",
                  "Curated free tools for every hands-on activity", tk_body))

# ===== LIBRARY =====
def reflist(items):
    r = "".join(
        f'<div class="pub">{html.escape(n)}{(" · <a href=\""+u+"\">link ↗</a>") if u else ""}</div>'
        for n, u in items)
    return r

method = [
 ("Vaswani et al. (2017) — Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
 ("Wei et al. (2022) — Chain-of-Thought Prompting", "https://arxiv.org/abs/2201.11903"),
 ("Lewis et al. (2020) — Retrieval-Augmented Generation", "https://arxiv.org/abs/2005.11401"),
 ("Argyle et al. (2023) — Out of One, Many (silicon sampling)", "https://www.cambridge.org/core/journals/political-analysis/article/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49"),
 ("Ziems et al. (2024) — Can LLMs Transform Computational Social Science?", "https://arxiv.org/abs/2305.03514"),
 ("Horton (2023) — LLMs as Simulated Economic Agents", "https://arxiv.org/abs/2301.07543"),
 ("Grossmann et al. (2023) — AI & the transformation of social science (Science)", "https://www.science.org/doi/10.1126/science.adi1778"),
 ("Bail (2024) — Can Generative AI improve social science? (PNAS)", "https://www.pnas.org/doi/10.1073/pnas.2314021121"),
 ("Navigating the Risks of LLM Text Annotation (2025)", "https://arxiv.org/abs/2306.00176"),
 ("Evaluation Guidelines for Empirical Studies with LLMs", "https://arxiv.org/abs/2411.10915"),
]
mgmt = [
 ("Brynjolfsson, Li & Raymond (2023) — Generative AI at Work", "https://www.nber.org/papers/w31161"),
 ("Eloundou et al. (2023) — GPTs are GPTs", "https://arxiv.org/abs/2303.10130"),
 ("Dell'Acqua et al. (2023) — Navigating the Jagged Technological Frontier", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321"),
 ("McKinsey — The State of AI", "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai"),
 ("Mollick — Co-Intelligence", "https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/"),
 ("Ethan Mollick — One Useful Thing (blog)", "https://www.oneusefulthing.org/"),
]
repos = [
 ("LLM-for-Social-Science-Research (provided)", ""),
 ("UCLA Anderson SSAI — App Development Kit", "https://ucla-anderson-ssai.github.io/SSAI/"),
 ("howtousellms — LLMs for text analysis", "https://github.com/howtousellms"),
 ("Awesome-LLM-for-Social-Science", "https://github.com/Sherryyy96/Awesome-LLM-for-Social-Science"),
 ("mlabonne/llm-course (technical)", "https://github.com/mlabonne/llm-course"),
 ("Anthropic — Prompt engineering interactive tutorial", "https://github.com/anthropics/prompt-eng-interactive-tutorial"),
 ("Google Prompting Essentials", "https://grow.google/prompting-essentials/"),
 ("DeepLearning.AI — ChatGPT Prompt Engineering", "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"),
 ("Elements of AI (free intro)", "https://www.elementsofai.com/"),
]
lib_body = f'''<div class="section-head" style="margin-bottom:26px">
  <span class="tag">Reading &amp; resources</span>
  <h2>The papers and resources behind the lessons.</h2>
  <p>A working bibliography spanning the research-methods literature, management readings, and the open courses, repos, and toolkits referenced throughout the curriculum.</p>
</div>
<p class="subh">Foundational papers (research method)</p>{reflist(method)}
<p class="subh">Foundational reading (management)</p>{reflist(mgmt)}
<p class="subh">Courses, repos &amp; toolkits</p>{reflist(repos)}'''
with open(os.path.join(ROOT, "library.html"), "w", encoding="utf-8") as f:
    f.write(shell("Reading & Resource Library",
                  "The papers, books, repos, and courses behind the curriculum.",
                  "Resources", "Reading &amp; Resource Library",
                  "Papers, books, repos &amp; courses behind the curriculum", lib_body))

print("toolkit + library done")
