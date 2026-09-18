# Phases 3–4 — Architecture and detailed outline

Output: `plan/architecture.md` (Gate C) and `plan/outline.md` (Gate D).

## 1. Structural archetypes for STEM books

| Archetype | Shape | Fits |
|---|---|---|
| Foundations → theory → methods → applications | linear | a first graduate course |
| Core plus independent tracks | core chapters, then branches | a book used by several courses; include a chapter dependency chart in the preface |
| Theory with a parallel lab track | each theory chapter has a code or lab companion | computational science and engineering |
| Running application | one application motivates each chapter's model | engineering design, applied modeling |
| Survey monograph | reference chapters on subtopics | a research field overview; the governing question is optional |

## 2. Budgets

Budget by pages or lecture hours, not by words. A display equation or a proof
carries much content in few words. Record for each chapter:

- page or lecture-hour budget;
- number of results introduced;
- number of exercises by type.

The sum of chapter budgets must match the book budget in `spec/book-spec.md`.

## 3. Chapter record

```yaml
chapter:
  number:
  title:
  purpose:                 # one sentence
  question:                # the question the chapter answers
  prerequisites:           # chapter numbers and result ids
  starting_state:
  ending_state:            # results the reader can now prove, compute, or apply
  results_introduced: []   # ids
  results_reused: []       # ids
  running_example_use:
  figures:                 # each with its teaching job
  code_labs: []
  exercises: {conceptual: , derivational: , computational: }
  budget:
  transition:              # the fact that makes the next chapter necessary
```

### Necessity test

Ask of each chapter: if it disappeared, would the reader's path from R₀ to R₁
lose a needed result? If not, merge or remove it.

Exception: a **reference chapter or appendix** (for example, a measure theory or
linear algebra review) may sit off the main path. Mark it `reference`.

### Overlap check

For chapters i and j, let Cᵢ and Cⱼ be the sets of result ids they introduce or
reuse. Compute

  Oᵢⱼ = |Cᵢ ∩ Cⱼ| / |Cᵢ ∪ Cⱼ|.

Report the pairs with the highest Oᵢⱼ to the author. There is no fixed threshold.
Shared results are acceptable when a chapter revisits them at higher generality,
applies them in a different setting, or uses them only as prerequisites. They are
a defect when a chapter only re-explains them.

## Gate C checklist

- Each chapter has one distinct purpose.
- Each chapter passes the necessity test, or is marked `reference`.
- Chapter order respects `plan/results.yaml` dependencies.
- High-overlap pairs are justified.
- Budgets sum to the book budget.
- The chapter dependency chart is drawn (required for the core-plus-tracks archetype).

## 4. Detailed outline

Hierarchy: Part (optional) → Chapter → Section → Subsection. A heading alone is
not an outline node. Each section node holds:

```yaml
section: "4.2 Von Neumann stability of the explicit scheme"
purpose: Show when the explicit heat-equation scheme amplifies round-off.
question: For which mesh ratios r does no Fourier mode grow?
results:
  - id: R-stab-vn
    statement: >-
      For u_j^{n+1} = u_j^n + r(u_{j+1}^n - 2u_j^n + u_{j-1}^n) with periodic
      boundary conditions, every Fourier mode satisfies |G(θ)| ≤ 1 for all θ
      if and only if 0 < r ≤ 1/2, where G(θ) = 1 - 4r sin²(θ/2).
defines: [G(θ)]
uses: [r, "R-fd-heat"]
hinge: sin²(θ/2) reaches 1 at θ = π, so the worst mode is the sawtooth.
smallest_setting: one Fourier mode e^{ijθ} on a periodic grid.
check: at r = 1/2 and θ = π, G = -1 (the marginal mode); a run with r = 0.55
  shows the sawtooth growing.
running_example: the rod-cooling problem from §1.1.
figure: |G(θ)| against θ for r = 0.25, 0.5, 0.55 — shows the crossing above 1.
exercises: [D: derive G for the implicit scheme; K: find the largest stable
  Δt for a given Δx and κ and confirm by simulation]
transition: The explicit scheme's r ≤ 1/2 limit makes Δt ∝ Δx²; §4.3 asks
  whether an implicit scheme removes that cost.
budget: 4 pages
```

The example is an illustration of node depth. Check its mathematics like any
other content before you reuse it.

## Gate D checklist (outline gate)

- Every section has a purpose and a question.
- Every result in the section has its exact statement written.
- Every symbol used is defined earlier or in this section, and is in `notation.md`.
- Every section names its check: limit case, numerical run, or measured value.
- Every figure has a teaching job. No figure exists to meet a count.
- Exercises cover conceptual, derivational, and computational types across the
  chapter. Computational exercises are not substitution into a boxed formula.
- Every transition states the fact that makes the next section necessary.
- Budgets are plausible for the stated statements and proofs.
