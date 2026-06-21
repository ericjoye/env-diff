# env-diff — Landing Page

## Headline

**env-diff: See what changed between your .env files.**

## Subhead

A zero-dependency CLI tool that compares two `.env` files and shows added, removed, and changed keys — ignoring order and comments. Stop fighting `diff` noise.

## Benefits

- **Instant clarity** — See at a glance which keys were added, removed, or changed. No more scrolling through unrelated `diff` output.
- **CI/CD ready** — Exit code 0/1 means you can gate deployments on env drift. Zero config, zero dependencies.
- **Developer-first design** — Color-coded output, `--quiet` mode for scripts, handles `export` prefixes and quoted values. Just one small Python file.

## CTA

```bash
pip install env-diff
```

Or try it right now:

```bash
python3 -m pip install env-diff && env-diff .env.example .env
```

[Install from PyPI →](https://pypi.org/project/env-diff/)
