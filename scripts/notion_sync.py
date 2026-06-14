#!/usr/bin/env python3
"""
Notion → GitHub Pages sync script.

Structure:
  Home page  (NOTION_PAGE_ID)
  ├── Course 1: Clinical Research Foundations  (NOTION_COURSE_1_ID)
  │   ├── Module 1  (toggle heading)
  │   │   ├── Subpage …
  │   │   └── Subpage …
  │   └── Module N …
  └── Course 2: ICH E6(R3) Principles  (NOTION_COURSE_2_ID)
      └── …

Output under docs/:
  docs/index.md                              ← home page
  docs/clinical-research-foundations/index.md        ← course 1 index (layout: page)
  docs/clinical-research-foundations/<module>/<page>/index.md
  docs/ich-e6-r3-principles/index.md                 ← course 2 index (layout: page)
  docs/ich-e6-r3-principles/<module>/<page>/index.md
"""

import os, re, time, requests
from pathlib import Path
from collections import OrderedDict

# ── Config ───────────────────────────────────────────────────────────────────
NOTION_TOKEN  = os.environ["NOTION_TOKEN"]
HOME_PAGE_ID  = os.environ["NOTION_PAGE_ID"]
COURSE_IDS    = [
    os.environ["NOTION_COURSE_1_ID"],
    os.environ["NOTION_COURSE_2_ID"],
]
OUTPUT_DIR = Path("docs")
API        = "https://api.notion.com/v1"
HEADERS    = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
}

# ── API helpers ───────────────────────────────────────────────────────────────
def api_get(path, **params):
    r = requests.get(f"{API}{path}", headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

def fetch_all_blocks(block_id):
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
        if a.get("code"):          s = f"`{s}`"
        if a.get("bold"):          s = f"**{s}**"
        if a.get("italic"):        s = f"*{s}*"
        if a.get("strikethrough"): s = f"~~{s}~~"
        href = t.get("href")
        if href:                   s = f"[{s}]({href})"
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

# ── Table helpers ─────────────────────────────────────────────────────────────
def is_separator_row(row_text):
    inner = row_text.strip().strip("|")
    cells = inner.split("|")
    return all(re.match(r"^[\s\-–—]+$", c) for c in cells)

def normalise_table_rows(rows):
    result, header_done = [], False
    for row in rows:
        if is_separator_row(row):
            if not header_done:
                n = len(row.strip().strip("|").split("|"))
                result.append("| " + " | ".join("---" for _ in range(n)) + " |")
                header_done = True
        else:
            result.append(row.strip())
            if not header_done:
                n = len(row.strip().strip("|").split("|"))
                result.append("| " + " | ".join("---" for _ in range(n)) + " |")
                header_done = True
    return result

# ── Block → Markdown ──────────────────────────────────────────────────────────
def blocks_to_md(blocks, indent=0):
    lines = []
    pad = "  " * indent
    i = 0
    while i < len(blocks):
        b  = blocks[i]
        bt = b["type"]

        if bt == "child_page":
            i += 1; continue

        elif bt == "paragraph":
            text     = rt_to_md(b["paragraph"]["rich_text"])
            stripped = text.strip()
            if stripped.startswith("|"):
                rows = [stripped]
                while i + 1 < len(blocks) and blocks[i+1]["type"] == "paragraph":
                    nxt = rt_to_md(blocks[i+1]["paragraph"]["rich_text"]).strip()
                    if nxt.startswith("|"):
                        rows.append(nxt); i += 1
                    else:
                        break
                lines.append("\n" + "\n".join(normalise_table_rows(rows)) + "\n\n")
                i += 1; continue
            lines.append(f"{pad}{text}\n" if stripped else "\n")

        elif bt == "heading_1":
            lines.append(f"\n# {rt_to_md(b['heading_1']['rich_text'])}\n\n")
        elif bt == "heading_2":
            lines.append(f"\n## {rt_to_md(b['heading_2']['rich_text'])}\n\n")
        elif bt == "heading_3":
            lines.append(f"\n### {rt_to_md(b['heading_3']['rich_text'])}\n\n")

        elif bt == "bulleted_list_item":
            lines.append(f"{pad}- {rt_to_md(b['bulleted_list_item']['rich_text'])}\n")
        elif bt == "numbered_list_item":
            lines.append(f"{pad}1. {rt_to_md(b['numbered_list_item']['rich_text'])}\n")
        elif bt == "to_do":
            chk = "x" if b["to_do"].get("checked") else " "
            lines.append(f"{pad}- [{chk}] {rt_to_md(b['to_do']['rich_text'])}\n")

        elif bt == "toggle":
            lines.append(f"\n**{rt_to_md(b['toggle']['rich_text'])}**\n\n")

        elif bt == "callout":
            icon  = b["callout"].get("icon") or {}
            emoji = icon.get("emoji", "💡") if icon.get("type") == "emoji" else "💡"
            lines.append(f"> {emoji} {rt_to_md(b['callout']['rich_text'])}\n")

        elif bt == "quote":
            lines.append(f"> {rt_to_md(b['quote']['rich_text'])}\n")

        elif bt == "code":
            lang = b["code"].get("language", "")
            lines.append(f"```{lang}\n{rt_to_md(b['code']['rich_text'])}\n```\n")

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
                lines.append("\n")
                for ri, row in enumerate(rows):
                    cells = row.get("table_row", {}).get("cells", [])
                    lines.append("| " + " | ".join(rt_to_md(c) for c in cells) + " |\n")
                    if ri == 0:
                        lines.append("| " + " | ".join("---" for _ in cells) + " |\n")
                lines.append("\n")
                i += 1; continue

        if b.get("has_children") and bt not in ("child_page", "table"):
            child_blocks = fetch_all_blocks(b["id"])
            content = [x for x in child_blocks if x["type"] != "child_page"]
            extra = 1 if bt in ("bulleted_list_item", "numbered_list_item", "to_do", "toggle") else 0
            lines.extend(blocks_to_md(content, indent + extra))

        i += 1
    return lines

# ── Collect child_pages nested at any depth ───────────────────────────────────
def collect_child_pages(blocks, module_label=""):
    found = []
    for b in blocks:
        bt = b["type"]
        if bt == "child_page":
            found.append({"id": b["id"], "title": b["child_page"]["title"], "module": module_label})
        elif b.get("has_children"):
            label = module_label
            if bt == "heading_1":
                rt = b["heading_1"]["rich_text"]
                label = rt[0]["plain_text"] if rt else module_label
            children = fetch_all_blocks(b["id"])
            found.extend(collect_child_pages(children, label))
    return found

# ── Sync a single Notion page → Markdown file ────────────────────────────────
def sync_page(page_id, out_path: Path, label=""):
    page   = fetch_page(page_id)
    title  = page_title(page)
    blocks = fetch_all_blocks(page_id)
    content_blocks = [b for b in blocks if b["type"] != "child_page"]
    md = [f'---\ntitle: "{title}"\nlayout: default\n---\n\n', f"# {title}\n\n"]
    md.extend(blocks_to_md(content_blocks))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(md), encoding="utf-8")
    print(f"  ✓ {out_path}  {label}")
    return title

# ── Sync one course ───────────────────────────────────────────────────────────
def sync_course(course_id, course_dir: Path, nav_order: int):
    page       = fetch_page(course_id)
    title      = page_title(page)
    blocks     = fetch_all_blocks(course_id)
    child_pages = collect_child_pages(blocks)

    # Group by module
    by_module = OrderedDict()
    for cp in child_pages:
        mod = cp["module"] or "General"
        by_module.setdefault(mod, []).append(cp)

    # Course index page (layout: page → appears in sidebar)
    course_md = [
        f'---\ntitle: "{title}"\nlayout: page\nnav_order: {nav_order}\n---\n\n',
        f"# {title}\n\n",
    ]
    content_blocks = [b for b in blocks if b["type"] != "child_page"]
    callout_text = ""
    for b in blocks:
        if b["type"] == "callout":
            callout_text = rt_to_md(b["callout"]["rich_text"]).strip()
            break
    if callout_text:
        course_md.append(f"> {callout_text}\n\n")

    if by_module:
        course_md.append("---\n\n")
        for module, pages in by_module.items():
            course_md.append(f"## {module}\n\n")
            for cp in pages:
                pg_slug = slugify(cp["title"])
                mod_slug = slugify(cp["module"]) if cp["module"] else "general"
                course_md.append(f"- [{cp['title']}](./{mod_slug}/{pg_slug}/)\n")
            course_md.append("\n")

    course_dir.mkdir(parents=True, exist_ok=True)
    (course_dir / "index.md").write_text("".join(course_md), encoding="utf-8")
    print(f"  ✓ {course_dir}/index.md  (course index)")

    # Module index pages
    for order, (module, pages) in enumerate(by_module.items(), start=1):
        mod_slug = slugify(module)
        mod_dir  = course_dir / mod_slug
        mod_dir.mkdir(parents=True, exist_ok=True)
        mod_md = [f'---\ntitle: "{module}"\nlayout: default\n---\n\n', f"# {module}\n\n"]
        for cp in pages:
            mod_md.append(f"- [{cp['title']}](./{slugify(cp['title'])}/)\n")
        (mod_dir / "index.md").write_text("".join(mod_md), encoding="utf-8")
        print(f"  ✓ {mod_dir}/index.md")

    # Subpages
    for cp in child_pages:
        mod_slug  = slugify(cp["module"]) if cp["module"] else "general"
        page_slug = slugify(cp["title"])
        out_path  = course_dir / mod_slug / page_slug / "index.md"
        try:
            sync_page(cp["id"], out_path, label=cp["module"])
            time.sleep(0.2)
        except Exception as e:
            print(f"  ✗ {cp['title']}: {e}")

    return title

# ── Clean stale docs ──────────────────────────────────────────────────────────
def clean_docs():
    if not OUTPUT_DIR.exists():
        return
    for f in OUTPUT_DIR.rglob("*.md"):
        f.unlink()
    for d in sorted(OUTPUT_DIR.rglob("*"), reverse=True):
        if d.is_dir():
            try: d.rmdir()
            except OSError: pass
    print("🧹  Cleared stale docs\n")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"🔄  Syncing Notion → {OUTPUT_DIR}/\n")
    clean_docs()
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. Home page
    home_page   = fetch_page(HOME_PAGE_ID)
    home_title  = page_title(home_page)
    home_blocks = fetch_all_blocks(HOME_PAGE_ID)

    callout_text = ""
    for b in home_blocks:
        if b["type"] == "callout":
            callout_text = rt_to_md(b["callout"]["rich_text"]).strip()
            break

    # 2. Sync each course
    course_titles = {}
    course_slugs  = {}
    for i, cid in enumerate(COURSE_IDS, start=1):
        page     = fetch_page(cid)
        title    = page_title(page)
        slug     = slugify(title)
        course_dir = OUTPUT_DIR / slug
        print(f"\n📚  Course {i}: {title}")
        sync_course(cid, course_dir, nav_order=i)
        course_titles[cid] = title
        course_slugs[cid]  = slug

    # 3. Home index
    home_md = [
        f'---\ntitle: "{home_title}"\nlayout: default\n---\n\n',
        f"# {home_title}\n\n",
    ]
    if callout_text:
        home_md.append(f"> {callout_text}\n\n")
    home_md.append("---\n\n## Courses\n\n")
    for cid in COURSE_IDS:
        slug  = course_slugs[cid]
        title = course_titles[cid]
        home_md.append(f"- [{title}](./{slug}/)\n")
    home_md.append("\n")

    (OUTPUT_DIR / "index.md").write_text("".join(home_md), encoding="utf-8")
    print(f"\n  ✓ docs/index.md  (home)")

    total = sum(1 for _ in OUTPUT_DIR.rglob("*.md"))
    print(f"\n✅  Done — {total} Markdown files written.")

if __name__ == "__main__":
    main()
