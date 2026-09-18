# Phase 1 — Book specification

Build the specification before any outline. Output three files:
`spec/book-spec.md`, `spec/house-style.md`, `spec/sources.yaml`.

## 1. Gather inputs

```yaml
book:
  working_title:
  subject:
  conceptual_spine:        # the model or question that orders the book
  governing_question:      # optional; a reference text may not have one
  target_reader:           # default in SKILL.md "The reader"
  prerequisites:
    courses: []
    results_assumed: []    # each with a standard reference
  learning_outcomes: []    # R1 as results the reader can prove, compute, or apply
  scope_in: []
  scope_out: []
  results_assumed_without_proof: []
  course_use:              # semesters, lecture hours, chapters per week
  length_budget:           # pages or lecture hours; not words
  format: html             # html | latex
  structural_archetype:    # see architecture-and-outline.md

author:
  name:
  relevant_expertise:
  supplied_material: []    # lecture notes, slides, papers, code, data
  decisions_reserved: []   # what the author must approve personally

math_and_code:
  notation_convention:     # the field's dominant convention and its source
  proof_depth:             # full | smallest setting that shows the mechanism | cite
  theorem_environments: [definition, lemma, proposition, theorem, corollary, example, remark]
  numbering: chapter.N
  exercise_types: [conceptual, derivational, computational]
  solutions:               # inline <details> | separate instructor manual
  software:                # language, version, libraries
  units_standard:          # SI unless the field convention differs
```

If a value is unknown, propose one and mark it `PROVISIONAL`. Never invent a fact
about the author.

## 2. Write the specification

```markdown
# Book Specification
## Working Title
## Conceptual Spine
## Reader and Prerequisites
## Reader Before (R0)
## Reader After (R1)
## Scope
## Out of Scope
## Results Assumed Without Proof
## Course Use and Length Budget
## Format and Numbering
## Primary Sources
## Author Decisions Reserved
```

### R₀ → R₁ as results

Write R₀ and R₁ as lists of results, not impressions. Example (illustration only):

```text
R0: can derive a finite-difference scheme for the 1-D heat equation and run it.
R1: can prove that the explicit scheme with r = κΔt/Δx² is stable
    in the von Neumann sense exactly when r ≤ 1/2; can state the
    Lax–Richtmyer equivalence theorem with its hypotheses; can choose
    between explicit and implicit schemes from a cost and stability argument.
```

Each learning outcome must map to at least one result in `plan/results.yaml`.

### Scope

List what the book covers, what it excludes, and what it assumes without proof.
An excluded topic that a later chapter needs is a scope defect. Fix it at Gate A.

## 3. House style sheet

`spec/house-style.md` replaces an author persona. Fill each heading:

- **Notation:** the field convention followed; vectors, matrices, operators,
  sets, random variables; where the full table lives (`plan/notation.md`).
- **Theorem layout:** environments used, what gets a proof, proof end mark.
- **Person and tense:** "we" for the reader-and-author pair; present tense for
  definitions and results; dated past tense for history.
- **Epistemic verbs:** *prove* for deduction; *observe*, *show*, *support* for
  evidence; *must* for an invariant, *can* for capability, *may* for
  uncertainty, *should* for a recommendation. Detail:
  `rigorous-explainer/references/technical-writing-guides.md` item 5.
- **Units and numbers:** unit system, significant figures, uncertainty format,
  percent vs percentage points.
- **Cross-references:** "Theorem 3.2", "eq. (3.14)", "Fig. 3.5", "§3.4". Never
  "the figure below" or "later".
- **Citations:** style, and the rule that a cited result carries a page or label.
- **Spelling:** US or UK; serial comma yes or no.
- **Approved sample:** after Gate D, the author approves one drafted section.
  It becomes the reference for voice.

## 4. Source ledger

```yaml
sources:
  - id: S001
    citation:          # full bibliographic entry
    type:              # paper | monograph | lecture notes | dataset | standard
    edition:
    local_path:        # PDF in the repo; empty means the source is unverifiable
    results_used:
      - label_in_source:   # e.g. Theorem 4.1
        page:
        used_in:           # result id in plan/results.yaml
        reproved_here:     # true | false
    notes:
```

A source with no `local_path` cannot verify a page number. Mark each claim that
depends on it as unverified until the author supplies the PDF.

## Gate A checklist

- The conceptual spine orders the book.
- R₁ is a list of results. Each one is testable by an exercise.
- Prerequisites name specific results, not only course titles.
- No out-of-scope topic is needed by an in-scope result.
- Format and numbering are chosen.
- Every `PROVISIONAL` value is listed for the author.
