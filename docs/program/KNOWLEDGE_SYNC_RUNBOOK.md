# Knowledge Sync Runbook (Repository → Notion Mirror)

- Status: Active (Wave 0, program P02)
- Artifact class: program documentation (procedural; creates no knowledge of its own)
- Governing artifacts: Baseline L-9 (the repository is authoritative; the knowledge workspace is a mirror), Blueprint INV-9.

## 1. Direction and authority

- Sync is strictly **one-way**: GitHub repository (`main`) → Notion mirror.
- Only merged state on `main` is ever synced. Branch, draft, or PR state is never mirrored.
- On any conflict, the repository wins. The mirror is corrected; the repository is never edited to match the mirror.

## 2. Trigger

Run after any merge to `main` that changes governance, architecture, RFC, specification, program, or risk state — or on explicit Maintainer instruction.

## 3. Procedure

1. Identify all PRs merged to `main` since the last recorded sync (see the Ops Log tail).
2. For each affected artifact class, update the corresponding mirror surface:

   | Repository source | Mirror surface |
   | --- | --- |
   | `docs/decisions/` | ADR Log |
   | `docs/rfc/` | RFC Index |
   | `specs/` | Spec Index |
   | `docs/program/` | Engineering Operations |
   | risk changes | Risk Register |

3. Mirror status fields exactly as written in the repository; never paraphrase normative language.
4. Check for mirror rows without a repository counterpart; delete or flag them.
5. Append a sync entry to the Ops Log: date, merged PR numbers, surfaces touched.

## 4. Prohibitions

- Never create knowledge in the mirror that does not exist in the repository.
- Never sync unmerged branches, drafts, or chat-only artifacts.
- Never resolve a repository inconsistency by editing the mirror — the fix goes through a repository PR.

## 5. Current state

The first full sync under this runbook (P02.2) executes after the Wave 0 PR merges, because the mirror reflects `main` only.
