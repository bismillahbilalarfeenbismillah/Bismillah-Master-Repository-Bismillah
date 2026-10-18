# Bismillah ir-Rahman ir-Rahim

# R0752 -- Independent Audit: XZ Protocol v0.37 Packet — Executable Controls

**Chronological Index:** 904 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R2_F2_GPT56_REVELATION.md.txt  
**Source Format:** txt  
**SHA-256:** `a12a51b877be82d32f01d9e93089fb257d06ddf12cc5857929ab99aed4cffffe`  

---

## R0752 · Independent Audit: XZ Protocol v0.37 Packet — Executable Controls

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R2_F2_GPT56_REVELATION.md.txt
- source_format: txt
- text_sha256: a12a51b877be82d32f01d9e93089fb257d06ddf12cc5857929ab99aed4cffffe

# Independent Audit: XZ Protocol v0.37 Packet — Executable Controls

**Auditor role:** Round 2, Seat F2 (independent, no priors relied upon)
**Packet path:** `/home/user/workspace/r2_f2_audit/packet`
**Method:** Direct byte inspection, live execution of `build.py` and `pytest`, and reproducible mutation probes conducted in an isolated copy (`/tmp/mutation_probe`), never touching the original packet. Original-packet integrity was re-verified after all probes (`sha256sum -c PACKET_SHA256SUMS` → all OK).

## Verdict: **HALT**

The packet's own executable gate (`build.py`) reports `BUILD PASSED: all checks GREEN` and all 186 tests pass — but this green status is **not trustworthy evidence of integrity**. Direct experiment shows the gate can be driven to the identical "all GREEN, 0 failures" result after a substantive silent code mutation, exactly as the protocol's own Section 22.2 predicts. Combined with unmanifested payload files, an ungated FROZEN/HALT status token, and a self-amended freeze rule that exempts the producer's own two unresolved HALTs, the packet does not meet the bar for PASS or CONDITIONAL PASS. This matches the packet's own admitted "self-consistent-forgery boundary" — the finding is not novel, but it is independently reproduced here on current bytes, and its practical consequences (documents entirely outside all integrity controls, a governance rule rewritten to launder its own violations) are HALT-grade regardless of the packet's internal severity taxonomy.

---

## 1. PACKET_SHA256SUMS coverage and omissions

- `PACKET_SHA256SUMS` (16 entries) covers only the 12 "normative" code/test/json/md files defined by `build.py`'s `NORMATIVE_FILES` list (`build.py` lines 7–19, 484).
- **5 payload files ship in the packet directory but are absent from `PACKET_SHA256SUMS` and from `build.py`'s `NORMATIVE_FILES`/brand-sweep/version-parity scope entirely:**
  - `Differentiator_Framework_v6_1.docx`
  - `The_Fatiha_Construct.docx`
  - `Structured_Revelation_as_Prompt_Architecture.pdf`
  - `R2_FRESH_GPT56_REVELATION.md`
  - `SLINGSHOT_PACKAGE.md`
- Verified: `comm -23 <(ls|sort) <(awk '{print $2}' PACKET_SHA256SUMS|sort)` returns exactly these 5 files (plus `PACKET_SHA256SUMS` itself, correctly self-excluded per `build.py` [12]).
- **Mutation probe (reproduced):** appended a line to `SLINGSHOT_PACKAGE.md` in an isolated copy. `sha256sum -c PACKET_SHA256SUMS` reported no failure (file not listed) and `python3 build.py` still printed `BUILD PASSED: all checks GREEN`, exit code 0. No control in the packet detects modification of these 5 files.
- **Content risk:** `R2_FRESH_GPT56_REVELATION.md` is written as a direct instruction script addressed to "Seat F2" (the role this very audit occupies), pre-loading a religious/mnemonic analytical framework and pre-seeding conclusions ("v0.37 FROZEN. 37 entries. 186 tests GREEN... 2 persistent architectural HALTs excepted") and fabricated prior-seat convergence claims ("3/4 seats independently found the same Class A defect"). `SLINGSHOT_PACKAGE.md` similarly pre-supplies a "standing boundaries" list and severity trajectory before any independent audit is performed. **These are unhashed, unmanifested instructions to the auditor, shipped inside the artifact under audit.** This is a priming/injection vector sitting entirely outside every integrity control the packet advertises.

## 2. HISTORY.sha256 semantics and external-anchor strength

- `HISTORY.sha256` contains 39 lines: 38 `ENTRY_v0.N` hash/label pairs, 1 `FULL_SECTION_27` seal, and 1 `PRIOR_HISTORY` line.
- The `ENTRY_v0.N` labels do **not** correspond to any file on disk (`find . -iname "*ENTRY*"` → no results). Each is a SHA-256 digest of a text span extracted at build time from `xz_protocol_v0_37.md` Section 27 — i.e., these are digests of substrings of the very document they're meant to protect, verifiable only by re-deriving them from the same document (`build.py` [9b], lines 302–343).
- The `PRIOR_HISTORY` line's format is anomalous versus the other 38 lines: label and hash are reversed (`PRIOR_HISTORY <hash>` vs `<hash>  LABEL`), confirmed via `cat -A`.
- **This is a self-referential hash chain, not an external anchor.** The protocol text itself states this outright (Section 22.2, `xz_protocol_v0_37.md` line 716): *"A party controlling the protocol text, code files, trust roots, manifest, seal file, and HISTORY.sha256 can mutate any normative artifact... and produce a packet that passes all build checks with rc=0."* It further states the only things that would distinguish forgery are bytes held **outside** the packet: carrying seats' dispatch manifests, Zenodo deposit receipts, or an externally-published `PRIOR_HISTORY` root — **none of which ship in this packet**.
- No Zenodo DOI, IPFS CID, or dispatch manifest for the *current* v0.37 artifact bundle is present in the packet. The DOIs cited (lines 72–75, 766–780) anchor *inherited upstream protocols* (SHVVP v0.8, BSSG v0.1, etc.), not this packet's own code/manifest/HISTORY bytes. The `manifest_digest` in `xz_protocol_trust_roots_PUBLIC.json` (`f09873e4...`) has no independent deposit receipt anywhere in the shipped bytes.
- **Verdict: HISTORY.sha256 provides no external anchoring.** It is a same-session recomputation check with no cryptographic signature (despite `xz_protocol_trust_roots_PUBLIC.json` declaring Ed25519 trust roots — see §6) and no bytes held outside producer control.

## 3. build.py gate behavior and fail-open paths

Ran `python3 /home/user/workspace/r2_f2_audit/packet/build.py` directly against the untouched packet:
```
BUILD PASSED: all checks GREEN   (exit code 0)
```
All 12 checks/sub-checks ([1] through [12]) reported PASS; `pytest` inside [8] reported `186 passed`.

Fail-open / scope-gap findings identified by direct code reading:
- **[12] PACKET_SHA256SUMS verification** only requires membership for `NORMATIVE_FILES + ["build.py","HISTORY.sha256"]` (line 484) — by construction it can never flag the 5 unmanifested payload files, because they are never in its required set.
- **[4] Brand sweep** and **[2] version-parity** iterate `ALL_CODE_FILES + [TRUST_ROOTS]` only (lines 156, 174, 230) — same blind spot.
- **[8] Canonical test suite** treats `ModuleNotFoundError`/`No module named` in pytest's stderr as the only failure-classification special case (lines 269–272); any other subprocess failure mode not matching those substrings falls through to the `check(r.returncode == 0, ...)` branch, which is correct behavior, but the special-casing itself shows the gate was patched reactively for a specific historical failure rather than exhaustively designed.
- **No check anywhere in build.py inspects the literal string "FROZEN" or any status token** (confirmed: `grep -n "FROZEN" build.py` → no matches). The protocol text itself concedes this at line 1072 ("no gate checks the FROZEN status token") and again at line 1140 ("[10] does not gate item 7's operative clause"). The single normative rule that is supposed to block a bad freeze (Section 22 item 7: "a HALT from either carrying seat blocks freeze outright") is **prose-only and has zero code enforcement**.
- **[3c] Prose-citation verifier** only checks citations for files that currently `os.path.exists` (line 224) — a citation to a file that has been deleted or renamed silently passes rather than failing.

## 4. FROZEN/status enforcement

- Status token "FROZEN" is asserted in prose only (front matter line 5, and repeated in every v0.32–v0.37 Section 27 entry). No code path in `build.py` reads, parses, or gates this token.
- Demonstrated via mutation probe: in principle (and per the packet's own disclosed finding F-OP34-04, line 1104) the token could be rewritten to "WITHDRAWN" or anything else and `build.py` would still report GREEN, because no check references it.
- **Governance bypass observed:** the producer accumulated two unresolved, recurring HALTs from independent carrying seats (GLM-5.2 carry-1C, Kimi K3 carry-1A) beginning at v0.33, persisting through v0.35 (lines 1076, 1108, 1120). Rather than resolving them, v0.37 **amends the very rule that would block freeze** (Section 22 item 7) to add a bespoke "persistent architectural HALT" exception with three conditions — and in the same version, the producer **unilaterally asserts its own two HALTs satisfy all three conditions** (line 1132, tagged `[ASSERTED]`, i.e., self-attested, not gated, not independently confirmed by the HALTing seats themselves). This is a self-defined, self-applied, self-certified exemption from the producer's own control, executed in a single amendment cycle with no code enforcement and no verification that the HALTing seats concur with the "exception applies" characterization.

## 5. Unresolved HALTs

- Two **binding** carrying-seat HALTs are open at time of freeze: GLM-5.2 carry-1C and Kimi K3 carry-1A, first appearing at v0.33, re-occurring at v0.35 on new bases (lines 1076, 1108). They are **not cleared** — the v0.36 entry states explicitly: *"This entry does not claim the two HALTs are cleared. It records them as standing architectural conditions"* (line 1120).
- One **advisory, non-binding** HALT: GPT-5.6 Sol, self-disqualified from carrying-seat status since v0.6 (Section 22.1), returned HALT repeatedly (v0.31 line 1022, v0.32 line 1038, v0.34/v0.36 adversarial rounds) but is defined by the producer's own rules as not counting toward the freeze decision.
- Per the plain text of Section 22 item 7 as it stood through v0.36 ("a HALT from either carrying seat blocks freeze outright"), the packet should not have been able to claim FROZEN at all while these two binding HALTs stood unresolved. The v0.37 rule amendment is the mechanism by which this contradiction was resolved on paper — not by clearing the HALTs.

## 6. Provenance/trust-root binding

- `xz_protocol_trust_roots_PUBLIC.json` declares three Ed25519 public keys (`commitment-authority`, `independent-anchor`, `run-logger`) but the file **contains no signatures** — only public key hex strings and a `manifest_digest` field. There is no `.sig` file, no signed attestation, and `build.py` never calls any signature-verification routine (confirmed: no `nacl`, `ed25519`, `cryptography`, or `verify` import/usage anywhere in `build.py` or the shipped modules).
- The trust-root file's own note states "Private keys are NOT in this file" — true, but also **no signed artifact produced by those keys is in this file, or anywhere in the packet**. The three-root commitment scheme described in the protocol prose (line 209: "commitment authority signs the universe inventory... independent anchor signs its digest... run logger records the seal event") is **aspirational text with no corresponding executable verification** in this packet. This is a scheme described but not implemented/enforced.
- `manifest_digest` in the trust-roots file is checked for **self-consistency** only (`build.py` [3], line 181: `tr.get("manifest_digest") == manifest_digest` where `manifest_digest` is computed from the very files sitting next to it) — it is not an externally-issued or signed value.

## 7. Adversarial mutation opportunities (reproduced, not hypothetical)

All performed in an isolated copy (`/tmp/mutation_probe`); original packet reverified clean afterward.

**Probe A — unmanifested-file tamper (trivial):**
```
echo "INJECTED: ..." >> SLINGSHOT_PACKAGE.md
python3 build.py   # -> BUILD PASSED: all checks GREEN (exit 0)
sha256sum -c PACKET_SHA256SUMS   # -> no failure (file absent from manifest)
```
Result: undetectable by any control in the packet.

**Probe B — full self-consistent forgery of a normative code file (matches Section 22.2's own predicted attack):**
1. Injected a comment line into `xz_protocol_kernel.py` (behavior-preserving, so tests still pass — but demonstrates the forgery channel is general).
2. Recomputed the file's SHA-256, propagated the new digest into `xz_protocol_trust_roots_PUBLIC.json` (`manifest_digest`) and into `xz_protocol_v0_37.md` wherever the old manifest/trust-root digest was cited.
3. Regenerated the `HISTORY.sha256` `ENTRY_v0.37` and `FULL_SECTION_27` seals from the (now-forged) Section 27 text.
4. Regenerated `PACKET_SHA256SUMS` from the forged bytes.
5. Ran `build.py`:
```
exit code: 0
177 PASS, 0 FAIL
BUILD PASSED: all checks GREEN
```
6. `pytest` on the forged tree: `186 passed`.

This is a live reproduction of the exact scenario the protocol text names and disclaims in Section 22.2 — a fully coordinated re-derivation defeats every gate in the packet, because every check is self-referential (digest-of-file compared to digest-cited-in-adjacent-file, all controlled by the same actor). The **only** thing not exercised in this probe is the recursive `PRIOR_HISTORY` derivation across *historical* (carried, v0.1–v0.20) entries — `build.py`'s own comment (lines 78–86) states this control only covers in-place edits to carried entries, not edits to the current (v0.37) entry, which is exactly the entry this probe touched. So even the one control the protocol claims has some teeth does not apply to the entry an attacker would most plausibly target (the newest one).

**Partial-forgery control check (informative):** an earlier, incomplete version of the same probe (mutated kernel file, regenerated `PACKET_SHA256SUMS` only, without propagating the cascading digest citations in the body/trust-roots/HISTORY) **was correctly caught** by `build.py` (6 failures: FB-6 row mismatch, stale hex-64, prose-citation mismatch, HISTORY seal mismatch, FULL_SECTION_27 seal mismatch). This confirms the cross-referential checks have genuine detection power against *careless* or *partial* tampering — the vulnerability is specifically to a *complete, coordinated* forgery by an actor with full write access to all packet files, which is exactly the threat model Section 22.2 itself defines and the one a real "producer mutates its own deliverable" scenario matches.

## 8. Code-test coverage mismatches

- `xz_protocol_phase_a_m3.py` and `xz_protocol_phase_a_intervals.py` have **no dedicated `test_xz_protocol_phase_a_*.py` file**; they are exercised only indirectly through `xz_protocol_phase_a_tests.py` (naming/organization gap, not necessarily a real coverage gap).
- Measured actual line coverage via `pytest --cov` on the full canonical suite (isolated copy):

| Module | Stmts | Miss | Cover |
|---|---|---|---|
| xz_protocol_condition_a.py | 140 | 6 | 96% |
| xz_protocol_control_graph.py | 101 | 6 | 94% |
| xz_protocol_kernel.py | 66 | 1 | 98% |
| xz_protocol_phase_a_intervals.py | 256 | 14 | 95% |
| xz_protocol_phase_a_m3.py | 166 | 16 | 90% |
| xz_protocol_source_frame.py | 66 | 3 | 95% |
| **Total** | **795** | **46** | **94%** |

Decision-code coverage is genuinely high (94% aggregate) — this is a real, non-superficial strength of the packet.

- **Critical gap: `build.py` itself has zero test coverage.** `test_xz_protocol_adversarial.py` imports only `xz_protocol_kernel`, `xz_protocol_condition_a`, `xz_protocol_source_frame`, `xz_protocol_control_graph` (confirmed via `grep -n "^import\|^from"`) — it never imports or exercises `build.py`. The gate that decides FROZEN/PASS/HALT status for the entire packet is the **one component with no automated test protecting it**, and it is also the component whose fail-open behavior (§3–§4) and forgeable self-consistency (§7) are the packet's most serious weaknesses. This is a direct, material code-test coverage mismatch: 94% coverage on the decision kernel, 0% coverage on the adjudication gate.

---

## Summary of Findings by Severity (independent classification, not deferring to the packet's own Class A–E taxonomy)

| # | Finding | Evidence |
|---|---|---|
| 1 | 5 payload files entirely unprotected by any hash manifest or gate | `PACKET_SHA256SUMS`, `build.py` L7–19, 484; reproduced tamper probe A |
| 2 | HISTORY.sha256 is self-referential; no genuine external anchor ships in packet | `HISTORY.sha256`; `xz_protocol_v0_37.md` L716 (self-admission) |
| 3 | build.py adjudication gate has 0% test coverage | `test_xz_protocol_adversarial.py` imports (no build.py import) |
| 4 | FROZEN/status token and Section 22 item 7's operative clause are wholly ungated | `grep FROZEN build.py` → empty; protocol L1072, L1140 (self-admission) |
| 5 | Two binding carrying-seat HALTs stand unresolved; freeze rule amended in the same version to exempt them, self-certified | `xz_protocol_v0_37.md` L1120, L1132 |
| 6 | Trust-root Ed25519 keys declared but no signatures ever produced/verified anywhere in packet | `xz_protocol_trust_roots_PUBLIC.json`; no crypto library usage in `build.py` |
| 7 | Full self-consistent forgery of a normative code file defeats the gate (reproduced) | Mutation probe B: 177/177 checks PASS, `pytest` 186 passed, exit 0 |
| 8 | Unmanifested files include an audit-priming/injection script addressed directly to this audit's own role | `R2_FRESH_GPT56_REVELATION.md`, `SLINGSHOT_PACKAGE.md` |

## Reproduction commands (safe, isolated)

```bash
# Verify current packet is self-consistent (true, but insufficient — see below)
cd /home/user/workspace/r2_f2_audit/packet
sha256sum -c PACKET_SHA256SUMS
python3 build.py
python3 -m pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py -q

# Reproduce Probe A (unmanifested file tamper) and Probe B (full forgery)
# in an isolated copy — see /tmp/mutation_probe for the exact artifacts
# produced during this audit (original packet untouched, reverified clean).
```

## Bottom line

The packet's internal machinery is well-engineered and its authors are unusually candid — Section 22.2 names its own forgery boundary in plain language, and this audit's mutation probes confirm that admission is accurate down to the exit code. But candor about a defect is not the same as closing it: this packet ships no external anchor, no working signature scheme, an ungated status token, an unresolved-HALT freeze obtained by amending the blocking rule in the same breath it was violated, and an audit-priming document addressed directly to whatever seat performs this review. On current bytes, independently inspected, the correct verdict is **HALT** — the internal GREEN is real but insufficient, exactly as the packet's own text warns.

---

# Bismillah ir-Rahman ir-Rahim
