# Claim ledger and verification

Every claim that the text does not prove or compute in place enters
`research/claims.yaml`.

## 1. Claims that enter the ledger

- A result cited from a source.
- A numerical value not computed in the text: constants, material properties,
  measured data, benchmark results.
- A historical date, priority claim, or attribution of a named theorem.
- An algorithm complexity or convergence-rate claim that the text does not prove.
- An empirical claim about a method, device, or system.
- A "first", "only", "largest", or "fastest" claim.

## 2. Evidence classes

| Class | Meaning | Required reference |
|---|---|---|
| `proved_here` | the text proves it | section anchor |
| `proved_earlier` | an earlier chapter proves it | result id and link |
| `cited` | a source proves it; the book does not | source id, result label, page, read from the PDF |
| `numerical_check` | a computation supports it; no proof | script path and output |
| `measured` | an experiment reports it | source, value, uncertainty, conditions |
| `empirical` | observed across studies; no single measurement | sources and the scope of the observation |
| `heuristic` | synthesis or rule of thumb | labeled as heuristic in the text |

The class appears in the prose next to the claim, not only in the ledger.

## 3. Verification status

| Status | Meaning | Action |
|---|---|---|
| V | verified | keep and cite |
| Q | qualified support | narrow the claim to what the source supports |
| U | uncertain | remove it, or state the uncertainty in the text |
| X | contradicted | correct the text |

Example of a Q action: "the scheme converges" becomes "the scheme converges for
smooth initial data under the hypotheses of the cited theorem".

## 4. Source order by claim type

| Claim type | Prefer | Then |
|---|---|---|
| Mathematical result | the original paper or a standard monograph, with label and page | lecture notes from a named course |
| Physical constant | CODATA values as published by NIST | a handbook that cites CODATA |
| Material or tissue property | the primary measurement paper, with conditions | a handbook table that names its source |
| Method performance | the paper with its setup and baselines | a reproduction study |
| History and attribution | the original publication | a scholarly history |

## 5. Search the smallest question

Search for the narrowest fact that settles the claim. Example:

- Broad: "finite difference stability".
- Narrow: "Lax–Richtmyer equivalence theorem exact hypotheses, Lax and
  Richtmyer 1956, Communications on Pure and Applied Mathematics".

Then open the PDF and read the page. Never repair a citation from memory. If the
PDF is not in the repo, mark the claim `cited_unverified` in `BOOK-STATE.yaml`.

## 6. Ledger entry

```yaml
- claim_id: CH04-S02-C01
  location: chapters/ch04.html#vn-stability
  claim: ""
  class: cited
  source: S003
  label: Theorem 2.1
  page:
  status: V
  checked_by: read PDF page | ran script | author
  qualification:
  notes:
```

## 7. Gate

A chapter passes when no material claim has status U or X, and no `cited`
claim lacks a page. An unresolved claim may remain only if the text states its
uncertainty.
