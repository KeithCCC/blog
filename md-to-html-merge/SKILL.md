---
name: md-to-html-merge
description: Convert a Markdown blog post into a standalone HTML page and insert a matching list entry into index.html. Use when adding a new .md post to this blog and you need both the HTML output and the index list updated.
---

# Md To Html Merge

## Overview

Convert a single Markdown file to a styled HTML post and insert a new list item into the blog index.

## Workflow

1. Decide the input Markdown file and confirm the `index.html` path.
2. Run `scripts/md_to_html_merge.py` with `--md` and `--index` (and optional overrides).
3. Verify the new HTML file and the new list item appears at the top of the list in `index.html`.

## Command

```powershell
python md-to-html-merge/scripts/md_to_html_merge.py `
  --md c:\Development\projects\blog\MyPost.md `
  --index c:\Development\projects\blog\index.html
```

## Options

- `--out`: Output HTML path (defaults to the Markdown filename with `.html`).
- `--title`: Override the title.
- `--date`: Override the date (`YYYY-MM-DD`).

## Behavior

- Use YAML frontmatter `title` and `date` when present.
- Otherwise use the first `# Heading` as title and today as date.
- Convert Markdown to HTML via the Python `markdown` package if available, else try `pandoc`.
- Wrap the HTML in a page template that matches the blog styling.
- Insert a new list item at the top of `<ul class="post-list">` in `index.html`.
- Skip insertion if the link already exists.

## Resources

### scripts/

`md_to_html_merge.py` converts Markdown to HTML and updates `index.html`.
