#!/usr/bin/env python3
"""
Notion → GitHub Pages sync script.

Handles deeply-nested toggle-heading structures by recursively walking
ALL blocks with has_children=True to find child_page blocks at any depth.

Output layout under docs/:
  docs/index.md                        ← root page
  docs/<module-slug>/index.md          ← module overview (if any module-level content)
  docs/<module-slug>/<page-slug>/index.md  ← each subpage
"""

import os, re, time, requests
from pathlib import Path

# ── Config ───────────────────────────────────────────────────────────────────
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
ROOT_PAGE_ID = os.environ["NOTION_PAGE_ID"]
OUTPUT_DIR   = Path("docs")
API          = "https://api.notion.com/v1"
HEADERS      = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
}

# ── API helpers ───────────────────────────────────────────────────────────────
def api_get(path, **params):
    r = requests.get(f"{API}{path}", headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

def fetch_all_blocks(block_id):
    """Fetch all children blocks (paginated)."""
    results, cursor = [], None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        data = api_get(f"/blocks/{block_id}/children", **params)
        results.extend(data["results"])
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
        time.sleep(0.15)
    return results

def fetch_page(page_id):
    return api_get(f"/pages/{page_id}")

# ── Text helpers ──────────────────────────────────────────────────────────────
def rt_to_md(rich_text):
    out = []
    for t in rich_text:
        s = t.get("plain_text", "")
        a = t.get("annotations", {})
        if a.get("code"):         s = f"`{s}`"
        if a.get("bold"):         s = f"**{s}**"
        if a.get("italic"):       s = f"*{s}*"
        if a.get("strikethrough"): s = f"~~{s}~~"
        href = t.get("href")
        if href:                  s = f"[{s}]({href})"
        out.append(s)
    return "".join(out)

def slugify(text):
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s or "page"

def page_title(page):
    props = page.get("properties", {})
    for key in ("title", "Name", "Title"):
        p = props.get(key)
        if p and p.get("title"):
            rt = p["title"]
            return rt_to_md(rt) if rt else "Untitled"
    return "Untitled"

# ── Block → Markdown (content only, no child_page blocks) ────────────────────
def blocks_to_md(blocks, indent=0):
    """Convert a list of blocks to markdown lines. Recurses into has_children
    for non-child_page blocks so toggle content is included."""
    lines = []
    pad = "  " * indent

    for b in blocks:
        bt = b["type"]

        if bt == "child_page":
            continue  # handled separately

        elif bt == "paragraph":
            text = rt_to_md(b["paragraph"]["rich_text"])
            lines.append(f"{pad}{text}\n" if text.strip() else "\n")

        elif bt == "heading_1":
            text = rt_to_md(b["heading_1"]["rich_text"])
            lines.append(f"\n# {text}\n\n")
        elif bt == "heading_2":
            text = rt_to_md(b["heading_2"]["rich_text"])
            lines.append(f"\n## {text}\n\n")
        elif bt == "heading_3":
            text = rt_to_md(b["heading_3"]["rich_text"])
            lines.append(f"\n### {text}\n\n")

        elif bt == "bulleted_list_item":
            text = rt_to_md(b["bulleted_list_item"]["rich_text"])
            lines.append(f"{pad}- {text}\n")
        elif bt == "numbered_list_item":
            text = rt_to_md(b["numbered_list_item"]["rich_text"])
            lines.append(f"{pad}1. {text}\n")
        elif bt == "to_do":
            text = rt_to_md(b["to_do"]["rich_text"])
            chk  = "x" if b["to_do"].get("checked") else " "
            lines.append(f"{pad}- [{chk}] {text}\n")

        elif bt == "toggle":
            text = rt_to_md(b["toggle"]["rich_text"])
            lines.append(f"\n**{text}**\n\n")

        elif bt == "callout":
            icon = b["callout"].get("icon") or {}
            emoji = icon.get("emoji", "💡") if icon.get("type") == "emoji" else "💡"
            text  = rt_to_md(b["callout"]["rich_text"])
            lines.append(f"> {emoji} {text}\n")

        elif bt == "quote":
            text = rt_to_md(b["quote"]["rich_text"])
            lines.append(f"> {text}\n")

        elif bt == "code":
            lang = b["code"].get("language", "")
            code = rt_to_md(b["code"]["rich_text"])
            lines.append(f"```{lang}\n{code}\n```\n")

        elif bt == "divider":
            lines.append("\n---\n\n")

        elif bt == "image":
            img = b["image"]
            url = (img.get("file") or img.get("external") or {}).get("url", "")
            cap = rt_to_md(img.get("caption") or [])
            if url:
                lines.append(f"![{cap or 'image'}]({url})\n")

        elif bt == "table":
            if b.get("has_children"):
                rows = fetch_all_blocks(b["id"])
                for ri, row in enumerate(rows):
                    cells = row.get("table_row", {}).get("cells", [])
                    lines.append("| " + " | ".join(rt_to_md(c) for c in cells) + " |\n")
                    if ri == 0:
                        lines.append("| " + " | ".join("---" for _ in cells) + " |\n")
                continue  # children already consumed

        elif bt in ("column_list", "column"):
            pass  # fall through to has_children handling below

        # Recurse into any block with children (toggle headings, columns, etc.)
        if b.get("has_children") and bt not in ("child_page", "table"):
            child_blocks = fetch_all_blocks(b["id"])
            # Only pass content blocks (skip child_pages here; they're collected separately)
            content = [x for x in child_blocks if x["type"] != "child_page"]
            lines.extend(blocks_to_md(content, indent + (1 if bt in ("bulleted_list_item","numbered_list_item","to_do","toggle") else 0)))

    return lines

# ── Collect all child_page blocks at any depth ────────────────────────────────
def collect_child_pages(blocks, module_label=""):
    """
    Walk blocks recursively. Returns list of dicts:
      { "id": page_id, "title": title, "module": module_label }
    """
    found = []
    for b in blocks:
        bt = b["type"]
        if bt == "child_page":
            found.append({
                "id":     b["id"],
                "title":  b["child_page"]["title"],
                "module": module_label,
            })
        elif b.get("has_children"):
            # Determine module label from heading_1
            label = module_label
            if bt == "heading_1":
                rt = b["heading_1"]["rich_text"]
                label = rt[0]["plain_text"] if rt else module_label
            children = fetch_all_blocks(b["id"])
            found.extend(collect_child_pages(children, label))
    return found

# ── Sync a single Notion page to a Markdown file ─────────────────────────────
def sync_page(page_id, out_path: Path, depth_label=""):
    page   = fetch_page(page_id)
    title  = page_title(page)
    blocks = fetch_all_blocks(page_id)

    content_blocks = [b for b in blocks if b["type"] != "child_page"]
    md_lines = [
        f'---\ntitle: "{title}"\nlayout: default\n---\n\n',
        f"# {title}\n\n",
    ]
    md_lines.extend(blocks_to_md(content_blocks))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(md_lines), encoding="utf-8")
    print(f"  ✓ {out_path}  ({depth_label})")
    return title

# ── Main ──────────────────────────────────────────────────────────────────────
def clean_docs():
    """Remove all .md files from docs/ (except _config.yml) before each sync
    so renamed/deleted Notion pages don't leave stale files."""
    if not OUTPUT_DIR.exists():
        return
    for f in OUTPUT_DIR.rglob("*.md"):
        f.unlink()
    # Remove empty directories (leave _config.yml untouched)
    for d in sorted(OUTPUT_DIR.rglob("*"), reverse=True):
        if d.is_dir():
            try:
                d.rmdir()  # only removes if empty
            except OSError:
                pass
    print("🧹  Cleared stale docs\n")


def main():
    print(f"🔄  Syncing Notion → {OUTPUT_DIR}/\n")
    clean_docs()
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. Root page
    root_page  = fetch_page(ROOT_PAGE_ID)
    root_title = page_title(root_page)
    root_blocks = fetch_all_blocks(ROOT_PAGE_ID)

    # 2. Collect ALL child pages (nested at any depth)
    print("  Scanning for subpages…")
    child_pages = collect_child_pages(root_blocks)
    print(f"  Found {len(child_pages)} subpages\n")

    # Extract callout text for site description (first callout block only)
    callout_text = ""
    for b in root_blocks:
        if b["type"] == "callout":
            callout_text = rt_to_md(b["callout"]["rich_text"]).strip()
            break

    # Build clean homepage — title + description + module nav only
    from collections import defaultdict, OrderedDict
    by_module = OrderedDict()
    for cp in child_pages:
        mod = cp["module"] or "General"
        by_module.setdefault(mod, []).append(cp)

    root_md = [
        f'---\ntitle: "{root_title}"\nlayout: default\n---\n\n',
        f"# {root_title}\n\n",
    ]
    if callout_text:
        root_md.append(f"> {callout_text}\n\n")

    if by_module:
        root_md.append("---\n\n")
        for module, pages in by_module.items():
            root_md.append(f"## {module}\n\n")
            for cp in pages:
                slug    = slugify(cp["title"])
                mod_slug = slugify(cp["module"]) if cp["module"] else "pages"
                root_md.append(f"- [{cp['title']}](./{mod_slug}/{slug}/)\n")
            root_md.append("\n")

    (OUTPUT_DIR / "index.md").write_text("".join(root_md), encoding="utf-8")
    print(f"  ✓ docs/index.md  (root)")

    # 3. Sync each subpage
    for cp in child_pages:
        mod_slug  = slugify(cp["module"]) if cp["module"] else "pages"
        page_slug = slugify(cp["title"])
        out_path  = OUTPUT_DIR / mod_slug / page_slug / "index.md"
        try:
            sync_page(cp["id"], out_path, depth_label=cp["module"])
            time.sleep(0.2)
        except Exception as e:
            print(f"  ✗ {cp['title']}: {e}")

    total = sum(1 for _ in OUTPUT_DIR.rglob("*.md"))
    print(f"\n✅  Done — {total} Markdown files written.")

if __name__ == "__main__":
    main()
