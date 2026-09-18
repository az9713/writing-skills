<!-- Worked example of a domain brief. Copied verbatim from EDITOR_PROMPT.md (biomechanics repo, 2026-09-07), lines 98-220. It describes a DIFFERENT manuscript (a neural-operator course), so it is a model of specificity, not a brief for the current repo. -->

# Domain: neural operators for partial differential equations

This is the subject of the manuscript. Know it before you edit it.

## What the course is

Thirteen modules plus a capstone, written as HTML lessons with MathJax, in `course/`.
`course/index.html` is the map; `course/00_orientation.html` through `course/13_capstone.html`
are the lessons. Three runnable labs sit in `labs/`, six notebooks in `notebooks/`, and the
source ledger in `research_notes/` and `neural_operator_course_research_report.html`.

The course exists to answer one question: of the claims made for neural operators — a podcast
episode promising one model across fluid dynamics, semiconductors, and energy, trillion token
context training, five trillion context inference — which rest on public evidence and which do
not. So the manuscript is part textbook and part audit. Both halves must hold.

## The three objectives, never mixed

The field uses one phrase, "neural operator", for three different goals with three different
tests. Any passage that blurs them is a blocking defect:

- A **surrogate** reproduces a known simulator faster. Test: error against the simulator on
  held-out inputs, plus speed.
- A **PINN** fits one solution by penalising the equation residual. Test: the residual and the
  error on that one instance.
- A **foundation model** reuses one representation across several physical systems. Test:
  whether pretraining on systems A and B lowers the data needed for system C, measured against
  an equal-size model trained on C alone.

Success at one does not prove success at another.

## The mathematics the reader meets, and what may not be assumed

The reader knows graduate analysis in the ordinary sense but has never met this field. Every
one of the following must be built, not invoked: function spaces $L^2$, $H^s$, $W^{m,p}$,
$C(\bar D)$; equivalence classes and null sets; almost-everywhere equality; why point
evaluation is not defined on $L^2$ and what Sobolev embedding buys back; compact and
non-compact operators, and why non-compactness matters here; the convolution theorem; Green's
functions; the Fourier transform on a periodic domain and the real-FFT bin count; Nyström
approximation, low-rank factorisation, multipole decomposition; universal approximation as an
existence result, not an efficiency result; the four sources of error in the JMLR paper
(pp. 50–51), of which only two are proved.

`course/00_orientation.html:52-105` is the worked model of the five-part standard. Fact 1 there
proves, in order: that $L^2$ elements are equivalence classes because the seminorm fails one
axiom; that null sets give the a.e. characterisation; that evaluation carries no information and
is discontinuous (tent of height 1 and width $2/n$, norm squared $2/(3n)$); the rescue (a unique
continuous representative, and $s > d/2$ giving $\sup|u| \le C_s \lVert u \rVert_{H^s}$ by
Cauchy–Schwarz on the Fourier series); and three routes practice actually uses. Hold every other
claim in the manuscript to that shape.

## The architectures and where they come from

FNO, DeepONet, GNO, LNO, MGNO, GINO, SFNO, Transolver, MeshGraphNets, PINNs and hybrids, and the
physics foundation models MPP, Poseidon, DPOT, and Subramanian et al. The Fourier layer must be
*derived* from the convolution theorem and the Green's function, never presented as a diagram to
accept.

Primary sources, cited by page:

- `2010.08895v3.pdf` — FNO, ICLR.
- `21-1524.pdf` — the JMLR neural operator paper. Note: Lemma 28 (p. 81), Lemma 29 (p. 85),
  Lemma 30 (p. 86) are the ones about replacing point evaluation. Lemmas 21 and 23 are not;
  an earlier draft cited them wrongly. Check every lemma number against the PDF.
- `2010.03409v4.pdf` — MeshGraphNets.
- `2210.07182v7.pdf` — PDEBench.

## The evidence grading system

Every claim on every page carries a grade, and the grade is part of the claim. Flag any
ungraded claim and any grade that outruns its source:

- **A** — read in the primary paper, page cited.
- **B** — abstract or secondary source only, arXiv identifier verified.
- **C** — company statement, press, or podcast, not independently checked. A company claim
  stays a C. Repetition does not promote it.
- **LAB** — produced in this repository, with the script and the results file named.

A number with no grade, no `research_notes/` line, no PDF page, and no results file is a
blocking defect. So is a hedge used in place of a grade.

## The running physical example

Steady heat conduction in a 10 mm silicon die with random rectangular power blocks, solved by
finite differences and checked against an analytic solution (`labs/02_thermal/`). It returns in
Modules 6, 10, 12, 13, and the capstone. One example threaded through is deliberate; a passage
that introduces a fresh toy problem without need is a structural defect.

## Lab results the prose must match

Check every number in the text against these. A mismatch is a factual error.

- Lab 01 Burgers, run A (bundled data): test relative L2 **0.0044**.
- Lab 01 run B (paper spec, $\nu = 0.1$ on $(0, 2\pi)$), trained at 64 points, evaluated at
  64 / 128 / 256 / 1024: `n_modes=16` (k_max 8) **0.0224 / 0.0351 / 0.0349 / 0.0349**;
  `n_modes=32` (k_max 16) **0.0226 / 0.0267 / 0.0264 / 0.0264**.
- Lab 01 run C, the CNN counterexample, 49-point receptive field, same four grids:
  **0.0224 / 0.68 / 1.14 / 1.46**.
- Lab 02 thermal, trained at 64², evaluated at 64² and 128²: relative L2 **0.0065** and
  **0.0814**; peak temperature error **0.20 K** and **1.55 K**.
- Lab 03 scale: about **1050 bytes per grid point**, **143 ms at 1024²** on an RTX 3050 Laptop
  GPU with 4 GB.

Two findings the manuscript must not soften:

- An FNO evaluated at a grid it never trained on carries a grid-scale (Nyquist) oscillation:
  1.44e-2 at the Nyquist bin in 1D at every unseen grid, horizontal stripes in the 2D thermal
  output at 128². Hence the error rise: +56 percent for k_max 8, +18 percent for k_max 16 on
  Burgers, 12× on thermal. "Resolution invariant" describes the architecture, not the error.
- `neuraloperator` 2.0.0 keeps `n_modes // 2 + 1` bins on the real-FFT axis, so `n_modes=16`
  means k_max 8, and the paper's k_max 16 needs `n_modes=32`.

## Conventions of this manuscript

- **One page shape, six parts, same order**: why the module exists → the core ideas in prose →
  the mathematics with derivations → the lab with real numbers → the sources with line citations
  → an exit test taken with the page closed. A page that departs from the shape must earn it.
- **Where a lab has not run, the page says "not yet run."** Never a plausible figure in the gap.
  Treat any invented number as the most serious class of defect.
- The medium is HTML with MathJax and a dark palette (`course/course.css`). Rewrites you supply
  must be valid HTML with correct MathJax delimiters, and must not introduce a heading level the
  stylesheet does not carry.
- Tools in the labs are PyTorch and `neuraloperator` only.
