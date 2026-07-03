#!/usr/bin/env python3
"""Generate all lesson pages for the AI course site from structured curriculum data.
Each lesson renders the six fixed blocks: Objective, Key concepts, Hands-on, Tools, Read/explore.
File citations are rendered as `ref:` chips the professor can later wire to slides/videos/papers.
"""
import os, html
from _common import slug, masthead, footer

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def tool_chip(t):
    name, url = t
    if url:
        return f'<li><a href="{html.escape(url)}">{html.escape(name)}</a></li>'
    return f'<li><a href="#" onclick="return false">{html.escape(name)}</a></li>'

def lesson_page(rel, track_url, track_name, code, title, objective, concepts,
                handson, tools, reads, refs, prev_l, next_l, siblings):
    sib = "\n      ".join(
        f'<a href="{u}"{" style=\"color:var(--brick);font-weight:600\"" if c==code else ""}>{c} · {t}</a>'
        for c, t, u in siblings)
    concept_li = "\n        ".join(f"<li>{html.escape(c)}</li>" for c in concepts)
    tool_li = "\n        ".join(tool_chip(t) for t in tools)
    read_li = "\n        ".join(
        (f'<li><a href="{html.escape(u)}">{html.escape(n)}</a></li>' if u
         else f'<li>{html.escape(n)}</li>') for n, u in reads)
    ref_html = ""
    if refs:
        chips = " ".join(f'<a class="ref" href="#" onclick="return false" title="To be linked: slides, video, or paper">ref: {html.escape(r)}</a>' for r in refs)
        ref_html = f'''<div class="block">
        <p class="blabel">Materials</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{chips}</div>
      </div>'''
    pager = ""
    if prev_l: pager += f'<a href="{prev_l[1]}">← {prev_l[0]}</a>'
    if next_l: pager += f'<a href="{next_l[1]}">{next_l[0]} →</a>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{code} — {html.escape(title)}</title>
<meta name="description" content="{html.escape(objective[:155])}">
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{masthead(rel)}
<main id="main">
<div class="lessonhead">
  <div class="wrap">
    <p class="crumb"><a href="{track_url}">{track_name}</a> · {code}</p>
    <h1>{html.escape(title)}</h1>
    <p class="lcode">{code} &nbsp;·&nbsp; part of the {track_name} track</p>
  </div>
</div>

<div class="wrap">
  <div class="lessonbody">
    <article>
      <div class="block">
        <p class="blabel">Objective</p>
        <p>{html.escape(objective)}</p>
      </div>

      <div class="block">
        <p class="blabel">Key concepts</p>
        <ul>
        {concept_li}
        </ul>
      </div>

      <div class="block handson">
        <p class="blabel">Hands-on</p>
        <p>{html.escape(handson)}</p>
      </div>

      <div class="block">
        <p class="blabel">Free tools</p>
        <ul class="toollist">
        {tool_li}
        </ul>
      </div>

      <div class="block">
        <p class="blabel">Read / explore</p>
        <ul>
        {read_li}
        </ul>
      </div>

      {ref_html}
    </article>

    <aside class="sidebar">
      <h4>In this module</h4>
      <nav>
      {sib}
      </nav>
      <div class="pager">
        {pager}
      </div>
    </aside>
  </div>
</div>
</main>
{footer(rel)}
<script src="{rel}assets/main.js"></script>
</body>
</html>'''

# ============================================================================
# CURRICULUM DATA  (source: AI_Curriculum_Outline.docx)
# lesson = (code, title, objective, [concepts], handson, [tools], [reads], [refs])
# ============================================================================

T = {"chatgpt":("ChatGPT","https://chatgpt.com"),"claude":("Claude","https://claude.ai"),
     "gemini":("Gemini","https://gemini.google.com"),"perplexity":("Perplexity","https://perplexity.ai"),
     "notebooklm":("NotebookLM","https://notebooklm.google.com"),"poe":("Poe","https://poe.com"),
     "aistudio":("Google AI Studio","https://aistudio.google.com"),"copilot":("Microsoft Copilot","https://copilot.microsoft.com"),
     "hf":("Hugging Face","https://huggingface.co"),"hfspaces":("Hugging Face Spaces","https://huggingface.co/spaces"),
     "tokenizer":("OpenAI Tokenizer","https://platform.openai.com/tokenizer"),"colab":("Google Colab","https://colab.research.google.com"),
     "gradio":("Gradio","https://gradio.app"),"langgraph":("LangGraph","https://github.com/langchain-ai/langgraph"),
     "crewai":("CrewAI","https://www.crewai.com"),"elicit":("Elicit","https://elicit.com"),
     "consensus":("Consensus","https://consensus.app"),"connpapers":("Connected Papers","https://www.connectedpapers.com"),
     "rabbit":("Research Rabbit","https://www.researchrabbit.ai"),"semantic":("Semantic Scholar","https://www.semanticscholar.org"),
     "openalex":("OpenAlex","https://openalex.org"),"scite":("Scite","https://scite.ai"),"scispace":("SciSpace","https://scispace.com"),
     "scholarcy":("Scholarcy","https://www.scholarcy.com"),"euact":("EU AI Act explorer","https://artificialintelligenceact.eu/the-act/"),
     "gamma":("Gamma","https://gamma.app"),"howto":("howtousellms notebook","https://github.com/howtousellms"),
     "ucla":("UCLA Anderson App Kit","https://ucla-anderson-ssai.github.io/SSAI/"),
     "llmsocsci":("LLM-for-Social-Science repo",""),"osf":("OSF pre-registration","https://osf.io/prereg/")}

FOUNDATION = [
 ("F1.1","From rules to learning to generation",
  "Build an accurate mental model of AI by tracing the path from rule-based systems to machine learning, deep learning, and generative AI.",
  ["AI vs. ML vs. deep learning vs. generative AI — the nested relationship",
   "Supervised, unsupervised, and reinforcement learning in plain language",
   "Discriminative vs. generative models: predicting a label vs. producing content",
   "Why “AI” today usually means large neural networks trained on huge data"],
  "Ask ChatGPT, Claude, and Gemini the same question and compare answers; note where they agree, differ, and hedge. This is your first model comparison.",
  [T["chatgpt"],T["claude"],T["gemini"]],
  [("Elements of AI (free course)","https://www.elementsofai.com/"),("Google ML Crash Course","https://developers.google.com/machine-learning/crash-course")],
  ["F1.1 slides","F1.1 video"]),
 ("F1.2","Live AI vs. marketing hype",
  "Separate what AI can reliably do today from vendor claims, using the Gartner Hype Cycle and the idea of a “jagged frontier” of capability.",
  ["The Gartner Hype Cycle applied to GenAI","Capability vs. reliability: where models are superhuman and where they fail",
   "The “jagged frontier” — tasks of similar difficulty, very different success","How to read a benchmark and a demo critically"],
  "Pick three AI claims from recent ads or LinkedIn posts and test each one directly in a chatbot; classify them as real, exaggerated, or false.",
  [T["perplexity"]],
  [("Dell'Acqua et al. — Navigating the Jagged Technological Frontier","https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321"),("Ethan Mollick — One Useful Thing","https://www.oneusefulthing.org/")],
  ["F1.2 slides"]),
 ("F1.3","Mapping the AI landscape",
  "Give yourself a map of the field: model families, providers, modalities (text, image, audio, video, code), and open vs. closed models.",
  ["Major model families and providers (OpenAI, Anthropic, Google, Meta, Mistral, open-source)","Modalities and multimodality",
   "Open-weight vs. proprietary models — trade-offs","Where Indian and global models fit"],
  "Build a one-page personal “AI stack”: list one free tool you would use for writing, search, images, and data.",
  [T["hf"],T["poe"]],
  [("Stanford AI Index Report","https://aiindex.stanford.edu/report/")],
  ["F1.3 slides"]),
 ("F2.1","Tokens, embeddings, and prediction",
  "Explain what a large language model actually does — predict the next token — and why that simple idea produces such capable behaviour.",
  ["Tokens and tokenisation","Embeddings: turning words into vectors of meaning","Next-token prediction and probability",
   "Why the same prompt can give different answers (temperature, sampling)"],
  "Use the OpenAI tokenizer to see how your own sentence is split into tokens; then lower/raise “creativity” in a playground and observe the change.",
  [T["tokenizer"],T["aistudio"]],
  [("Vaswani et al. — Attention Is All You Need","https://arxiv.org/abs/1706.03762")],
  ["F2.1 slides","F2.1 video"]),
 ("F2.2","Context windows, hallucination, and limits",
  "Understand the practical limits that shape every AI workflow: context length, hallucination, knowledge cut-offs, and bias.",
  ["Context window: the model's short-term memory","Hallucination — why models invent confident, wrong answers",
   "Training cut-offs and why models need search or documents","Bias and representativeness of training data"],
  "Deliberately trigger a hallucination (ask for citations on a niche topic), then verify each one — a memorable lesson in always checking.",
  [T["notebooklm"]],
  [("Anthropic — Prompt engineering overview","https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview")],
  ["F2.2 slides"]),
 ("F2.3","The frontier: reasoning and test-time compute",
  "Introduce reasoning models and the shift from training-time to test-time (inference-time) compute — the current frontier.",
  ["System 1 vs. System 2 thinking applied to models (Kahneman)","Chain-of-thought and why “thinking longer” helps",
   "Train-time scaling laws vs. test-time compute","Latency and cost vs. reasoning depth — a manager's trade-off"],
  "Run a multi-step logic puzzle on a standard model and a reasoning model; compare quality, time, and cost.",
  [T["chatgpt"],T["claude"]],
  [("Wei et al. — Chain-of-Thought Prompting","https://arxiv.org/abs/2201.11903")],
  ["F2.3 slides"]),
 ("F3.1","Prompting fundamentals",
  "Learn a repeatable prompting method so you get reliable results instead of lucky ones.",
  ["A simple framework: Task, Context, References, Evaluate, Iterate","Role, format, and constraints in a prompt",
   "Few-shot prompting: showing examples","Giving the model a way to say “I don't know”"],
  "Take a weak one-line prompt and improve it through five iterations, saving each version to start a personal prompt library.",
  [("Anthropic prompting tutorial","https://github.com/anthropics/prompt-eng-interactive-tutorial"),("Google Prompting Essentials","https://grow.google/prompting-essentials/")],
  [("OpenAI Prompt Engineering Guide","https://platform.openai.com/docs/guides/prompt-engineering")],
  ["F3.1 slides","F3.1 video"]),
 ("F3.2","Advanced prompting patterns",
  "Move beyond single prompts to structured techniques that improve accuracy and control.",
  ["Chain-of-thought and step-by-step decomposition","Self-critique and “reflect then revise”",
   "Structured output (tables, JSON, templates)","Prompt chaining and reusable templates"],
  "Design a reusable prompt template for a recurring task (e.g., summarising a report into a one-pager) and test it on three inputs.",
  [T["claude"]],
  [("DeepLearning.AI — ChatGPT Prompt Engineering","https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/")],
  ["F3.2 slides"]),
 ("F3.3","Co-intelligence: being the human in the loop",
  "Frame AI as a collaborator, not an oracle, using Mollick's practical rules for working with AI.",
  ["“Always invite AI to the table” and “be the human in the loop”","Treating AI as a smart but unreliable colleague",
   "When to trust, when to verify, when to refuse","Augmentation vs. automation of a task"],
  "Pick one task from your week; redesign it as a human-AI workflow, deciding what AI drafts and what you must check.",
  [T["chatgpt"],T["claude"]],
  [("Ethan Mollick — Co-Intelligence","https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/")],
  ["F3.3 slides"]),
 ("F4.1","What makes an agent (vs. a chatbot)",
  "Define agentic AI: models that plan, use tools, remember, and act over multiple steps toward a goal.",
  ["The augmented LLM: model + tools + memory + retrieval","Reason–Act–Reflect loops",
   "Why memory, tools, and reasoning enable autonomy","Human-in-the-loop and escalation triggers"],
  "Use a free agentic feature (e.g., a chatbot that can browse or run code) to complete a 3-step task and inspect each step.",
  [T["aistudio"]],
  [("Anthropic — Building Effective Agents","https://www.anthropic.com/engineering/building-effective-agents")],
  ["F4.1 slides","F4.1 video"]),
 ("F4.2","Memory and Retrieval-Augmented Generation (RAG)",
  "Explain how agents overcome context limits and hallucination using memory types and RAG.",
  ["Short-term vs. long-term memory; episodic, semantic, procedural","Embeddings and vector databases",
   "RAG pipeline: ingest, retrieve, generate","Reducing hallucination by grounding in documents"],
  "Upload your own PDFs to NotebookLM and ask source-grounded questions; notice it citing your documents instead of guessing.",
  [T["notebooklm"],T["hfspaces"]],
  [("Lewis et al. — Retrieval-Augmented Generation","https://arxiv.org/abs/2005.11401")],
  ["F4.2 slides"]),
 ("F4.3","Tools, multi-agent systems, and protocols",
  "Introduce tool use and multi-agent coordination — how several specialised agents collaborate.",
  ["Tool/function calling and JSON schemas","Multi-agent patterns: centralized, decentralized, hierarchical",
   "Frameworks: LangGraph, CrewAI, AutoGen (overview only)","Emerging protocols: MCP and Agent-to-Agent (A2A)"],
  "Sketch (on paper or in a chatbot) a “committee” of 3 agents for a task you know well — who does what, and who checks whom.",
  [T["langgraph"],T["crewai"]],
  [("Model Context Protocol (MCP)","https://modelcontextprotocol.io/")],
  ["F4.3 slides"]),
 ("F5.1","Ethics, bias, and fairness",
  "Equip yourself to spot and reason about bias, fairness, and harm in AI systems.",
  ["Sources of bias: data, design, deployment","Fairness trade-offs and disparate impact",
   "Transparency and explainability","Algorithmic accountability and liability"],
  "Probe a model for biased outputs on a sensitive scenario, then attempt to mitigate with better prompting; document what changed.",
  [T["perplexity"]],
  [("NIST AI Risk Management Framework","https://www.nist.gov/itl/ai-risk-management-framework")],
  ["F5.1 slides","F5.1 video"]),
 ("F5.2","Privacy, governance, and regulation",
  "Map the governance landscape: data privacy, IP, and the major regulatory frameworks.",
  ["What not to paste into a public chatbot (data leakage)","Copyright, IP, and provenance of AI output",
   "Global frameworks: EU AI Act; India's DPDP Act and emerging guidance","Building an organisational responsible-AI policy"],
  "Draft a one-page “safe use” checklist for your team covering data, disclosure, and verification.",
  [T["euact"]],
  [("OECD AI Principles","https://oecd.ai/en/ai-principles")],
  ["F5.2 slides"]),
]

RESEARCH = [
 ("R1.1","Why AI matters for research now",
  "Frame the opportunity and the risks of AI for research, and set norms for responsible scholarly use.",
  ["Where AI helps across the lifecycle: ideation, review, data, analysis, writing","What journals and funders currently say about AI use and disclosure",
   "The reproducibility problem with stochastic models","Academic integrity and authorship"],
  "Read your target journal's AI policy and write a two-line disclosure statement you could reuse.",
  [T["semantic"]],
  [("Grossmann et al. — AI and the transformation of social science (Science)","https://www.science.org/doi/10.1126/science.adi1778"),("Bail — Can Generative AI improve social science? (PNAS)","https://www.pnas.org/doi/10.1073/pnas.2314021121")],
  ["R1.1 slides","R1.1 video"]),
 ("R1.2","The AI-augmented research workflow",
  "Get a map of free tools for each research stage so you can assemble a zero-cost stack.",
  ["Discovery, synthesis, extraction, analysis, writing, references","Matching tool to task (and knowing each tool's failure mode)",
   "Keeping a research log of prompts and model versions","Validation as a habit, not an afterthought"],
  "Assemble your free research stack from the Tools Directory and note one validation step for each tool.",
  [T["elicit"],T["consensus"],T["connpapers"]],
  [("howtousellms — practical notebook","https://github.com/howtousellms")],
  ["R1.2 slides"]),
 ("R2.1","Literature discovery and synthesis",
  "Use AI search and synthesis tools to map a field quickly without losing rigour.",
  ["AI literature search vs. traditional databases","Citation-graph exploration to find seminal and adjacent work",
   "Evidence synthesis and the risk of fabricated citations","Building a defensible search log"],
  "Run the same review question through Elicit, Consensus, and Connected Papers; triangulate and verify five key papers in Semantic Scholar.",
  [T["elicit"],T["consensus"],T["rabbit"],T["connpapers"]],
  [("Scite — citation context","https://scite.ai")],
  ["R2.1 slides","R2.1 video"]),
 ("R2.2","Reading, summarising, and note-making at scale",
  "Turn large source sets into structured, source-grounded notes you can trust.",
  ["Grounded summarisation vs. open-ended summarisation","Extracting structured data from papers (PICO-style tables)",
   "Audio/visual overviews for fast orientation","Avoiding summary drift and overclaiming"],
  "Load 5–10 PDFs into NotebookLM, generate a briefing and a concept map, then spot-check three claims against the originals.",
  [T["notebooklm"],T["scispace"],T["scholarcy"]],
  [("OpenAlex — open scholarly data","https://openalex.org")],
  ["R2.2 slides"]),
 ("R2.3","Writing, editing, and academic communication",
  "Use AI to improve clarity and structure of scholarly writing while preserving voice and integrity.",
  ["Drafting vs. editing with AI; keeping authorial voice","Improving structure, flow, and reviewer-readiness",
   "Reverse-outlining and gap-finding","Disclosure, plagiarism, and the limits of AI-assisted writing"],
  "Take a rough abstract, ask AI to reverse-outline it, identify gaps, and tighten it — then compare against your original.",
  [T["claude"],T["chatgpt"]],
  [("Anthropic prompt engineering","https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview")],
  ["R2.3 slides"]),
 ("R3.1","Theory development and hypothesis generation",
  "Use AI as a sparring partner for theory-building without outsourcing judgement.",
  ["Brainstorming constructs, mechanisms, and rival explanations","Stress-testing a theory with adversarial prompting",
   "Surfacing assumptions and boundary conditions","Guarding against plausible-but-empty output"],
  "Give the model your research question and ask for three competing theoretical framings plus the strongest objection to each.",
  [T["claude"]],
  [("Awesome-LLM-for-Social-Science (paper hub)","https://github.com/Sherryyy96/Awesome-LLM-for-Social-Science")],
  ["R3.1 slides","R3.1 video"]),
 ("R3.2","Research design and methods planning",
  "Use AI to pressure-test design choices: sampling, measures, identification, and threats to validity.",
  ["Mapping questions to designs (experimental, survey, qualitative, mixed)","Anticipating threats to internal and external validity",
   "Power, measurement, and operationalisation as a dialogue","Pre-registration thinking"],
  "Ask the model to critique your draft design as “Reviewer 2”; convert its best three points into design changes.",
  [T["chatgpt"]],
  [("OSF — pre-registration","https://osf.io/prereg/")],
  ["R3.2 slides"]),
 ("R3.3","AI strategy for a research programme",
  "Decide where AI belongs in a multi-year agenda — and where it should not.",
  ["Build vs. buy vs. avoid for research infrastructure","Cost, reproducibility, and longevity of tools",
   "Ethics review and data governance for AI-in-research","Documenting an AI-use protocol for a lab"],
  "Draft a one-page “AI in this project” protocol: tools, prompts, versions, validation, and disclosure.",
  [],
  [("Argyle et al. — Out of One, Many (Political Analysis)","https://www.cambridge.org/core/journals/political-analysis/article/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49")],
  ["R3.3 slides"]),
 ("R4.1","LLMs for text annotation and classification",
  "Use LLMs to code and classify text at scale, and validate against human labels properly.",
  ["Zero-shot and few-shot classification","Inter-rater reliability between model and humans (Cohen's / Krippendorff's)",
   "Prompt sensitivity and the need for multiple runs","When fine-tuned classical models still win"],
  "Replicate the howtousellms workflow: classify a small labelled text set (e.g., populism), compute agreement with the gold labels, and report it.",
  [T["howto"],T["colab"],T["hf"]],
  [("Ziems et al. — Can LLMs Transform Computational Social Science?","https://arxiv.org/abs/2305.03514"),("Navigating the Risks of LLM Text Annotation","https://arxiv.org/abs/2306.00176")],
  ["R4.1 slides","R4.1 video","R4.1 notebook"]),
 ("R4.2","Silicon samples and synthetic respondents",
  "Critically explore using LLMs to simulate human samples for early-stage and pilot research.",
  ["“Silicon sampling”: conditioning models on personas to mimic populations","Where it is useful (piloting, pretesting) and where it misleads",
   "Validity, coverage, and bias of synthetic respondents","Ethical and reporting standards"],
  "Adapt the LLM-for-Social-Science synthetic-sampling notebook to generate synthetic survey responses, then compare distributions to a real benchmark.",
  [T["llmsocsci"],T["colab"]],
  [("Argyle et al. — Out of One, Many","https://www.cambridge.org/core/journals/political-analysis/article/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49"),("Horton — LLMs as Simulated Economic Agents","https://arxiv.org/abs/2301.07543")],
  ["R4.2 slides","R4.2 notebook"]),
 ("R4.3","Agent-based and simulation studies",
  "Introduce multi-agent LLM simulations as an emerging method for studying interaction and emergence.",
  ["LLM agents as simulated actors in social/market settings","Designing a simulation: roles, environment, interaction rules",
   "Interpreting emergent behaviour with caution","Reproducibility of stochastic simulations"],
  "Build a tiny 2–3 agent negotiation or market simulation in a chatbot or Colab and log the transcript for analysis.",
  [T["colab"],T["langgraph"]],
  [("Multi-Agent LLM Systems for Social Science (arXiv)","https://arxiv.org/abs/2310.06692")],
  ["R4.3 slides"]),
 ("R4.4","Building and sharing a research app or demo",
  "Package a method as a small, shareable app so others can reproduce and extend it.",
  ["From notebook to interactive demo","Editable system prompts and transparency",
   "Synthetic data for safe demonstration","Deployment options (free): Hugging Face Spaces, GitHub Pages"],
  "Follow the UCLA Anderson App Development Kit to stand up a minimal AI app, then publish a no-backend version on Hugging Face Spaces or GitHub Pages.",
  [T["ucla"],T["hfspaces"],T["gradio"]],
  [("UCLA Anderson SSAI (course site)","https://ucla-anderson-ssai.github.io/SSAI/")],
  ["R4.4 slides","R4.4 demo"]),
 ("R4.5","Validity, reliability, and reporting standards",
  "Establish how to validate AI-as-method results and report them so others can reproduce the work.",
  ["Run multiple iterations; report variability, not a single run","Human validation subsets and agreement metrics",
   "Reporting prompts, model versions, dates, and parameters","Threats to validity specific to LLM measurement"],
  "Write a methods paragraph for one of the earlier R4 exercises that a reviewer could reproduce exactly.",
  [],
  [("Evaluation guidelines for empirical studies with LLMs (arXiv)","https://arxiv.org/abs/2411.10915")],
  ["R4.5 slides"]),
]

MANAGEMENT = [
 ("M1.1","Intelligent systems: what AI actually is for business",
  "Give managers an accurate, hype-free model of AI and a shared vocabulary for cross-functional conversations.",
  ["Rule-based to GenAI in business terms","Live capability vs. marketing hype",
   "Mapping the AI landscape to business functions","What AI changes about competitive dynamics"],
  "Audit your own role: list five tasks and mark each as automate, augment, or leave alone.",
  [T["chatgpt"],T["gemini"]],
  [("McKinsey — The State of AI","https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai")],
  ["M1.1 slides","M1.1 video"]),
 ("M1.2","The AI revolution so far — promise vs. delivery",
  "Assess what AI has actually delivered globally and in India, and the implications for firms.",
  ["Global and Indian model ecosystems","Promised vs. realised value; the adoption gap",
   "Why most AI projects fail (and the data behind it)","Adoption implications for Indian firms"],
  "Find one AI success and one failure case in your industry; identify the single biggest factor in each.",
  [],
  [("BCG/HBS — Jagged Frontier field study","https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321")],
  ["M1.2 slides"]),
 ("M1.3","What comes next: models, workflows, and agents",
  "Help managers anticipate the move from models to workflows to autonomous agents.",
  ["Models vs. workflows vs. agents","Human–AI interface design",
   "Predicting 3-year enterprise maturity","Where to place safe early bets"],
  "Sketch a 3-year AI maturity path for your function with one initiative per year.",
  [T["perplexity"]],
  [("Anthropic — Building Effective Agents","https://www.anthropic.com/engineering/building-effective-agents")],
  ["M1.3 slides"]),
 ("M2.1","Prompting and productivity for managers",
  "Build practical prompting skill for management tasks: analysis, drafting, synthesis, and decision prep.",
  ["Task–Context–References–Evaluate–Iterate for business","Prompt templates for recurring management tasks",
   "Human-in-the-loop verification","Building a team prompt library"],
  "Create three reusable prompts (board summary, customer email triage, meeting-notes-to-actions) and test them.",
  [T["claude"],T["chatgpt"],T["copilot"]],
  [("Google Prompting Essentials","https://grow.google/prompting-essentials/")],
  ["M2.1 slides","M2.1 video"]),
 ("M2.2","GenAI across business functions",
  "Tour high-value GenAI use cases by function with realistic ROI and risk.",
  ["Marketing & content; sales; service; HR; finance; operations","Personalisation and customer experience",
   "Augmenting vs. replacing roles","Estimating value and cost"],
  "Pick one function and design a small GenAI pilot with a success metric and a risk to watch.",
  [T["notebooklm"],T["gamma"]],
  [("Brynjolfsson et al. — Generative AI at Work","https://www.nber.org/papers/w31161")],
  ["M2.2 slides"]),
 ("M2.3","Low-code prototyping for managers",
  "Build a working proof-of-concept without engineers, to make AI concrete.",
  ["No-code/low-code AI builders","Custom GPTs / assistants for a workflow",
   "Connecting a chatbot to your own documents (RAG, lightly)","From prototype to a business case"],
  "Build a custom assistant grounded in a few of your documents and demo it to a colleague.",
  [T["hfspaces"],T["aistudio"],T["gradio"]],
  [("UCLA Anderson App Development Kit","https://ucla-anderson-ssai.github.io/SSAI/")],
  ["M2.3 slides","M2.3 demo"]),
 ("M3.1","Data before models: why transformations win or fail",
  "Show managers why data quality and readiness decide AI outcomes more than model choice.",
  ["Four data dimensions: quality, availability, governance, structure","Diagnosing a client's or firm's data posture",
   "Why most AI failures are really data failures","Building a minimum viable data foundation"],
  "Run a quick data-readiness self-assessment for one use case in your organisation.",
  [],
  [("McKinsey — The State of AI","https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai")],
  ["M3.1 slides","M3.1 video"]),
 ("M3.2","Decision systems and managing risk",
  "Translate model metrics into business decisions about acceptable error and cost.",
  ["Precision and recall in business terms","Cost of false positives vs. false negatives",
   "Decision thresholds as a management choice","Segmentation and customer intelligence beyond demographics"],
  "For a churn or fraud scenario, decide where to set the threshold and justify the trade-off in money terms.",
  [T["chatgpt"]],
  [("Google ML Crash Course — classification","https://developers.google.com/machine-learning/crash-course/classification/video-lecture")],
  ["M3.2 slides"]),
 ("M3.3","From text and behaviour to intelligence",
  "Use NLP and pattern-mining to turn customer voice and behaviour into decisions.",
  ["Sentiment and topic modelling; classical NLP vs. LLM cost/complexity","Association and co-purchase patterns (cross-sell, assortment)",
   "Actionable signal vs. noise","Semantic search and RAG for enterprise knowledge"],
  "Paste a set of customer reviews into a chatbot and extract themes, sentiment, and three actions; sanity-check the themes.",
  [T["claude"],T["notebooklm"]],
  [("howtousellms (text analysis)","https://github.com/howtousellms")],
  ["M3.3 slides"]),
 ("M4.1","Reasoning, memory, and agents in the enterprise",
  "Explain agentic AI for managers: what it automates, where it needs oversight, and the governance implications.",
  ["Reason–Act–Reflect loops in a business process","Memory and RAG for institutional knowledge",
   "Escalation triggers, audit trails, human oversight","Specifying memory and tools for a client need"],
  "Map one end-to-end process and mark where an agent could act vs. where a human must approve.",
  [],
  [("Anthropic — Building Effective Agents","https://www.anthropic.com/engineering/building-effective-agents")],
  ["M4.1 slides","M4.1 video"]),
 ("M4.2","Multi-agent systems and orchestration",
  "Show how a “committee” of specialised agents can run a workflow, and the failure modes to manage.",
  ["Generic (proxy) vs. specialist agents","Centralized, decentralized, hierarchical patterns",
   "Agent-to-Agent communication and failure modes","Roles, recovery, and accountability"],
  "Design a multi-agent committee for a real workflow (e.g., loan review): name each agent, its tools, and its checks.",
  [T["crewai"],T["langgraph"]],
  [("Model Context Protocol","https://modelcontextprotocol.io/")],
  ["M4.2 slides"]),
 ("M5.1","AI strategy and business models",
  "Connect AI capability to strategy: where it creates durable advantage and where it is just table stakes.",
  ["AI as feature vs. AI as platform","Build vs. buy vs. partner",
   "Data and workflow as moats","Portfolio approach to AI initiatives"],
  "Place three possible AI initiatives on an impact-vs-feasibility grid and pick one to champion.",
  [],
  [("Wharton — AI for Business (exec ed overview)","https://executiveeducation.wharton.upenn.edu/")],
  ["M5.1 slides","M5.1 video"]),
 ("M5.2","Innovation, disruption, and the future of work",
  "Examine how GenAI reshapes industries, roles, and the labour market.",
  ["Exposure of occupations and tasks to GenAI","Augmentation vs. displacement",
   "Reskilling and workforce strategy","Industry disruption patterns"],
  "Estimate the AI exposure of your own team's tasks and draft a reskilling priority.",
  [],
  [("Eloundou et al. — GPTs are GPTs","https://arxiv.org/abs/2303.10130")],
  ["M5.2 slides"]),
 ("M6.1","AI without guardrails: governance, fairness, liability",
  "Prepare managers to govern AI: bias, fairness, liability, and responsible-AI frameworks.",
  ["Algorithmic bias and consultant/firm liability","Responsible-AI principles in practice",
   "India-specific regulation (DPDP) and global frameworks","Vendor due diligence and contractual safeguards"],
  "Draft a responsible-AI checklist for evaluating a vendor's AI product.",
  [T["euact"]],
  [("NIST AI Risk Management Framework","https://www.nist.gov/itl/ai-risk-management-framework"),("OECD AI Principles","https://oecd.ai/en/ai-principles")],
  ["M6.1 slides","M6.1 video"]),
 ("M6.2","Implementing AI and leading change",
  "Turn an AI plan into adoption by managing people, process, and resistance.",
  ["Change frameworks (e.g., ADKAR) for AI adoption","Overcoming middle-management resistance",
   "90-day post-deployment monitoring and stakeholder plans","Measuring realised value"],
  "Build a 90-day adoption plan for one AI initiative, including a resistance-mitigation step.",
  [],
  [("McKinsey — The State of AI","https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai")],
  ["M6.2 slides"]),
]

TRACKS = {
 "foundation": ("Foundation", FOUNDATION, "foundation/index.html"),
 "research":   ("Research",   RESEARCH,   "research/index.html"),
 "management": ("Management", MANAGEMENT, "management/index.html"),
}

for tkey, (tname, lessons, turl) in TRACKS.items():
    rel = "../"
    siblings = [(c, t, f"{slug(c)}.html") for c, t, *_ in lessons]
    for i, (code, title, obj, concepts, handson, tools, reads, refs) in enumerate(lessons):
        prev_l = (lessons[i-1][0], f"{slug(lessons[i-1][0])}.html") if i > 0 else None
        next_l = (lessons[i+1][0], f"{slug(lessons[i+1][0])}.html") if i < len(lessons)-1 else None
        modpref = code.split(".")[0]
        mod_sib = [(c, t, u) for c, t, u in siblings if c.split(".")[0] == modpref]
        page = lesson_page(rel, rel+turl, tname, code, title, obj, concepts, handson,
                           tools, reads, refs, prev_l, next_l, mod_sib)
        path = os.path.join(ROOT, tkey, f"{slug(code)}.html")
        with open(path, "w", encoding="utf-8") as f: f.write(page)
        print("wrote", path)

print("DONE")
