---
name: stem-textbook
description: >-
  Co-author a graduate-level science, mathematics, or engineering textbook with
  a human author, from book specification to final manuscript. Plans the book
  as a graph of results and a book-wide notation table, gates the plan with the
  author before any prose, drafts one section at a time with every symbol
  defined and every number computed, keeps a state file across sessions, sends
  each chapter to science-editor for rigor review, and runs book-level passes
  for structure, notation, continuity, exercises, and final integrity. Use when
  the user says "write a textbook", "graduate textbook on X", "plan my STEM
  book", "turn my lecture notes into a book", "outline the book", "draft
  chapter N", "continue the book", or "resume the textbook". For one standalone
  lesson or explainer use rigorous-explainer. For a review of an existing
  chapter with no drafting use science-editor.
---

# stem-textbook

Co-author a graduate STEM textbook. The human author decides the scope, the
results, the notation, and the final text. You plan, draft, compute, check, and
keep the state of the book.

## Three skills, three jobs

| Job | Skill |
|---|---|
| Plan the book, gate the plan, draft sections in order, keep state, run book-level passes | this skill |
| Craft of one chapter: definitions, derivations, figures, exercises, HTML template, check scripts | `rigorous-explainer` at `~/.claude/skills/rigorous-explainer/` |
| Rigor review of a drafted chapter: five-part claim standard, located defects with replacement text | `science-editor` (invoke it; do not imitate it) |

Do not copy rules or scripts from the other two skills into this one. Read them
when a phase needs them. If `rigorous-explainer` moves, update the paths in this
file and in `references/drafting.md`.

## The reader

Default reader, unless the specification changes it: a graduate in a
quantitative field. The reader is fluent in linear algebra, multivariable
calculus, and probability. The reader has close to zero exposure to this
subfield. Never assume subfield knowledge. Never dumb down the mathematics.

## Priorities, in order

1. Mathematical, physical, and factual correctness.
2. Every term, symbol, domain, unit, and assumption defined before first use.
3. Fidelity to the author's results, sources, and scope. If the author's
   derivation is wrong, flag it before you draft on top of it.
4. Logical order of results: dependencies point backward.
5. Explanation: statement, derivation, interpretation in words, and a check.
6. Notation and terminology consistent across the whole book.
7. House style.
8. Concision. Never cut a definition, a derivation step, a condition, or a limit.

## Hard rules

- **Never invent** a paper, author, title, theorem number, page number, DOI,
  URL, quotation, data value, physical constant, experimental result, or author
  experience.
- **Label the status of each claim** at the claim: proved here, proved earlier,
  cited with page, numerically checked, measured, or heuristic. Never present a
  cited result as proved here. Schema: `references/claim-ledger.md`.
- **No decorative equations.** Every equation states a real relation between
  defined symbols. Do not write "Quality = A × B × C" style formulas.
- **Compute every number you print.** Run the code. Quote real output. Print
  the punchline number before you build a figure around it.
- **One section at a time.** Never generate a whole chapter or the whole book
  in one pass.
- **No prose before Gates A–D pass.** The author approves each gate.
- **Placeholders, not guesses.** Use `[PROOF NEEDED]`,
  `[CITATION NEEDED: result, source, page]`, `[NUMBER NOT YET COMPUTED]`, or
  `[AUTHOR DECISION NEEDED: question]`. No placeholder may remain at the end.
- **Prose lives in the chapter file.** Generator scripts compute figure data
  only. Prose authored inside a script string evades review.

## Workflow

| Phase | Read | Output | Gate (author approves) |
|---|---|---|---|
| 1. Specification | `references/book-spec.md` | `spec/book-spec.md`, `spec/house-style.md`, `spec/sources.yaml` | **A:** reader, R₀ → R₁, prerequisites, scope, format are coherent |
| 2. Results and notation | `references/results-and-notation.md` | `plan/results.yaml`, `plan/notation.md` | **B:** no dependency cycle; each result has a status plan |
| 3. Architecture | `references/architecture-and-outline.md` | `plan/architecture.md` | **C:** each chapter has a distinct purpose and passes the necessity test |
| 4. Detailed outline | `references/architecture-and-outline.md` | `plan/outline.md` | **D:** outline gate passes; exact statements written |
| 5. Draft by section | `references/drafting.md` + rigorous-explainer | `chapters/chNN.html` | per section: checks pass, state updated |
| 6. Chapter review | invoke `science-editor` | `reviews/chNN-editor.md` | **E:** blocking defects fixed or tagged as placeholders |
| 7. Book passes | `references/editorial-passes.md` | `reviews/book-passes.md` | **F:** structure fixed before sentence edits |
| 8. Final integrity | `references/editorial-passes.md` | final manuscript | **G:** every proof checked, every number reproduced, no placeholder, all links resolve |

**Plan review.** Before you ask for Gates A–D, review the plan yourself with the
checklist in `references/editorial-passes.md` ("Plan review"). Report the
defects with the plan. The author decides.

**Stops.** Stop for author review at each gate and after each chapter. An
autonomous run never skips Gates A–D. It never skips approval of the first
figure of a new figure class.

**Resume.** When a session starts on an existing book, read `BOOK-STATE.yaml`,
`plan/notation.md`, and the current outline node first. Never rely on memory of
earlier sections.

## Format

- **Default: HTML + MathJax, one file per chapter.** Start each chapter from
  `rigorous-explainer/assets/template.html`. All rigorous-explainer check scripts
  apply per file. Run `scripts/check_book_links.py BOOK_DIR` for links between
  chapter files.
- **Numbering:** Chapter.N for theorems, equations, and figures (Theorem 3.2,
  eq. (3.14), Fig. 3.5). The template numbers figures "Fig. N" with a CSS
  counter (`counter-reset: fig`). Change the caption prefix to include the
  chapter number in each chapter file.
- **LaTeX:** allowed when the author chooses print. The rigorous-explainer HTML
  scripts do not apply. Compile the whole book. Treat undefined-reference and
  multiply-defined-label warnings as blocking. `science-editor` still applies.

## Project layout

```text
book/
  BOOK-STATE.yaml          state; update after every section
  spec/                    book-spec.md, house-style.md, sources.yaml
  plan/                    results.yaml, notation.md, architecture.md, outline.md
  chapters/                ch01.html, ch02.html, ...
  figures/                 one generator script per computed figure
  code/                    labs and scripts that produce printed numbers
  research/                claims.yaml, references.bib
  reviews/                 chNN-editor.md, book-passes.md
```

Create a folder only when the book needs it.

## Common mistakes

- **Nonfiction habits in a STEM book.** An author persona, anecdotes, word
  budgets, and "maximize information per word" push out derivation steps.
  Budget by pages or lecture hours. Use a house style sheet, not a persona.
- **Checking the mathematics at the end.** Check each proof and number when you
  draft its section. A wrong lemma in chapter 2 costs every later chapter.
- **A symbol that changes meaning between chapters.** Search `plan/notation.md`
  before you introduce any symbol.
- **An asserted result beside proved peers.** Give results of equal weight equal
  rigor, or demote the asserted one and cite it.
- **Citing from memory.** Open the PDF and read the page, or mark the citation
  unverified.
- **Reviewing your own draft by rereading it.** Invoke `science-editor`.
- **Drafting from the outline title alone.** A section needs its exact
  statements, symbols, check, and transition before prose.

## Origin

Built 2026-09-17 from three inputs: the book workflow in
`~/Downloads/write_a_book_dollwet/sean-book-writing-skill.md`, adapted for STEM
per `combine-skills-assessment.html` §11 in the same folder; the chapter craft
of `rigorous-explainer`; and the review role of `science-editor`.
