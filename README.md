# AI for Management &amp; Research — course website

A free, static, hands-on course website with three tracks (a shared **Foundation**, an **AI for Research** track, and an **AI for Managers** track), plus a teaching portfolio, a free-tools directory, and a reading library.

Built as plain **HTML + CSS** (no framework, no build step) so it hosts free on **GitHub Pages** and the professor can edit content in a text editor.

---

## Structure

```
/                       landing page (index.html)
/about.html             instructor / portfolio bio
/toolkit.html           free tools directory
/library.html           reading & resource library
/foundation/            Shared Foundation — index + lessons (f1-1.html … f5-2.html)
/research/              Research Track — index + lessons (r1-1.html … r4-5.html)
/management/            Management Track — index + lessons (m1-1.html … m6-2.html)
/courses/               teaching portfolio index + SPJIMR course outlines
/assets/style.css       the single shared stylesheet (the whole visual identity)
/assets/main.js         mobile-nav toggle
```

Every lesson page renders the same six blocks: **Objective → Key concepts → Hands-on → Free tools → Read / explore → Materials.**

## Wiring up slides, videos &amp; papers

Throughout the lessons and course outlines you'll see chips like `ref: F2.1 slides` or `ref: S3 notebook`. These are placeholders. To turn one into a real link, open the page, find the chip, and replace:

```html
<a class="ref" href="#" onclick="return false" title="To be linked">ref: F2.1 slides</a>
```

with:

```html
<a class="ref" href="https://link-to-your-slides">ref: F2.1 slides</a>
```

(Remove the `onclick="return false"`.)

## Adding or editing a lesson

The lesson and outline pages were generated from data files for consistency:

- `gen_lessons.py` — all Foundation / Research / Management lesson pages (edit the `FOUNDATION`, `RESEARCH`, `MANAGEMENT` lists, then re-run `python3 gen_lessons.py`).
- `gen_indexes.py` — the Research &amp; Management track index pages.
- `courses/gen_courses.py` — the SPJIMR course outline pages.
- `gen_resources.py` — the toolkit &amp; library pages.

You can also just edit any `.html` file by hand — they're self-contained. To add a brand-new lesson by hand, copy an existing lesson page (e.g. `foundation/f2-1.html`), change the content, and add a link to it from that track's `index.html`.

## Publish on GitHub Pages

1. Create a new **public** repository (e.g. `ai-course-site`) and push these files to the `main` branch.
2. In the repo: **Settings → Pages → Build and deployment → Source = GitHub Actions**.
3. The included workflow (`.github/workflows/deploy.yml`) deploys the site on every push to `main`. The live URL appears under Settings → Pages.

The site uses **relative links** throughout, so it works whether served from the domain root or a project sub-path (`username.github.io/ai-course-site/`). The `.nojekyll` file tells Pages to serve the files as-is.

## Custom domain (optional)

Add a `CNAME` file containing your domain, point a DNS record at GitHub Pages, and enable **Enforce HTTPS** in Settings → Pages.

## License

This project is dual-licensed to separate the code from the educational content:

- **Code** (the Python generator scripts, `assets/style.css`, `assets/main.js`) — [MIT License](LICENSE).
- **Content** (lesson text, course outlines, descriptions, and other prose) — [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT).

Where a file mixes both (e.g. a generator script containing course text), the code is under MIT and the embedded content is under CC BY 4.0. Reuse of the content requires attribution to **Prof. Abhishek Kumar Jha, SPJIMR**.

---

© 2026 · Prof. Abhishek Kumar Jha · SPJIMR Information Management. Open learning, free to use.
