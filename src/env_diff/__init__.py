#!/usr/bin/env python3
"""env-diff: Compare two .env files and show added, removed, and changed keys."""

import argparse
import sys


def parse_env(filepath: str) -> dict:
    """Parse a .env file into a dict of key-value pairs.

    Skips blank lines and comment lines starting with #.
    Handles optional 'export ' prefix.
    Strips matching surrounding quotes from values.
    """
    env = {}
    with open(filepath, "r") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("export "):
                stripped = stripped[len("export ") :]
            if "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            env[key] = value
    return env


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def colorize(text, color, use_color):
    if use_color:
        return f"{color}{text}{RESET}"
    return text


def diff_envs(env1, env2, label1, label2, use_color=True):
    """Compare two env dicts and return (lines, counts).

    lines: formatted diff output lines
    counts: dict with 'removed', 'added', 'changed' counts
    """
    lines = []
    keys1 = set(env1.keys())
    keys2 = set(env2.keys())

    removed_keys = sorted(keys1 - keys2)
    added_keys = sorted(keys2 - keys1)
    common_keys = sorted(keys1 & keys2)

    for key in removed_keys:
        lines.append(colorize(f"- {key}  (only in {label1})", RED, use_color))

    for key in added_keys:
        lines.append(colorize(f"+ {key}  (only in {label2})", GREEN, use_color))

    changed_keys = []
    for key in common_keys:
        if env1[key] != env2[key]:
            changed_keys.append(key)
            lines.append(colorize(f"~ {key}: {env1[key]} -> {env2[key]}", YELLOW, use_color))

    counts = {
        "removed": len(removed_keys),
        "added": len(added_keys),
        "changed": len(changed_keys),
    }
    return lines, counts


def main():
    parser = argparse.ArgumentParser(
        description="Compare two .env files and show added, removed, and changed keys."
    )
    parser.add_argument("file1", help="First .env file")
    parser.add_argument("file2", help="Second .env file")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    parser.add_argument("--quiet", "-q", action="store_true", help="Exit code only, no output")
    args = parser.parse_args()

    use_color = not args.no_color and sys.stdout.isatty()
    env1 = parse_env(args.file1)
    env2 = parse_env(args.file2)
    lines, counts = diff_envs(env1, env2, args.file1, args.file2, use_color)

    if not args.quiet and lines:
        for line in lines:
            print(line)

    if not args.quiet:
        if lines:
            parts = []
            if counts["removed"]:
                parts.append(f"{counts['removed']} removed")
            if counts["added"]:
                parts.append(f"{counts['added']} added")
            if counts["changed"]:
                parts.append(f"{counts['changed']} changed")
            print(f"\n{', '.join(parts)} total")
        else:
            print("No differences found.")

    return 1 if lines else 0


if __name__ == "__main__":
    sys.exit(main())
