# Operating Contract

Use this reference to decide what may change and what evidence is required.

## Mode Contract

| User intent | Allowed work | Default result |
| --- | --- | --- |
| Archive, retain, or file these materials | Copy external inputs into the project-defined location, preserve in-place inputs, record metadata and hashes | Evidence inventory and archive note |
| Review, inspect, compare, or assess impact | Read and analyze only | Delta report, impact map, conflicts, recommended updates |
| Sync, update, ingest, or incorporate into project context | Archive, analyze, edit affected project documents, and validate | Updated truth layer plus evidence report |
| Publish, send, release, delete, or replace originals | Require explicit authority and exact targets | Perform only the explicitly authorized action |

If intent is ambiguous, preserve read-only behavior while continuing all useful analysis. Ask only when the unresolved choice would materially change or destroy project state.

## Original Archive Decision

1. Determine whether the input is already under the project root and in a directory allowed by project rules.
2. If yes, preserve it in place and reference that path. Do not create a duplicate merely to satisfy an abstract archive convention.
3. If it is under the project root but in an ad hoc intake directory, preserve it until links and summaries are understood. Copy or move only when project rules and user intent make the destination clear; moving is never the default.
4. If it is outside the project or temporary, copy it to the closest project-defined original-input/archive directory.
5. If the destination name exists with different content, retain both using the project's version/date convention. Never overwrite silently.
6. Create derived text, OCR, previews, extracted tables, and summaries beside the project's derived-document location, not inside the original file.

Record at least:

- original filename and project-relative path;
- source or sender when known;
- source document date and project received date as separate fields;
- declared version and observed version clues;
- size and SHA256;
- relationship to prior and superseded versions;
- parsing or extraction limitations.

## Evidence Classes

| Class | Meaning | Permitted state effect |
| --- | --- | --- |
| Confirmed fact | Directly supported by an authoritative record, completed test, signed decision, accepted delivery, or explicit user confirmation | May update the current baseline with a source reference |
| Document-recorded proposal | A source proposes a design, date, owner, or approach but does not prove approval | Record as proposal, input, candidate, or pending review |
| AI inference | A conclusion derived from evidence but not stated by an authority | Label as inference; never promote to project fact automatically |
| Pending confirmation | Missing, conflicting, ambiguous, or stale information | Create a targeted question, owner, and required closure evidence |

Evidence strength depends on the claim. A filename or modification time proves file presence and timing, not technical approval. A meeting transcript proves what was said, not necessarily the final decision. A production package proves package contents, not supplier acceptance or delivery commitment. A test result proves only its documented environment and scope.

## State Promotion Gates

Require the following before changing state:

| Promotion | Minimum evidence |
| --- | --- |
| Proposal -> confirmed | Named decision authority plus written conclusion or accepted controlled document |
| Planned -> in progress | Owner acknowledgement or execution evidence |
| In progress -> completed | Deliverable, review record, test result, acceptance record, or equivalent closure evidence |
| Risk open -> mitigated | Mitigation implemented and its trigger/impact re-evaluated |
| Risk mitigated -> closed | Verification evidence and no remaining open dependency |
| Input version -> frozen baseline | Version identity, scope, approver, effective date, and downstream compatibility decision |

When evidence is insufficient, retain the prior state and append the new evidence as an input or pending item.

## Impact Routing

| Change type | Primary consumers | Conditional consumers |
| --- | --- | --- |
| Requirement, product scope, or acceptance | Shared context, requirement baseline, milestone/acceptance records | Architecture, tests, release notes, weekly status |
| Interface, protocol, pin, timing, or state machine | Interface matrix, common protocol, module boundary, risk list | Hardware records, architecture, bring-up checklist, tests |
| Responsibility, owner, or commitment date | Responsibility table, shared context, execution plan | Weekly status, escalation list, automation summary |
| Hardware, structure, material, or supplier version | Original archive, shared context, version lineage, risk list | Interface matrix, assembly checklist, schedule, release package |
| Test, review, or validation evidence | Test record, issue/risk state, shared context | Acceptance baseline, release note, weekly status |
| Meeting or chat evidence | Current-week record and affected truth documents | Checklist, brief, decision log; only when the evidence changes project truth |

Update only consumers affected by a real delta. Do not create meeting artifacts for ordinary material synchronization.

## Conflict Handling

For every conflict, record:

- source A and its exact claim;
- source B and its exact claim;
- dates, versions, and authority level;
- affected modules and milestones;
- the named role or person who must decide;
- the evidence that will close the conflict.

Do not resolve a conflict by preferring the newest timestamp unless project rules explicitly make that source authoritative.

## Completion Report

Return a compact report containing:

1. mode used and project root;
2. originals retained or copied, including destination and hash verification;
3. factual deltas and withdrawn items;
4. modified project files and the reason for each;
5. unresolved conflicts, pending questions, owners, and required evidence;
6. validation performed and any remaining limitation.

If no project document requires an update, say so and explain why. A correct no-change result is preferable to manufacturing edits.
