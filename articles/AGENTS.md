# Repository Guidelines

## Project Structure & Module Organization
This repository is a small static blog. Most content lives at the repo root.
- `*.md`: Source posts in Markdown (e.g., `EndofSaaS.md`).
- `*.html`: Rendered HTML versions of posts and landing pages (e.g., `EndofSaaS.html`, `index.html`).
- `md-to-html-merge/`: Helper tooling for Markdown-to-HTML workflows (restricted; see repo owner if needed).
- `node_modules/`, `package.json`, `package-lock.json`: Node dependency for Markdown rendering.

## Build, Test, and Development Commands
There is no formal build pipeline or test suite in this repo.
- `npm install`: Install the `markdown-it` dependency for local conversion scripts.
- If you add or edit a post, update both the `.md` and corresponding `.html` file and verify links in `index.html`.

## Coding Style & Naming Conventions
- Markdown: Keep headings short, use sentence case, and prefer 1–2 sentence paragraphs.
- HTML: Keep formatting consistent with existing files; avoid reformatting unless necessary.
- File naming: Use descriptive, CamelCase filenames for posts (e.g., `HumanSkillinAI.md`) and keep `.md` / `.html` pairs aligned.

## Testing Guidelines
No automated tests are configured. Verify changes manually:
- Open `index.html` and the updated post HTML in a browser.
- Check relative links and navigation text.

## Commit & Pull Request Guidelines
Commit messages are short, imperative, and scoped (e.g., `Add EndofSaaS post and index link`, `Fix index titles and shopify link`).
For pull requests:
- Provide a concise summary of the content change.
- Note which files were updated (e.g., `EndofSaaS.md`, `EndofSaaS.html`, `index.html`).
- Include before/after screenshots for visual changes to `index.html`.

## Agent-Specific Instructions
When generating or editing posts, treat the Markdown file as the source of truth and keep the HTML version in sync. Avoid introducing large formatting diffs unless requested.
