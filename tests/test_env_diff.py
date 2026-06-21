"""Tests for env-diff CLI tool."""

import os
import tempfile
import unittest

from env_diff import parse_env, diff_envs


def write_env(content: str) -> str:
    """Write content to a temp file and return its path."""
    fd, path = tempfile.mkstemp(suffix=".env")
    with os.fdopen(fd, "w") as f:
        f.write(content)
    return path


class TestParseEnv(unittest.TestCase):
    """Test the parse_env function."""

    def test_basic_key_value(self):
        path = write_env("FOO=bar\nBAZ=qux\n")
        try:
            result = parse_env(path)
            self.assertEqual(result, {"FOO": "bar", "BAZ": "qux"})
        finally:
            os.unlink(path)

    def test_skips_comments(self):
        path = write_env("# This is a comment\nFOO=bar\n# Another comment\nBAZ=qux\n")
        try:
            result = parse_env(path)
            self.assertEqual(result, {"FOO": "bar", "BAZ": "qux"})
        finally:
            os.unlink(path)

    def test_skips_blank_lines(self):
        path = write_env("\n\nFOO=bar\n\n\nBAZ=qux\n\n")
        try:
            result = parse_env(path)
            self.assertEqual(result, {"FOO": "bar", "BAZ": "qux"})
        finally:
            os.unlink(path)

    def test_strips_quotes(self):
        path = write_env('FOO="hello world"\nBAZ=\'single quoted\'\n')
        try:
            result = parse_env(path)
            self.assertEqual(result, {"FOO": "hello world", "BAZ": "single quoted"})
        finally:
            os.unlink(path)

    def test_handles_export_prefix(self):
        path = write_env("export FOO=bar\nBAZ=qux\n")
        try:
            result = parse_env(path)
            self.assertEqual(result, {"FOO": "bar", "BAZ": "qux"})
        finally:
            os.unlink(path)

    def test_value_with_equals(self):
        path = write_env("DATABASE_URL=postgres://user:pass@host/db?opt=val\n")
        try:
            result = parse_env(path)
            self.assertEqual(result, {"DATABASE_URL": "postgres://user:pass@host/db?opt=val"})
        finally:
            os.unlink(path)


class TestDiffEnvs(unittest.TestCase):
    """Test the diff_envs function."""

    def test_identical_files(self):
        """No differences when both envs have the same keys and values."""
        env1 = {"A": "1", "B": "2"}
        env2 = {"A": "1", "B": "2"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(lines, [])
        self.assertEqual(counts, {"removed": 0, "added": 0, "changed": 0})

    def test_completely_different(self):
        """All keys are either added or removed."""
        env1 = {"A": "1", "B": "2"}
        env2 = {"C": "3", "D": "4"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(counts["removed"], 2)
        self.assertEqual(counts["added"], 2)
        self.assertEqual(counts["changed"], 0)
        self.assertIn("- A  (only in a.env)", lines)
        self.assertIn("- B  (only in a.env)", lines)
        self.assertIn("+ C  (only in b.env)", lines)
        self.assertIn("+ D  (only in b.env)", lines)

    def test_subset(self):
        """file2 is a subset of file1."""
        env1 = {"A": "1", "B": "2", "C": "3"}
        env2 = {"A": "1"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(counts["removed"], 2)
        self.assertEqual(counts["added"], 0)
        self.assertEqual(counts["changed"], 0)

    def test_changed_values(self):
        """Same keys but different values."""
        env1 = {"A": "old", "B": "same"}
        env2 = {"A": "new", "B": "same"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(counts["added"], 0)
        self.assertEqual(counts["changed"], 1)
        self.assertIn("~ A: old -> new", lines)

    def test_mixed_changes(self):
        """Mix of added, removed, and changed keys."""
        env1 = {"KEEP": "same", "REMOVE": "x", "CHANGE": "old"}
        env2 = {"KEEP": "same", "ADD": "y", "CHANGE": "new"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(counts["removed"], 1)
        self.assertEqual(counts["added"], 1)
        self.assertEqual(counts["changed"], 1)

    def test_ignores_order(self):
        """Key order in the dict doesn't matter; output is sorted."""
        env1 = {"Z": "1", "A": "2", "M": "3"}
        env2 = {"A": "2", "M": "3", "Z": "1"}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(lines, [])

    def test_empty_files(self):
        """Both files empty -> no differences."""
        lines, counts = diff_envs({}, {}, "a.env", "b.env", use_color=False)
        self.assertEqual(lines, [])

    def test_one_empty(self):
        """One file empty, other has keys -> all added/removed."""
        env1 = {"A": "1", "B": "2"}
        env2 = {}
        lines, counts = diff_envs(env1, env2, "a.env", "b.env", use_color=False)
        self.assertEqual(counts["removed"], 2)
        self.assertEqual(counts["added"], 0)


class TestEndToEnd(unittest.TestCase):
    """End-to-end tests using the CLI script directly."""

    def test_identical_files_exit_code(self):
        """Exit code 0 for identical files."""
        path1 = write_env("FOO=bar\nBAZ=qux\n")
        path2 = write_env("BAZ=qux\nFOO=bar\n")
        try:
            exit_code = os.system(f"python3 {os.path.dirname(__file__)}/../env-diff --quiet {path1} {path2}")
            self.assertEqual(exit_code, 0)
        finally:
            os.unlink(path1)
            os.unlink(path2)

    def test_different_files_exit_code(self):
        """Exit code 1 for different files."""
        path1 = write_env("FOO=bar\n")
        path2 = write_env("FOO=baz\n")
        try:
            exit_code = os.system(f"python3 {os.path.dirname(__file__)}/../env-diff --quiet {path1} {path2}")
            # os.system returns wait status; on Unix, actual exit code is in high byte
            actual_exit = os.WEXITSTATUS(exit_code) if os.WIFEXITED(exit_code) else exit_code
            self.assertEqual(actual_exit, 1)
        finally:
            os.unlink(path1)
            os.unlink(path2)


if __name__ == "__main__":
    unittest.main()
