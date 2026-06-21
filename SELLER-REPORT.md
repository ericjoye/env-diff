# SELLER-REPORT: PyPI / GitHub Publish Plan — env-diff

**Product:** env-diff — Compare two .env files, see what changed
**Slug:** env-diff
**Date:** 2026-06-20
**QA Status:** PASS (16/16 tests)

---

## Publishing Summary

- **PyPI Package Name:** `env-diff` (v0.1.0)
- **GitHub Repo:** `github.com/ericjoye/env-diff`
- **Build System:** hatchling (pyproject.toml ready)
- **Entry Point:** `env_diff:main`
- **Blockers:** None — fully ready to publish

---

## PyPI Publishing Steps

1. Ensure PyPI account exists (https://pypi.org/account/register/)
2. Ensure API token is configured in `~/.pypirc` or env vars
3. Build:
   ```
   cd ~/businesses/env-diff/
   python3 -m build
   ```
4. Upload:
   ```
   python3 -m twine upload dist/*
   ```
5. Verify: https://pypi.org/project/env-diff/

---

## GitHub Repository Steps

1. Create public repo at https://github.com/new — name: `env-diff`
2. Push code:
   ```
   cd ~/businesses/env-diff/
   git init
   git add .
   git commit -m "Initial release"
   git remote add origin git@github.com:ericjoye/env-diff.git
   git branch -M main
   git push -u origin main
   ```
3. Add MIT license file
4. Enable Issues in repo settings

---

## Marketing Launch

- **Hacker News:** "Show HN: env-diff — compare two .env files, see what changed"
- **Reddit:** r/Python, r/devops, r/programming
- **Twitter:** pip install env-diff + demo GIF

---

## Success Metrics (30 days)

- PyPI downloads: 500+
- GitHub stars: 50+
- HN upvotes: 20+
