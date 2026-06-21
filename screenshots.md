# Screenshots — env-diff

**Product:** env-diff — Compare two `.env` files and see what changed, ignoring order and comments.

**Type:** CLI Tool (Python)

---

## Screenshot 1: Main Interface — Basic Comparison

**What to capture:** A terminal showing the basic `env-diff` command comparing two `.env` files with color-coded output showing added, removed, and changed keys.

**Terminal Output Mockup:**

```
$ env-diff .env.example .env

──────────────────────────────────────────────
  env-diff: .env.example → .env
──────────────────────────────────────────────

  - REDIS_URL=redis://localhost:6379    (only in .env.example)
  - CACHE_TTL=300                       (only in .env.example)

  + DEBUG=true                          (only in .env)
  + LOG_LEVEL=debug                     (only in .env)

  ~ DATABASE_URL:
      .env.example:  postgres://prod-server:5432/myapp
      .env:          postgres://localhost:5432/myapp

  ~ API_KEY:
      .env.example:  sk-prod-xxxxxxxxxxxx
      .env:          sk-test-yyyyyyyyyyyy

──────────────────────────────────────────────
  2 removed, 2 added, 2 changed  (6 total)
──────────────────────────────────────────────
```

---

## Screenshot 2: Key Feature — CI/CD Quiet Mode

**What to capture:** Terminal showing the `--quiet` mode used in CI/CD pipelines, with exit code output.

**Terminal Output Mockup:**

```
$ env-diff .env.example .env --quiet
$ echo $?
1

$ env-diff .env.example .env.example --quiet
$ echo $?
0

# In a CI/CD script:
$ env-diff .env.example .env --quiet
if [ $? -ne 0 ]; then
  echo "⚠️  .env files differ! Review changes before deploying."
  exit 1
fi
✓ .env files match — safe to deploy
```

---

## Screenshot 3: No-Color Mode for Piping

**What to capture:** Terminal showing the `--no-color` flag for piping output to other tools.

**Terminal Output Mockup:**

```
$ env-diff .env.example .env --no-color
- REDIS_URL=redis://localhost:6379    (only in .env.example)
+ DEBUG=true                          (only in .env)
~ DATABASE_URL: postgres://prod-server:5432/myapp -> postgres://localhost:5432/myapp

1 removed, 1 added, 1 changed total

$ env-diff .env.example .env --no-color | grep "^\+" | wc -l
2

$ env-diff .env.example .env --no-color | grep "^-" > removed_keys.txt
$ cat removed_keys.txt
- REDIS_URL=redis://localhost:6379    (only in .env.example)
- CACHE_TTL=300                       (only in .env.example)
```

---

## Screenshot 4: Results — Complex Comparison

**What to capture:** Terminal showing a more complex comparison with many changes, demonstrating the tool's ability to handle real-world `.env` files.

**Terminal Output Mockup:**

```
$ env-diff .env.production .env.staging

──────────────────────────────────────────────
  env-diff: .env.production → .env.staging
──────────────────────────────────────────────

  - SENTRY_DSN=https://abc@sentry.io/123  (only in .env.production)
  - STRIPE_LIVE_KEY=sk_live_xxx           (only in .env.production)
  - CDN_URL=https://cdn.example.com       (only in .env.production)

  + STRIPE_TEST_KEY=sk_test_yyy           (only in .env.staging)
  + DEBUG=true                            (only in .env.staging)
  + MOCK_PAYMENTS=true                    (only in .env.staging)

  ~ DATABASE_URL:
      .env.production:  postgres://prod-db.internal:5432/app
      .env.staging:      postgres://staging-db.internal:5432/app

  ~ REDIS_URL:
      .env.production:  redis://prod-redis.internal:6379
      .env.staging:      redis://staging-redis.internal:6379

  ~ API_BASE_URL:
      .env.production:  https://api.example.com/v1
      .env.staging:      https://staging-api.example.com/v1

  ~ LOG_LEVEL:
      .env.production:  warn
      .env.staging:      debug

──────────────────────────────────────────────
  3 removed, 3 added, 4 changed  (10 total)
──────────────────────────────────────────────
```

---

## Notes for Actual Screenshots

1. **Use a dark terminal theme** with syntax highlighting for colors (red/green/yellow)
2. **Show the color coding clearly:** Red for removed, green for added, yellow for changed
3. **Use realistic `.env` values:** database URLs, API keys, service URLs
4. **CI/CD mode** is a key differentiator — show the exit code usage
5. **Pipe mode** demonstrates scripting integration
6. **Font:** Monospace font (JetBrains Mono, Fira Code)
7. **Terminal width:** ~80 characters for clean output
8. **Show the summary line** at the bottom — it's the most important takeaway
