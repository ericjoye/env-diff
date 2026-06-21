# env-diff — PyPI Store Listing

## Package Name

`env-diff`

## Short Description

Compare two .env files and see what changed — ignoring order and comments.

## Long Description

env-diff is a zero-dependency Python CLI tool that compares two `.env` files and shows you exactly what changed — added keys, removed keys, and changed values — while ignoring line order and comments. Perfect for CI/CD pipelines, code reviews, and environment audits.

**WHY ENV-DIFF?**

When you have `.env.example`, `.env.local`, `.env.production`, and `.env.ci`, keeping them in sync is painful. A missing key in production, an extra key in local that shouldn't be there, a database URL that points to the wrong host — these bugs waste hours. env-diff makes it instant: run a diff, see what changed, fix it.

**COLOR-CODED OUTPUT**
Every change is clearly marked: red for removed keys (only in file1), green for added keys (only in file2), and yellow for changed values (in both files but different). A summary line tells you exactly how many keys were added, removed, or changed. Use `--no-color` for piping to other tools, or `--quiet` for CI/CD scripts that just need an exit code (0 = identical, 1 = differences found).

**SMART PARSING**
env-diff handles `export KEY=VALUE` prefixes, strips surrounding quotes from values, skips `#` comments and blank lines, and compares by key name regardless of line order. It's zero-dependency Python 3.11+ stdlib — no pip install needed at runtime.

## Key Features

- **Key-based comparison** — ignores line order, compares by key name
- **Color-coded output** — red (removed), green (added), yellow (changed)
- **CI/CD friendly** — `--quiet` mode with exit code 0/1
- **Smart parsing** — handles `export` prefix, strips quotes, skips comments
- **Zero dependencies** — pure Python 3.11+ stdlib
- **Cross-platform** — Linux, macOS, Windows/WSL
- **Pipe-friendly** — `--no-color` for scripting workflows

## Installation

```bash
pip install env-diff
```

Or run directly:

```bash
python3 env-diff file1.env file2.env
```

## Requirements

- **Python:** 3.11+
- **No external dependencies** — stdlib only

## Support

- **Contact:** eric@ericjoye.com
- **GitHub:** https://github.com/ericjoye/env-diff
- **Issues:** https://github.com/ericjoye/env-diff/issues
- **License:** MIT

## Keywords

env, dotenv, diff, compare, cli, developer-tools, devops, command-line, environment-variables, config, ci-cd, python, zero-dependencies
