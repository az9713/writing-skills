# Domain brief: template

A domain brief tells the editor what this manuscript is, what it must never blur,
and which numbers and sources are ground truth. Write one per manuscript. Keep it at
the repo root as `EDITOR_DOMAIN.md`, or as a `# Domain:` section inside
`EDITOR_PROMPT.md`. Fill every heading. A heading with nothing to say gets one line
that says so ("No evidence grades; all claims are derived in the text.").

`example-domain-neural-operators.md` is a filled-in brief. Match its specificity:
file paths, page numbers, exact measured values, the concrete correction that an
earlier draft got wrong.

---

# Domain: <subject of the manuscript>

This is the subject of the manuscript. Know it before you edit it.

## What the manuscript is

- Format and location: how many chapters or modules, what medium (HTML + MathJax,
  LaTeX, Markdown), which file is the map, where the lessons live.
- Supporting material: labs, notebooks, source ledgers, research notes, and where
  each sits.
- The one question the manuscript exists to answer. If it is part textbook and part
  audit, say so; both halves must hold.

## The objectives or results that must never be blurred

List the distinct goals, models, or claims the field tends to run together, each with
its own test of success. A passage that blurs two of them is a blocking defect.
Success at one does not prove success at another.

## The mathematics the reader meets, and what may not be assumed

The reader has graduate fluency in the general tools but has never met this field.
List every field-specific object, theorem, and construction that must be built, not
invoked. Point to the passage in the manuscript that already meets the five-part
standard, with its `file:line` range, so every other claim can be held to that shape.

## The methods, models, or architectures, and where they come from

Name each one. State which must be derived from first principles rather than
presented as a diagram to accept.

Primary sources, cited by page:

- `<file>.pdf` — what it is. Note any lemma, theorem, or page number an earlier draft
  cited wrongly, and the correct one. Check every citation against the PDF.

## The evidence-grading scheme

If the manuscript grades claims, define every grade and its test. State what an
ungraded or misgraded number counts as. If there is no scheme, say so in one line.

## The running example

The one concrete problem threaded through the manuscript, where it is defined, and
which chapters return to it. A passage that introduces a fresh toy problem without
need is a structural defect.

## Measured results the prose must match

Every number the manuscript reports from a lab, experiment, or computation, with the
run it came from and the results file. A mismatch in the prose is a factual error.
Include the findings the manuscript must not soften.

## Conventions of this manuscript

- Page shape: the fixed parts, in order.
- What the page says where a result has not been produced ("not yet run").
- Medium constraints: valid HTML with MathJax delimiters, heading levels the
  stylesheet carries, dark or light palette, symbol conventions in SVG text.
- Tooling constraints: which libraries the labs may use.
