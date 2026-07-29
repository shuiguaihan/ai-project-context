---
name: sync-project-context
description: Archive original project inputs, compare new or revised evidence, and synchronize affected shared context, interfaces, risks, issues, responsibilities, schedules, checklists, tests, releases, and status records while preserving provenance. Use when users ask to ingest, archive, sync, or assess the impact of project materials; refresh project-wide information after new files or versions arrive; or keep a project's context consistent across documents. Support archive-only, read-only impact review, and authorized update modes. Do not use for ordinary source-code changes or isolated document editing that has no project-context impact.
---

# Sync Project Context

Maintain a project's evidence and truth layer when source materials arrive or change. Preserve originals first, extract only factual deltas, update the smallest justified document set, and keep proposals separate from confirmed baselines.

## Select The Mode

Infer the mode from the user's verb and scope:

- **Archive only**: preserve originals and record provenance; do not update project status.
- **Impact review**: inspect and report affected context; keep the workspace read-only.
- **Sync and update**: archive originals, analyze changes, and update affected project documents when the user asks to sync, update, ingest, or incorporate the materials.

Do not broaden a review request into writes. Treat an explicit request to update or sync project context as authorization for normal in-scope document edits and validation, but not for deletion, external publishing, or unrelated code changes.

## Run The Workflow

1. **Locate the project root and rules.** Read the nearest applicable `AGENTS.md` files and the project's lifecycle-document entry. Follow existing directory, naming, ownership, and status conventions. Do not edit `AGENTS.md` unless the user explicitly asks to change rules.
2. **Protect the workspace.** Inspect the target files and current worktree state before writing. Preserve unrelated or unexplained changes. Stop before overwriting a target whose existing edits cannot be attributed or safely merged.
3. **Identify the evidence batch.** Enumerate exact input files, related prior versions, existing summaries, and likely consumers. Record source path, source or sender when known, document date, received date, version, size, and SHA256. Use `scripts/evidence_inventory.py` for deterministic file metadata.
4. **Preserve originals.** If an input is already in a project-controlled location, leave it in place. If it is external or temporary, copy it to the project-defined archive/input location; never move or delete the source by default. Never overwrite an older version. Keep extracted text, summaries, renders, and indexes separate from the original binary.
5. **Read the authoritative content.** Parse structured formats with suitable document, spreadsheet, PDF, image, or text tools. Read the original when no adequate summary exists, the original is newer, or sources conflict. Do not infer content from filenames.
6. **Extract deltas.** Compare against the prior baseline and capture additions, modifications, withdrawals, unchanged items, and version-lineage changes. Convert relative dates such as “tomorrow” using the source document's date, not the current run date.
7. **Classify every conclusion.** Label it as confirmed fact, document-recorded proposal, AI inference, or pending confirmation. Require evidence before promoting a proposal to a frozen baseline, a task to complete, or a risk to closed.
8. **Map the impact.** Determine affected modules, interfaces, requirements, responsibilities, milestones, risks, tests, release content, and downstream summaries. Read `references/operating-contract.md` for routing and promotion gates. Follow any project-specific rules and lifecycle documents found in the target workspace.
9. **Apply minimal updates.** Update the authoritative project truth before optional meeting notes, briefs, dashboards, or automation summaries. Preserve historical records, avoid duplicating the same fact across unrelated files, and add source links or version references where the project convention supports them.
10. **Validate the result.** Recheck source hashes when originals should remain unchanged; verify all new references, UTF-8 text, dates, versions, ownership, state labels, and cross-document consistency. Run the closest available document or project validation.
11. **Report the evidence chain.** State which originals were archived, what changed, which project files were updated, what validation ran, what conflicts remain, and who must decide them. Never describe an unverified edit as a completed synchronization.

## Enforce Boundaries

- Do not make meetings a prerequisite. Meeting notes, checklists, weekly reports, and briefs are optional downstream outputs.
- Do not decide technical disputes for the project team or silently choose between conflicting sources.
- Do not treat a newer file as authoritative solely because of its timestamp or filename.
- Do not overwrite, normalize, rename, move, or delete originals unless the user and project rules explicitly require it.
- Do not modify source code, release externally, send messages, or update unrelated project state by default.
- Do not replace `project-lifecycle-docs`; use the project's existing lifecycle structure and invoke that skill when a task independently requires lifecycle documentation.

## Load Resources Selectively

- Read `references/operating-contract.md` for archive decisions, state promotion, impact routing, and the completion report.
- Run `scripts/evidence_inventory.py --help` before first use. Prefer stdout for inspection; specify `--output` only for a new project manifest path.
