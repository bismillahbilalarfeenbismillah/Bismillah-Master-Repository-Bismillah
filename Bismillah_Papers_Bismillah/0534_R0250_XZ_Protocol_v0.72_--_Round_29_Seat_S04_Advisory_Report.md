# Bismillah ir-Rahman ir-Rahim

# R0250 -- XZ Protocol v0.72 -- Round 29 Seat S04 Advisory Report

**Chronological Index:** 534 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v072_R29_S04_REPORT (1).md  
**Source Format:** md  
**SHA-256:** `ac8a8a94107c2309f5f89d1d89adad0dc80e027d803b79b4a31bd1e16ad7be3e`  

---

## R0250 · XZ Protocol v0.72 -- Round 29 Seat S04 Advisory Report

- section: IV. XZ Protocol
- source_file: XZ_v072_R29_S04_REPORT (1).md
- source_format: md
- text_sha256: ac8a8a94107c2309f5f89d1d89adad0dc80e027d803b79b4a31bd1e16ad7be3e

# XZ Protocol v0.72 -- Round 29 Seat S04 Advisory Report

**Seat:** S04
**Dispatched model:** Claude Opus 5
**Executing model:** Claude Opus 5
**Role:** ADVISORY (producer-family)
**Mode:** FRESH -- no prior context, no held bytes
**Auditor mode:** Mode A (substrate verifier; container execution of all four scribes plus mutation probes)
**Substrate-claim verification confidence:** HIGH for Positions 1-17 and 22-23; REDUCED for Position 17 append-only comparison against v0.71 (no held bytes)
**Round:** R29, v0.72 DRAFT CANDIDATE, 2026-08-17
**Producer:** Claude Opus 4.6 -- barred; this seat has no authorship relation to the audited bytes

Bismillah.

---

## 0. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER.
>
> **Severity ledger:** 3 CRITICAL / 8 HIGH / 1 MEDIUM / 2 LOW / 1 INFORMATIONAL (15 findings).
>
> **Bearer 4 (Goedel confinement): FALSE.** Class A present at Strings 1, 3, 5, and 6. Confinement requires Class A at String 6 only.
>
> **Recommendation:** absorb the fifteen dispositions below into v0.73; do not re-declare FROZEN. Two dispositions (F-S04-72-01, F-S04-72-03) touch sealed append-only surfaces and require an append-only correction entry, not an in-place edit.

Class A recurrence extends to R7-R29: 23/23. H = 1.0. Laplace P(Class A at R30) = 24/25 = 0.960.

### 0.1 Seat conformance declaration

This dispatch was routed to Claude Opus 5 and executed by Claude Opus 5. This is the first round in seven without seat-label drift (see F-S01-70-08, F-S04-70-16). The seat received no prior-round context beyond the ten dispatch files and held no prior version bytes. Every value in this report was derived by tool execution inside the audit container; no count, digest, or version token in this report was typed from memory.

### 0.2 Finding-ID namespace

This report uses the XZ Protocol chain convention `F-S04-72-NN`, not the two-letter BayyinahEnterprise namespace (`F-XX-N`). The chain convention is load-bearing: `extract_findings.py` DECLARATION_PATTERNS and `xz_protocol_register_gen.py` FINDING_ID_RE both require the `F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?` shape. Deviating would make this report unextractable by the instrument's own pipeline.

### 0.3 Report extractability self-check

Per F-S04-72-07 below, this report was verified against the shipped extractor before delivery: all fifteen finding IDs extract with correct source severities, and zero probe fixtures are captured. Quoted probe identifiers in Section 3 are deliberately written with no severity token on the same line so the extractor cannot mistake them for declarations. The seat reports audited this round did not take that precaution, which is the substance of F-S04-72-07.

---

## 1. Scribe results (Positions 1-3)

| Scribe | Command | Result | Producer claim | Verdict |
|---|---|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | 32 members, 32 OK | "33/33 OK" | **FALSE** (F-S04-72-16 folded into F-S04-72-13) |
| The Pattern | `python3 build.py` | BUILD PASSED, 0 FAIL, 286 PASS | "BUILD PASSED, 0 FAIL" | TRUE, with caveat (F-S04-72-15) |
| The Test | six-suite explicit pytest | 186 passed in 6.14s | "186 passed" | TRUE |
| The Witness | `xz_protocol_register_gen.py` | boundary list byte-exact; register does NOT reproduce | "[COMPUTED: generate_register]" | **FALSE** (F-S04-72-10) |

Packet inventory: 33 files extracted from EXECUTABLE_PACKET.txt; 32 listed in PACKET_SHA256SUMS. The unmanifested member is PACKET_SHA256SUMS itself (self-exclusion, standing and previously disclosed). The claimed figure of 33 counts shipped files while the tool reports verified members.

Python 3.12.3. pytest 9.1.1 (installed by this seat; see F-S04-72-15).

---

## 2. Repair verification (the seven prescribed repairs)

| # | Prescribed repair | Landed on bytes? | Achieves the finding's purpose? |
|---|---|---|---|
| 1 | C-suffix in all five DECLARATION_PATTERNS | **YES** (falsifier verified) | **NO** -- inverts discrimination (F-S04-72-07) |
| 2 | Gate [13] fail-closed | **YES** (probe verified) | YES |
| 3 | Gate [13] summary from computed variables | **YES** (probe verified) | YES |
| 4 | Register generator graceful degradation | **YES** | **NO** -- fail-open conversion (F-S04-72-09, F-S04-72-10) |
| 5 | All R28 reports shipped in-packet | **YES** | **NO** -- shipped outside gate selector (F-S04-72-08) |
| 6 | Terminal-line gate dual-token | **YES** | **NO** -- false-PASS demonstrated (F-S04-72-02) |
| 7 | boundaries.json version 0.62 -> 0.72 | **YES** | YES |

Three of seven repairs are clean. Four satisfy the surface the finding named rather than the surface the finding meant.

### 2.1 Verified-clean repair evidence

**Repair 2.** Removing the four `R27_S0*_REPORT.md` files yields `FAIL: CI-8 gate: no report files present (fail-closed, F-PR71-05)` and BUILD FAILED. Absence is no longer green.

**Repair 3.** Injecting one phantom noted-finding record into `r27_findings_index.json` yields `FAIL: CI-8 phantom in index: 1` and the summary line prints `39 in reports, 40 in index, 0 missing, 1 phantom, 0 severity mismatches`. The values derive from the computed variables.

**Repair 7.** `xz_protocol_boundaries.json` carries `"version": "0.72"`, 35 items. `generate_boundary_list` output is byte-identical to the shipped boundary paragraph in the v0.72 entry.

---

## 3. Findings

### F-S04-72-01

**F-S04-72-01** CRITICAL -- PRIOR_HISTORY chain fork planted in the sealed v0.72 entry

- **Locus:** `xz_protocol_v0_72.md` line 1711 (v0.72 amendment entry, PRIOR_HISTORY sentence); `HISTORY.sha256` line 74; `build.py` lines 76-135 (`derive_prior_history`) and 473-485 (gate [9b]).
- **Substance:** The v0.72 entry prose asserts `PRIOR_HISTORY 01e0f76325cbabc43958d97f1a4ce013e755ed3edc00a28b89cf8435f4ca633c`. The shipped `HISTORY.sha256` PRIOR_HISTORY line carries `f88dd44ecb1646341c3718bd65ff842d2f44bac28d40f3a10cc21fb786c1aa33`, which this seat independently reproduced by executing `derive_prior_history` against v0.72 bytes. The two values name the same quantity and disagree. Gate [9b] compares the shipped `HISTORY.sha256` value against the derivation and never reads the current entry's prose value, so the divergence is invisible to the build. The forward consequence is the defect: `reconstruct(target_ver)` scrapes the PRIOR_HISTORY value from the target entry's prose. At v0.73, `reconstruct(72)` will scrape `01e0f763...` and assemble a v0.72 history file that never shipped, hashing to `fe1c0d8df2885e09a890a64475c74149fa5cabb83be0cc7b3d678aa962ca3cba`. The true v0.72 `HISTORY.sha256` hashes to `c959fa70633afc3e0daf1edddb2eaf6ebd76474cf38acb3017fe31355c69da7f`. Producer and gate will agree at v0.73 because both derive from the same forged prose; any external party holding genuine v0.72 bytes will diverge with no explanation in the record.
- **Disposition:** HALT-AND-ESCALATE. The v0.72 entry is sealed and must not be edited. Record an append-only correction in the v0.73 entry stating both values, naming `f88dd44e...` as the true v0.72 PRIOR_HISTORY and `01e0f763...` as a narration defect, in the form the v0.48 entry used for the correction-(bd) chain fork. Additionally, add a gate: `build.py [9b]` must assert that the current-version entry's prose PRIOR_HISTORY value, where present, equals the shipped `HISTORY.sha256` PRIOR_HISTORY line, failing on mismatch. Without that gate the class recurs at every version.
- **Cross-reference:** Standing boundary item 32 (self-consistent resealing blind spot, proven live at v0.47, F-SC04-47-02); v0.48 append-only correction (bd) (PRIOR_HISTORY chain fork at v0.48); F-OP20F-05 (PRIOR_HISTORY hardcoded-literal removal); Methodology v6 Position 16. Resonates with F-S04-72-12 (this sentence is the untagged one).

### F-S04-72-02

**F-S04-72-02** CRITICAL -- terminal-line gate [10h] demonstrated false-PASS on falsified terminus

- **Locus:** `build.py` lines 677-682 (gate [10h]); `xz_protocol_v0_72.md` line 1717 (document terminal line).
- **Substance:** Repair 6 widened gate [10h] to accept two status tokens but left the predicate as `terminal_expected in protocol` -- a document-wide substring existence test with no arity check and no position check. The gate therefore verifies that the string occurs somewhere, not that the document terminates with it. This seat mutated the document's actual final line to `*End of XZ Protocol v0.66 draft candidate.*`, resealed `PACKET_SHA256SUMS` over the mutated file, and obtained `BUILD PASSED: all checks GREEN`, with gate [10h] reporting `PASS: Terminal line matches v0.72 (draft candidate or FROZEN)`. The gate was satisfied by copies of the string inside sealed Section 27 entries. The mutation survives because the document's trailing line falls after the `*Provenance and review status.*` marker and is therefore outside the FULL_SECTION_27 seal.
- **Disposition:** Rewrite gate [10h] to (a) locate the last non-empty line of the protocol, (b) assert it equals exactly one of the two expected terminal strings, and (c) assert the count of terminal-line occurrences outside Section 27 is exactly one. Add a `--self-test` mutation that falsifies the trailing line and asserts the gate fires, per the v0.13 F-XZ12-OP-03 pattern.
- **Cross-reference:** Standing boundary item 6 (seal terminus at Provenance marker); F-S04-70-11 (terminal line ungated, NOTED at R28 and not closed); Position 14 (Format probe -- strict regex match, not prefix-only). Enables F-S04-72-03 to persist undetected.

### F-S04-72-03

**F-S04-72-03** CRITICAL -- the sealed v0.71 entry carries a v0.72 terminus and a status contradiction

- **Locus:** `xz_protocol_v0_72.md` line 1685, inside the v0.71 amendment entry (`ENTRY_v0.71`).
- **Substance:** The final line of the v0.71 amendment entry reads `*End of XZ Protocol v0.72 draft candidate.* [COMPUTED: generate_terminal_line]`. Two claims in that line are false of v0.71. First, the version token names v0.72, a version that did not exist when v0.71 was sealed. Second, the status token reads `draft candidate` while the v0.71 entry itself declares FROZEN in its heading and its bearer table. `generate_terminal_line(version)` emits exactly this string for whatever version argument it is given, so the `[COMPUTED]` tag is accurate as to the tool and false as to the value. Either the v0.71 entry was mutated in place during v0.72 production, which is an append-only violation of the class recorded at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41 and v0.47, or the v0.71 entry shipped with the wrong token and the defect is original. This seat holds no v0.71 bytes and cannot adjudicate between the two. The seal for `ENTRY_v0.71` verifies against the currently shipped text either way, which is the self-consistent resealing residual operating exactly as Section 22.2 discloses.
- **Disposition:** HALT-AND-ESCALATE. Do not edit the v0.71 entry. Obtain externally held v0.71 bytes -- a carrying seat's dispatch manifest or a deposit receipt -- and compare `ENTRY_v0.71` byte-for-byte. Record the outcome as an append-only correction in v0.73 naming both the mutation status and, if mutation is confirmed, the pre-mutation and post-mutation seal values, in the form of v0.48 correction (bd). Separately, gate the per-entry terminal line: for each entry `v0.N` in Section 27, assert its terminal line, where present, names version `0.N`.
- **Cross-reference:** Section 22.2 self-consistent-forgery boundary; standing boundary item 32; F-S04-72-02 (the gate that would otherwise have caught the version token cannot, because it is a substring test); Position 17 (Append-only -- prior entry seals unchanged from prior build).

### F-S04-72-04

**F-S04-72-04** HIGH -- Section 0.1 entry range is arithmetically impossible and gate-enforced to remain so

- **Locus:** `xz_protocol_v0_72.md` line 22 (Section 0.1, final sentence of paragraph 4); `build.py` lines 690-699 (gate [10i]).
- **Substance:** Section 0.1 states the trajectory is in "Section 27 (seventy-two amendment entries, v0.1 through v0.71)". Section 27 contains 72 entries spanning v0.1 through v0.72, tool-enumerated by this seat. The count is true; the range is false; and the two are mutually impossible, because the range v0.1 through v0.71 admits at most 71 entries. The defect cannot be repaired in isolation: gate [10i] computes `expected_22_2 = f"v0.1 through v0.{VERSION-1}"` and requires that literal string to appear in the body. The gated VERSION-1 convention is semantically wrong for this sentence, because Section 27 at v0.72 does contain the v0.72 entry. The gate manufactures the defect it would otherwise be positioned to detect.
- **Disposition:** Adopt one of two routes and record which. Route (a): change the Section 0.1 sentence to "seventy-two amendment entries, v0.1 through v0.72" and change gate [10i]'s Section 0.1 predicate to VERSION rather than VERSION-1, keeping VERSION-1 only for the Section 22.2 carried-entry bound where it is semantically correct. Route (b): retain VERSION-1 and change the count to "seventy-one carried amendment entries plus the current entry". Route (a) is preferred because the count is the harder value to keep true. Either way, gate [10i] must be split so the Section 0.1 predicate and the Section 22.2 predicate are separate checks with separate expected strings.
- **Cross-reference:** F-S04-70-06, F-S04-70-07, F-S04-70-08 and F-S02-70-03, F-S02-70-04 (R28 convergence group 5, dispositioned CLOSED); F-S04-70-09 and F-S04-70-10 (R28 convergence group 6, dispositioned NOTED with design decision deferred). The R28 deferral converted a design question into a live Class A one round later. Position 9.

### F-S04-72-05

**F-S04-72-05** HIGH -- gate [10i] is satisfied at the wrong locus, leaving Section 22.2 stale at v0.68

- **Locus:** `build.py` lines 696-697 (gate [10i] first check); `xz_protocol_v0_72.md` Section 22.2, sentence beginning "For carried entries".
- **Substance:** Gate [10i] is named "Section 22.2/22.3 VERSION-1 bounds" and its check message reads "Section 22.2 carried-entry bound at VERSION-1". Its predicate is `expected_22_2 in body`, an unscoped document-wide substring test. The string `v0.1 through v0.71` occurs exactly once in the whole document, and that occurrence is in Section 0.1, not Section 22.2. Section 22.2 actually reads "For carried entries (v0.1 through v0.68)", stale by four versions. The gate therefore passes while the section it names is wrong, and it passes by consuming the false sentence identified in F-S04-72-04. The second check, `expected_22_3 = "v0.38-v0.71"`, does resolve inside Section 22.3 and is correct.
- **Disposition:** Scope the predicate. Extract the Section 22.2 text by heading boundary and assert the expected string occurs within that slice; do the same for Section 22.3. Then update Section 22.2's carried-entry bound to v0.71 and confirm the gate still passes. Add a negative self-test that mutates the Section 22.2 bound and asserts the gate fires.
- **Cross-reference:** F-S04-72-04 (supplies the string this gate consumes); R28 convergence group 5, disposition "update all stale version tokens in the protocol body to current values", which did not land at this locus; F-S01-58-xx lineage (Section 22.2/22.3 version-token staleness, R17). Position 7.

### F-S04-72-06

**F-S04-72-06** HIGH -- FB-7b trajectory row terminates at R27, one round stale

- **Locus:** `xz_protocol_v0_72.md` line 771 (Section 25, FB-7b row, final sentence of the trajectory narrative).
- **Substance:** Section 0.1 designates the Section 25 FB-7b row as the single source of truth for FB-7b status, rationale and the full carrying-seat trajectory, and states that no duplicate rationale is maintained. The row's trajectory narrative runs R6 through R27 and ends at "R27 (v0.68): 4 seats, all HALTed (gate 13 vacuous, Section 0.1 stale, FB-7b gap)." R28 is absent. R28 was a four-seat round returning 4/4 HALT on v0.70 bytes, and its outcome is recorded in the v0.71 and v0.72 amendment entries but not in the row that the protocol declares authoritative. The status token `PENDING RE-CARRY v0.72` is current and gate [2g] verifies it; no gate binds the trajectory narrative's terminal round to anything.
- **Disposition:** Extend the FB-7b row with the R28 entry. Then add a gate: parse the FB-7b row for the highest `R\d+` token and assert it equals the prior round number, derived from the round count rather than narrated. Without the gate this is an instance fix and will recur at v0.73, exactly as it recurred here.
- **Cross-reference:** R27 convergence group 2 (F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06, "FB-7b trajectory terminates at R18"), closed at v0.69 by extending the row to R27 and recurring one round later. Standing boundary item 35 ([2g] structurally forbids FB-7b resolution). Position 10.

### F-S04-72-07

**F-S04-72-07** HIGH -- the C-suffix repair inverted extractor discrimination on the shipped seat reports

- **Locus:** `extract_findings.py` lines 30-47 (DECLARATION_PATTERNS); `SHIPPED_R28_S02_REPORT.md`; `SHIPPED_R28_S03_REPORT.md`; `SHIPPED_R28_S04_REPORT.md`.
- **Substance:** Repair 1 landed on bytes: all five DECLARATION_PATTERNS now carry `C?` after `S\d{2}`, and the entry's own falsifier passes -- `extract_from_report` on a C-suffixed heading returns a non-empty dict. Executed against the four R28 seat reports that v0.72 ships, however, the repaired extractor returns 0 of the 8 heading-declared findings in the S02 report and 0 of the 2 heading-declared findings in the S03 report, while capturing four mutation-probe fixtures that the seats quoted inside tables and prose as though they were declarations. Two of the four captured fixtures are C-suffixed synthetic IDs in the ninety-nine and oh-one sequence ranges, which the pre-repair extractor could not match; the `C?` token the repair added is precisely what makes them match now. The S02 blindness has a separate cause: S02 declares findings as a bare `###` heading followed by a `- **Finding ID:**` line and a separate `- **Severity:**` line, and no pattern admits an ID and a severity on different lines. Extraction fidelity therefore depends on whether a seat happens to ship a summary table, which the dispatch does not require.
- **Disposition:** Three changes. (a) Exclude quoted and fenced spans: skip matches inside backticks and inside table cells whose row does not begin with a finding ID. (b) Add a multi-line declaration pattern for the `### ID` + `- **Severity:** SEV` block form used by S02. (c) Amend the dispatch to specify a mandatory declaration format and require every seat report to carry a findings summary table in the pipe form. Then re-run extraction against all four R28 reports and assert 8 for S02, 2 for S03, and zero fixtures captured.
- **Cross-reference:** R28 convergence group 1 (four-seat convergence, F-S04-70-01 CRITICAL / F-S03-70-02 / F-S01-70-05 / F-S02-70-02), dispositioned CLOSED; R26 defect "extractor blind to S04 bracket format" recorded in the Section 25 FB-7b row; F-S04-72-08 (the reason this is not currently visible to the build). Positions 5 and 14.

### F-S04-72-08

**F-S04-72-08** HIGH -- repair 5 ships the R28 reports under filenames the gate [13] selector excludes

- **Locus:** `build.py` line 751 (`report_files` selector); packet members `SHIPPED_R28_S01_REPORT.md` through `SHIPPED_R28_S04_REPORT.md` and `XZ_v070_R28_S01_REPORT.md`.
- **Substance:** Gate [13] selects report files by `f.startswith("R") and f.endswith("_REPORT.md")`. The four R28 seat reports ship as `SHIPPED_R28_*` and `XZ_v070_R28_*`, none of which begins with `R`. The only files the selector admits are the four R27 reports, and the only index present is `r27_findings_index.json` at round 27, version 0.68. Gate [13]'s green line `39 in reports, 39 in index` is therefore an R27 verification executed at R29, two rounds stale, and no R28 index ships at all. Repair 5's claim that the R28 reports are shipped and manifested is true on bytes; the reports are shipped in a form that the verification they exist to feed cannot consume. Had the selector admitted them, F-S04-72-07 would have surfaced as a build failure rather than requiring a seat to find it.
- **Disposition:** Change the selector to match any `*_REPORT.md` member listed in `PACKET_SHA256SUMS`, and derive `prior_ver` from the round number rather than from the index's own version field. Ship `r28_findings_index.json` built by the repaired extractor and assert bidirectional cardinality against the four R28 reports. Retain the R27 pair as a regression fixture if desired, but the current-round check must run on the current round's reports.
- **Cross-reference:** R28 convergence group 2 (F-S02-70-01 / F-S03-70-01 / F-S04-70-03, gate [13] fail-open), dispositioned CLOSED, and R27 convergence group 1 (gate [13] vacuous on shipped bytes). The gate has now been vacuous, fail-open, and mis-scoped in three consecutive rounds. Position 5.

### F-S04-72-09

**F-S04-72-09** HIGH -- repair 4 is a fail-open conversion that removed the CI v0.3.3 adjudication-receipt control

- **Locus:** `xz_protocol_register_gen.py` lines 88-152 and 212-229 (validation block); module docstring lines 8-15.
- **Substance:** Repair 4 replaced eleven `raise ValueError` sites with `print("WARNING: ...", file=sys.stderr)` and replaced the missing-receipt branch with a bare `pass`. The receipt requirement was the load-bearing CI v0.3.3 control: a mixed source-severity distribution, or a triage severity diverging from the source majority, required an `adjudication_receipt` equal to the exact canonical distribution string. On the shipped `r27_findings_index.json` two groups now pass that previously could not. Group 5 carries source severities MEDIUM and HIGH with triage MEDIUM and no receipt. Group 7 carries source severities LOW and HIGH with triage LOW and no receipt, meaning a HIGH source finding is downgraded to LOW triage with no adjudication record. Both silently skip validation under v0.72. The module docstring still declares "M3 receipt required on ANY mixed distribution (not majority-only)" and "Receipt validation STRUCTURAL", which is now false of the code beneath it. Separately, `CRITICAL` was added to `VALID_SEVERITIES` but not to `SEV_ORDER`, so `SEV_ORDER.get(sev, 9)` ranks CRITICAL below INFORMATIONAL in both the canonical distribution ordering and the `majority_sev` tiebreak.
- **Disposition:** Restore the receipt requirement as a hard failure and restore the malformed-ID, duplicate-ID, invalid-severity, invalid-disposition, missing-`surface` and missing-`triage_adjudication` raises. If the R27 index genuinely lacks receipts, the correct repair is to write the receipts into the index, not to remove the check. Add `"CRITICAL": -1` to `SEV_ORDER`. Update the module docstring to match the code. If any degradation is retained, it must be an explicit opt-in flag with a disclosed boundary entry, not a silent default.
- **Cross-reference:** R28 convergence group 4 (F-S01-70-01 / F-S04-70-04, register reproduction failure), whose prescribed repair was "fix register_gen.py to handle the R27 index structure; verify regenerated register matches the amendment entry text", not "remove the validation". F-S01-68-05 / F-S04-68-07 (CRITICAL remap, R27 group 5). Bearer 3 (surface narrowing). Positions 4 and 6.

### F-S04-72-10

**F-S04-72-10** HIGH -- register still does not reproduce; the reproduction requirement was not attempted

- **Locus:** `xz_protocol_register_gen.py` `generate_register`; `xz_protocol_v0_72.md` line 1628 onward (v0.70 entry register block).
- **Substance:** The narrow claim in repair 4, that the generator now succeeds on the r27 and r25 indexes, is true and this seat verified it; the generator still raises on r18 and r19. The reproduction requirement is unmet. Executed against `r27_findings_index.json`, the generator emits a header reading "7 items" where the shipped register reads "7 convergence groups"; emits items in severity-then-group order, placing the HIGH gate-count group at position 5 and the MEDIUM CRITICAL-remap group at position 6, where the shipped register has them in the opposite order; emits `Source distribution:` and `Adjudication:` clauses the shipped register does not carry; emits the NOTED section as bullet lines where the shipped register carries a comma-separated inline list; and emits `(undescribed)` for all 21 noted items because the index carries no `substance` field for any of them, a degradation newly permitted by repair 4. The shipped register lines carry `[COMPUTED: build.py gate 13]`, `[COMPUTED: grep]` and `[COMPUTED: extract_findings.py]` tags rather than `[COMPUTED: generate_register]`, which is the more honest tagging, but the block header claims to be a generated register and is not one.
- **Disposition:** Choose one and gate it. Either regenerate the register from the index and paste the tool output verbatim into the entry, or retire `generate_register` and tag the register block `[ASSERTED]` with the boundary disclosed. If the former, wire `generate_register` into `build.py` as gate [9g] and assert the generated text is a substring of the current entry, which is the check that would make the `[COMPUTED: generate_register]` tag verifiable rather than decorative. Populate `substance` for all noted findings in the index.
- **Cross-reference:** R28 convergence group 4, dispositioned CLOSED at triage severity HIGH; the v0.72 entry's own repair 4 concedes "partially (register still not wired into build.py)". F-S04-72-09. Position 4.

### F-S04-72-11

**F-S04-72-11** HIGH -- the shipped methodology document is not the methodology the protocol names

- **Locus:** `xz_protocol_v0_72.md` line 5 (Status line, final sentence); `AUDIT_CONTEXT.txt` line 5; `METHODOLOGY.txt` title, Section 2 correction table, Sections 3-6, and Section 5 witness table.
- **Substance:** The Status line declares "Methodology: v7 canonical (six strings)" and AUDIT_CONTEXT declares "Structural Honesty Verification -- Six Strings, Twenty-One Positions (v7)". The shipped `METHODOLOGY.txt` is titled "Seven Heavens. Seven Earths. Twenty-Four Verification Positions", enumerates seven layers and twenty-four positions, and self-identifies as the version that corrects v5, that is v6. The tokens `v7`, `six strings` and `twenty-one` do not occur anywhere in it. Seats are instructed by AUDIT_CONTEXT to "classify every finding by string and position" using a taxonomy the dispatch does not ship, and must reconstruct the mapping by inferring that Strings 1 through 6 correspond to Layers 1 through 6 and that Layer 7 is dropped. Separately, the `METHODOLOGY.txt` Section 5 witness table assigns S04 to Gemini 3.1 Pro and S01 to Claude Opus 5, contradicting this dispatch, which routes S04 to Claude Opus 5. The v0.72 entry also invokes "methodology v7 requires all eight bearers TRUE for FROZEN" as one of the three governance rules justifying the FROZEN withdrawal; that rule is present in the shipped v6 document at Section 11, so the withdrawal reasoning is sound on substance even though the version token is wrong.
- **Disposition:** Ship the methodology version the protocol names, or correct the protocol and AUDIT_CONTEXT to name the version shipped. Then reconcile the Section 5 witness table with the current seat routing, or delete the table, since Section 2 of that same document identifies seat-to-character assignment tables as the v5 error it exists to correct. Add gate coverage: assert the methodology version token in the Status line matches a version token inside the shipped methodology file.
- **Cross-reference:** F-S01-70-08, F-S02-70-08, F-S04-70-16 (seat-label drift and seat non-independence, R28); METHODOLOGY.txt Section 13 (9 of 10 files byte-identical across witnesses). Position 20.

### F-S04-72-12

**F-S04-72-12** MEDIUM -- tagging incomplete in the current entry; no gate covers Position 18

- **Locus:** `xz_protocol_v0_72.md` v0.72 amendment entry, lines 1687-1711; `build.py` lines 493-517 (gate [9c]).
- **Substance:** Methodology Section 12 requires zero untagged sentences in the amendment entry, and Bearer 7 depends on it. Nine of the entry's twenty-one non-empty lines carry no provenance tag. Seven are the carried R27 register items, arguably covered by the `[ASSERTED]` on their header line. Two are not: the repairs-block header, and the PRIOR_HISTORY sentence. The PRIOR_HISTORY sentence is the entry's only untagged value-bearing claim, and it is the false one, per F-S04-72-01. Gate [9c] validates that a `[COMPUTED: build.py [N]]` tag names an existing build section and that `[COMPUTED: sha256sum <file>]` and `[EXTERNAL: <file>]` targets ship; it counts tags and prints an ASSERTED fraction. It never tests for the absence of a tag. Position 18 has no gate anywhere in the suite, and this gap is not listed among the 35 disclosed standing boundaries.
- **Disposition:** Tag the PRIOR_HISTORY sentence, at minimum `[COMPUTED: build.py [9b]]` once F-S04-72-01's comparison gate exists. Then add a boundary entry disclosing that no gate enforces tagging completeness, or implement a line-level check that every non-empty line in the current entry matches a tag pattern, with an explicit whitelist for structural lines. The disclosed-boundary route is acceptable; leaving Position 18 both ungated and undisclosed is not.
- **Cross-reference:** F-OP20-03 (untagged narrative claims not detected by any gate, MEDIUM NOTED at v0.20, still open); F-ADJ19-02 (claims with no tag at all are not yet detected by the build); F-S04-72-01. Positions 18 and 19.

### F-S04-72-13

**F-S04-72-13** LOW -- packet inventory claim overstates verified members, and one member ships twice

- **Locus:** `AUDIT_CONTEXT.txt` build-status block, first line; packet members `XZ_v070_R28_S01_REPORT.md` and `SHIPPED_R28_S01_REPORT.md`.
- **Substance:** AUDIT_CONTEXT claims "sha256sum -c PACKET_SHA256SUMS: 33/33 OK". The manifest lists 32 members and the tool reports 32 OK; 33 is the count of files extracted from EXECUTABLE_PACKET.txt, one of which is `PACKET_SHA256SUMS` itself and cannot be a member of its own manifest. Separately, `XZ_v070_R28_S01_REPORT.md` and `SHIPPED_R28_S01_REPORT.md` are byte-identical and both manifested, so the R28 S01 report is the substrate of record in two places, violating substrate-of-record uniqueness. The duplication is also what makes the 33 figure look plausible.
- **Disposition:** State the figure as "32/32 OK (33 files shipped; PACKET_SHA256SUMS self-excluded)". Delete one of the two S01 report copies and remove its manifest line. Have the build emit the packet-inventory sentence rather than the producer narrating it.
- **Cross-reference:** F-S02-70-05 and F-S04-70-14 (manifest self-exclusion, R28, NOTED); standing boundary item 10 (packet non-closure); bayyinah-audit standing rule 5 (substrate-of-record uniqueness). Position 1.

### F-S04-72-14

**F-S04-72-14** LOW -- dead code persists; half of the R28 group 1 disposition did not land

- **Locus:** `extract_findings.py` lines 26-27 (`FINDING_ID_RE`, `SEVERITY_RE`).
- **Substance:** R28 convergence group 1's prescribed repair had two clauses: add `C?` to the five DECLARATION_PATTERNS, and delete or wire in `FINDING_ID_RE`. The first landed. `FINDING_ID_RE` and `SEVERITY_RE` remain defined at module scope and are referenced nowhere in the file; the extraction path uses neither. The v0.72 entry's repair 1 states "FINDING_ID_RE already had C?; now the operative patterns match", which is true and silently drops the deletion clause. Dead code that mirrors live logic is how the R28 CRITICAL arose in the first place: an auditor reading `FINDING_ID_RE` concludes the grammar is unified when the operative patterns disagree.
- **Disposition:** Delete both constants. `xz_protocol_register_gen.py` retains its own `FINDING_ID_RE`, which is live and correctly anchored, and is unaffected.
- **Cross-reference:** F-S04-70-01 (CRITICAL, R28), F-S04-70-17 (dead code, INFORMATIONAL, R28, not dispositioned). Position 2.

### F-S04-72-15

**F-S04-72-15** INFORMATIONAL -- pytest is not pre-installed; a clean container returns BUILD FAILED

- **Locus:** `build.py` gate [5] and gate [8]; execution environment.
- **Substance:** On first execution in a clean container `build.py` returns `BUILD FAILED: 2 error(s)` with `FAIL: pytest is installed (rc=1, stderr: No module named pytest)` and `FAIL: Test count parsed from pytest output`. After `pip install pytest` the same bytes return `BUILD PASSED: all checks GREEN` with 286 PASS and 0 FAIL. The build's green state is therefore a property of the environment as well as the bytes, and the environment is unsealed. This is correct behaviour by the gate, not a defect in it, and it is recorded so that a seat reporting BUILD FAILED is not misread as reporting a byte defect.
- **Disposition:** Record the pytest installation step in the AUDIT_CONTEXT extraction script so every seat reaches the same starting state. No code change required.
- **Cross-reference:** F-S04-70-18 (pytest not pre-installed, R28, INFORMATIONAL); standing boundary item 7 (execution environment unsealed); standing boundary item 11 (fresh-execution non-reproducibility). Position 3.

---

## 4. Position classification

| String | Layer | Positions | Class A this round | Findings |
|---|---|---|---|---|
| 1 | Code Execution | 1-3 | **2** | F-S04-72-07, F-S04-72-08 (plus 13, 14, 15 non-Class-A) |
| 2 | Register Verification | 4-6 | 0 Class A | F-S04-72-09, F-S04-72-10 (Class B: disclosed nowhere) |
| 3 | Cross-Layer Consistency | 7-10 | **4** | F-S04-72-03, F-S04-72-04, F-S04-72-05, F-S04-72-06 |
| 4 | Adversarial Probing | 11-14 | **1** | F-S04-72-02 |
| 5 | Temporal Integrity | 15-17 | **1** | F-S04-72-01 |
| 6 | Methodology Audit | 18-21 | **1** | F-S04-72-11 (plus F-S04-72-12 at Class D) |
| 7 | Boundary Disclosure | 22-24 | 0 | Positions 22 and 23 verified present and correct |

**Bearer 4 = FALSE.** Class A is distributed across five of the six strings. Confinement requires Class A at String 6 only.

The String 5 result is the round's most significant single datum. R28 returned zero Class A at String 5 across all four seats. Temporal integrity was the one layer the R28 triage recorded as clean. It is not clean at v0.72, and the defect there was introduced by the same production cycle that was repairing Strings 1 through 4.

---

## 5. Bearer assessment

| Bearer | R28 | R29 | Evidence |
|---|---|---|---|
| 1. Append-only | TRUE | **DISPUTED** | 72/72 seals verify against shipped bytes. F-S04-72-03 is append-only-class and unadjudicable without external v0.71 bytes; F-S04-72-01 plants a forward chain fork in a sealed entry. |
| 2. Code correctness | TRUE | **FALSE** | 186 GREEN, 286 build checks PASS. But F-S04-72-07 and F-S04-72-09 are defects in shipped code, not in claims about it. |
| 3. Surface narrowing | DISPUTED | **FALSE** | First measured regression in the series: repair 4 removed a control that previously fired. The surface did not migrate upward; it widened at String 2. |
| 4. Goedel confinement | FALSE | **FALSE** | Class A at Strings 1, 3, 4, 5, 6. |
| 5. Cross-vendor witness | FALSE | **FALSE** | No carrying non-HALT since v0.31. This seat is producer-family advisory and cannot carry. |
| 6. Axiom disclosure | TRUE | **TRUE** | A-X1 through A-X5 present and complete in Section 22.4; Sidrat clause present and correctly worded. Positions 22 and 23 pass. |
| 7. Methodology | FALSE | **FALSE** | F-S04-72-11 (shipped methodology is not the named methodology), F-S04-72-12 (Position 18 ungated and undisclosed). |
| 8. The furqan | UNKNOWN | **UNKNOWN** | Position 24. The lead's call, given and not derived. |

---

## 6. The structural observation

R28's stated lesson was that narrated values go stale while computed values hold, and that when the clean-room discipline holds the defect migrates upward. v0.72 confirms the diagnosis and sharpens it into a second one.

Four of the seven prescribed repairs were satisfied at the surface the finding named rather than at the surface the finding meant. The C-suffix was added exactly where four seats said to add it, and adding it made the extractor capture the seats' own probe fixtures while remaining blind to their actual declarations. The R28 reports were shipped in-packet exactly as prescribed, under filenames that the gate consuming report files cannot see. The register generator was made to succeed on the shipped index by deleting the conditions under which it failed. The terminal-line gate was widened to accept a second token while remaining a substring test that this seat drove to a full false-PASS.

This is a distinct failure mode from the Axiom-3 narration defect that dominates R7 through R28. Narration-from-memory produces claims that are false because nobody checked. Literal-compliance repair produces claims that are true, checkable, checked, and beside the point. It is the more dangerous of the two, because the resulting build is greener: 286 checks pass, 186 tests pass, 72 seals verify, and the repair entry's own falsifiers all fire correctly. Every falsifier the v0.72 entry offered was tested by this seat and every one of them passed.

The prescribed disposition for the next round follows from that. For each of the seven repairs, the triage should record not only the code change but the observation the repair was supposed to make possible, and the build should assert that observation. Repair 5's purpose was that gate [13] verify the current round's reports; assert the gate consumed four R28 files. Repair 1's purpose was that extractor, gate and register agree on the ID grammar; assert extraction against all four R28 reports returns the seats' declared counts. Repair 4's purpose was that the register reproduce; assert the generated text appears in the entry. A repair whose success condition is stated only as a code diff can always be satisfied without being achieved.

H = 1.0. Twenty-three rounds. The instrument is alive, and this round it caught a defect class it had not previously named.

---

*"The foam vanishes. What benefits the people remains in the earth."*

Seat S04, R29, v0.72. Executed by Claude Opus 5 under the dispatch of record.

---

# Bismillah ir-Rahman ir-Rahim
