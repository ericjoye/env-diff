# LAUNCH-PLAN: env-diff

**Date:** 2026-06-20
**Prepared by:** SELLER
**Product:** env-diff (zero-dependency .env file comparison CLI)

---

## 1. Launch Channels

| Channel | Priority | Rationale |
|---------|----------|-----------|
| PyPI (Python Package Index) | **P0** | Primary distribution. Every Python developer's first stop. |
| GitHub | **P0** | Source code, issues, stars. Social proof for devs. |
| Reddit (r/Python, r/devops, r/programming) | **P1** | High-engagement developer communities. Show-and-tell format. |
| Hacker News (news.ycombinator.com) | **P1** | "Show HN: env-diff" — CLI tools do well here. |
| Twitter/X (developer community) | **P2** | Short demo video/gif of terminal output. |
| Dev.to / Hashnode | **P2** | Blog post: "Stop using diff on .env files" — SEO play. |

---

## 2. First-Week Plan

### Day 1 (Launch Day)
- [ ] Publish to PyPI (`python3 -m build && twine upload dist/*`)
- [ ] Push to GitHub with README, LICENSE, pyproject.toml
- [ ] Post "Show HN" to Hacker News
- [ ] Share on Reddit: r/Python, r/devops

### Day 2-3
- [ ] Monitor GitHub issues and respond
- [ ] Post to Twitter/X with terminal demo GIF
- [ ] Share in relevant Discord/Slack communities (Python, DevOps)

### Day 4-5
- [ ] Write and publish a Dev.to blog post
- [ ] Submit to Python newsletters (Pycoders Weekly, Real Python)

### Day 6-7
- [ ] Review metrics: PyPI downloads, GitHub stars, HN ranking
- [ ] Triage any bug reports from early adopters
- [ ] Plan v1.1 based on feedback (likely `--json` output, `--ignore` flag)

---

## 3. Human Actions Required (EXACT checklist)

These are the steps a human must perform. SELLER cannot do them.

### PyPI Publishing
1. **Create PyPI account** → https://pypi.org/account/register/
2. **Enable 2FA** on PyPI account (required for trusted publishing)
3. **Set up trusted publishing** in PyPI project settings (or use API token)
4. **Build the package:**
   ```bash
   cd ~/businesses/env-diff/
   python3 -m build
   ```
5. **Upload to PyPI:**
   ```bash
   python3 -m twine upload dist/*
   ```
6. **Verify** → https://pypi.org/project/env-diff/

### GitHub Repository
7. **Create GitHub repo** → https://github.com/new (name: `env-diff`)
8. **Push code:**
   ```bash
   cd ~/businesses/env-diff/
   git init
   git remote add origin https://github.com/<username>/env-diff.git
   git add .
   git commit -m "Initial release"
   git push -u origin main
   ```
9. **Add LICENSE** file (MIT) if not already present
10. **Enable Issues** in repo settings

### Hacker News
11. **Create HN account** → https://news.ycombinator.com/login
12. **Post "Show HN"** with title: "env-diff — compare two .env files, see what changed"
13. **Link to GitHub repo**, include example output in post body

### Reddit
14. **Post to r/Python** with title: "env-diff — a zero-dependency CLI to compare .env files"
15. **Post to r/devops** with title: "Stop using diff on .env files — env-diff shows added/removed/changed keys"
16. **Engage with comments** in both threads

### Twitter/X
17. **Record terminal demo** (screen recording → GIF showing `env-diff .env.example .env` output)
18. **Post tweet** with GIF, link to PyPI, hashtags: #python #devops #cli #opensource

---

## 4. Success Metrics (30 days)

| Metric | Target |
|--------|--------|
| PyPI downloads | 500+ |
| GitHub stars | 50+ |
| HN front page | Yes (top 50) |
| Blog post views | 200+ |
| Issues/feedback | At least some signal |

---

## 5. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Low engagement on HN | Post Tuesday-Thursday morning EST for best visibility |
| PyPI name taken | Check availability before launch; fallback: `envdiff-cli` |
| Negative feedback on scope | MVP is intentionally minimal; roadmap is public |
| No Twitter following | Lean on Reddit + HN for initial reach |

---

## 6. Assets Ready

All launch assets are in `~/businesses/env-diff/launch/`:
- `landing.md` — Headline, subhead, 3 benefit bullets, CTA
- `store-listing.md` — PyPI name, short + long description, keywords
- `pricing.md` — Free/open-source model with future monetization path

Human escalation checklist: `~/hermes_ops/escalations/env-diff.md`
