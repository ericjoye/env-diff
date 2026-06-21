# env-diff

Compare two `.env` files and see what changed — ignoring order and comments.

## Install

```bash
# From source
pip install -e .

# Or run directly
python3 env-diff file1.env file2.env
```

## Usage

```bash
# Basic comparison
env-diff .env.example .env

# Disable colors (for piping)
env-diff .env.example .env --no-color

# Quiet mode (exit code only, for CI/CD)
env-diff .env.example .env --quiet
echo $?   # 0 = identical, 1 = differences found
```

## Output

- **Red `-`**: Keys only in file1 (removed)
- **Green `+`**: Keys only in file2 (added)
- **Yellow `~`**: Keys in both files with different values (changed)

Example:
```
- REDIS_URL  (only in .env.example)
+ DEBUG  (only in .env)
~ DATABASE_URL: postgres://prod/db -> postgres://localhost/db

1 removed, 1 added, 1 changed total
```

## Features

- Compares by key name, ignores line order
- Skips `#` comments and blank lines
- Handles `export KEY=VALUE` prefix
- Strips surrounding quotes from values
- Color-coded output (disable with `--no-color`)
- Exit code 0/1 for CI/CD pipelines
- Zero dependencies — pure Python 3.11+ stdlib

## Running tests

```bash
PYTHONPATH=src python3 -m unittest tests.test_env_diff -v
```

## License

MIT
