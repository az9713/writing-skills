# Changelog — science-editor skill

## 2026-09-07 — Created from `EDITOR_PROMPT.md`

- Split the source prompt in two. The generic editor persona (role, reader, five-part
  standard, style, structure, delivery) became `SKILL.md`. The `# Domain:` section,
  which describes a neural-operator course and not the repo it sat in, became
  `references/example-domain-neural-operators.md`, copied verbatim.
- Added `references/domain-brief-template.md` so a new manuscript gets a brief of the
  same shape. Fixes the observed problem: the prompt hard-coded one project's lab
  numbers and file paths, so it could not edit any other manuscript.
- Added a "load the domain brief" lookup order to `SKILL.md` (root domain file, then
  project docs, then assemble from the repo and say so). Fixes: the skill fires in
  repos with no brief and must not invent ground truth.
- Added a "Numbers, sources, and grades" section that generalises the neural-operator
  evidence-grade rules (check every number, grades are part of the claim, never
  repair a citation from memory) so they survive the split.
- Added a "Scope of the edit" section: report the edit, apply only when asked.
