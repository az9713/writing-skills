---
name: technical-docs-writer
description: >
  Write comprehensive, production-quality technical documentation for software projects,
  following Google/Stripe documentation conventions. Use this skill whenever a user wants
  to document a codebase, create docs from scratch, eliminate doc debt, write an onboarding
  guide, create API or architecture reference docs, audit or improve existing docs, or says
  anything like: "document this", "write docs", "create documentation", "no doc debt",
  "getting started guide", "README is outdated", "new developers need to understand this",
  "360-degree view of the codebase", "onboarding for new devs", or "technical docs".
  Invoke this skill even if the user only mentions one doc type — the skill will determine
  the right full set for the project.
---

# Technical Documentation Writer

You are writing production-quality documentation for a technical project. Your goal is docs that eliminate doc debt permanently: a new engineer should be able to understand the project from scratch, and an experienced engineer should be able to find any answer without asking a teammate.

The conventions and templates in this skill are derived from how world-class engineering teams (Google, Stripe, AWS, Vercel) structure their docs as of 2026.

---

## Phase 1: Audit

Before writing anything, understand what you're documenting.

**Read the codebase:**
- Root README and any existing docs (note gaps and staleness)
- Top-level directory structure
- Key source files: entry points, main abstractions, config schemas
- Existing architecture notes, CHANGELOG, CONTRIBUTING

**Identify:**
1. **Project type** — Library/SDK, Platform/Product, CLI tool, API service, or Multi-component system (each gets a different IA — see `references/ia-patterns.md`)
2. **Primary audiences** — new developers onboarding, experienced developers building on top, operators deploying it, external API consumers, **and end users** (people who use the product's output or UI without touching code — if they exist, they get their own `user-guide/` section; see `references/ia-patterns.md`)
3. **What already exists** — don't recreate good existing docs; link to them or extend them
4. **What's missing** — the gaps are your todo list

If the user gave you specific docs to write, still do a quick audit to ensure your output integrates with what exists.

---

## Phase 2: Plan the Information Architecture

Choose the right doc structure for the project type (see `references/ia-patterns.md` for full templates). The standard full set for a platform or multi-component system is:

```
docs/
├── index.md                        ← navigation hub, entry point
├── overview/
│   ├── what-is-this.md             ← concept: what it is and why it exists
│   └── key-concepts.md             ← glossary of every important term
├── getting-started/
│   ├── prerequisites.md            ← exact deps with verify commands
│   ├── quickstart.md               ← working in <15 minutes
│   └── onboarding.md               ← zero-to-hero for newcomers
├── concepts/                       ← deep dives into each major subsystem
├── guides/                         ← task-oriented how-tos
├── reference/                      ← complete API/config/schema reference
├── architecture/
│   ├── system-design.md
│   └── adr/                        ← Architecture Decision Records
├── user-guide/                     ← end-user docs (only if the project has non-developer users)
│   ├── using-<the-thing>.md
│   └── faq.md
├── history/
│   └── development-journey.md      ← optional: the build chronicle (see doc-types.md)
└── troubleshooting/
    └── common-issues.md
```

For smaller projects, use a subset. For CLI tools or libraries, see the patterns in `references/ia-patterns.md`. Always include: index, quickstart, and at least one concepts doc.

Present the planned file list to the user before writing if there are more than 10 files, or if the project scope is ambiguous. Otherwise proceed directly.

---

## Phase 3: Write

Write all docs in one pass using the builder pattern: write every planned file completely before stopping. Follow the conventions in `references/conventions.md`.

**The most important rule:** Every file must be complete and self-contained. No stubs, no "TBD", no "see X for details" without actually explaining it first. A reader should be able to read any single doc and get real value from it.

**Per doc-type guidance** — read `references/doc-types.md` before writing each type for the first time. Key reminders:

- **index.md**: Lead with a 2-sentence description of the project, then a navigation table. No prose beyond that.
- **what-is-this.md**: Start with a one-sentence answer. Then mental model, then architecture overview. End with a "how does it all fit together" section.
- **key-concepts.md**: Every term that appears in other docs without explanation belongs here. Format: `**Term** — definition. Example: ...`
- **quickstart.md**: Numbered steps. Every command in a fenced code block. Show expected output. Should work end-to-end without reading anything else.
- **onboarding.md**: Assumes zero familiarity. Use analogies. Build the mental model before commands. End with a narrative walkthrough of a realistic end-to-end scenario.
- **concepts/**: One file per major subsystem. Structure: what it is → how it works → data flows → key decisions made.
- **guides/**: Task-oriented. Title is a verb phrase. Structured as: goal → prerequisites → numbered steps → verification → troubleshooting for this task.
- **reference/**: Complete. Every field, every option, every error code. Tables preferred over prose.
- **architecture/**: Cover the why (decisions), not just the what (diagrams). Include ADRs for non-obvious choices.
- **troubleshooting/**: Top N issues actually encountered. Each: symptom → cause → fix. Keep fixes actionable (exact commands).
- **user-guide/**: For non-developer users. Task-oriented, zero code in the main flow, screenshots/stills where they carry meaning. Plain language: no repo paths, no CLI flags unless the user genuinely types them.
- **history/development-journey.md**: The build chronicle. If one already exists (DEVELOPMENT.md, devlog), link it from index.md — never recreate it.

---

## Phase 4: Validate

After writing, scan the full output for:

- **Broken cross-links** — every `../concepts/foo.md` reference must point to a file you actually created
- **Terminology consistency** — if you call something a "task" in one doc and "issue" in another, pick one and use it everywhere (or define both in key-concepts.md)
- **Orphaned files** — every file must be linked from index.md or a parent doc
- **Stub detection** — grep for "TBD", "TODO", "coming soon", "see X for details" — replace all with actual content

---

## Phase 5: Keep the docs true (maintenance)

"No doc debt permanently" requires a mechanism, not just a complete snapshot. Close every doc set with these, adapted to the project:

- **Same-change rule** — state in CONTRIBUTING (or index.md for small projects) that docs change in the same commit/PR as the behavior they describe.
- **Ownership line** — each top-level section names the file(s) it must track (e.g., "this reference tracks `build.sh` — update both together").
- **Staleness markers** — date-stamp docs that describe external services, prices, or UIs; these rot fastest.
- **Re-validate on edit** — rerun the Phase 4 checks (links, terminology, stubs) after any doc change, not just the first write.

---

## Installing the docs

By default, write docs to `docs/` at the project root. If a `docs/` directory already exists with real content, preserve it and integrate your new files, noting any conflicts.

After writing, report:
```
✓ Created N files in docs/
✓ Cross-links verified
✓ No stubs detected

Entry point: docs/index.md
Onboarding: docs/getting-started/onboarding.md
```

---

## Reference files

Read these when you need them — don't read all upfront:

- `references/conventions.md` — Full style guide: banned phrases, formatting rules, heading patterns, callout syntax. Read before writing your first file.
- `references/ia-patterns.md` — IA templates for: Library/SDK, CLI tool, API service, Platform/Product, Multi-component system. Read during Phase 2 if your project type needs a non-standard structure.
- `references/doc-types.md` — Detailed guidance for each doc type. Read when writing a type you haven't written yet in this session.


## Common mistakes

- **Leaving a stub in a doc** — "TBD", "TODO", "coming soon", or "see X for details" without actually explaining it first; every file must be complete and self-contained.
- **Recreating an existing build chronicle** — if a DEVELOPMENT.md or devlog already exists, link it from index.md instead of rewriting `history/development-journey.md`.
- **Overwriting an existing docs/ directory** — if it already has real content, preserve it and integrate new files, noting any conflicts.
- **Leaving broken cross-links or orphaned files** — every `../concepts/foo.md` reference must point to a file you actually created, and every file must be linked from index.md or a parent doc.
- **Using inconsistent terminology across docs** — e.g. "task" in one doc and "issue" in another; pick one and use it everywhere, or define both in key-concepts.md.

## Other files in this skill

- `evals/evals.json` — eval data, read it when the task needs it.
