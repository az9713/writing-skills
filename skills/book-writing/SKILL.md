---
name: book-writing
description: Co-author a nonfiction book (how-to guide, self-help, business, general nonfiction) with a human author, from topic validation and positioning through specification, author persona, outline, section-by-section drafting, editorial passes, and optional production and publishing (formatting, cover, store description, Amazon KDP). Starts from nothing and works for a first-time author with no topic, notes, writing samples, or publishing knowledge (uses the author-interview and kdp-publishing helper skills). Never fabricates author experience, sources, quotes, or reviews. Use when the user says "write a book", "nonfiction book", "how-to book", "self-help book", "plan my book", "book outline", "draft chapter N", "continue my book", "I want to write a book but have never written anything", or "publish on KDP". Not for fiction. For a graduate STEM textbook use stem-textbook.
---

# Book Writing Skill

## Purpose

Use this skill to produce a coherent, substantive nonfiction book with AI while keeping the human author in control of:

* thesis
* ideas
* sources
* structure
* voice
* examples
* evidence
* interpretation
* final editorial judgment

The AI acts as a **co-author**, not an autonomous author.

The workflow is:

$$
\boxed{
\text{Inputs}
\rightarrow
\text{Market Positioning}
\rightarrow
\text{Book Specification}
\rightarrow
\text{Author Persona}
\rightarrow
\text{Concept System}
\rightarrow
\text{Architecture}
\rightarrow
\text{Detailed Outline}
\rightarrow
\text{Sequential Drafting}
\rightarrow
\text{Editorial Passes}
\rightarrow
\text{Final Manuscript}
\rightarrow
\text{Production (optional)}
}
$$

Do not begin drafting chapters until the pre-writing specification and outline have been approved.

---

# 0. Start from Nothing

Assume the author has nothing: no topic, no knowledge of book terms, no notes, no writing samples, no stories written down, no publishing account. Every later phase has a path for an author who lacks its input. This section runs first, every time a new book starts.

## 0.1 Talk to the author in plain words

The terms in this skill (thesis, archetype, persona, R0/R1, Class A/B/C, Gate A–G, V/Q/U/X, Pass 1–13) are for the agent and the files. Never use them with the author unless the author uses them first. Say "the main idea", "where your reader starts and ends", "how you write", "from you / from research / my own reasoning", "your approval", "confirmed / partly true / unsure / wrong", "edit round".

## 0.2 Set up the book folder

First action on a new book:

1. Create the `book/` folder (§15) in the current working directory, or where the author asks.
2. Create `book/BOOK.md` with the working title (or "untitled") and the §16 state block.
3. Tell the author the full folder path and the sentence to type to continue in a later session: "Use the book-writing skill. Read the progress notes and tell me where we are."

## 0.3 Set honest expectations

Before the first question, tell the author, in 5 lines or fewer:

* The book takes many sessions: planning, then one section at a time, then edit rounds.
* The author must supply the ideas, stories, and decisions. The AI will not invent them.
* Publishing on KDP is free to start; costs are optional (a designer, an editor, a bought ISBN, proof copies).
* Sales are not certain. Do not state sales figures or income that have not been checked.

## 0.4 Intake interview, not a form

Do not show the §2 input form to the author. Fill it yourself from an interview:

* Ask one plain question at a time. Offer a suggested answer the author can accept, change, or skip.
* Suggested answers the author accepts are recorded as `PROVISIONAL` until Gate A.
* If the author has no topic, run the author-interview skill in **topic** mode.
* Use defaults for what a beginner cannot judge, and say so: how-to books of about 25,000–40,000 words and 8–12 chapters are a reasonable first plan (a planning default, not a market fact); the structure is chosen by the AI in §7 and explained in one sentence.

## 0.5 Check what the author knows (warn, do not refuse)

A how-to or advice book needs an author who knows the subject. Ask what the author has done, for how long, and with what results. If the answers show little experience, **warn the author plainly** and offer four honest paths:

1. **Write from your own life.** Narrow the topic to what you have lived ("my first year of X").
2. **Learn and record it.** Do the thing for a set period and write the book as a record of what happened.
3. **Interview people who know.** With their permission; they become named sources.
4. **Pick a different topic** that fits your experience (author-interview, topic mode).

The author may continue anyway. Record the warning and the author's choice in `book/BOOK.md`, and let it shape the claims: the book must not present the author as an expert they are not. For health, legal, financial, or safety topics, the warning also says that a qualified person must review the facts before publishing (Pass 7).

---

# 1. Operating Principles

## 1.1 Specification before prose

Do not ask an LLM to:

> Write a book about X.

Instead progressively constrain the generation process.

The manuscript should emerge from a structured specification:

$$
M =
f(
T,
A,
P,
V,
S,
C,
O,
R
)
$$

where:

* \(T\) = topic/thesis
* \(A\) = audience
* \(P\) = purpose
* \(V\) = author voice/persona
* \(S\) = sources
* \(C\) = core concepts
* \(O\) = outline
* \(R\) = prior manuscript state

---

## 1.2 Outline depth before generation

Every significant section should already have:

* purpose
* argument
* concepts to introduce
* evidence needed
* examples
* relationship to previous sections
* transition to the next section

A heading alone is not a sufficient outline.

---

## 1.3 Draft sequentially

Prefer:

```text
section 1
→ review
→ edit
→ section 2 using section 1 as context
→ review
→ edit
→ section 3
→ ...
```

over:

```text
"Write the entire book"
```

Each new section should have access to relevant earlier material.

Sean's tool also offers whole-book generation in one run. He says it is faster but gives less control. If that option is used, run the Phase I section review on every section afterward.

---

## 1.4 Treat generated text as a first draft

Generated prose is never presumed final.

The human author should inspect:

* reasoning
* voice
* facts
* examples
* evidence
* redundancy
* pacing
* transitions
* claims
* citations

---

## 1.5 Never fabricate author experience

The skill must never invent:

* credentials
* employment history
* personal experiences
* conversations
* anecdotes
* case studies
* experiments performed by the author
* quotations attributed to real people

When an experience would improve the manuscript but none is supplied, insert:

```text
[AUTHOR EXPERIENCE NEEDED HERE]
```

rather than inventing one.

To fill the marker, run the author-interview skill in **story** mode. Writing a story from facts the author supplied is allowed; the author approves the draft. Adding any fact, feeling, name, or number the author did not supply is fabrication.

---

# 2. Required Inputs

Before outlining, gather the following.

```yaml
book:
  working_title:
  topic:
  central_thesis:
  purpose:
  reader_transformation:
  target_audience:
  audience_prior_knowledge:
  scope:
  exclusions:
  desired_word_count:
  desired_chapter_count:
  structural_archetype:

market:
  demand_evidence:
  comparable_titles:
  competitive_angle:
  unique_selling_proposition:
  key_selling_points:

author:
  name:
  pen_name_or_real_name:
  inspired_by_authors:
  background:
  relevant_experience:
  expertise:
  motivations:
  worldview_constraints:
  tone:
  writing_samples:  # none supplied? follow §5.2; never leave empty, never fill with AI-written text

content:
  mandatory_topics:
  key_concepts:
  arguments:
  frameworks:
  examples:
  stories:
  source_material:
  claims_requiring_evidence:

style:
  desired_voice:
  undesirable_tendencies:
  complexity_level:
  pacing:
  use_of_math:
  use_of_examples:
  use_of_metaphor:
```

If some values are unknown, infer provisional values only when reasonable and mark them:

```text
PROVISIONAL
```

Do not silently invent important authorial facts.

Do not show this form to the author. Fill it from the §0.4 interview.

---

# 2A. Phase 0 — Validate the Topic and Position the Book

Do this before the book specification. A well-written book on a topic nobody buys fails its purpose.

Skip this phase when the author writes for a fixed reason (a course, a client, a personal project) and sales do not matter.

## 2A.1 Validate demand

Find books on the candidate topic that already sell.

Sean's filters on Amazon:

```text
Best Sellers Rank (BSR) < 30,000   → the book sells well
reviews <= 100                     → competition is still low
category filter                    → e.g. self-help
```

Caveat: a book by a famous author can sell on the author's name alone. Exclude such books, or filter to self-published titles, before you conclude that a topic has demand.

Record the evidence in `market.demand_evidence`.

If you cannot read store data yourself (no web tool, or the store blocks automated reading), guide the author instead:

1. Give the exact search words to type into the Amazon search box.
2. Tell the author which numbers to copy back for the top 10 results: title, author, Best Sellers Rank (in "Product details"), number of reviews, and the date published.
3. Ask them to paste 5–10 of the most useful 1-star to 3-star reviews of the best matching books.
4. Do the analysis from what they paste.

If no data comes back, mark every demand claim `[UNVERIFIED CLAIM]` and say that the topic is not validated.

## 2A.2 Select comparable titles

Pick the best-selling books that are on the exact topic.

* Remove books that are off-topic.
* Remove books with few reviews; they give weak evidence of what readers value.
* Add titles the author supplies.

Use comparable titles to learn what structure and content readers reward.

Never copy their text, structure verbatim, or unique examples. The goal is a better book, not a cheaper copy.

## 2A.3 Find the competitive angle

Read the reviews of the comparable titles. List what readers praise, what they miss, and what they complain about.

Generate candidate angles. Sean's three angle types:

| Angle | Pattern | Example from the transcript |
|---|---|---|
| Niche down | Serve a subset of the audience that current books ignore | communication skills for introverts |
| Simpler / faster | Less theory, shorter practice | "5 minutes a day" communication |
| More value | More scenarios, worksheets, or tools | masterclass with 101 scenarios and worksheets |

For each angle, write the reasoning: which reader gap it fills, and which evidence shows the gap.

## 2A.4 Write the positioning

```yaml
positioning:
  unique_selling_proposition:
  differentiation:         # what this book does that comparable titles do not
  key_selling_points:
  target_audience:
```

## 2A.5 Generate title options

Generate several title and subtitle options. A good title:

* contains the words readers type into the store search
* states the benefit to the reader
* matches the chosen angle

Do not claim a keyword has search volume unless search data supports it. Mark such claims `[UNVERIFIED CLAIM]`.

## Gate 0 — Positioning

The author chooses the angle and the working title. Only then write the book specification.

---

# 3. Phase A — Build the Book Specification

Create a concise book specification before doing any substantial writing.

Output:

```markdown
# Book Specification

## Working Title

## Central Thesis

## Reader

## Reader's Starting State

## Reader's Desired End State

## Core Promise

## Unique Selling Proposition

## Differentiation from Comparable Titles

## Scope

## Explicit Exclusions

## Tone

## Intellectual Level

## Structural Archetype

## Target Length

## Chapter Count

## Primary Sources

## Key Constraints
```

---

## 3.1 Define the reader transformation

Express the intended transformation as:

$$
R_0 \rightarrow R_1
$$

where:

* \(R_0\) = reader before the book
* \(R_1\) = reader after the book

Example:

```text
R0:
Understands LLMs conceptually but cannot design reliable agent systems.

R1:
Can reason about agent architecture, context, tools, memory,
evaluation, failure recovery, and orchestration well enough
to build production-grade systems.
```

This transformation should guide inclusion and exclusion decisions.

---

## 3.2 Define the book's governing question

Write one question that the entire book answers.

Example:

> How can a technically sophisticated individual design AI agents that remain reliable as tasks become longer, messier, and less deterministic?

Every chapter should contribute materially to answering this question.

---

## 3.3 Establish scope boundaries

Explicitly identify what the book will not attempt to cover.

This prevents topic drift.

Example:

```text
IN SCOPE:
- agent architecture
- context engineering
- tool use
- memory
- orchestration
- evaluation

OUT OF SCOPE:
- introductory Python
- generic ML history
- basic transformer derivations
- vendor-specific API walkthroughs
```

---

# 4. Phase B — Ingest Source Material

Collect all material that should influence the manuscript.

Sources may include:

* notes
* essays
* papers
* transcripts
* books
* interviews
* URLs
* datasets
* personal journals
* lectures
* prior writing
* diagrams
* research summaries

If the author has no notes or sources, run the author-interview skill in **knowledge** mode, one chapter area per session. Each saved interview file is a source with `type: author interview` (Class A for what happened to the author; any general fact in it still needs checking).

Create a source ledger.

```yaml
sources:
  - id: S001
    title:
    author:
    type:
    location:
    relevance:
    reliability:
    key_topics:
```

---

## 4.1 Separate source material from model knowledge

Maintain three epistemic classes:

### Class A — supplied source

Directly supported by source material provided for the book.

### Class B — externally verified

Added through explicit research and backed by a source.

### Class C — synthesis

Reasoning, interpretation, explanation, analogy, or structure generated by the author/AI.

Do not present Class C material as though it were Class A or B.

---

# 5. Phase C — Construct the Author Persona

The purpose of the persona is to maintain consistent voice and perspective.

Sean emphasizes defining author background and supplying representative writing samples before generating the book.

In his demo Sean has the AI generate the writing sample "to save a little bit of time". Do not copy that shortcut. A sample the AI wrote teaches the AI its own generic voice. Use it only as a placeholder labelled `AI-WRITTEN PLACEHOLDER`, and replace it by a §5.2 method before Phase H starts.

Create:

```markdown
# Author Persona

## Background

## Relevant Experience

## Domain Knowledge

## Motivations

## Intellectual Style

## Writing Voice

## Voice Source

## Typical Sentence Structure

## Preferred Explanatory Devices

## Level of Formality

## Humor

## Use of Personal Stories

## Use of Equations

## Use of Analogies

## Things This Author Would Never Say

## Recurring Stylistic Failure Modes to Avoid

## Inspired-By Authors

## Author Bio
```

Build the author bio only from facts the author supplies. The bio appears in the book and on the store page.

Background can be personal experience instead of a profession. Sean's example: no professional credential, but a lifelong struggle with social anxiety that he overcame. That is valid, if it is true. Never upgrade it into an invented credential.

---

## 5.1 Learn style from writing samples

Extract style dimensions from supplied writing samples.

Analyze:

$$
V =
(
L,
S,
D,
F,
M,
E,
H,
R
)
$$

where:

* \(L\) = lexical complexity
* \(S\) = sentence structure
* \(D\) = density
* \(F\) = formality
* \(M\) = metaphor frequency
* \(E\) = example frequency
* \(H\) = humor
* \(R\) = rhetorical style

Do not copy characteristic phrases verbatim.

Infer the abstract style.

---

## 5.2 No writing samples

Many authors have no finished writing to supply. Do not stop, and do not invent a sample. Try these methods in order. Go to the next method only when the one before it produces nothing usable.

1. **Find writing the author already has.** Ask for emails, social media posts, long text messages, newsletters, speeches, talk or podcast transcripts, and school or work essays. Informal real writing is better than no writing.
2. **Interview the author** (author-interview skill, **voice** mode). Ask 6–8 open questions about the book's topic, for example "Tell me about the first time this went wrong." The author answers in their own words, typed or dictated. Use the answers as the writing sample. Keep the author's words as they said them; do not polish them before the style analysis.
3. **Choose by reaction.** Write one short paragraph on the book's topic in 3 clearly different voices. The author picks one and says what to change. Repeat for 2–3 rounds. Record the final choice and every correction.
4. **Describe in words.** Ask which authors the author likes and how they want to sound. Convert the answer into the §5.1 dimensions (for example "short sentences, dry humour, few metaphors"). Never copy a real author's sentences.

Rules:

* **Record the voice source.** Fill `## Voice Source` in the persona with one of: `real writing`, `interview`, `chosen by reaction`, `described`, or `AI-WRITTEN PLACEHOLDER`. Any source other than `real writing` or `interview` marks the voice `PROVISIONAL`.
* **Calibrate after the first section.** The author reads the first drafted section and names every sentence that does not sound like them. Add those corrections to the persona under `## Recurring Stylistic Failure Modes to Avoid` and `## Things This Author Would Never Say`. The Phase I voice check and Pass 4 then use the corrected persona.
* **Replace the placeholder.** An `AI-WRITTEN PLACEHOLDER` voice must be replaced by method 1, 2, 3 or 4 before Phase H starts.

---

# 6. Phase D — Build the Concept System

Before creating chapters, identify the intellectual primitives of the book.

Sean's workflow uses selected focus concepts that later propagate into the outline.

Create:

```yaml
concepts:
  - name:
    definition:
    why_it_matters:
    dependencies:
    examples:
    misconceptions:
    evidence_needed:
```

---

## 6.1 Build a dependency graph

Represent dependencies as:

$$
C_i \rightarrow C_j
$$

meaning:

> Concept \(C_i\) should be understood before \(C_j\).

Example:

```text
tokens
  ↓
context window
  ↓
context engineering
  ↓
agent state
  ↓
memory
  ↓
long-horizon agents
```

Use this graph to determine chapter order.

---

## 6.2 Identify recurring frameworks

If the book contains reusable mechanisms, name and define them before drafting.

For example:

```text
Observe → Model → Decide → Act → Verify
```

or:

$$
\text{Reliability}
=
\text{Planning}
\times
\text{Execution}
\times
\text{Verification}
\times
\text{Recovery}
$$

A framework should recur consistently across chapters.

---

# 7. Phase E — Choose the Book Architecture

Specify:

* target word count
* chapter count
* approximate chapter sizes
* structural archetype

Possible archetypes include:

### How-to

```text
problem
→ principles
→ methods
→ implementation
→ advanced practice
```

### Problem → solution

```text
symptoms
→ causes
→ model
→ intervention
→ validation
```

### Conceptual ladder

```text
fundamentals
→ intermediate abstractions
→ advanced synthesis
```

### Historical-developmental

```text
origin
→ competing ideas
→ breakthroughs
→ current state
→ future questions
```

### Case-driven

```text
case
→ problem
→ analysis
→ principles
→ generalized lesson
```

### Story + lessons (memoir-based advice)

```text
where I started
→ what went wrong
→ turning point
→ what I learned (one lesson per chapter, each tied to a part of the story)
→ how the reader can apply it
```

A common first book. Every story event must come from the author (§1.5); the lessons are the author's, and general claims in them still go through Pass 7.

---

## 7.1 Establish word budgets

Let:

$$
W_T = \text{target words}
$$

$$
W_i = \text{chapter } i \text{ budget}
$$

Require:

$$
\sum_{i=1}^{N} W_i \approx W_T
$$

Then subdivide:

$$
W_i =
\sum_{j=1}^{m_i} W_{ij}
$$

This prevents severe length imbalance.

---

# 8. Phase F — Generate the Chapter Architecture

Generate chapter-level structure first.

For each chapter specify:

```yaml
chapter:
  number:
  title:
  purpose:
  reader_question:
  starting_state:
  ending_state:
  key_claims:
  concepts_introduced:
  concepts_reused:
  evidence_needed:
  examples:
  dependencies:
  transition_to_next_chapter:
  word_budget:
```

---

## 8.1 Validate chapter necessity

For each chapter ask:

> If this chapter disappeared, would the reader's path from \(R_0\) to \(R_1\) materially weaken?

If not, merge or remove it.

---

## 8.2 Avoid chapter duplication

For every pair of chapters \(i,j\), estimate conceptual overlap:

$$
O_{ij}
=
\frac{|C_i \cap C_j|}
{|C_i \cup C_j|}
$$

High overlap should trigger inspection.

Repeated concepts are acceptable only when they are:

* deliberately revisited
* expanded
* applied differently
* used as prerequisites

not merely re-explained.

---

# 9. Phase G — Generate the Detailed Hierarchical Outline

This is the last major stage before prose generation.

Sean's workflow decomposes chapters into sections and subsections and attaches writing direction to those nodes.

Use at least:

```text
Book
  Chapter
    Section
      Subsection
```

For complex books:

```text
Book
  Part
    Chapter
      Section
        Subsection
```

---

## 9.1 Every subsection must contain writing direction

Bad:

```text
3.2 Context Windows
```

Good:

```yaml
3.2 Context Windows

purpose:
  Explain why finite context changes agent architecture.

claims:
  - context is an active computational resource
  - retrieval does not eliminate context-selection problems
  - irrelevant context can degrade performance

examples:
  - long coding session
  - multi-agent handoff

dependencies:
  - tokens
  - attention

evidence:
  - relevant context-window research
  - benchmark examples

transition:
  Leads into context engineering.
```

---

## 9.2 Outline quality gate

Do not draft until:

* every chapter has a distinct function
* every section has a purpose
* every subsection advances an argument
* concept dependencies are respected
* evidence requirements are identified
* major examples are placed
* word budgets are plausible
* transitions are understood

---

# 10. Phase H — Draft Sequentially

Generate one meaningful section at a time.

Sean specifically recommends this because the next section can account for prior sections, reducing repetition and increasing continuity.

For section \(S_n\), provide:

$$
S_n =
f(
O_n,
B,
V,
C,
S_{1:n-1}
)
$$

where:

* \(O_n\) = section outline
* \(B\) = book specification
* \(V\) = author voice
* \(C\) = concept system
* \(S_{1:n-1}\) = relevant prior manuscript

---

## 10.1 Drafting prompt template

For every section:

```text
Write the next section of the manuscript.

BOOK:
[book specification]

AUTHOR VOICE:
[author persona]

SECTION PURPOSE:
[...]

READER QUESTION:
[...]

KEY CLAIMS:
[...]

CONCEPTS:
[...]

EVIDENCE AVAILABLE:
[...]

EXAMPLES:
[...]

RELEVANT PRIOR TEXT:
[...]

NEXT SECTION:
[...]

WORD BUDGET:
[...]

Requirements:

1. Advance the argument; do not merely restate prior material.
2. Preserve terminology established earlier.
3. Refer naturally to earlier concepts when useful.
4. Introduce only concepts required at this point.
5. Distinguish evidence from interpretation.
6. Do not fabricate facts, sources, quotes, examples, or author experiences.
7. Avoid generic introductions and summaries.
8. Avoid listicle-style prose unless the content genuinely requires a list.
9. End in a way that creates a logical bridge to the next section.
```

---

# 11. Phase I — Section-Level Review

After every generated section, inspect it before continuing.

Use this checklist.

### Argument

* What claim is this section making?
* Is the claim clear?
* Has it actually been supported?
* Does each paragraph contribute?

### Novelty

* Does it merely repeat earlier text?
* Is a previously introduced idea being extended?

### Voice

* Does it match the author persona?
* Does it sound like a generic LLM?
* For the first drafted section: has the author read it and corrected the voice (§5.2)?

### Specificity

Replace vague prose such as:

> AI agents can be very powerful.

with precise statements such as:

> Tool-using agents expand the model's effective action space from token generation to operations over external state.

### Evidence

* Which claims require citations?
* Which claims are interpretation rather than established fact?

### Continuity

* Does terminology match previous sections?
* Are earlier concepts referenced correctly?
* Does the ending prepare the next section?

### Fact-check and originality

* Fact-check the section immediately after generation. Do not wait for Pass 7.
* Run the fact-check again after every edit that changes a claim.
* Run a plagiarism check against the comparable titles and the supplied sources. The AI can compare only against texts it has been given. For the rest of the web, ask the author to paste the section into an online plagiarism checker and report the result. Never record a check as passed unless one actually ran; otherwise record `plagiarism check: not run`.

Only then proceed.

---

# 12. Phase J — Chapter-Level Coherence Pass

After finishing a chapter, inspect it as a unit.

Create:

```yaml
chapter_review:
  thesis:
  reader_start_state:
  reader_end_state:
  major_claims:
  repeated_material:
  missing_prerequisites:
  unsupported_claims:
  terminology_conflicts:
  transition_quality:
  revisions_required:
```

---

## 12.1 Chapter compression test

Summarize the chapter in:

* one sentence
* one paragraph
* five bullet points

If this cannot be done coherently, the chapter may lack a clear architecture.

---

# 13. Phase K — Manuscript Editorial Passes

After the complete first draft exists, do not perform one generic "edit."

Perform distinct passes.

---

# Pass 1 — Structural Coherence

Read the manuscript at chapter level.

Check:

* chapter order
* missing prerequisites
* premature concepts
* dead-end ideas
* duplicated chapters
* weak transitions
* missing synthesis

Construct:

$$
G=(V,E)
$$

where:

* \(V\) = major concepts
* \(E\) = prerequisite/reference relationships

Look for:

* disconnected nodes
* cycles caused by bad exposition order
* concepts used before introduction
* concepts introduced and never reused

Revise structure before sentence-level polishing.

---

# Pass 2 — Argument Integrity

For every major claim, reconstruct:

$$
\text{Premises}
\rightarrow
\text{Inference}
\rightarrow
\text{Conclusion}
$$

Check for:

* missing premises
* invalid inference
* overstatement
* correlation interpreted as causation
* anecdote presented as evidence
* false precision
* unstated assumptions

Mark weak reasoning:

```text
[ARGUMENT GAP]
```

Then repair it.

---

# Pass 3 — Repetition and Redundancy

Search for semantic repetition, not merely duplicate wording.

For each repeated concept ask:

### Is repetition pedagogically useful?

If yes, preserve it but explicitly build on prior knowledge.

### Is it accidental?

If yes:

* remove it
* compress it
* cross-reference earlier discussion
* replace repetition with extension

A useful model:

$$
I_n
=
\text{new information introduced by section } n
$$

Aim to maximize:

$$
\frac{I_n}{W_n}
$$

without making the prose unnaturally dense.

---

# Pass 4 — Voice Consistency

Compare every chapter against the author persona.

Look for drift into:

* textbook voice
* generic AI voice
* marketing copy
* motivational cliché
* excessive rhetorical questions
* repeated "not X, but Y" constructions
* excessive headings
* overly symmetrical sentence patterns
* unnecessary conclusions
* fake quotations
* invented anecdotes

Rewrite outliers.

---

# Pass 5 — Explanatory Quality

For every difficult concept, check whether the manuscript contains the appropriate combination of:

$$
E =
D + I + M + X
$$

where:

* \(D\) = definition
* \(I\) = intuition
* \(M\) = mechanism
* \(X\) = example

For mathematical material consider:

$$
E =
D + I + M + X + F
$$

where \(F\) = formalism.

Do not force all five components where unnecessary.

---

# Pass 6 — Examples, Stories, and Applications

Inspect abstract sections for insufficient grounding.

Add one or more of:

* worked example
* counterexample
* case study
* thought experiment
* analogy
* diagram
* table
* personal story supplied by the author
* practical exercise
* call to action (how-to books: tell the reader the next thing to do)

Never fabricate real-world case studies or personal experiences.

If a needed example is unavailable:

```text
[CASE STUDY NEEDED]
```

Honest ways to fill it: the author's own trial of the method; a friend or client who gives permission to be described; a published case, with a citation; or an imagined example that is clearly labelled as imagined ("Imagine a nurse who…").

---

# Pass 7 — Targeted Research, Fact-Checking, and Citation Strengthening

Inspect every factual, empirical, historical, quantitative, or attribution-dependent claim.

Sean's editing workflow explicitly includes strengthening text with historical facts, quotations, sources, citations, studies, and data.

**No search tool.** If you cannot search the web, do not verify from memory. Keep every material claim `[UNVERIFIED CLAIM]`, and give the author a checklist: each claim, the exact search words to use, and the kind of source that would settle it (a government agency, a professional body, a named study). Update the ledger from what the author reports.

**High-risk topics.** For claims about health, medicine, food safety, law, money, or physical safety, a qualified person (for example a doctor, dietitian, lawyer, or accountant, as fits the claim) must review them before the book is final. Record the reviewer and date in the claim ledger, or record `expert review: not done` and tell the author the book is not ready.

## 7.1 Identify claims requiring verification

Examples:

* statistics
* dates
* scientific claims
* technical claims
* historical claims
* quotations
* named studies
* causal claims
* claims about companies or institutions
* precise numerical statements
* superlatives
* claims of first/only/largest/fastest

---

## 7.2 Search specifically

Do not broadly research the entire chapter.

Search the smallest question needed to verify the claim.

Bad:

```text
research social anxiety
```

Better:

```text
US adult lifetime prevalence social anxiety disorder
```

Better still:

```text
NIMH lifetime prevalence social anxiety disorder US adults
```

The objective is:

$$
\text{Research Scope}
\rightarrow
\min
$$

subject to:

$$
\text{Evidence sufficient to evaluate claim}
$$

---

## 7.3 Prefer authoritative evidence

Approximate source hierarchy:

```text
primary research / official dataset
        ↓
systematic review / meta-analysis
        ↓
major academic or institutional source
        ↓
high-quality secondary analysis
        ↓
general web source
```

The hierarchy may differ by discipline.

Use the most appropriate original evidence available.

---

## 7.4 Classify every researched claim

Assign:

$$
C \in
\{
V,Q,U,X
\}
$$

where:

* \(V\) = verified
* \(Q\) = qualified support
* \(U\) = uncertain
* \(X\) = contradicted

Then act accordingly.

### Verified

Retain and cite.

### Qualified support

Narrow the prose.

Example:

```text
Before:
X causes Y.

After:
Several observational studies report an association between X and Y.
```

### Uncertain

Remove or explicitly communicate uncertainty.

### Contradicted

Correct the text.

---

## 7.5 Strengthen important claims

Where it materially improves the manuscript, add:

* primary citation
* statistic
* historical example
* experiment
* dataset
* expert quotation
* table
* figure

Do not add evidence merely to decorate prose.

---

## 7.6 Never fabricate evidence

Never invent:

* papers
* authors
* study titles
* quotations
* DOI numbers
* URLs
* statistics
* institutions
* publication dates

If evidence cannot be located:

```text
[UNVERIFIED CLAIM]
```

or rewrite the claim.

---

## 7.7 Maintain a claim ledger

```yaml
claim_id: CH04-S03-C02
chapter: 4
section: 3
claim: ""
claim_type: empirical
source:
source_type:
verification_status: verified
citation_added: true
qualification_needed: false
notes:
```

---

## 7.8 Evidence quality gate

A chapter passes when:

$$
N_{\text{unsupported material claims}}
=
0
$$

or any unresolved uncertainty is explicitly communicated.

---

# Pass 8 — Terminology and Concept Consistency

Build a glossary of important terms.

```yaml
term:
preferred_definition:
first_introduced:
allowed_synonyms:
forbidden_variants:
```

Check that the book does not accidentally use several names for the same concept.

Example:

```text
agent state
working state
runtime memory
active context state
```

If these represent the same concept, normalize them.

If they represent different concepts, explicitly distinguish them.

---

# Pass 9 — Cross-Chapter Continuity

Inspect backward and forward references.

Look for:

* "as discussed earlier" where it was not discussed
* references to future concepts not yet introduced
* examples reused inconsistently
* frameworks changing names
* equations whose variables change meaning
* repeated definitions that differ subtly

Create a continuity ledger if necessary.

```yaml
concept:
introduced_in:
expanded_in:
referenced_in:
final_synthesis:
```

---

# Pass 10 — Prose Quality

Now perform sentence-level editing.

Optimize:

* clarity
* precision
* rhythm
* paragraph structure
* sentence variation
* transitions
* concision

Remove:

* filler
* clichés
* generic openings
* generic conclusions
* unnecessary adverbs
* empty intensifiers
* redundant qualifiers
* canned AI phrases

Prefer:

$$
\text{precision} > \text{ornament}
$$

---

# Pass 11 — Compression Without Information Loss

Try to reduce unnecessary words while preserving:

* argument
* evidence
* examples
* nuance
* voice

For candidate edit:

$$
Q =
\frac{\text{meaning preserved}}
{\text{words}}
$$

Seek higher \(Q\), but do not compress pedagogically useful explanation.

---

# Pass 12 — Reader Simulation

Simulate representative readers.

For each reader type ask:

```text
What would confuse me?

What prerequisite am I missing?

Where would I stop reading?

Which claim would I challenge?

Which example would I want?

What seems obvious?

What seems unsupported?

What would I want explained mathematically?

What feels unnecessarily difficult?
```

Repeat for:

* novice reader
* target reader
* skeptical expert

Do not modify the book automatically based on every simulated objection.

Use simulation to surface possible weaknesses.

---

# Pass 13 — Final Manuscript Integrity

Before declaring the manuscript complete, verify:

### Structure

* chapter order is coherent
* TOC matches manuscript
* numbering is correct
* headings are consistent

### Content

* no placeholders remain
* no duplicated sections remain
* no orphan concepts remain
* no contradictory definitions remain

### Evidence

* citations resolve
* bibliography entries exist
* quotations are accurate
* data values match cited sources
* every in-text citation has an entry in the reference section

### Originality

* the plagiarism check passes on the full manuscript (a real check by a real tool, recorded with its date; not the AI's own judgement)
* no passage copies a comparable title

### Voice

* author persona is consistent
* no unexplained style shifts exist

### Technical integrity

* equations are defined
* tables are referenced
* figures are referenced
* acronyms are expanded on first use

---

# 14. Human-in-the-Loop Gates

The agent must pause conceptually at these quality gates.

## Gate A — Book specification

Do not outline until the central thesis and reader transformation are coherent.

## Gate B — Concept system

Do not outline until major concepts and dependencies are identified.

## Gate C — Chapter architecture

Do not generate detailed sections until chapter purposes are distinct.

## Gate D — Detailed outline

Do not draft until the outline is sufficiently specific to guide prose.

## Gate E — Section review

Do not automatically generate hundreds of pages without periodic review.

## Gate F — Structural edit

Do structural edits before sentence polishing.

## Gate G — Evidence verification

Do not finalize empirical nonfiction before verifying material claims.

## 14.1 Ask the author plain questions at each gate

A first-time author cannot judge "coherence". Before each approval, check the work yourself, name its weakest point, then ask 3–5 yes/no questions such as:

| Gate | Questions for the author |
|---|---|
| 0 | Would you buy this book? Does the title say what the reader gets? |
| A | Is the reader someone you know or have been? Can you picture them at the start and at the end? Is anything in the "left out" list something you want in? |
| B | Is anything a beginner needs missing from the list? Is the order the order you learned it? |
| C | Can you say in one sentence why each chapter is there? Do any two chapters feel the same? |
| D | Could you explain each section to a friend from its brief? Is every story it asks for one you really have? |
| E | Does this section sound like you? Is anything in it untrue about you? |
| G | Has every health, money, legal, or safety claim been checked or reviewed? |

Show one good and one weak example when the author is unsure what to look for.

---

# 15. Recommended Project Structure

```text
book/
│
├── BOOK.md
├── README.md
│
├── specification/
│   ├── positioning.md
│   ├── book-spec.md
│   ├── audience.md
│   ├── author-persona.md
│   ├── style-guide.md
│   └── glossary.md
│
├── concepts/
│   ├── concepts.yaml
│   ├── frameworks.md
│   └── dependency-graph.md
│
├── sources/
│   ├── source-ledger.yaml
│   ├── papers/
│   ├── notes/
│   ├── transcripts/
│   └── excerpts/
│
├── outline/
│   ├── architecture.md
│   ├── full-outline.md
│   └── word-budget.yaml
│
├── manuscript/
│   ├── introduction.md
│   ├── chapter-01.md
│   ├── chapter-02.md
│   ├── chapter-03.md
│   └── conclusion.md
│
├── research/
│   ├── claims.yaml
│   ├── verification-notes/
│   └── references.bib
│
├── reviews/
│   ├── structural-review.md
│   ├── repetition-review.md
│   ├── voice-review.md
│   ├── evidence-review.md
│   └── final-review.md
│
├── final/
│   └── manuscript.md
│
└── production/
    ├── store-description.md
    ├── cover/
    └── marketing/
```

---

# 16. Agent State

Maintain a compact state file.

```yaml
book_state:

  current_phase:
  current_chapter:
  current_section:

  completed_chapters: []

  concepts_introduced: []

  concepts_pending: []

  unresolved_questions: []

  claims_needing_verification: []

  author_input_needed: []

  structural_issues: []

  continuity_notes: []

  next_action:
```

Update after every meaningful writing operation.

---

# 17. Context Management

Do not send the entire manuscript into every generation request unless necessary.

For section \(S_n\), assemble context from:

$$
K_n =
B + V + O_n + G_n + R_n
$$

where:

* \(B\) = compact book spec
* \(V\) = author persona
* \(O_n\) = current outline node
* \(G_n\) = relevant glossary/concepts
* \(R_n\) = retrieved prior passages relevant to the current section

This preserves continuity without overwhelming the context window.

---

# 18. Retrieval Strategy

Retrieve previous manuscript sections based on:

* concepts referenced
* prior definitions
* recurring examples
* unresolved arguments
* chapter dependencies

Do not retrieve merely because text is nearby.

Use semantic relevance over proximity.

---

# 19. Anti-Patterns

Never use these as the primary workflow.

## One-shot book generation

```text
Write a 50,000-word book about X.
```

## Outline-only generation followed by autonomous completion

```text
Here is the table of contents.
Write everything.
```

## Evidence-afterthought workflow

```text
Write confidently now.
Find citations later.
```

## Style-by-adjective

```text
Write intelligently and engagingly.
```

Instead provide writing samples and an explicit persona.

## Unbounded elaboration

Do not expand every section merely because more words are possible.

The criterion is:

$$
\text{Does this improve reader understanding?}
$$

not:

$$
\text{Can more text be generated?}
$$

---

# 20. Quality Function

Think of manuscript quality as approximately:

$$
Q =
S
\times
A
\times
C
\times
E
\times
V
\times
R
$$

where:

* \(S\) = structural quality
* \(A\) = argument quality
* \(C\) = coherence
* \(E\) = evidential quality
* \(V\) = voice consistency
* \(R\) = readability

The multiplicative model is intentional.

A severe failure in one dimension can undermine the entire manuscript.

A beautifully written but factually unreliable book is poor.

A rigorously sourced but structurally incoherent book is poor.

A logically strong but unreadable book is poor.

---

# 21. Master Workflow

Execute in this order:

```text
0. Start from nothing: plain words, book folder, expectations, intake interview, knowledge check (§0)
       ↓
1. Gather author inputs
       ↓
1a. Validate topic, select comparable titles, choose angle and title (Phase 0, optional)
       ↓
2. Create book specification
       ↓
3. Ingest sources
       ↓
4. Construct author persona
       ↓
5. Build concept system
       ↓
6. Choose book architecture
       ↓
7. Design chapters
       ↓
8. Generate detailed hierarchical outline
       ↓
9. Human review of outline
       ↓
10. Draft one section
       ↓
11. Review/edit section
       ↓
12. Update book state
       ↓
13. Draft next section using relevant prior context
       ↓
14. Complete chapter
       ↓
15. Chapter coherence review
       ↓
16. Repeat until first draft complete
       ↓
17. Structural coherence pass
       ↓
18. Argument integrity pass
       ↓
19. Repetition pass
       ↓
20. Voice consistency pass
       ↓
21. Explanatory-quality pass
       ↓
22. Example/application pass
       ↓
23. Targeted research + fact-checking + citation pass
       ↓
24. Terminology consistency pass
       ↓
25. Cross-chapter continuity pass
       ↓
26. Prose-quality pass
       ↓
27. Compression pass
       ↓
28. Reader simulation
       ↓
29. Final manuscript integrity check
       ↓
30. Final manuscript
       ↓
31. Production and publishing (section 23, optional)
```

---

# 22. Definition of Done

The book is complete only when all of the following are true.

## Architecture

* Every chapter has a distinct purpose.
* Concept order respects prerequisites.
* The narrative advances rather than circles.

## Argument

* Major conclusions are supported.
* Material assumptions are explicit.
* Evidence and interpretation are distinguished.

## Sources

* Material factual claims are supported.
* Quotations are verified.
* Citations resolve.
* No references were fabricated.
* High-risk claims (health, food safety, law, money, physical safety) have a recorded expert review (Pass 7).

## Voice

* The manuscript consistently resembles the intended author.
* Personal stories are authentic.
* AI-generated stylistic artifacts have been removed.

## Coherence

* Terminology is stable.
* Cross-references are accurate.
* Earlier concepts are reused intelligently.
* Later chapters build on earlier chapters.

## Pedagogy

* Difficult concepts have sufficient explanation.
* Examples appear where abstraction becomes difficult.
* Reader prerequisites are respected.

## Prose

* Redundancy is controlled.
* Paragraphs have clear functions.
* Sentences are precise.
* The manuscript does not read like concatenated AI essays.

## Integrity

The final text should feel like:

$$
\boxed{
\text{one author}
+
\text{one intellectual architecture}
+
\text{one continuous argument}
}
$$

rather than:

$$
\text{many independently generated chapters}
$$

---

# 23. Production and Publishing (optional)

Start this only after the Definition of Done is met. These steps package the book. They do not change its content.

For a first-time author, run the kdp-publishing skill: it covers the account, tax and bank details, the AI-content question, ISBN, formatting, cover, price, and upload, step by step. KDP asks whether a book contains AI-generated text or images; a book drafted with this skill contains AI-generated text, so the honest answer is yes.

## 23.1 Interior formatting

Choose a style, body font, and line spacing. Sean's example: "modern" style, 12 pt body, 1.5 line spacing, drop caps optional.

Download the formatted manuscript and record its final page count. The cover spine depends on it.

## 23.2 Store description

Write the store description from the positioning (Phase 0). Every claim in it must also be true of the manuscript.

## 23.3 Cover

1. Front cover: title, subtitle, author name. A best-selling cover in the same category can serve as a style reference. Do not copy it.
2. Back cover: copy that states the benefit, plus the author bio.
3. Spine: set its size from the final page count. Leave the barcode area clear.
4. Make a separate cover file for each format (paperback, hardcover).

## 23.4 Marketing assets

Optional: store page graphics (Amazon calls them A+ content), a book trailer or ad video, and translations.

Every quote, review, or testimonial in a marketing asset must be real. Never publish invented reader reviews.

## 23.5 Publish

Sean publishes on Amazon KDP. It is free to join and uses print-on-demand: Amazon prints a copy only after a sale.

Sean states that more than 70% of US book sales happen on Amazon. Treat that figure as `[UNVERIFIED CLAIM]` until checked.

---

# Core Instruction to the Writing Agent

You are the author's co-author and editorial system.

Your job is not to maximize generated text.

Your job is to help the author produce a coherent, rigorous, distinctive manuscript.

Prioritize, in order:

1. intellectual coherence
2. fidelity to the author's ideas and sources
3. factual reliability
4. explanatory clarity
5. continuity
6. authorial voice
7. prose quality
8. concision

Never fabricate author experience, sources, quotations, evidence, or facts.

Do not begin prose generation until the relevant specification and outline are sufficiently developed.

Generate long-form prose sequentially and maintain continuity with earlier manuscript state.

Treat every generated passage as editable first-draft material.

The human author remains the final authority over the manuscript.
