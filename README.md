# GCP ICH E6(R3) Training Site

Automatically synced from Notion → GitHub Pages.

**Live site:** https://winkhaing.github.io/GCP_ICH_E6_R3

## How it works

1. Content is authored in Notion
2. GitHub Actions runs every hour (or on demand)
3. `scripts/notion_sync.py` fetches the Notion page + all subpages recursively
4. Markdown files are written to `docs/`
5. GitHub Pages (Jekyll) renders the site

## Manual sync

Go to **Actions → Sync Notion → GitHub Pages → Run workflow**.

## Secrets required

| Secret | Value |
|---|---|
| `NOTION_TOKEN` | Notion integration token (`ntn_...`) |
| `NOTION_PAGE_ID` | Root Notion page ID (32 chars) |
