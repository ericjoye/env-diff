# env-diff — PyPI / Store Listing

## Name

**env-diff**

## Short Description (140 chars)

Compare two .env files and see what changed — added, removed, and changed keys. Ignores order and comments. Zero dependencies.

## Long Description

`env-diff` is a lightweight CLI tool for developers and DevOps engineers who manage multiple `.env` files across environments (local, staging, production, `.env.example`).

**The problem:** Standard `diff` is noisy — line order differs, comments and blank lines create false positives, and you can't quickly tell which keys actually changed vs which are just missing.

**The solution:** `env-diff` parses both files by key name, ignores order and comments, and outputs three clean categories:

- **Red `-`**: Keys only in file1 (removed)
- **Green `+`**: Keys only in file2 (added)
- **Yellow `~`**: Keys in both files with different values (changed)

**Features:**

- Zero dependencies — pure Python 3.11+ stdlib
- Handles `export KEY=VALUE` prefix
- Strips surrounding quotes from values
- Color-coded output (auto-disabled for pipes)
- `--quiet` mode for CI/CD (exit code only)
- Exit code 0 (identical) / 1 (differences found)
- Sorted output for deterministic results

**Install:**

```bash
pip install env-diff
```

**Usage:**

```bash
env-diff .env.example .env
env-diff .env.staging .env.production --quiet
```

## Keywords

env, dotenv, diff, cli, developer-tools, devops, environment-variables, ci-cd, python, pip, terminal, productivity
