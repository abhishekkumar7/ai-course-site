#!/usr/bin/env python3
"""Generate SPJIMR course outline pages in courses/."""
import os, html
from _common import masthead, footer, page_shell

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REL = "../"

def course_page(fname, badge, title, subtitle, desc_paras, clos, pedagogy, sessions, refs):
    clo_html = "".join(f"<li>{html.escape(c)}</li>" for c in clos)
    ped_html = "".join(f"<li>{html.escape(p)}</li>" for p in pedagogy)
    desc_html = "".join(f"<p>{html.escape(p)}</p>" for p in desc_paras)
    sched = ""
    if sessions:
        rows = ""
        for num, t, detail, ref in sessions:
            refc = f'<a class="ref" href="#" onclick="return false" title="To be linked">ref: {html.escape(ref)}</a>' if ref else ""
            rows += f'''<tr><td class="num">{html.escape(num)}</td><td class="ttl">{html.escape(t)}<div style="font-weight:400;color:var(--slate);font-size:13.5px;margin-top:5px">{html.escape(detail)}</div></td><td>{refc}</td></tr>'''
        sched = f'''<div class="block"><p class="blabel">Session plan</p>
        <div class="tablewrap"><table class="schedule">
          <thead><tr><th style="width:70px">#</th><th>Session</th><th style="width:120px">Materials</th></tr></thead>
          <tbody>{rows}</tbody>
        </table></div></div>'''
    refnote = ""
    if refs:
        refnote = f'<div class="lead-note"><b>Note.</b> {html.escape(refs)}</div>'
    body = f'''<div class="lessonhead">
  <div class="wrap">
    <p class="crumb"><a href="index.html">All courses</a> · SPJIMR</p>
    <h1>{html.escape(title)}</h1>
    <p class="lcode">{html.escape(subtitle)}</p>
  </div>
</div>
<section>
  <div class="wrap">
    <div class="lessonbody">
      <article>
        <div class="block"><p class="blabel">Course description</p>{desc_html}</div>
        <div class="block"><p class="blabel">Learning outcomes</p><ul>{clo_html}</ul></div>
        <div class="block"><p class="blabel">Pedagogy</p><ul>{ped_html}</ul></div>
        {sched}
        {refnote}
      </article>
      <aside class="sidebar">
        <h4>Course</h4>
        <nav>
          <a href="#">{html.escape(badge)}</a>
          <a href="../about.html">Instructor</a>
          <a href="index.html">All courses</a>
        </nav>
        <div class="pager">
          <a href="index.html">← Back to all courses</a>
        </div>
        <div class="lead-note" style="margin-top:20px;font-size:13px">This course is taught in residence at SPJIMR. Materials for enrolled students live on the institute's platforms.</div>
      </aside>
    </div>
  </div>
</section>'''
    full = page_shell(REL, f"{title} — SPJIMR course", subtitle, body)
    with open(os.path.join(ROOT, "courses", fname), "w", encoding="utf-8") as f: f.write(full)
    print("wrote", fname)

# ---------- AAI Foundation (PGPM) — full 18-session schedule ----------
aai_sessions = [
 ("1", "Intelligent Systems: What AI Actually Is", "Rule-based to GenAI · live AI vs. marketing hype · mapping the AI landscape. Term paper & project roll-out.", ""),
 ("2", "The AI Revolution So Far", "Global & Indian models · promised vs. actual delivery · adoption implications for Indian firms.", ""),
 ("3", "What Comes Next: Scaling AI Up, Down, Sideways", "Models vs. workflow vs. agents · hands-on human-AI interface · predicting 3-year enterprise maturity.", ""),
 ("4", "Data Before Models", "Four data dimensions · diagnosing client data posture · lessons from business caselets.", ""),
 ("5", "Predicting Outcomes at Scale", "Decision design · precision/recall in business terms · managing false positive/negative costs.", ""),
 ("6", "Discovering Hidden Segments", "Uncovering 'Bharat' micro-segments · Elbow/Silhouette as business confidence · data-driven product & pricing.", ""),
 ("7", "Reading What Customers Buy Together", "Co-purchase & association rule mining · actionable patterns vs. data noise.", ""),
 ("8", "Listening to Millions", "Sentiment/topic modelling · classical NLP vs. LLM cost & complexity.", ""),
 ("9", "Mid-Course Check-In", "Critiquing mid-term proposals · sharpening problem statements. Mid review (10%).", ""),
 ("10", "AI Without Guardrails", "Algorithmic bias & liability framework · Responsible AI. Pre-read: Mercor case study.", "Mercor case"),
 ("11", "How AI Understands Meaning", "Semantic search · vector DBs and RAG architecture · multimodal search. Quiz (15%).", ""),
 ("12", "Reasoning AI and Deliberate Thinking", "System 1 vs. System 2 in AI · latency vs. reasoning depth · human-oversight checkpoints.", ""),
 ("13", "Memory in AI Systems", "Episodic, semantic, procedural · chunking & context-window management · specifying memory for client needs.", ""),
 ("14", "Introduction to AI Agents", "Reasoning-Action-Reflection loops · human-in-the-loop governance · escalation triggers & audit trails.", ""),
 ("15", "Multi-Agent Systems", "Centralized, decentralized, hierarchical patterns · A2A communication & failure modes. Term project (30%).", ""),
 ("16", "Implementing AI in Organisations", "Applying ADKAR to overcome middle-management resistance · 90-day post-deployment monitoring.", ""),
 ("17–18", "Final Project Presentations & Synthesis", "Critiquing peer proposals on rigor & ethics · presenting a consulting-ready plan covering data, governance, ROI.", ""),
]
course_page("aai-foundation.html", "PGPM · 2 credits", "AI & Analytics Foundation",
  "PGPM · Co-taught with Prof. Deep Prakash · 18 sessions · 2 credits",
  ["In an era where every business function is being reshaped by AI, the ability to understand, evaluate, and implement AI solutions is the defining competency of the next generation of management leaders. This course is a foundational pillar for future leaders stepping into implementation and transformation-consulting roles, where the gap between a technically sound proposal and successful organisational adoption can cost crores and careers.",
   "It does not treat AI as a subject for data scientists alone. Instead, it builds the strategic and applied literacy a consultant, business leader, or transformation manager needs: to diagnose AI opportunities, evaluate vendor claims, manage implementation risk, and drive adoption across complex organisations — from why projects fail on data quality, to ethical governance, to agentic architectures, all grounded in Indian and global contexts."],
  ["Evaluate AI technologies, from classical ML to generative and agentic systems, to assess business fit, data requirements, and implementation risk in consulting contexts.",
   "Design ethical, governance-compliant AI solutions by applying responsible-AI principles, India-specific regulatory frameworks, and stakeholder risk tools.",
   "Create and present a consulting-grade AI implementation plan integrating data strategy, model selection, change management, and agentic architecture for a real organisational problem."],
  ["Class and case discussion grounded in Indian and global business contexts.",
   "Individual term paper and project carried through the course, with a mid-review checkpoint.",
   "Quiz, class participation, and a final project with viva."],
  aai_sessions,
  "Evaluation: Quiz 15% · Class participation 10% · Individual term project 35% · Mid-review 10% · Final project & viva 30%.")

# ---------- LLM Research Workshop — 8 sessions ----------
llm_sessions = [
 ("1", "LLMs for Management Research", "What LLMs are (next-token prediction, transformers, scale) · five research roles · capability benchmarks · course tools (HuggingFace, Colab, GPT-4 API).", "S1 slides"),
 ("2", "Embeddings & Semantic Similarity", "From bag-of-words to sentence embeddings · cosine similarity as construct measurement · UMAP for research mapping · embedding 200 abstracts.", "S2 notebook"),
 ("3", "Data Collection: Web, APIs & Documents", "Web scraping · social media APIs · SEC EDGAR extraction · handling long documents · coreference resolution.", "S3 notebook"),
 ("4", "Data Creation I: Synthetic Respondents", "LLMs as survey participants · persona design · few-shot & RAG · coding open-ended responses · governance.", "S4 notebook"),
 ("5", "Data Creation II: Experiments & Evaluators", "LLM as stimulus generator & evaluator · DICE paradigm · detecting AI-generated responses in panels.", "S5 notebook"),
 ("6", "Data Analysis I: Classification & Measurement", "Zero-shot / few-shot / fine-tuning · GPT vs. fine-tuned BERT · synthetic-expert pipeline · Cohen's kappa, ICC.", "S6 notebook"),
 ("7", "Data Analysis II: Qualitative at Scale", "Inductive pipeline: text→embed→cluster→label→propositions · explainable ML · epistemic risks.", "S7 notebook"),
 ("8", "Meta-Research: Reviews, Theory & Ethics", "Computational literature review · the Janus effect · model collapse · methodological pluralism · project pitches.", "S8 slides"),
]
course_page("llm-research-workshop.html", "Doctoral · Research", "Using LLMs for Management Research",
  "Workshop · Prompt-first, Colab-based · Google Colab + HuggingFace · 8 sessions",
  ["A hands-on, prompt-first workshop on using large language models as instruments of management research. Built on the Google Colab and HuggingFace ecosystem, it moves through five research roles — collect, create, code, analyse, and theorize — and ends with project pitches.",
   "Every session pairs a methodological idea with a runnable notebook: embedding abstracts and clustering them, scraping and cleaning corporate filings, generating and validating synthetic respondents, computing inter-rater reliability against gold labels, and running a mini computational literature review."],
  ["Map LLM capabilities to stages of the management research lifecycle and judge where they help versus mislead.",
   "Build and run reproducible pipelines for collection, annotation, synthesis, and measurement using Colab and HuggingFace.",
   "Validate AI-as-method results against human or real-data benchmarks and report them so others can reproduce the work."],
  ["Prompt-first instruction with live Colab walkthroughs and consulting.",
   "Group exercises mapping LLM applications to each participant's research domain.",
   "A running project culminating in 3-slide, 4-minute pitches."],
  llm_sessions,
  "Anchored in recent methods readings across Organizational Research Methods, the Journal of Marketing, Marketing Science, and related venues.")

# ---------- Agentic AI ----------
course_page("agentic-ai.html", "PGDM · Elective", "Agentic AI",
  "PGDM · Concept-driven instruction + guided labs · capstone with live evaluation",
  ["A comprehensive, practice-oriented introduction to Agentic AI systems — moving beyond standalone LLMs toward autonomous, tool-using, memory-enabled agents. It covers the conceptual foundations of reasoning LLMs, test-time compute scaling, and memory architectures, alongside practical techniques such as Retrieval-Augmented Generation (RAG), tool integration, and multi-agent coordination.",
   "Learners explore how agents plan, reason, and act in complex environments by combining short- and long-term memory, external tools, and structured orchestration. The course culminates in a hands-on capstone where participants design and deploy a multi-agent 'committee' system that solves a realistic, domain-specific problem under evaluation conditions."],
  ["Explain the foundations of agentic AI, including the transition from traditional LLMs to autonomous agents that incorporate reasoning, memory, retrieval, and tool use.",
   "Design and implement intelligent agent architectures applying reasoning strategies, memory systems, RAG, tool integration, and multi-agent coordination frameworks.",
   "Build, orchestrate, and evaluate end-to-end agentic solutions that address realistic domain-specific problems through autonomous planning, decision-making, and collaboration."],
  ["Concept-driven instruction combined with real-world context.",
   "Guided hands-on labs that progressively build agent design, memory, tools, and orchestration skills.",
   "Case-based learning to translate problem statements into system requirements and architectures.",
   "Iterative system development integrating components into a complete agentic solution.",
   "Capstone with collaborative development and live evaluation on unseen data."],
  None,
  "Readings made available on Wisenet. A surprise quiz may be conducted at any time, with weightages adjusted accordingly.")

# ---------- Maker Lab ----------
course_page("maker-lab.html", "PGDM · Maker Lab", "AI Maker Lab",
  "PGDM · Discussions, tech demos, in-class group work & mini-experiments",
  ["The course enables students to structure messy managerial problems into AI-solvable tasks using large language models such as Gemini, with a focus on clear inputs, logic, and outputs. Students learn to design low-code interfaces and connect them to institutional or synthetic data (Sheets, Firebase, document repositories) to create AI-enabled business applications.",
   "It introduces Retrieval-Augmented Generation (RAG) and workflow automation (e.g., via tools like n8n) as levers to augment decision-making and redesign processes. Emphasis is placed on responsible, human-in-the-loop AI — using synthetic data, personas, and light digital twins to explore risk, governance, and accountability."],
  ["Analyse messy business problems and reframe them as well-structured AI tasks by specifying inputs, processing logic, and outputs — deciding when to use prompting, RAG, or tuning.",
   "Design and configure low-code interfaces connecting LLMs with institutional or synthetic data sources to implement basic AI-enabled business applications.",
   "Examine AI-driven workflows, identify points of failure or bias, and evaluate where human-in-the-loop checkpoints, escalation rules, and audit trails are required.",
   "Create and demonstrate an AI-enabled prototype for a real organisational problem and critically reflect on its managerial, ethical, and innovation implications."],
  ["Classroom discussion combined with technology demonstrations.",
   "In-class group-work exercises and mini-experiments.",
   "Build-focused prototyping with synthetic data and personas."],
  None,
  "No prescribed textbook. Readings shared in the course handout.")

# ---------- GenAI for Business ----------
course_page("genai-business.html", "Executive / PGPM", "Generative AI for Business",
  "Executive / PGPM · Applied, tool-supported · 17 interactive learning tools",
  ["An applied tour of generative AI for business decisions, supported by a purpose-built set of 17 interactive 'prepared playground' learning tools. Each tool is fully scaffolded so learners interact only with the parts that teach the concept — hallucination, prompting patterns, embeddings, RAG, and agents — across three delivery formats: static HTML/JS, Google Colab notebooks, and Hugging Face Spaces.",
   "The course pairs concept sessions with these hands-on tools so that managers can build intuition by doing, using free-tier models and their own API keys where needed."],
  ["Understand how generative models work and where they reliably add business value.",
   "Apply structured prompting and lightweight RAG to real management tasks.",
   "Evaluate risks — hallucination, bias, data leakage — and design human-in-the-loop safeguards."],
  ["Concept sessions paired with interactive 'prepared playground' tools.",
   "Browser-based and Colab labs requiring no installation.",
   "Free-tier model access via learner-supplied keys or hosted Spaces."],
  None,
  "Supported by a developer specification booklet covering 17 interactive tools across three delivery formats (static HTML/JS, Colab, Hugging Face Spaces).")

# ---------- Theory & Theorizing ----------
course_page("theory-theorizing.html", "Doctoral", "Theory & Theorizing",
  "Doctoral seminar · The conceptual companion to computational method",
  ["A doctoral seminar on what theory is and how it is built. Where the computational courses in this portfolio teach AI as method, this seminar develops the craft of theorizing itself — constructs, mechanisms, boundary conditions, and the moves by which scholars turn observation into explanation.",
   "It serves as the conceptual companion to the LLM research workshop: the same questions of validity and contribution, approached from the side of theory rather than tooling."],
  ["Distinguish strong theoretical contribution from description, and articulate what makes a construct and a mechanism.",
   "Critically read and position work within a theoretical conversation.",
   "Develop and defend an original theoretical argument with attention to boundary conditions."],
  ["Seminar-style close reading and discussion.",
   "Iterative development of an individual theoretical argument.",
   "Peer critique with attention to academic integrity and independent effort."],
  None,
  "Refer to the SPJIMR student manual for the plagiarism policy and academic-integrity guidelines.")

print("ALL COURSE PAGES DONE")
