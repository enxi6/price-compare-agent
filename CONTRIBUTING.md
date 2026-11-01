# Contributing Guide

## Three hard lines first

1. **Rankings never accept paid influence**: any PR that ties a ranking factor to merchant payment
   is rejected outright.
2. **A new merchant adapter must come with two things**: a statement of data-source legitimacy
   (official API / feed / catalog, or public structured data), and at least 3 eval cases
   (same-product identification + total-price composition).
3. **Prices must carry source and time**: a quote without a source link and fetch time is not merged.

## How to participate

- File an issue: start with the product category + the specific problem (wrong match? stale price?
  merchant blocking?), attaching the product link and the expected result.
- Submit a PR: small steps, one thing per PR; a PR that changes ranking logic must also run the
  eval set and post the results.
- Discuss trade-offs: append a new entry in `DECISIONS.md`, stating clearly "decision / why /
  why the alternatives were not chosen".

## Local development

```bash
cd price-compare-agent
python3 -m price_agent.cli compare "Sony WH-1000XM5"
python3 -m unittest discover -s tests -v
```

No API key is needed to run the skeleton (mock merchant data).

## Releasing

Every feature update leaves a record on GitHub. The process is:

- **Commit messages follow Conventional Commits**: `feat:`, `fix:`, `docs:`,
  `chore:`, `refactor:`, `test:` (e.g. `feat: add price-drop alerts`).
  The type drives the changelog section and the release notes.
- **CHANGELOG.md is updated in the same change**: every user-visible
  change gets an entry under `[Unreleased]` first. A change without a
  changelog entry is incomplete, including corrections — a corrected
  claim is recorded as a new entry, never by silently rewriting history.
- **Cutting a release**: move the `[Unreleased]` entries into a new
  versioned section with the release date, commit, tag `vX.Y.Z`
  (Semantic Versioning; `0.x` while pre-stable), push the tag, and
  create a GitHub Release from the tag with that changelog section as
  the notes. The release notes list known gaps alongside the wins.
- **No force-pushes to the main branch.** History is corrected by new
  commits and new releases, not by rewriting published commits.
