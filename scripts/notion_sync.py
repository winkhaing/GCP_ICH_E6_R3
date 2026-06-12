#!/usr/bin/env python3
"""
Notion → GitHub Pages sync script.
Fetches a Notion page and all its subpages recursively,
converts them to Markdown, and writes to docs/ for Jekyll/GitHub Pages.
"""

import os
import re
import sys
import json
import time
import requests
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
NOTION_TOKEN  = os.environ["NOTION_TOKEN"]
ROOT_PAGE_ID  = os.environ["NOTION_PAGE_ID"]
OUTPUT_DIR    = Path("docs")

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
API = "https://api.notion.com/v1"

# ── Helpers ──────────────────────────────────────────────────────────────────
def get(url, **params):
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

def post(url, data):
    r = requests.post(url, headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()

def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-") or "page"

# ── Rich text → Markdown ─────────────────────────────────────────────────────
def rt_to_md(rich_text):
    out = []
    for t in rich_text:
        s = t.get("plain_text", "")
        a = t.get("annotations", {})
        if a.get("bold"):        s = f"**{s}**"
        if a.get("italic"):      s = f"*{s}*"
        if a.get("code"):        s = f"`{s}`"
        if a.get("strikethrough"): s = f"~~{s}~~"
        href = t.get("href")
        if href:                 s = f"[{s}]({href})"
        out.append(s)
    return "".join(out)

# ── Block → Markdown ─────────────────────────────────────────────────────────
def blocks_to_md(blocks, depth=0):
    lines = []
    indent = "  " * depth

    i = 0
    while i < len(blocks):
        b = blocks[i]
        bt = b["type"]

        if bt == "paragraph":
            text = rt_to_md(b["paragraph"]["rich_text"])
            lines.append(f"{indent}{text}\n" if text.strip() else "")

        elif bt == "heading_1":
            lines.append(f"# {rt_to_md(b['heading_1']['rich_text'])}\n")
        elif bt == "heading_2":
            lines.append(f"## {rt_to_md(b['heading_2']['rich_text'])}\n")
        elif bt == "heading_3":
            lines.append(f"### {rt_to_md(b['heading_3']['rich_text'])}\n")

        elif bt == "bulleted_list_item":
            text = rt_to_md(b["bulleted_list_item"]["rich_text"])
            lines.append(f"{indent}- {text}\n")
            if b.get("has_children"):
                child_blocks = fetch_blocks(b["id"])
                lines.extend(blocks_to_md(child_blocks, depth + 1))

        elif bt == "numbered_list_item":
            text = rt_to_md(b["numbered_list_item"]["rich_text"])
            lines.append(f"{indent}1. {text}\n")
            if b.get("has_children"):
                child_blocks = fetch_blocks(b["id"])
                lines.extend(blocks_to_md(child_blocks, depth + 1))

        elif bt == "toggle":
            text = rt_to_md(b["toggle"]["rich_text"])
            lines.append(f"{indent}**{text}**\n")
            if b.get("has_children"):
                child_blocks = fetch_blocks(b["id"])
                lines.extend(blocks_to_md(child_blocks, depth + 1))

        elif bt == "callout":
            icon = b["callout"].get("icon", {})
            emoji = icon.get("emoji", "💡") if icon.get("type") == "emoji" else "💡"
            text = rt_to_md(b["callout"]["rich_text"])
            lines.append(f"> {emoji} {text}\n")

        elif bt == "quote":
            text = rt_to_md(b["quote"]["rich_text"])
            lines.append(f"> {text}\n")

        elif bt == "code":
            lang = b["code"].get("language", "")
            code = rt_to_md(b["code"]["rich_text"])
            lines.append(f"```{lang}\n{code}\n```\n")

        elif bt == "divider":
            lines.append("---\n")

        elif bt == "image":
            img = b["image"]
            url = (img.get("file") or img.get("external") or {}).get("url", "")
            caption = rt_to_md(img.get("caption", []))
            alt = caption or "image"
            if url:
                lines.append(f"![{alt}]({url})\n")

        elif bt == "table":
            if b.get("has_children"):
                rows = fetch_blocks(b["id"])
                for ri, row in enumerate(rows):
                    cells = row.get("table_row", {}).get("cells", [])
                    row_md = "| " + " | ".join(rt_to_md(c) for c in cells) + " |"
                    lines.append(row_md + "\n")
                    if ri == 0:
                        sep = "| " + " | ".join("---" for _ in cells) + " |"
                        lines.append(sep + "\n")

        elif bt == "column_list":
            if b.get("has_children"):
                cols = fetch_blocks(b["id"])
                for col in cols:
                    if col.get("has_children"):
                        col_blocks = fetch_blocks(col["id"])
                        lines.extend(blocks_to_md(col_blocks, depth))

        elif bt == "child_page":
            # Handled separately in recursive page sync — skip inline
            pass

        elif bt == "to_do":
            text = rt_to_md(b["to_do"]["rich_text"])
            checked = "x" if b["to_do"].get("checked") else " "
            lines.append(f"{indent}- [{checked}] {text}\n")

        i += 1

    return lines

# ── Notion API calls ──────────────────────────────────────────────────────────
def fetch_page(page_id):
    return get(f"{API}/pages/{page_id}")

def fetch_blocks(block_id):
    results = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        data = get(f"{API}/blocks/{block_id}/children", **params)
        results.extend(data["results"])
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
        time.sleep(0.2)
    return results

def page_title(page):
    props = page.get("properties", {})
    for key in ("title", "Name", "Title"):
        p = props.get(key)
        if p and p.get("title"):
            return rt_to_md(p["title"]) or "Untitled"
    return page.get("object", "Untitled")

# ── Recursive page sync ───────────────────────────────────────────────────────
def sync_page(page_id, parent_path: Path, nav: list, depth=0):
    """
    Sync one page and recurse into child_pages.
    nav: list collecting {title, path} for nav generation.
    """
    page = fetch_page(page_id)
    title = page_title(page)
    slug = slugify(title)
    out_dir = parent_path / slug if depth > 0 else parent_path
    out_dir.mkdir(parents=True, exist_ok=True)

    blocks = fetch_blocks(page_id)

    # Separate child_page blocks from content blocks
    content_blocks = [b for b in blocks if b["type"] != "child_page"]
    child_page_blocks = [b for b in blocks if b["type"] == "child_page"]

    md_lines = [f"---\ntitle: \"{title}\"\nlayout: default\n---\n\n",
                f"# {title}\n\n"]
    md_lines.extend(blocks_to_md(content_blocks))

    # Add subpage links at the bottom if any
    if child_page_blocks:
        md_lines.append("\n---\n\n## Subpages\n\n")
        for cp in child_page_blocks:
            child_title = cp["child_page"]["title"]
            child_slug = slugify(child_title)
            rel_path = f"./{slug}/{child_slug}/" if depth == 0 else f"./{child_slug}/"
            md_lines.append(f"- [{child_title}]({rel_path})\n")

    # Write index.md for this page
    out_file = out_dir / "index.md"
    out_file.write_text("".join(md_lines), encoding="utf-8")
    rel = str(out_file.relative_to(OUTPUT_DIR))
    print(f"  {'  ' * depth}✓ {rel}")

    nav_entry = {"title": title, "path": str(out_dir.relative_to(OUTPUT_DIR)), "children": []}
    nav.append(nav_entry)

    # Recurse
    for cp in child_page_blocks:
        sync_page(cp["id"], out_dir, nav_entry["children"], depth + 1)
        time.sleep(0.3)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"🔄  Syncing Notion page {ROOT_PAGE_ID} → {OUTPUT_DIR}/\n")
    OUTPUT_DIR.mkdir(exist_ok=True)

    nav = []
    sync_page(ROOT_PAGE_ID, OUTPUT_DIR, nav, depth=0)

    print(f"\n✅  Done — {sum(1 for _ in OUTPUT_DIR.rglob('*.md'))} pages written.")

if __name__ == "__main__":
    main()
