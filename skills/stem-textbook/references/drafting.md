# Phases 5–6 — Draft by section, review by chapter

Draft one section at a time. Check it before you draft the next one.

`RE` below means `~/.claude/skills/rigorous-explainer/`.

## 1. Section loop

1. **Assemble context.** Load only:
   - the compact specification and `spec/house-style.md`;
   - `plan/notation.md` (whole table);
   - the outline node for this section;
   - the result nodes for this section and their direct dependencies;
   - prior passages retrieved by result id, symbol, or running example — not
     because they are nearby;
   - `BOOK-STATE.yaml`.
2. **Write the exact statements first.** Copy them from the outline node into
   the chapter file. Do not change a statement silently. If a statement is
   wrong, stop and flag it.
3. **Draft in the chapter file.** Follow RE `SKILL.md` steps 3–4 and read
   `RE/references/textbook-style.md`, `RE/references/technical-writing-guides.md`,
   and `RE/references/pedagogy-checklist.md`. Read
   `RE/references/figures-and-animation.md` before the first figure.
4. **Compute.** Run every computation that produces a printed number, a figure,
   or a code output. Keep one generator per figure in `figures/`. Print the
   punchline number before you build the figure.
5. **Run the mechanical checks (HTML).** Run the RE step-6 hardening loop on the
   chapter file. Run `check_bodyprop.py`, `check_probfig.py`, and
   `check_provenance.py` only when the book's domain uses them. Run
   `scripts/check_book_links.py BOOK_DIR` when the section links to another
   chapter.
6. **Review the section** with the checklist in §3.
7. **Update the records:** `plan/notation.md`, the `status` in
   `plan/results.yaml`, `research/claims.yaml`, and `BOOK-STATE.yaml`.

## 2. Drafting requirements

1. Advance the argument. Do not restate an earlier section.
2. Use the terms and symbols already established.
3. Introduce only the results this section needs.
4. State each claim's status at the claim: proved here, proved earlier (with a
   link), cited (with page), numerically checked, measured, or heuristic.
5. Do not invent facts, sources, quotations, numbers, or experiences.
6. Do not write an empty introduction or an empty summary. A chapter summary of
   main results, a "Notes and references" section, and an exercise section are
   standard and allowed.
7. Use a list only when the content is a list.
8. End with a transition that states why the next section is necessary.

## 3. Section review checklist

- Every result statement is exact and matches its node.
- Every symbol has a local definition at first use and a row in `notation.md`.
- Every derivation step is reproducible with a pen. The hinge is explained.
- Every invoked result is named and linked.
- Each important equation is interpreted in words.
- The section's check (limit case, numerical run, or measured value) is present.
- Every printed number matches a script output.
- Results of equal weight get equal rigor.
- Each figure agrees with the mathematics. Each caption states what to infer.
- No AI-voice tells: rhetorical questions, "not X, but Y" chains, symmetric
  sentence patterns, empty closing summaries, "clearly", "obviously".
- The transition carries a reason.

## 4. State file

`BOOK-STATE.yaml` at the book root:

```yaml
phase:                      # 1-8
gates: {A: , B: , C: , D: , E: , F: , G: }   # pending | passed <date> | reopened
current_chapter:
current_section:
completed_sections: []
results:
  proved: []                # ids
  proof_pending: []
  cited_unverified: []
numbers_to_reproduce: []    # {location: , script: }
placeholders_open: []       # {tag: , location: }
author_decisions_needed: []
structural_issues: []
continuity_notes: []
next_action:
```

Update it after every section. Read it first when a session resumes.

## 5. Chapter completion

1. Invoke `science-editor` on the chapter file. Save its report as
   `reviews/chNN-editor.md`.
2. Show the author the verdict and the blocking defects. Apply only the fixes
   the author approves. Tag any deferred defect with a placeholder.
3. Re-run the section checks and the mechanical checks on the changed chapter.
4. Write the chapter record:

```yaml
chapter_review:
  main_results: []          # id + one-line statement with assumptions
  reader_start_state:
  reader_end_state:
  placeholders_open: []
  terminology_or_notation_conflicts: []
  missing_prerequisites: []
  transition_quality:
```

5. **Compression test:** list the chapter's main results with their assumptions.
   If you cannot write that list, the chapter lacks a clear architecture.
6. Stop for the author (Gate E).
