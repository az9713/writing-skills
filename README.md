# writing-skills

Fourteen Claude Code skills for writing, shaping, and editing text.

**Explainer page:** https://az9713.github.io/writing-skills/ — what each skill does, when to use which, and where they overlap. Source: [`index.html`](index.html).

**Origin of the book skills:** `book-writing` and `stem-textbook` started from Sean Dollwet's YouTube video [How to Write a Book with AI in 2026 (Full Step-By-Step Tutorial)](https://www.youtube.com/watch?v=KrRDFpSjcR4) (video ID `KrRDFpSjcR4`, channel [@SeanDollwet](https://www.youtube.com/@SeanDollwet)). See [Attributions](#attributions) for all credits.

| Family | Skills |
|---|---|
| Nonfiction book | `book-writing`, `author-interview`, `kdp-publishing` |
| STEM teaching | `stem-textbook`, `rigorous-explainer`, `science-editor` |
| Article craft | `writing-fragments`, `writing-shape`, `writing-beats` |
| Prose style | `no-ai-slop`, `asd-ste100` |
| Technical documents | `technical-docs-writer`, `writing-for-agents`, `dev-journey` |

## Install

Copy a folder from `skills/` into `~/.claude/skills/`. Copy partner skills too: `book-writing` calls `author-interview` and `kdp-publishing`; `stem-textbook` calls `rigorous-explainer` and `science-editor`.

## Attributions

### Skills copied from other authors

These skills are redistributed unchanged under their MIT licenses.

- `writing-fragments`, `writing-shape`, `writing-beats`, `writing-for-agents`: by **Matt Pocock**, from [mattpocock/skills](https://github.com/mattpocock/skills). MIT license, Copyright (c) 2026 Matt Pocock. A copy of the license is in each of the four skill folders (`LICENSE`).
- `no-ai-slop`: by **Peter Yang**, from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop). MIT license, Copyright (c) 2026 Peter Yang (`skills/no-ai-slop/LICENSE`).

### Skills adapted from another author's workflow

- `book-writing`, and through it `author-interview`, `kdp-publishing`, and `stem-textbook`: adapted from the book-writing workflow of **Sean Dollwet** ([@SeanDollwet](https://www.youtube.com/@SeanDollwet)), shown in the video [How to Write a Book with AI in 2026 (Full Step-By-Step Tutorial)](https://www.youtube.com/watch?v=KrRDFpSjcR4). The workflow was rewritten and extended here (beginner path, market check, publishing steps, STEM adaptation). No license was published with the original workflow; credit goes to Sean Dollwet for the method.

### Sources that shaped the rules

- `rigorous-explainer` technical-prose rules draw on Gernot Heiser, [Tips and Guidance for Students and ECRs Writing Papers and Reports](https://gernot-heiser.org/style-guide.html), and Derek Abbott, [Guide to technical writing](https://www.eleceng.adelaide.edu.au/personal/dabbott/wiki/index.php/Guide_to_technical_writing).
- `rigorous-explainer` teaching structure draws on a style study of 12 machine-learning texts: Mohri, Rostamizadeh and Talwalkar, *Foundations of Machine Learning*; Bishop, *Pattern Recognition and Machine Learning*; Murphy, *Probabilistic Machine Learning: An Introduction* and *Advanced Topics*; Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*; James, Witten, Hastie, Tibshirani and Taylor, *An Introduction to Statistical Learning with Applications in Python*; Bach, *Learning Theory from First Principles*; Mitchell, *Machine Learning*; Hardt and Recht, *Patterns, Predictions, and Actions*; Shalev-Shwartz and Ben-David, *Understanding Machine Learning*; Telgarsky, *Deep Learning Theory Lecture Notes*; Phuong and Hutter, *Formal Algorithms for Transformers*. Only methods are borrowed, not wording (see `skills/rigorous-explainer/references/textbook-style.md`).
- `asd-ste100` follows ASD-STE100 Simplified Technical English, a specification maintained by [ASD](https://www.asd-ste100.org/). The skill is a summary of its rules, not the specification.
- `technical-docs-writer` conventions are modelled on public documentation from Google, Stripe, AWS, and Vercel.
- `kdp-publishing` facts come from the Amazon [KDP Help Center](https://kdp.amazon.com/help), checked 2026-09-17.
