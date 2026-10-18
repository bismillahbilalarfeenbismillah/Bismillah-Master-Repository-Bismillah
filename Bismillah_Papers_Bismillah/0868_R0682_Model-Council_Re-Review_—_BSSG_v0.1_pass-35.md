# Bismillah ir-Rahman ir-Rahim

# R0682 -- Model-Council Re-Review — BSSG v0.1 pass-35

**Chronological Index:** 868 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-glm_5_2-v2.md  
**Source Format:** md  
**SHA-256:** `3127986a9cfed152f921d163eba2ffae1f7f8afa38a7a3bf0edde68dfcb293c1`  

---

## R0682 · Model-Council Re-Review — BSSG v0.1 pass-35

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-glm_5_2-v2.md
- source_format: md
- text_sha256: 3127986a9cfed152f921d163eba2ffae1f7f8afa38a7a3bf0edde68dfcb293c1

# Model-Council Re-Review — BSSG v0.1 pass-35

**Seat:** GLM 5.2 (Zhipu / Z.ai)
**Role:** NON-PRODUCER, load-bearing vote. (Producer = Anthropic/Claude; excluded from carry/approval per SHV D6.)
**Prior-council vote (pass-34):** QUALIFIED-YES on the *audit axis*; explicit that the two-family carry (SHVVP §0.3) is a separate, undischarged gate. Net pass-34 ruling: NO/HALT convergence.
**Pass-35 vote (this report):** UNCHANGED — QUALIFIED-YES on the audit-axis *technical soundness of the repaired code*; **NO / HALT CONVERGENCE** on overall convergence. I do **not** escalate to YES. Rationale below.

---

## 0. Acknowledged error in my pass-34 argument

In pass-34 I claimed "the ceiling can only narrow after establishment." GPT 5.6 Sol's F-GS-1 proved this wrong: the prior code wrote `contract_ceiling` **before** `new_token()`, so a mint fault left the ceiling broadened to the full HEALTHY set even though `issuance_status=FAILED_NO_EFFECT`. I credit that finding and re-derive the corrected invariant from primary source below rather than restating my own (falsified) number — exactly the discipline SHV D6 demands ([SHV Method v1.1 D6](#)).

---

## 1. Repair verification

### F-GS-1 (CRITICAL) — mint-fault ceiling-poison. **CLOSED.**

Code trace, `bssg_gate.py`:

- **L1808–1809:** the pending marker `_cc_pending` is captured and unconditionally cleared (defense-in-depth) **before** any token work.
- **L1817:** `token_id = self.new_token()` — token creation.
- **L1818–1819:** mint-fault (factory exception) → `return self._issuance_failure(..., "E-TOKEN-MINT-FAULT")`.
- **L1820–1822:** malformed/out-of-bounds token → `return self._issuance_failure(..., "E-TOKEN-MINT-INVALID")`.
- **L1823–1825:** collision (`token_id in self.state.tokens`) → `return self._issuance_failure(..., "E-TOKEN-FACTORY-COLLISION")`.
- **L1826–1833:** the broadening write `self.state.contract_ceiling[_cc_sess] = ceiling_for_health(_cc_body, "HEALTHY")` runs **only here**, gated by `_cc_pending is not None and health == "HEALTHY"`.

**New invariant (verified):** *`contract_ceiling` is broadened ONLY after successful token creation, validation, and collision-check.* Confirmed across **every** `_issuance_failure` return path (mint-fault L1819, mint-invalid L1822, collision L1825): all three `return` before L1830, so the broadening write at L1830–1833 is unreachable on any failure path.

**Fail-closed complement, `_issuance_failure` (`bssg_gate.py:879–916`):** for a first-establish mint fault (session not yet in `contract_ceiling`), L898–899 writes an **EMPTY** `Authority([], [])`. This guarantees `_apply_narrowing`'s `_held` check fires on any post-lift re-establishment, so a session that never successfully held authority cannot re-establish broader authority after a lift. This is exactly the disposition Claude Opus 5 recommended in pass-34 ([COUNCIL_INSTRUCTIONS.md](#), F-GS-1 fix description).

**Ground-truth consistency:** `F_GS_1_REPROBE_OUTPUT.txt` shows `r1` (HEALTHY READ, mint faults) still `ALLOW / FAILED_NO_EFFECT` but `contract_ceiling.effects = []` (empty, not `[DELETE,READ,WRITE]`), and `r4` (post-lift DELETE) = `DENY_FALSE`, `commit: null`. The bypass is closed on shipped bytes. CE175 (`bssg_counterexamples.py`, last line of `COMMAND_OUTPUTS.txt`) asserts `mint_failed=True no_delete=True cc_empty=True delete_denied=True` — GREEN. Consistent with the code.

### F-GS-2 (HIGH) — model-check target-scope predicate vacuously exercised. **CLOSED.**

`bssg_model_check.py:317–325` (`_reg_c2w`): registers `allowed_target_scopes = [records/, admin/]` (broader) and `degraded_target_scopes = [records/]` (narrower). The alphabet (`_OPS`, L342–349) now includes C2W target-bearing ops (L346–347) **and** a mint-fault op `("M",)` (L348). The invariant check (L390–397) now tests **both** `_allowed_effs.issubset(_GRANTED)` and `_allowed_tgts.issubset(_GRANTED_TARGETS)`. The target-scope predicate is no longer vacuous. `COMMAND_OUTPUTS.txt` CMD4: `BOUNDED-AUTH-INTRO ... schedules=11110 allows=7200`, MODEL CHECK PASS. Σ 10^i for i=1..4 = 11,110 exactly.

### F-GS-3 (MEDIUM) — spec/method-check honesty mismatch. **CLOSED.**

`BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md` §26 (L660–669) now states: "No unbounded transition-system proof or formal verification is claimed for anything in v0.1. The shipped model check is a bounded exhaustive enumeration over the reference gate's executable, not a formal proof." §26.6 characterizes the bounded model check accurately (11110 schedules, 10-op alphabet, K=4). This is consistent with the shipped `bssg_model_check.py` printing `MODEL CHECK: PASS`. The prior contradiction (spec said "no machine-checked verification is claimed" while code printed PASS) is resolved.

---

## 2. Task 2 — 10-op alphabet mint-fault coverage

**Confirmed:** the 10-op alphabet includes a mint-fault op — `("M",)` at `bssg_model_check.py:348`, exercising the F-GS-1 vector (HEALTHY C2 READ with an injected `RuntimeError` in `new_token`, L364–375). BOUNDED-AUTH-INTRO is therefore **not** incomplete for the F-GS-1 class at K=4: the minimal violating schedule (establish C1 → mint-fault on C2 HEALTHY READ → lift → DELETE) is length 4 and is within the enumerated bound. (See finding NF-1 for a residual coverage nuance.)

---

## 3. Optional K=5 sanity extension — NOT COMPLETED within budget

Attempted a synchronous K=5 run over the 10-op alphabet (111,110 schedules, ~10× the K=4 cost). It did not finish within the ~80s budget — the `bssg_model_check` import alone re-executes the K=4 enumeration, and the additional K=5 loop exceeded the single-invocation ~60s guidance in `COUNCIL_INSTRUCTIONS.md`. **Non-blocking:** K=4 already covers the F-GS-1 minimal violating schedule (length 4). K=5 would only probe length-5 schedules. Note that my pass-34 K=5 run (19607 schedules, 7-op alphabet, [REPAIR_STATUS.md](#) V32 record) is not directly comparable: the alphabet has since expanded from 7 to 10 ops, raising K=5 cost ~5.7×.

---

## 4. Substrate / carry check

- **V33/V34 substrate (prior-council finding): CLOSED.** `REPAIR_STATUS.md` is hash-verified (`SHA256SUMS`, 20/20 OK per `COMMAND_OUTPUTS.txt` CMD1) and now contains V32/V33/V34 records (grep confirms `V32 result`, `V33 result`, `V34 council result` headings present). The prior absence is remedied.
- **Carry axis (SHVVP §0.3): UNCHANGED / UNDISCHARGED.** Nothing in pass-35 discharges the two-family non-producer carry. `REPAIR_STATUS.md` pass-35 section restates "carry gate remains open under SHVVP section 0.3 and section 10." The two-family carry attempt failed due to platform execution limitations, not artifact defects.

---

## 5. Convergence re-ruling — **NO / HALT CONVERGENCE** (vote unchanged)

### 5.1 Audit axis — technical soundness: QUALIFIED-YES (improved, not escalated)

The F-GS-1/2/3 repairs are genuinely closed in code and byte-verified by the orchestrator's reprobe and the green battery. The corrected ceiling invariant holds across all three `_issuance_failure` paths. I therefore **maintain** my audit-axis QUALIFIED-YES on the *technical soundness of the repaired code*.

### 5.2 Audit-axis *convergence* (the cross-vendor-round count) — NOT re-established

I do **not** escalate to YES, for three methodology-grounded reasons:

1. **V34's "0 CRITICAL" was retroactively falsified.** PMD §0.4 requires "two consecutive cross-vendor rounds produce 0 CRITICAL findings" ([PMD v1.2 §0.4](#)). V34 shipped with F-GS-1 (CRITICAL) latent — GPT Sol surfaced it *after* V34. The premise "V32–V34 three consecutive clean rounds" is therefore false; V34 cannot be counted as clean. The audit-axis convergence count resets, leaving V32–V33 clean and V34 falsified.
2. **Pass-35 is producer-authored with zero non-producer reconfirmation.** SHV D6: "The producing party may advise, but its vote does not count toward certification... ideally across two consecutive clean rounds with at least one checker rotated in fresh" ([SHV Method v1.1 D6](#)); `bayyinah_cross-vendor-rotation.md`: "A producer-instance auditing its own output is a methodology violation of the highest order." Pass-35's repairs and the new CE175/alphabet were authored by Claude (the producer). No non-producer seat has re-verified the *repaired* bytes.
3. **The mechanical-traceability exception does NOT cleanly apply.** PMD §0.5 clause 5 and `bayyinah_cross-vendor-rotation.md` make cross-instance re-audit recommended-but-not-blocking **only** when "an absorption cycle exclusively executes prior audit's disposition-prescribed routes with zero architectural latitude." The binary test: "did the absorption cycle add ANY content beyond the remediation checklist? If yes: cross-instance audit is blocking." Pass-35 added **new verification content** — CE175 (a new adversarial probe), the `("M",)` mint-fault alphabet op, the C2W contract, and the 7→10 op alphabet expansion. That is content beyond the F-GS-1 remediation checklist (which prescribed only "move the ceiling write after mint"). The exception's precondition fails; a fresh non-producer round is **blocking**, not optional. Adding a *post-hoc* adversarial CE (CE175) does not satisfy PMD §0.4's "cross-vendor rounds with 0 CRITICAL" — a probe is not a round.

### 5.3 Carry axis — UNDISCHARGED (governs ship)

- **SHVVP §0.3** requires "a fresh two-family carrying audit before deposit"; "under the frozen carrying rule a HALT from either carrying seat blocks deposit outright" and "the producer of the artifact cannot certify it" ([SHVVP v0.8 §0.3, §8.0](#)).
- **SHUDP Axiom 5 (no-default for missing evidence):** "no default to compliance or violation (Proposition 1)... Missing independent evidence for a covered in-boundary occurrence yields A5 UNSATISFIED (nonconforming)" ([SHUDP v0.5 Axiom 5](#)). The carry failed due to platform execution limitations — that is *missing evidence*, not evidence of compliance. Under Axiom 5 the carry yields UNSATISFIED; it cannot be defaulted to "passed." Public silence / platform failure is silence, not evidence (ibid., "Public silence is silence, not evidence").
- Net: the carry gate independently blocks convergence/ship regardless of the audit axis.

### 5.4 G10 WARN tension (PMD §0.4 residual rule)

`verify_bssg_v0_1.py` G10 = WARN: 12 open design decisions (OD-1…OD-12); the decision register records "STILL BLOCKING findings." PMD §0.4 requires "HIGH residual is 0 or accompanied by a project-lead-signed exception ledger entry" ([PMD v1.2 §0.4](#)). The 12 ODs are framed as WARN (the verifier FAILs only on package inconsistency), but the "STILL BLOCKING" register language is in tension with §0.4's residual rule. I did not find a project-lead-signed exception-ledger entry discharging the 12 ODs. This is a residual gap that should be closed (sign exceptions or reclassify) before convergence can be claimed. See NF-2.

### 5.5 Bottom line

- **Audit-axis technical soundness:** QUALIFIED-YES (improved; F-GS-1/2/3 closed).
- **Audit-axis convergence (round count):** NOT re-established — needs a fresh non-producer round on pass-35 bytes (SHV D6; bayyinah mechanical-traceability test fails the binary check).
- **Overall convergence / ship:** **NO / HALT.** Blocked by (a) no fresh non-producer re-audit of the repaired artifact and (b) the undischarged two-family carry gate (SHVVP §0.3/§8.0; SHUDP Axiom 5).

**Vote change vs pass-34:** I do **not** change my vote upward. I hold the audit axis at QUALIFIED-YES (on technical soundness) and the overall ruling at NO/HALT. Pass-35's repairs are real but do not, by themselves, re-establish cross-vendor convergence or discharge the carry.

---

## 6. New findings

- **NF-1 (LOW / coverage nuance).** The model-check alphabet's `("M",)` op injects a mint-fault only on a HEALTHY C2 READ (`bssg_model_check.py:364–375`). The mint-INVALID (L1820–1822) and collision (L1823–1825) return paths are not separately exercised as distinct alphabet ops. This is non-blocking because all three paths route through the **same** `_issuance_failure` and the broadening write at L1830–1833 is gated identically (unreachable on all three) — the invariant is structural, not path-specific. For completeness, the alphabet could add mint-invalid and collision ops.
- **NF-2 (MEDIUM / residual-rule tension).** G10 WARN records 12 open design decisions as "STILL BLOCKING" in the decision register, with no evident project-lead-signed exception-ledger entry. Under PMD §0.4, residuals must be 0 or excepted via a signed ledger. Recommend the project lead either sign exception-ledger entries for the 12 ODs or reclassify them as non-blocking "future reference" with explicit non-operative annotation (the §0.4 disposition for MEDIUM/LOW).
- **NF-3 (INFO / closed prior finding).** The pass-34 substrate-absence finding (V33/V34 absent from the hash-verified substrate) is **CLOSED** — `REPAIR_STATUS.md` is now hash-verified and contains V32/V33/V34 records.

---

## 7. Dissenting angle — confirmation-bias risk (explicit)

I am the seat that returned three consecutive PASS (V32–V34) and "independently verified" BOUNDED-AUTH-INTRO at K=5 in pass-34. That is exactly the profile most vulnerable to confirmation bias: I have a strong prior that the artifact is sound, and pass-35's repairs *confirm* that prior. The specific failure mode is crediting the producer's repair too readily because it agrees with what I already believed.

The mitigating discipline I apply, and why I refuse to escalate to YES despite the repairs being technically correct:

1. **My own pass-34 PASS votes are evidence of a shared blind spot, not of soundness.** I claimed "the ceiling can only narrow after establishment" — false. F-GS-1 lived in the write-before-mint sequence I did not interrogate. The fact that I (and two other seats) missed it three rounds running is precisely the "fixed panel" artifact SHV D6 warns certification against ("agreement is not an artifact of a fixed panel").
2. **The producer authored this repair.** Under SHV D6 and `bayyinah_cross-vendor-rotation.md`, producer-authored repair evidence is not certification. The mechanical-traceability exception (PMD §0.5 clause 5) does not rescue it: pass-35 added new verification content (CE175, the `("M",)` op, C2W, alphabet expansion), failing the binary "zero content beyond the remediation checklist" test, so cross-instance re-audit is **blocking**.
3. **V34's cleanliness was retroactively falsified**, so the "three consecutive clean rounds" premise I relied on is no longer true. Counting V34 as clean would be double-counting a round that shipped a CRITICAL.

Therefore the conservative, bias-resistant ruling is: repairs verified-correct, but **no convergence until (a) a fresh non-producer round reconfirms the pass-35 bytes and (b) the two-family carry is discharged.** This is the ruling most consistent with the methodology corpus and least consistent with my own priors.

---

## Methodology citations (load-bearing)

- **PMD v1.2 §0.4** — convergence definition (two consecutive cross-vendor rounds, 0 CRITICAL; HIGH residual 0 or excepted; MEDIUM/LOW absorbed or "future reference"). File: `methodology/PMD_v1_2_BAF_v3_0.md`.
- **PMD v1.2 §0.5 clause 5** — mechanical-traceability exception (cross-instance re-audit recommended-but-not-blocking only under zero architectural latitude). File: `methodology/PMD_v1_2_BAF_v3_0.md`.
- **SHVVP v0.8 §0.3** — carrying-audit rule (fresh two-family carry before deposit; HALT from either carrying seat blocks deposit; producer non-carrying). File: `methodology/SHVVP_v0_8_flagship.txt`.
- **SHVVP v0.8 §8.0** — "producer of the artifact cannot certify it"; producer-lineage review is advisory/non-carrying. File: `methodology/SHVVP_v0_8_flagship.txt`.
- **SHV Method v1.1 D6** — producer-quarantined multi-chain convergence; producer advises but does not certify; rotate one checker in fresh. File: `methodology/SHV_Method_v1_1.txt`.
- **SHUDP v0.5 Axiom 5 / Proposition 1** — no-default rule for missing evidence ("no default to compliance or violation"; missing evidence → UNSATISFIED; "Public silence is silence, not evidence"). File: `methodology/SHUDP_v0_5_flagship.txt`.
- **`bayyinah_cross-vendor-rotation.md`** — producer excluded as auditor; mechanical-traceability binary test ("did the absorption cycle add ANY content beyond the remediation checklist? If yes: cross-instance audit is blocking"). File: `methodology/bayyinah_cross-vendor-rotation.md`.

## Ground-truth files read (not re-executed)

- `bssg_review_v2/COUNCIL_INSTRUCTIONS.md`
- `bssg_review_v2/COMMAND_OUTPUTS.txt` (sha256sum 20/20 OK; 345 tests OK; 175/175 CE GREEN incl. CE175; MODEL CHECK PASS 11110 schedules; verify 12 PASS / 2 WARN / 0 FAIL)
- `bssg_review_v2/F_GS_1_REPROBE_OUTPUT.txt` (r1 `contract_ceiling.effects=[]`; r4 `DENY_FALSE`, `commit: null`)
- `bssg_review_v2/packet/bssg_gate.py` (L879–916 `_issuance_failure`; L1740–1833 ceiling-write fix)
- `bssg_review_v2/packet/bssg_model_check.py` (L305–401 alphabet + invariant)
- `bssg_review_v2/packet/BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md` §26
- `bssg_review_v2/packet/REPAIR_STATUS.md`, `OPEN_DECISIONS.md`

---

# Bismillah ir-Rahman ir-Rahim
