# env-diff

## One-liner
A zero-dependency CLI tool that compares two `.env` files and shows added, removed, and changed keys — ignoring order and comments.

## Target user
Developers and DevOps engineers who manage multiple `.env` files (local, staging, production, `.env.example`) and need a quick way to spot differences without the noise of line-by-line `diff`.

## Problem
Comparing `.env` files with `diff` is painful: line order differs, comments and blank lines create false positives, and you can't quickly see "which keys changed" vs "which keys are missing." Existing solutions are either generic `diff` (noisy) or full env-management tools (heavy, overkill). There's no simple, dedicated tool for this.

## MVP scope (4 features)
1. **Compare two `.env` files**: `env-diff file1.env file2.env` — outputs keys only in file1 (removed), only in file2 (added), and keys in both with different values (changed).
2. **Clean output**: Color-coded terminal output (red for removed, green for added, yellow for changed) with one change per line. Changed lines show `KEY: old_value -> new_value`.
3. **Ignore order and comments**: Parses `.env` properly — skips `#` comments and blank lines, compares by key name regardless of file order.
4. **Exit code**: Returns `0` if files are identical, `1` if differences found — usable in CI/CD pipelines.

## Tech approach
- **Language**: Python 3.11+ (available on all dev machines)
- **Dependencies**: Zero external packages. Uses only `sys`, `os`, `re`, `argparse` from stdlib.
- **Packaging**: Single-file script (`env-diff`), installable via `pip install -e .` or `uv tool install`. PyPI package for distribution.
- **Size**: ~60 lines of Python. Trivial to build and test.

## Risks
1. **Existing alternatives**: `diff`, `comm`, and `envdir` exist but don't solve the "compare by key, ignore order" problem cleanly. Mitigation: position as the simplest possible tool — one command, zero config.
2. **Edge cases in .env parsing**: Multi-line values, quoted values, `export` prefixes. Mitigation: MVP handles the common case (simple `KEY=VALUE` lines). Advanced parsing can come later.
3. **Monetization**: This is a free developer tool. Monetization path is indirect — portfolio piece, leads to paid tooling, or sponsor via GitHub Sponsors.

## Definition of done for the MVP
- `env-diff a.env b.env` runs and produces correct output for all three categories (added/removed/changed)
- Handles comments (`#`) and blank lines correctly
- Exit code 0/1 works for CI usage
- Published to PyPI as `env-diff`
- A README with install instructions and usage examples
- At least 5 test cases covering: identical files, completely different files, subset, changed values, comments/blank lines
