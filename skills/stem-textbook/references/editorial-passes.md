# Plan review, book passes, and final integrity

Two review levels live here. Per-chapter rigor review is not here: invoke
`science-editor` for that.

Report every finding the same way: location (`file:line` or plan node id), the
quoted text, the defect, and the fix written out.

## 1. Plan review (before Gates A–D)

Review the plan as an editor before the author sees it.

- **Gate A (specification):** use the checklist in `book-spec.md`. Also: is the
  reader transformation achievable within the length budget?
- **Gate B (results and notation):** use the checklist in
  `results-and-notation.md`. Also: does any result depend on an out-of-scope topic?
- **Gate C (architecture):** use the checklist in `architecture-and-outline.md`.
  Also: does the chapter order match the dependency graph with no forward edge?
- **Gate D (outline):** use the outline gate in `architecture-and-outline.md`.
  Also: can each section's exercises be solved from the text up to that point?

## 2. Book passes

Run passes 1, 4, and 5 in light form after each chapter, against the earlier
chapters. Run all passes in full after the first draft is complete. Fix
structure (passes 1–3) before sentences (passes 7–8).

### Pass 1 — Structure

Compare `plan/results.yaml` with the manuscript:

- a result used before the section that introduces it;
- a result introduced and never used, and not in R₁;
- a forward reference the reader must accept on faith;
- a chapter whose purpose moved away from its chapter record;
- a missing synthesis where two chapters' results must be combined.

### Pass 2 — Assumptions across chapters

`science-editor` checks proofs inside a chapter. This pass checks between chapters:

- a result proved under assumptions in one chapter, then applied in a later
  chapter where the assumptions do not hold;
- a numerical value that differs between chapters for the same running example;
- a model limit stated in one chapter and ignored in a later one.

### Pass 3 — Repetition

Classify each repeated explanation:

- **Useful:** a revisit at higher generality, in a new setting, or as a stated
  prerequisite. Keep it and name the earlier section.
- **Accidental:** a re-explanation. Remove it, compress it, replace it with a
  cross-reference, or turn it into an extension.

Do not maximize information per word. Do not cut derivation steps to remove
repetition.

### Pass 4 — Notation and terminology

- Every symbol in the text matches `plan/notation.md`.
- No symbol has two meanings. No concept has two names.
- Chapter-local symbols are redefined in each chapter that uses them.
- Each acronym is expanded at first use in the book and after a long gap.

### Pass 5 — Continuity and links

- "As shown in §N" points to a section that shows it.
- Named models and frameworks keep their names.
- Equation variables keep their meanings.
- Run `scripts/check_book_links.py BOOK_DIR`. Every cross-chapter link resolves.

### Pass 6 — Exercises and solutions

- Each chapter mixes conceptual, derivational, and computational exercises.
- Each exercise is solvable from the text up to that point.
- Each solution is verified. Computed answers come from a run.
- Computational exercises need a simulation, optimization, inverse problem,
  sensitivity sweep, or regime comparison. See
  `rigorous-explainer/references/pedagogy-checklist.md` §8.

### Pass 7 — Prose

- House style (`spec/house-style.md`) and the approved sample section.
- AI-voice tells: rhetorical questions, "not X, but Y" chains, symmetric sentence
  patterns, empty closing summaries, hedges ("clearly", "obviously", "simply").
- Epistemic verbs and modal verbs match the claim's status.
- Textbook voice is the target. Do not rewrite it into essay voice.

### Pass 8 — Reader simulation

Read each chapter as four readers. Record the answers. Do not change the book for
every objection; report them to the author.

| Reader | Questions |
|---|---|
| Student missing one prerequisite | Where do I stop? Which prerequisite is missing, and does the chapter name it? |
| Target graduate reader | Which step can I not reproduce? Which symbol did I lose? |
| Specialist referee | Which statement is imprecise? Which citation is wrong or missing? Which result is misattributed? |
| Instructor | Can I teach this chapter in its lecture-hour budget? Are the exercises assignable? |

## 3. Final integrity (Gate G)

- **Structure:** table of contents matches the chapters; numbering of chapters,
  sections, theorems, equations, and figures is continuous; headings are consistent.
- **Content:** no placeholder remains; no duplicated section; no orphan result;
  no contradictory definition.
- **Mathematics:** every result is proved, proved earlier, or cited with a page;
  every printed number is reproduced by its script; every code listing runs.
- **Evidence:** every ledger claim has status V, or its uncertainty is stated;
  every citation resolves to `research/references.bib`; quotations match their
  sources.
- **Figures and tables:** each is referenced by number from the prose; each
  figure generator reruns.
- **Links:** `check_book_links.py` passes; per-chapter RE checks pass.
- **State:** `BOOK-STATE.yaml` shows all gates passed and no open placeholder.
