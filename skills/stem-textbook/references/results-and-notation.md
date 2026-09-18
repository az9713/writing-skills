# Phase 2 — Results graph and notation table

A STEM book is a graph of results, not a list of topics. Build the graph and the
notation table before the chapter plan. Output: `plan/results.yaml`,
`plan/notation.md`.

## 1. Result nodes

```yaml
results:
  - id: R-stab-vn               # stable id; never renumber
    kind: theorem               # definition | lemma | proposition | theorem |
                                # corollary | algorithm | model | empirical fact
    statement: >-               # exact, with quantifiers, domains, and units
    assumptions: []
    depends_on: []              # result ids
    status: prove_here          # prove_here | proved_in: <id> |
                                # cite: {source: S001, label: , page: } |
                                # numerical_check | measured: {source: , value: , uncertainty: }
    smallest_setting:           # the smallest case where the mechanism is visible
    limit_or_rescue:            # where the hypotheses bind; what breaks without them
    concrete_tie:               # code, figure, measured number, or source page
    symbols: []                 # must exist in notation.md
    misconceptions: []
    planned_chapter:
```

Rules:

- Write the statement now, before prose. A vague statement is a Gate B defect.
- A `cite` status needs a label and a page from a PDF in the repo. Otherwise
  write `[CITATION NEEDED: result, source, page]`.
- A `model` node also lists what the model captures and what it misses, and
  where each omission is repaid. See `rigorous-explainer/references/pedagogy-checklist.md` §2.

## 2. Dependency checks

Check the graph before Gate B:

1. **No cycle.** A cycle means an exposition order problem or a circular proof.
2. **No forward edge.** Each dependency is planned in an earlier chapter, or
   earlier in the same chapter.
3. **Orphans.** A result that nothing depends on must appear in R₁ or be marked
   terminal. Otherwise cut it or connect it.
4. **Outcome coverage.** Each R₁ outcome is reached by at least one node.
5. **Whole laws.** If a node introduces a law with several parts (for example
   force balance and moment balance), later nodes use each part.

For a graph larger than about 40 nodes, check items 1–3 with a short script over
`results.yaml`. Keep the script in `plan/`.

## 3. Notation table

`plan/notation.md` is the contract for every symbol in the book.

| Symbol | Meaning | Type / domain | Units | Introduced | Scope | Note |
|---|---|---|---|---|---|---|
| $r$ | mesh ratio $\kappa\Delta t/\Delta x^2$ | $\mathbb{R}_{>0}$ | dimensionless | §4.1 | book | |
| $G(\theta)$ | amplification factor of one Fourier mode | $\mathbb{C}$ | — | §4.2 | book | |

Rules:

- One symbol, one meaning, in the whole book.
- A chapter-local symbol is declared `chapter` in Scope and redefined at its
  first use in each chapter that uses it.
- Search this table before you introduce a symbol. On a collision, rename, add a
  subscript, or declare scopes. Record the decision in Note.
- Follow the field's dominant convention (`spec/house-style.md`). Record each
  deliberate departure and its reason.
- Each symbol also gets a local definition in the text at first use. The table
  supplements the text. It never replaces a local definition.

## 4. Recurring models

If the book reuses one model across chapters, name its parts once. Each later
chapter states which part of the model it changes. A model written as an
equation must be a real equation with defined symbols.

## Gate B checklist

- Every node has an exact statement and a status.
- No cycle, no forward edge, no unexplained orphan.
- Every symbol in every node exists in `notation.md` with one meaning.
- Every `cite` node has a source id, label, and page, or a placeholder.
- Every R₁ outcome is covered.
