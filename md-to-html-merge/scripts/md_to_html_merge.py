import argparse
import datetime
import html
import os
import re
import subprocess
import sys
from typing import Dict, Tuple


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def parse_frontmatter(markdown_text: str) -> Tuple[Dict[str, str], str]:
    pattern = r"^---\s*\n(.*?)\n---\s*\n"
    match = re.match(pattern, markdown_text, flags=re.DOTALL)
    if not match:
        return {}, markdown_text

    raw_frontmatter = match.group(1)
    body = markdown_text[match.end():]
    data: Dict[str, str] = {}

    for line in raw_frontmatter.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key:
            data[key] = value

    return data, body


def extract_first_h1(markdown_text: str) -> Tuple[str, str]:
    lines = markdown_text.splitlines()
    for idx, line in enumerate(lines):
        match = re.match(r"^\s*#\s+(.+)$", line)
        if match:
            title = match.group(1).strip()
            remaining = "\n".join(lines[:idx] + lines[idx + 1:])
            return title, remaining
    return "", markdown_text


def convert_markdown(markdown_text: str) -> str:
    try:
        import markdown  # type: ignore
        return markdown.markdown(
            markdown_text,
            extensions=["fenced_code", "tables"],
        )
    except Exception:
        try:
            result = subprocess.run(
                ["pandoc", "-f", "markdown", "-t", "html"],
                input=markdown_text.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return result.stdout.decode("utf-8")
        except Exception as exc:
            raise RuntimeError(
                "Markdown conversion failed. Install the 'markdown' package or pandoc."
            ) from exc


def build_html(title: str, body_html: str, site_title: str) -> str:
    escaped_title = html.escape(title)
    escaped_site = html.escape(site_title)
    return f"""<!doctype html>
<html lang=\"ja\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <meta name=\"color-scheme\" content=\"dark\" />
  <title>{escaped_title} | {escaped_site}</title>

  <style>
    :root {{
      --bg: #0f1115;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --accent: #4f8cff;
      --line: rgba(255,255,255,.08);
      --code-bg: #1a1d24;
    }}

    html {{ color-scheme: dark; }}

    body {{
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont,
                   "Segoe UI", Roboto, "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.85;
    }}

    main {{
      max-width: 720px;
      margin: 0 auto;
      padding: 32px 20px 80px;
    }}

    h1 {{
      font-size: 1.9rem;
      margin: 0 0 0.6em;
      padding-bottom: 0.4em;
      border-bottom: 1px solid var(--line);
    }}

    h2 {{
      font-size: 1.4rem;
      margin: 2em 0 0.8em;
      padding-bottom: 0.3em;
      border-bottom: 1px solid var(--line);
    }}

    h3 {{
      font-size: 1.1rem;
      margin: 1.6em 0 0.6em;
      font-weight: 600;
    }}

    p {{
      margin: 1em 0;
    }}

    a {{
      color: var(--accent);
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    ul, ol {{
      margin: 1em 0;
      padding-left: 1.5em;
    }}

    li {{
      margin: 0.3em 0;
    }}

    strong {{
      color: #fff;
      font-weight: 600;
    }}

    blockquote {{
      margin: 1.5em 0;
      padding: 0.8em 1.2em;
      border-left: 3px solid var(--accent);
      background: var(--code-bg);
      color: var(--muted);
    }}

    pre {{
      background: var(--code-bg);
      padding: 1em;
      border-radius: 6px;
      overflow-x: auto;
      margin: 1.5em 0;
    }}

    code {{
      background: var(--code-bg);
      padding: 0.2em 0.4em;
      border-radius: 3px;
      font-size: 0.9em;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}

    pre code {{
      background: none;
      padding: 0;
    }}

    .back-link {{
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 2em;
      display: inline-block;
    }}

    .back-link:hover {{
      color: var(--accent);
    }}

    footer {{
      max-width: 720px;
      margin: 0 auto;
      padding: 24px 20px 40px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 0.85rem;
    }}
  </style>
</head>

<body>
  <main>
    <a href=\"./index.html\" class=\"back-link\">Back to index</a>

    <h1>{escaped_title}</h1>

    {body_html}
  </main>

  <footer>
    &copy; {escaped_site} / GitHub Pages
  </footer>
</body>
</html>
"""


def find_site_title(index_html: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", index_html, flags=re.DOTALL)
    if not match:
        return "Keith CCC Blog"
    raw = re.sub(r"<.*?>", "", match.group(1))
    return html.unescape(raw).strip() or "Keith CCC Blog"


def insert_into_index(index_path: str, link_name: str, title: str, date_str: str) -> bool:
    content = read_text(index_path)
    if f"./{link_name}" in content:
        return False

    list_match = re.search(r"<ul class=\"post-list\">", content)
    if not list_match:
        raise RuntimeError("Could not find <ul class=\"post-list\"> in index.html")

    insert_pos = content.find("\n", list_match.end()) + 1
    if insert_pos <= 0:
        raise RuntimeError("Could not determine insertion point in index.html")

    escaped_title = html.escape(title)
    entry = (
        "\n"
        "      <li>\n"
        f"        <a href=\"./{link_name}\">\n"
        f"          {escaped_title}\n"
        "        </a>\n"
        f"        <span class=\"post-date\">{date_str}</span>\n"
        "      </li>\n\n"
    )

    updated = content[:insert_pos] + entry + content[insert_pos:]
    write_text(index_path, updated)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML and merge into index.html")
    parser.add_argument("--md", required=True, help="Path to Markdown file")
    parser.add_argument("--index", required=True, help="Path to index.html")
    parser.add_argument("--out", help="Output HTML path")
    parser.add_argument("--title", help="Override title")
    parser.add_argument("--date", help="Override date (YYYY-MM-DD)")
    args = parser.parse_args()

    md_path = os.path.abspath(args.md)
    index_path = os.path.abspath(args.index)
    out_path = os.path.abspath(args.out) if args.out else os.path.splitext(md_path)[0] + ".html"

    markdown_text = read_text(md_path)
    frontmatter, body = parse_frontmatter(markdown_text)

    title_from_h1, body_without_h1 = extract_first_h1(body)
    title = args.title or frontmatter.get("title") or title_from_h1 or os.path.splitext(os.path.basename(md_path))[0]

    date_from_frontmatter = frontmatter.get("date", "").strip()
    if date_from_frontmatter:
        date_value = date_from_frontmatter.split()[0]
    else:
        date_value = datetime.date.today().isoformat()
    date_value = args.date or date_value

    if title_from_h1 and title == title_from_h1:
        markdown_for_conversion = body_without_h1
    else:
        markdown_for_conversion = body

    body_html = convert_markdown(markdown_for_conversion)

    index_html = read_text(index_path)
    site_title = find_site_title(index_html)

    html_output = build_html(title, body_html, site_title)
    write_text(out_path, html_output)

    inserted = insert_into_index(index_path, os.path.basename(out_path), title, date_value)
    if inserted:
        print(f"Updated index.html with link to {os.path.basename(out_path)}")
    else:
        print("index.html already contains a link to this post; no changes made.")

    print(f"Wrote HTML: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
