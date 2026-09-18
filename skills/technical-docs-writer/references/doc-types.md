# Doc Type Reference

How to write each type of doc. Read the relevant section before writing a doc of that type for the first time in a session.

---

## index.md (Navigation Hub)

**Purpose:** A map. The reader lands here and immediately knows where to go.

**Structure:**
1. Project name as H1
2. One sentence: what is this. One sentence: why does it exist or who is it for.
3. Horizontal rule
4. Navigation table: Section | What's inside (one line each)
5. Optional: "New here?" call-to-action pointing to onboarding

**What not to do:**
- Don't put architecture diagrams here (put them in `what-is-this.md`)
- Don't put getting-started instructions here (put them in `quickstart.md`)
- Don't write more than 2 paragraphs of prose

---

## what-is-this.md (Concept: Overview)

**Purpose:** Build the mental model. The reader should finish this doc with a clear picture of what the system does, how it's structured, and how the pieces fit together.

**Structure:**
1. One-sentence answer to "what is this?"
2. The problem it solves (2-3 sentences)
3. How it works — the mental model, not implementation details
4. Architecture overview (diagram or ASCII art if helpful)
5. How the pieces fit together — a brief narrative of a typical end-to-end flow
6. What this is NOT — scope boundaries, to prevent misuse

**Tone:** Conceptual. No code, no commands. The reader is building a picture in their head.

---

## key-concepts.md (Glossary)

**Purpose:** Define every term that appears in the docs without being self-evident. Prevents confusion when the same thing is called by different names in the codebase.

**Structure:** Alphabetical or grouped by domain. Each entry:

```markdown
**Term** — One-sentence definition that stands alone out of context.
Example: A Workspace is the top-level org unit, equivalent to a GitHub organization.
```

Include:
- Technical terms specific to this project
- Terms that have a specific meaning in this project vs. general usage
- Acronyms and abbreviations
- Terms that appear in multiple docs and could cause confusion

---

## prerequisites.md (Getting Started)

**Purpose:** Tell readers exactly what they need before they start. No surprises mid-quickstart.

**Structure:** For each dependency:
```markdown
### Node.js 20+
Verify: `node --version` (should print `v20.x.x` or higher)
Install: [nodejs.org/download](https://nodejs.org/download)
```

Include: software deps, API keys needed, minimum hardware (if relevant), OS requirements.

Keep it factual. Don't explain what Node.js is — just say what version and where to get it.

---

## quickstart.md (Getting Started)

**Purpose:** Get the reader to a working system as fast as possible. This is the most important doc in the set — if it's wrong, broken, or slow, you've lost the reader.

**Structure:**
1. Time estimate ("This takes about 10 minutes")
2. Prerequisites (link to prerequisites.md)
3. Numbered steps — each with: what to do, the command, expected output
4. "What happened" — one paragraph explaining what just ran
5. "Next steps" — 2-3 links to follow-on docs

**Rules:**
- Every command must be copy-pasteable and work exactly as written
- Show expected output after each command so readers can verify success
- Steps should be numbered 1, 2, 3... not headed sections
- Must work end-to-end without reading any other doc

---

## onboarding.md (Zero-to-Hero)

**Purpose:** Get a complete newcomer to confident understanding. This is different from quickstart — it's conceptual before practical, and assumes no prior familiarity with the project's domain.

**Structure:**
1. Start with analogies: "If you've used X before, Y is like Z but..."
2. Build the mental model: what are the core abstractions and how do they relate?
3. Walk through a realistic scenario narrative (not a tutorial — just tell the story)
4. Answer "why does it work this way?" for the 3 most surprising design choices
5. End with "where to go next" — curated learning path

**Tone:** Patient, conversational. Use "you" and "your". Explain why, not just what. The reader should feel like they just had a great onboarding chat with a knowledgeable teammate.

---

## concepts/X.md (Deep Dive)

**Purpose:** Explain one subsystem completely. After reading this, the developer should understand it deeply enough to debug it, extend it, or explain it to someone else.

**Structure:**
1. What it is (2 sentences)
2. What problem it solves / why it exists as its own subsystem
3. How it works — internal mechanics, data flows
4. Key data structures and their meaning
5. Interaction with other subsystems
6. Configuration and tuning
7. Common gotchas

**Link generously** to related concepts docs and guides.

---

## guides/X.md (How-To)

**Purpose:** Help the reader accomplish a specific task. Task-oriented — not "what is X" but "how do I do Y".

**Structure:**
1. Title is a verb phrase: "Create an agent", "Handle approval failures"
2. One sentence: what this guide accomplishes and when you'd need it
3. Prerequisites (tools, permissions, context needed)
4. Numbered steps
5. Verification — how to confirm it worked
6. Troubleshooting section for this specific task (top 2-3 failures)

**Rule:** One guide = one task. If the guide covers two tasks, split it.

---

## reference/X.md (Complete Reference)

**Purpose:** The authoritative lookup. Every option, every field, every behavior. Developers come here when they need specifics they can't remember.

**Structure depends on type:**

*API reference:*
```
## POST /api/resource

Description: what this endpoint does.

**Headers:** Authorization: Bearer {token}

**Request body:**
| Field | Type | Required | Description |
...

**Response:**
| Field | Type | Description |
...

**Error codes:**
| Code | Meaning | Fix |
...

**Example:**
```curl ... ```
```

*Config reference:*
```
## fieldName
Type: string | number | boolean | enum
Default: value
Required: yes/no
Description: what it does, when to change it
Example: fieldName: "value"
```

**Rules:**
- Every field must be documented, even obvious ones
- Include default values
- Include valid values for enums
- Never say "see source code for details"

---

## architecture/system-design.md

**Purpose:** Explain the technical architecture to developers who will work on (not just use) the system.

**Structure:**
1. High-level architecture diagram (ASCII or Mermaid)
2. Component breakdown — what each major component does
3. Data flows — how data moves between components for key operations
4. Key design decisions and why (non-obvious ones)
5. Scaling characteristics — what is and isn't scalable
6. Dependencies — external services, databases, protocols

**Tone:** Technical and precise. This is for developers, not users. Use exact terminology.

---

## architecture/adr/NNN-title.md (Architecture Decision Record)

**Purpose:** Record why a non-obvious decision was made, so future engineers don't undo it by accident or without understanding the trade-offs.

**Structure:**
```markdown
# ADR NNN: [Decision title]

**Status:** Accepted / Proposed / Deprecated / Superseded by ADR NNN

## Context
What problem were we solving? What constraints existed? What alternatives were on the table?

## Decision
What we decided to do, stated clearly.

## Alternatives considered

### Option A: [name]
[Description, pros, cons]

### Option B: [name]
[Description, pros, cons]

## Rationale
Why we chose the decision over the alternatives. What made the difference.

## Trade-offs
What we gave up. What risks we accepted. What this makes harder in the future.

## Consequences
What changes as a result of this decision. What other decisions this enables or constrains.
```

Write an ADR for every decision that a future engineer might reasonably reverse or question without the original context.

---

## user-guide/X.md (End-User Guide)

**Purpose:** Help someone *use* the product or its output — not build, deploy, or extend it. The reader may be non-technical.

**Structure:**
1. Title is what the user wants to do, in their words: "Watching the film", "Sharing your report"
2. One sentence: what you'll be able to do after reading
3. Numbered steps in plain language — UI actions, not commands
4. What you should see at each step (screenshots or stills where they carry meaning)
5. "If something looks wrong" — the 1-2 most likely user-visible problems, with plain-language fixes

**Rules:**
- Zero code and zero file paths in the main flow, unless the user genuinely types/opens them
- Never assume knowledge of the repo, the stack, or the build process
- Define any unavoidable technical term inline, in one clause
- Link to troubleshooting for anything deeper — don't escalate the reader into developer docs mid-task

---

## user-guide/faq.md (FAQ)

**Purpose:** Answer the questions real users actually ask, fast.

**Structure:** H2 per question, phrased exactly as a user would ask it. Answer in 1-4 sentences, answer-first. Group related questions under H1 sections if there are more than ~10.

**Rules:**
- Only include questions with real or strongly expected demand — an FAQ of invented questions is filler
- If an answer needs more than a short paragraph, give the short answer here and link to the full doc
- Keep answers standalone: the reader lands here from search

---

## history/development-journey.md (Build Chronicle)

**Purpose:** Record how the project was actually built — the narrative that code and reference docs can't carry. Serves future maintainers ("why is it like this?"), and showcases the process itself when that process is part of the story (agentic builds, unusual constraints, research projects).

**Structure:**
1. Header block: what was built, by whom/what, over what period, headline stats
2. The journey in phases or turns — chronological, each with what happened and what was decided
3. Tools/stack actually used (and notable rejections)
4. Decision forks — every major fork, who/what resolved it, and why
5. Failure catalog — what broke and how it was absorbed
6. Costs — money/credits, wall-clock time, human time
7. Verification — how the output was tested, including gaps that were found late
8. Lessons / what this demonstrates

**Rules:**
- Honesty over polish: include the failures and the checks that were missed — a chronicle that only records wins reads as marketing
- Real numbers with sources; state magnitude honestly when exact figures aren't available
- If a chronicle already exists (DEVELOPMENT.md, devlog, lab notebook), link it from index.md and do NOT recreate it — extend it only if asked

---

## troubleshooting/common-issues.md

**Purpose:** Fast answers to the most common failures. Developers come here frustrated — make it easy to scan.

**Structure:** For each issue:
```markdown
## [Symptom as the user would describe it]

**Cause:** [What's actually wrong]

**Fix:**
[Exact commands to fix it]

**If that doesn't work:**
[Escalation path]
```

**Rules:**
- Order by frequency, not severity
- The symptom heading should match what the user would search for
- Fixes must be exact — don't say "check your config", say which field in which file
- Include the 3 most common failures for each major component/operation
