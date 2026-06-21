# BUILD-REPORT: env-diff

## What was built

A zero-dependency CLI tool that compares two `.env` files and shows added, removed, and changed keys — ignoring order and comments.

## File layout

```
env-diff/
├── env-diff                  # Standalone CLI script (executable, ~90 lines)
├── pyproject.toml            # Hatchling build config, PyPI packaging
├── README.md                 # Install instructions, usage examples
├── src/
│   └── env_diff/
│       ├── __init__.py       # Package entry point (same logic as standalone)
│       └── __main__.py       # Enables `python3 -m env_diff`
├── tests/
│   └── test_env_diff.py      # 16 test cases (unittest)
└── BUILD-REPORT.md           # This file
```

## How to run

```bash
# Direct (no install)
python3 env-diff file1.env file2.env

# With colors disabled
python3 env-diff file1.env file2.env --no-color

# Quiet mode (exit code only)
python3 env-diff file1.env file2.env --quiet

# After pip install -e .
env-diff file1.env file2.env
```

## What works

- Compare two `.env` files: shows added (+), removed (-), and changed (~) keys
- Color-coded terminal output (red/green/yellow), auto-disabled for pipes
- Ignores line order — compares by key name
- Skips `#` comments and blank lines
- Handles `export KEY=VALUE` prefix
- Strips matching surrounding quotes from values
- Values containing `=` are preserved correctly
- Exit code 0 if identical, 1 if differences found (--quiet for CI/CD)
- Summary line: "N removed, M added, P changed total"
- 16 tests pass covering: identical files, completely different, subset, changed values, comments/blank lines, export prefix, quoted values, values with =, empty files, exit codes

## Known gaps (out of scope for MVP)

- Multi-line values (e.g., PEM keys with `\n` escapes) — not handled
- `.env` files with no `=` on a non-comment line are silently skipped
- No `--json` or machine-readable output format
- No `--ignore` flag to exclude specific keys
- Not yet published to PyPI (needs `twine upload` with credentials)

## Dependencies

Zero. Uses only `argparse` and `sys` from the Python 3.11+ standard library.
