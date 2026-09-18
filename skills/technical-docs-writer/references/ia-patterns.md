# Information Architecture Patterns

Doc structures by project type. Choose the one that matches the project, then adapt.

---

## Library / SDK

A reusable package that developers import into their own projects.

```
docs/
├── index.md                   ← what it is, install command, 3-line usage example
├── getting-started/
│   ├── installation.md        ← npm/pip/cargo install + verify
│   └── quickstart.md          ← working example in <10 lines of code
├── guides/
│   ├── common-use-case-1.md
│   └── common-use-case-2.md
├── reference/
│   ├── api.md                 ← every exported function/class, complete signatures
│   └── configuration.md       ← config options table
├── CHANGELOG.md
└── CONTRIBUTING.md
```

**Key docs to get right:**
- `index.md` must have a working code sample in the first screenful
- API reference must be complete — every parameter, return value, and exception
- Quickstart must install + run without reading anything else

---

## CLI Tool

A command-line program users install and run in their terminal.

```
docs/
├── index.md                   ← what it does, install command
├── getting-started/
│   ├── installation.md        ← all install methods (npm, brew, binary, etc.)
│   └── quickstart.md          ← first real command with output
├── commands/                  ← one file per major command or command group
│   ├── overview.md            ← command summary table
│   ├── command-one.md         ← flags, arguments, examples, exit codes
│   └── command-two.md
├── guides/
│   └── common-workflow.md
├── reference/
│   ├── configuration.md       ← config file format, env vars
│   └── exit-codes.md
└── troubleshooting/
    └── common-issues.md
```

**Key docs to get right:**
- Commands reference: every flag, every argument, at least 2 examples per command
- Config reference: every field, default value, env var override
- Troubleshooting: the top 5 errors users actually hit

---

## API Service

An HTTP API that developers integrate with.

```
docs/
├── index.md                   ← base URL, auth method, first API call
├── getting-started/
│   ├── authentication.md      ← API keys / OAuth, token management
│   └── quickstart.md          ← authenticated request in 5 lines
├── guides/
│   ├── pagination.md
│   ├── error-handling.md
│   ├── webhooks.md            ← if applicable
│   └── rate-limits.md
├── reference/
│   ├── endpoints/             ← one file per resource
│   │   ├── users.md
│   │   └── orders.md
│   ├── errors.md              ← every error code, cause, fix
│   ├── types.md               ← shared object schemas
│   └── sdks.md                ← links to client libraries
├── changelog/
│   └── api-changelog.md
└── troubleshooting/
    └── common-issues.md
```

**Key docs to get right:**
- Every endpoint: method, path, auth required, request schema, response schema, error codes, curl example
- Errors reference: machine-readable code + human explanation + what to do
- Authentication: every auth method with a complete working example

---

## Platform / Product

A self-hosted platform with its own UI, API, and agent/worker model.

```
docs/
├── index.md
├── overview/
│   ├── what-is-this.md        ← mental model + architecture diagram
│   └── key-concepts.md        ← glossary
├── getting-started/
│   ├── prerequisites.md       ← system requirements
│   ├── installation.md        ← Docker / binary / cloud
│   ├── quickstart.md          ← running in <15 min
│   └── onboarding.md          ← zero-to-hero conceptual guide
├── concepts/                  ← one file per major subsystem
├── guides/                    ← task-oriented how-tos
├── reference/
│   ├── api.md                 ← REST/GraphQL reference
│   ├── configuration.md       ← all config options
│   └── env-vars.md            ← all environment variables
├── deployment/
│   ├── docker.md
│   ├── production.md
│   └── upgrading.md
├── architecture/
│   ├── system-design.md
│   └── adr/
└── troubleshooting/
    └── common-issues.md
```

---

## Multi-Component System

Multiple distinct components that integrate (e.g., Paperclip + gstack + Engineering Company).

```
docs/
├── index.md                   ← what each component is, how they fit together
├── overview/
│   ├── what-is-this.md        ← the combined system
│   └── key-concepts.md
├── getting-started/
│   ├── prerequisites.md
│   ├── quickstart.md          ← running the full system
│   └── onboarding.md
├── concepts/
│   ├── component-a.md         ← deep dive: Component A alone
│   ├── component-b.md         ← deep dive: Component B alone
│   └── integration.md         ← how they work together (the "bridge")
├── guides/
│   ├── end-to-end-workflow.md ← a real use case touching all components
│   └── component-specific/
├── reference/
│   ├── component-a-api.md
│   ├── component-b-config.md
│   └── integration-config.md
├── architecture/
│   ├── system-design.md       ← all components, data flows, interactions
│   └── adr/                   ← one ADR per non-obvious integration decision
└── troubleshooting/
    └── common-issues.md       ← issues specific to the integration
```

**Key docs to get right:**
- Each component doc must be useful standalone (someone might only be using one component)
- The integration doc explains the "bridge" — what problem it solves and exactly how it works
- ADRs for each major integration decision: why this approach vs. alternatives

---

## Product with End Users (add-on section)

Any of the patterns above can gain a `user-guide/` section when the project has users who never touch code — people who consume the product's output (a report, a film, a dashboard) or operate its UI. Bolt this onto the base pattern:

```
docs/
├── ...base pattern...
├── user-guide/
│   ├── <primary-user-task>.md     ← e.g. watching-the-film.md, reading-your-report.md
│   ├── <secondary-task>.md        ← sharing, exporting, customizing
│   └── faq.md                     ← real questions, answer-first
└── history/                       ← optional
    └── development-journey.md     ← build chronicle (link, don't recreate, if one exists)
```

**Key docs to get right:**
- The primary-task doc must work for a reader with zero repo knowledge — no paths, no commands
- The FAQ answers what users actually ask, including "how was this made?" and "can I trust it?" for AI-generated artifacts
- Developer docs and user docs never share a page: link between them, don't blend them

---

## Adapting Patterns

These are starting points, not rules. Adapt based on:

- **Scale**: small projects can collapse `concepts/` and `guides/` into a single `reference.md`
- **Audience**: internal-only tools can skip the onboarding zero-to-hero; public APIs need it
- **Existing docs**: if there's already a good README, build from it rather than replacing it
- **Missing pieces**: an index + quickstart + key-concepts is a good minimum viable doc set

The test: can a new engineer who has never seen the project open `index.md`, read `getting-started/quickstart.md`, and have a working system within 15 minutes?
