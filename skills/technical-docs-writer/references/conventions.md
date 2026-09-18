# Documentation Conventions

The style rules that make docs feel like Stripe or Google wrote them.

---

## Core Principle: Lead with the Answer

Every section, every paragraph, every sentence: put the conclusion first. Never make the reader wade through context before getting what they came for.

❌ "In this guide, we will walk through the process of setting up authentication, which is an important first step..."
✅ "Set up authentication in three steps."

❌ "It's worth noting that the API rate limit is 100 requests per minute."
✅ "Rate limit: 100 requests per minute."

---

## Banned Phrases

Remove these on sight. They add zero information:

- "In this document, we will..."
- "It's important to note that..."
- "As you can see above..."
- "Before we get started..."
- "At this point in time..."
- "In order to..."  (use "to")
- "Please note that..."
- "This section will cover..."
- "First and foremost..."
- "Last but not least..."
- "Feel free to..."

---

## Heading Patterns

Match heading style to doc type:

| Doc type | Heading style | Example |
|----------|--------------|---------|
| Guides (task-oriented) | Verb phrase | "Create a task", "Handle approvals" |
| Concepts | Noun phrase | "The approval flow", "Session continuity" |
| Reference | Thing name | "budgetMonthlyCents", "POST /api/issues" |
| Onboarding | Question | "What is an agent?", "Why does delegation happen?" |

Use sentence case for headings, not Title Case (exception: proper nouns).

---

## Code Blocks

Every command goes in a fenced code block with a language tag. Never inline a command.

```bash
pnpm install
pnpm dev
```

Show expected output when it helps the reader verify success:

```bash
$ pnpm dev
Server started at http://localhost:3100
Database: embedded PostgreSQL (auto-started)
```

For multi-step sequences, number the steps and put each command in its own block.

---

## Tables

Use tables whenever you're listing things with 2+ attributes. Tables are scannable; prose lists are not.

❌
"The agent has a name field, a role field, and a title field. The role can be ceo, manager, or ic. The title is a free-form string."

✅
| Field | Type | Values |
|-------|------|--------|
| name | string | Any |
| role | enum | `ceo`, `manager`, `ic` |
| title | string | Any |

---

## Callout Boxes

Use `>` blockquotes for tips, warnings, and notes. Always include the label:

```markdown
> **Note:** This only applies to production deployments.

> **Warning:** This action is irreversible.

> **Tip:** Use `--dry-run` to preview changes before applying them.
```

Use sparingly — if every paragraph has a callout, none of them stand out.

---

## Paragraph Length

One idea per paragraph. Three to four sentences maximum. If you're explaining a complex system, break it into multiple short paragraphs rather than one long one. White space is readable.

---

## Cross-Links

Link generously between related docs. Use relative paths so links work regardless of hosting:

```markdown
See [key concepts](../overview/key-concepts.md) for definitions.
```

Never use absolute URLs for internal docs. Never link to a heading anchor unless you're sure the heading won't change.

---

## Terminology Consistency

Pick one term and stick to it across all docs. Define aliases in `key-concepts.md` if both terms exist in the codebase.

Common pitfalls (illustrative — always resolve in favor of whichever term the code itself uses):
- "issue" vs "task" — pick one (or define both and note they're synonyms)
- "agent" vs "bot" vs "worker" — pick one
- "plugin" vs "extension" vs "add-on" — pick one
- "organization" vs "workspace" vs "team" — pick one

---

## Numbers and Examples

Use real, specific examples. Fake examples that look real are more useful than abstract placeholders.

❌ `"name": "<your-agent-name>"`
✅ `"name": "CTO"`

❌ "Set the API key to your Anthropic API key."
✅ `ANTHROPIC_API_KEY=sk-ant-...`

---

## File Naming

Use lowercase kebab-case for all doc files: `getting-started.md`, `system-design.md`, `add-a-new-agent.md`. Never use spaces or underscores.

---

## The "No Stubs" Rule

Every section you write must be complete. If you don't have enough information to write a section, write what you know and note the gap explicitly in the PR — don't write "TBD" or "coming soon" in the published doc.

Stubs erode trust. A reader who hits "TBD" stops trusting the rest of the docs.

---

## Index File Pattern

Every `docs/index.md` (or root README) follows this structure:

```markdown
# Project Name

One sentence what it is. One sentence why it matters.

---

## Documentation

| Section | What's inside |
|---------|--------------|
| [Overview](overview/what-is-this.md) | Mental model, architecture |
| [Getting Started](getting-started/quickstart.md) | Installation, first task |
| [Concepts](concepts/) | Deep dives per subsystem |
| [Guides](guides/) | Task-oriented how-tos |
| [Reference](reference/) | Complete API and config |
| [Architecture](architecture/) | Design decisions, ADRs |
| [Troubleshooting](troubleshooting/common-issues.md) | Top issues and fixes |
```

No more than two paragraphs of prose before the navigation table. The index is a map, not an essay.
