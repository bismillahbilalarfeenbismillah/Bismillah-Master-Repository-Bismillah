# Bismillah ir-Rahman ir-Rahim

# R0669 -- Model Council Seat Report — BSSG v0.1 pass-35 Re-Review

**Chronological Index:** 860 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-claude_opus_5_0-v2.md  
**Source Format:** md  
**SHA-256:** `724417b09e30371a5d77bd3adaaf6936d3a003a22d181d702a1cf3f38f24675e`  

---

## R0669 · Model Council Seat Report — BSSG v0.1 pass-35 Re-Review

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-claude_opus_5_0-v2.md
- source_format: md
- text_sha256: 724417b09e30371a5d77bd3adaaf6936d3a003a22d181d702a1cf3f38f24675e

# Model Council Seat Report — BSSG v0.1 pass-35 Re-Review

## 0. Model self-identification and vote status

**Model:** Claude Opus 5 (Anthropic).

> **PRODUCER FAMILY — ADVISORY ONLY. THIS SEAT CASTS NO LOAD-BEARING VOTE.**
> Anthropic/Claude is the producer of the BSSG v0.1 artifact. Under
> `bayyinah_cross-vendor-rotation.md` § *Producer-instance exclusion* ("If the artifact under
> audit was produced by Claude: Claude is excluded from the auditor pool for that audit, OR
> Claude is relegated to advisory-only role (cannot HALT or assign CRITICAL / HIGH severities;
> can flag for human review)"), this seat:
> - **MAY NOT** assign CRITICAL or HIGH severity;
> - **MAY NOT** HALT;
> - **MAY NOT** contribute consensus weight to the council's convergence vote;
> - **MAY** flag findings for human/project-lead review and advise.
>
> Severities below are therefore written as **advisory-CRITICAL-class / advisory-HIGH-class**,
> i.e. *what a non-producer seat would need to independently reproduce and re-rate before the
> finding carries any weight*. This is also the discipline of **SHV Method v1.1 D6**
> ("Producer-quarantined, multi-chain convergence. No party certifies its own work… The
> producing party may advise, but its vote does not count toward certification.").

**Prior seat (pass-34):** Qualified-NO (advisory). Filed A-01 (advisory-HIGH-class: G12 heading
selector silently locks onto the pass-30/V28 section because V32/V33 sections used a
non-canonical heading format) plus five further advisory findings, and recommended the exact
F-GS-1 remedy (defer the `contract_ceiling` write until after successful token mint) that
pass-35 implements.

**This pass (advisory):** **QUALIFIED-NO — vote UNCHANGED.** The three named defects are
genuinely closed on shipped bytes; the *convergence* claim is not thereby restored. Reasoning in
§4.

---

## 1. Ground truth consumed (not re-executed)

Per instruction, the five prescribed commands were **not** re-run. I read the orchestrator's
verbatim outputs:

- `/home/user/workspace/bssg_review_v2/COUNCIL_INSTRUCTIONS.md`
- `/home/user/workspace/bssg_review_v2/COMMAND_OUTPUTS.txt` — 20/20 SHA256 OK; 345 tests OK
  (skipped=8); **175/175 CE GREEN, 0 RED**; MODEL CHECK: PASS (kernel 243 + antitone 729 +
  bounded-auth-intro 11,110 schedules / 7,200 allows / 10-op alphabet at K=4 + operational
  refinement); verifier **12 PASS / 2 WARN / 0 FAIL**; status **SELF-CONSISTENT DRAFT (not
  carried, not publication ready)**; gate banner **DRAFT / NOT CARRIED. No effectiveness claim.**
- `/home/user/workspace/bssg_review_v2/F_GS_1_REPROBE_OUTPUT.txt`

Arithmetic spot-check of the model-check claim: Σ 10^i for i=1..4 = 10 + 100 + 1000 + 10000 =
**11,110**. Reconciles exactly. The alphabet expansion from 7 ops (2,800 schedules) to 10 ops is
therefore genuine, not a relabeling.

---

## 2. Repair verification

### 2.1 A-01 (my pass-34 finding) — G12 heading selector: **CLOSED**, with residual

**Mechanism (read, not assumed).** `verify_bssg_v0_1.py` G12 selects the current claim surface
with:

```
_heads = [(int(m.group(1)), m.start())
          for m in re.finditer(r"# BSSG v0\.1 -- Repair Status \(pass-(\d+)", status)]
_newest_n     = max(n for n, _ in _heads)
_newest_start = min(pos for n, pos in _heads if n == _newest_n)
_later        = [pos for _, pos in _heads if pos > _newest_start]
current       = status[_newest_start:(min(_later) if _later else len(status))]
```

**Heading census of the shipped `REPAIR_STATUS.md` (1,179 lines):**

| Line | Heading | Matches selector regex? | Selected `pass-N` |
|---|---|---|---|
| 1 | `# BSSG v0.1 -- Repair Status (pass-35)` | YES | **35 (newest)** |
| 48 | `# BSSG v0.1 -- Repair Status (pass-34)` | YES | 34 → section terminator |
| 74 | `# BSSG v0.1 -- repair33 / V30 adjudication …` | no | — |
| 127 | `# BSSG v0.1 -- pass-30 V29 WITHDRAWAL …` | no | — |
| 179 | `# BSSG v0.1 -- Repair Status (pass-30, post V28 audit)` | YES | 30 |
| 280… | `… (pass-29 … pass-16, post V… audit)` | YES | 29…16 |

`max(_heads) = 35` at offset(line 1); nearest later canonical head = line 48. **Current surface =
lines 1–47, which is the pass-35 section.** The pass-34 lock-onto-pass-30 failure I filed in A-01
cannot occur on these bytes. The producer's own changelog records the fix: "G12 heading selector:
REPAIR_STATUS headings restored to canonical (pass-N) format" (`REPAIR_STATUS.md` line 26).

**CE-count reconciliation.** The canonical statement inside the selected section is
`REPAIR_STATUS.md` line 31: "This document claims 175 counterexamples." G12 clause (5) compares
this to `len(set(re.findall(r'record\("CE(\d+)"', ce_src)))`. Corpus execution reports
**175/175 GREEN** (`COMMAND_OUTPUTS.txt` CMD 3). **175 = 175. Matches.** A-01's silent-staleness
vector (a stale section supplying a stale numeric claim that nonetheless passes) is closed on
these bytes.

**Advisory-MEDIUM residual A-01-R (see §5.1):** the fix restores *data* conformance, not
*selector* robustness — two of the six historical section headings (lines 74, 127) still do not
match the canonical regex, and the selector's section terminator is "next *canonical* heading in
file order," so any non-canonical-headed section inserted between the newest canonical head and
the next one is silently absorbed into the current claim surface.

### 2.2 V33/V34 records now in the hash-verified substrate: **PRESENT** (advisory-MEDIUM caveat)

Prior council found V33/V34 absent from the hash-verified ledger substrate. On pass-35 bytes,
`REPAIR_STATUS.md` — which is itself a `SHA256SUMS`-verified file, `REPAIR_STATUS.md: OK`
(`COMMAND_OUTPUTS.txt` CMD 1) — carries all three inside the pass-35 section:

- **V34** (lines 3–9): eight-model council, F-GS-1 CRITICAL, F-GS-2 HIGH, unanimous NO on
  convergence without carry, carry open under SHVVP §0.3 and §10.
- **V33** (lines 11–14): three seats (GPT-5.6, GLM-5.2, Kimi K2.6), zero BLOCKERs (third
  consecutive), 1 MODERATE (AUDIT-V33-01 commit BaseException totality → CE174).
- **V32** (lines 16–18): three seats, zero BLOCKERs, GLM first PASS in program history.

**Caveat.** These are *narrated inside the pass-35 producer section*, not deposited as separate
per-round audit records with their own substrate identity. Under
`bayyinah_substrate-of-record.md`-style substrate-uniqueness discipline and **PMD v1.2 §0.4**'s
requirement that "all standing-rule compliance checks pass (… substrate uniqueness)", a
producer's prose summary of a non-producer round is weaker evidence than the seat reports
themselves. Recording the *result* of V33/V34 is not the same as depositing the V33/V34 seat
artifacts. Advisory-MEDIUM; for project-lead disposition.

Also flagged: line 16 reads "**V32 result.** … zero BLOCKERs (**first and second consecutive**)",
which is internally incoherent — a single round cannot be both the first and the second
consecutive clean round. Advisory-LOW (ledger hygiene), but it sits directly on the
two-consecutive-clean-rounds axis that **PMD §0.4** makes load-bearing, so it should not be left
ambiguous.

### 2.3 F-GS-1 (mint-fault ceiling poison) — **CLOSED** on shipped bytes

`bssg_gate.py` ALLOW path, in execution order:

- **1808–1809** — `_cc_pending = getattr(self, "_contract_ceiling_pending", None)`; then
  `self._contract_ceiling_pending = None` unconditionally (defense-in-depth clear).
- **1815** — `token_id = self.new_token()` inside `try`; on exception →
  `return self._issuance_failure(request, conjuncts, snapshot, "E-TOKEN-MINT-FAULT")`. **No
  ceiling write occurs on this path.**
- **1817–1818** — malformed/out-of-bounds token → `_issuance_failure("E-TOKEN-MINT-INVALID")`.
- **1820–1822** — collision → `_issuance_failure("E-TOKEN-FACTORY-COLLISION")`.
- **1830–1834** — *only now*:
  `if _cc_pending is not None and health == "HEALTHY": self.state.contract_ceiling[_cc_sess] = ceiling_for_health(_cc_body, "HEALTHY")`.
- **897–899** (`_issuance_failure`) — F-GS-1 companion: if the session has no
  `contract_ceiling` entry, write `Authority([], [])`, so the `_held` check at **1935** fires on a
  post-lift re-establishment instead of falling through the free-establishment branch.

This is precisely the remedy this seat recommended in pass-34: the write is now downstream of
mint, validation, and collision-check, and the failure path installs an *empty* held-authority
floor rather than none.

Consistent with ground truth: `F_GS_1_REPROBE_OUTPUT.txt` `state_after_r1.contract_ceiling =
{effects: [], target_scopes: []}` (was `[DELETE, READ, WRITE]`), and
`r4_healthy_delete_after_lift` = `DENY_FALSE`, `authority_snapshot: null`, top-level
`commit: null`. CE175 locks the vector (`mint_failed=True no_delete=True cc_empty=True
delete_denied=True`). **Code, probe, and corpus agree. F-GS-1 CLOSED.**

### 2.4 F-GS-2 (vacuous target-scope coverage) — **CLOSED** (accepted on orchestrator verification)

Per `COUNCIL_INSTRUCTIONS.md`, `bssg_model_check.py:317–322` `_reg_c2w` sets
`allowed_target_scopes = [records/, admin/]` (strictly broader) with
`degraded_target_scopes = [records/]` (narrower), and `_OPS` now includes C2W target-bearing
operations. The independent arithmetic check confirms the alphabet genuinely grew to 10 ops
(11,110 schedules at K=4; 7,200 allows) and `COMMAND_OUTPUTS.txt` CMD 4 reports
`BOUNDED-AUTH-INTRO … no violation`. The predicate is no longer vacuous w.r.t. target
introduction. Closed. *(Advisory note: I did not re-derive the 7,200-allow figure; a non-producer
seat should, since it is the only number in the packet not cross-checked by a second artifact.)*

### 2.5 F-GS-3 (§26 verification-claim contradiction) — **CLOSED as an internal contradiction**

`REPAIR_STATUS.md` line 27 records "README verifier block and spec section 26 updated to match
current state", and G5 PASSes with "no prohibited effectiveness language outside the registry"
(`COMMAND_OUTPUTS.txt` CMD 5). The surface contradiction ("no machine-checked verification is
claimed" shipped alongside `MODEL CHECK: PASS`) is resolved.

**But the underlying blocker is not.** `BSSG_v0_1_DECISION_REGISTER.md` §6 still lists
**GP-R4 and GP-R8 as STILL BLOCKING** — "No transition-system model and no model-checked
invariants exist. Antitonicity is tested, not proved." F-GS-3 was a *labeling* defect over a real
*substantive* gap; pass-35 fixed the label. Under **SHUDP v0.5 Axiom 5 / no-default discipline**
(missing evidence defaults to nothing, never to satisfaction; the corpus's own practice is to mark
an unresolvable item **NOT EVALUABLE** / **UNKNOWN** rather than infer discharge), the honest
reading is "bounded-model-check PASS at K=4 over a 10-op alphabet," not "verified." A bounded
check at K=4 is a *falsification budget*, not a proof; nothing in the packet bounds the
diameter of the reachable state space, so K=4 exhaustiveness is a scale claim in the sense of
**SHV Method v1.1 D5's scale ladder** ("treating a claim proven at one scale as if it were proven
at another") and must be tagged as such.

---

## 3. The 12 open design decisions and PMD §0.4

`verify_bssg_v0_1.py` G10 = **WARN**: "12 open design decisions (OD-1 … OD-12); decision register
records STILL BLOCKING findings." From `OPEN_DECISIONS.md` (all UNRESOLVED at v0.1):

| ID | Open decision | Blocking marker |
|---|---|---|
| OD-1 | Canonical byte form for digest binding (JCS/RFC 8785 style vs COSE wrapped bytes); gate uses non-conformant `BSSG-CANON-1` | — |
| OD-2 | External monotonicity root for cross-session rollback | **STILL BLOCKING** (register §6.4, Claude C-4) |
| OD-3 | Numeric freshness bounds per evidence type (300 s / 5 s are placeholders with no evidentiary basis) | — |
| OD-4 | Hash/signature agility incl. post-quantum boundary | — |
| OD-5 | Append-only log vs current-corrected-value view | — |
| OD-6 | Strict narrowing vs non-increase + dependent-capability removal (my own unresolved objection) | — |
| OD-7 | Split vs co-located PE/PA/PEP roles | — |
| OD-8 | Max session duration and re-arming semantics | — |
| OD-9 | Evidence independence / non-bypassability optional at Minimal | — |
| OD-10 | Contract & policy as digests only vs normative schemas | — |
| OD-11 | Diagnostic richness vs regime-signal suppression (PR-6 clause (b) tension) | **STILL BLOCKING** (blocking-adjacent, register §6.3) |
| OD-12 | Witness quorum size and diversity rule | — |

**STILL BLOCKING count = 4 items** (`BSSG_v0_1_DECISION_REGISTER.md` line 7: "Four items remain
STILL BLOCKING and are listed in Section 3", enumerated in §6): (1) GP-R4 + GP-R8 — no
transition-system model, no model-checked invariants, antitonicity tested not proved; (2) CL-B4
residue — **no second independent implementation by a non-producer lineage agreeing on the frozen
vectors, so conformance-suite adequacy (falsifier AF-11) is untested**; (3) OD-11; (4) OD-2. The
register closes: "A freeze or deposit of BSSG while these remain open would misrepresent the
council's disposition."

**Does this preclude convergence under PMD §0.4?** §0.4 requires, conjunctively: two consecutive
cross-vendor rounds at 0 CRITICAL; **"HIGH residual is 0 or accompanied by a project-lead-signed
exception ledger entry"**; MEDIUM/LOW absorbed or explicitly non-operative; and all standing-rule
checks passing. Two of the four STILL BLOCKING items came from **HALT-class verdicts** (register
§6.1–§6.2), i.e. they are HIGH-or-above residuals by provenance. They are neither 0 nor carrying a
project-lead-signed exception ledger entry — the register instead states the opposite, that the
packet "remains DRAFT because of them."

**Therefore: yes, on the face of the shipped register, the HIGH-residual clause of PMD §0.4 is
not satisfied, and convergence is precluded independently of F-GS-1/2/3.** Note also that a
G10 **WARN** is a verifier-severity artifact, not a methodology disposition: `OPEN_DECISIONS.md`
states the verifier "does not FAIL on them; it FAILS only on package inconsistency." The verifier's
12 PASS / 2 WARN / 0 FAIL is thus fully compatible with a PMD §0.4 failure, and must not be read
as evidence against it. Under **SHUDP Axiom 5 / no-default**, an unresolved decision does not
default to benign.

CL-B4 deserves emphasis: "no second independent implementation by a non-producer lineage agreeing
on the frozen vectors" is *definitionally* a **SHV D6** failure — D6 requires that "each must
re-derive the load-bearing result from the primary source rather than accept the producer's… number."

---

## 4. Convergence re-ruling (ADVISORY — no vote weight)

**Advisory ruling: NO / QUALIFIED-NO. Vote UNCHANGED from pass-34.** The narrow question ("has
closure of F-GS-1/2/3 changed the answer?") is: **the defects are closed; the answer is not
changed.** Four independent grounds, each sufficient alone.

**(a) Post-hoc CE addition is not a round. — PMD v1.2 §0.4.** §0.4 requires "**two consecutive
cross-vendor rounds** produce 0 CRITICAL findings." Pass-35 is step 5 of the PMD §0.3 cycle
("**Absorb** — producer-instance generates next version absorbing audit findings"), followed by
step 6 (Ledger). It is *not* step 3 (Audit). CE175 is the producer encoding the auditor's finding
into its own regression corpus. That is exactly right as absorption and exactly insufficient as
certification: the repaired bytes have had **zero** cross-vendor audit rounds, so the count of
consecutive clean cross-vendor rounds on the pass-35 artifact is **0 of the required 2**. F-GS-1
was a CRITICAL surfaced at V34 — the most recent cross-vendor round on the artifact lineage
scored 1 CRITICAL, which resets the two-round window rather than extending V32–V34.

**(b) Producer-authored repair cannot self-certify. — SHV Method v1.1 D6 +
`bayyinah_cross-vendor-rotation.md`.** D6: "**Producer-quarantined, multi-chain convergence. No
party certifies its own work.** … The producing party **may advise, but its vote does not count
toward certification.** Treat a result as certified only when independent checkers agree
repeatedly, ideally across two consecutive clean rounds **with at least one checker rotated in
fresh**, so that agreement is not an artifact of a fixed panel." Pass-35 is Claude-authored
absorption of a Claude-excluded audit. The rotation doc's *Producer-instance exclusion* clause bars
Claude from HALT/CRITICAL/HIGH on this artifact — which symmetrically bars Claude from *clearing*
them. **Answer to the load-bearing methodological question: producer-authored repair is NOT
sufficient under D6; a fresh non-producer audit round on the pass-35 bytes must precede any
re-claim of convergence.**

The §0.1 **same-instance named exception** does not rescue it. Its binary test is: "did the
absorption cycle add ANY content beyond the remediation checklist? If yes: cross-instance audit is
blocking." Pass-35 **added** an entirely new model-check contract (`_reg_c2w`), expanded the
operation alphabet from 7 to 10 ops (2,800 → 11,110 schedules), rewrote the ALLOW-path ordering,
added a new `_issuance_failure` empty-Authority write at lines 897–899, changed the G12 selector
substrate, and edited spec §26 and the README. That is architectural latitude, not mechanical
execution. **§0.1 / PMD §0.5 clause 5 mechanical-traceability exception: DOES NOT APPLY.**
(Process note, retained from the prior council: the label "PMD M1.5" has no canonical referent;
the corpus text lives at `PMD_v1_2_BAF_v3_0.md` §0.5 and in the rotation doc's *Same-instance §0.1
named exception*. Citing a non-existent clause number is itself a traceability defect.)

**In-corpus precedent, directly on point.** `SHUDP_v0_5_flagship.txt` (Author and authority note):
"**This producer revision has not yet received a new independent council re-attestation; the v0.4
convergence does not extend to the v0.5 additions.**" The methodology corpus applies exactly this
rule to *itself*. BSSG pass-35 is the same shape: prior-round convergence does not extend to
producer-authored additions.

**(c) The carry is undischarged and nothing on that axis changed. — SHVVP v0.8 §0.3, §8.0, §10.**
§0.3 (frozen): "there has been **no independent human peer review**, and cross-model consistency
checking is a **consistency check rather than peer review**." Every pass-35 artifact — 345 tests,
175 CEs, model check, verifier — is a consistency check by that definition. The SHVVP audit
history further freezes the carry rule: "**Under the frozen carrying rule a HALT from either
carrying seat blocks deposit outright**" (v0.1–v0.6 all HALTED on that rule). §8.0 supplies the
governing methodological posture on repair-after-finding: the producer "**will not construct one
after seeing an audit finding, because a sampling model invented to rescue a claim is exactly the
postdiction**" the method forbids — the discipline that a fix authored in response to a finding
must be re-audited, not credited. `REPAIR_STATUS.md` lines 7–9 confirm the producer's own reading:
"carry gate remains open under SHVVP section 0.3 and section 10." **No change on the carry axis in
pass-35.** The platform-execution framing (DeepSeek/Qwen unavailability) is irrelevant to this:
§0.3's carry is a positive-evidence requirement, and under **SHUDP Axiom 5 / no-default**, absent
evidence yields no credit regardless of *why* it is absent. A failed carry attempt is not a
discharged carry.

**(d) HIGH residuals ≠ 0 and unexcepted. — PMD §0.4.** Per §3 above: 4 STILL BLOCKING items, two
from HALT verdicts, no project-lead-signed exception ledger entry, register text explicitly stating
freeze would misrepresent the council's disposition.

**Would I ever move to QUALIFIED-YES?** Only on the conjunction of: (i) ≥2 consecutive
cross-vendor rounds on pass-35-or-later bytes at 0 CRITICAL with ≥1 fresh-rotated non-producer
seat (D6); (ii) SHVVP §0.3 carry discharged by two families that actually execute the gate, or a
signed exception; (iii) the 4 STILL BLOCKING items closed or each carrying a project-lead-signed
exception ledger entry (PMD §0.4). None of the three obtains today. Note that (i)+(ii) are
*structurally unreachable* by any amount of further producer work — which is the correct and
intended consequence of D6.

**Correct current status statement:** the packet's own banner is accurate and should not be
upgraded. **DRAFT / NOT CARRIED. SELF-CONSISTENT DRAFT (not carried, not publication ready).**
"Self-consistent" is the honest ceiling of what pass-35 evidence supports.

---

## 5. New findings (advisory)

Severity labels are advisory-class only, per §0.

### 5.1 A-01-R (advisory-MEDIUM) — G12 current-section selector is data-conformant, not robust

The pass-35 fix repaired the *headings* (the data) rather than the *selector* (the control).
`verify_bssg_v0_1.py` G12 terminates the current section at the **next regex-matching heading in
file order**. Two shipped historical headings do not match the regex: `REPAIR_STATUS.md:74`
("`# BSSG v0.1 -- repair33 / V30 adjudication …`") and `:127`
("`# BSSG v0.1 -- pass-30 V29 WITHDRAWAL …`"). Consequence: any future section whose heading
deviates from the canonical form — the exact mistake pass-34 made — and which is placed between
the newest canonical heading and the next one, is **silently absorbed into the current claim
surface**, contributing its `{claim:ID}` tags, its `CE<N>` citations, and its
"claims N counterexamples" line to the check without ever being recognized as a section.
Recommendation: make G12 recognize `^# BSSG v0\.1 --` as a section boundary regardless of
suffix, and **FAIL** (not silently ignore) any such heading that does not carry a parseable
`(pass-N)`. This converts A-01's failure mode from silent to loud. *This is A-01 downgraded, not
A-01 re-filed: the currently shipped bytes are correct.*

### 5.2 A-05 (advisory-HIGH-class — REQUIRES NON-PRODUCER REPRODUCTION) — ceiling-record failure after successful mint leaves the session in free-establishment state

This is the requested stress-test of the F-GS-1 fix: **what if an exception raises inside
`ceiling_for_health` itself, after the token mint has already succeeded?**

`bssg_gate.py:1830–1836`:

```
if _cc_pending is not None and health == "HEALTHY":
    _cc_sess, _cc_body = _cc_pending
    try:
        self.state.contract_ceiling[_cc_sess] = ceiling_for_health(_cc_body, "HEALTHY")
    except Exception:
        reasons.append("E-CEILING-RECORD-FAILED")
```

Trace of the except branch. `_contract_ceiling_pending` was already cleared at line 1809, so
nothing is retried. `self.state.contract_ceiling[_cc_sess]` is **never assigned** — the key stays
absent. Execution then **falls through to the ALLOW receipt** and the token is live and
redeemable: the session obtains a HEALTHY authorization while its demonstrably-held-authority
record is missing. On a subsequent post-lift re-establishment, `_apply_narrowing`
(`bssg_gate.py:1935`) executes `_held = self.state.contract_ceiling.get(session)` → **`None`** →
the widening guard `if _held is not None and not (new_ceiling <= _held)` is **skipped**, and the
code takes the "FIRST-ever authorize … establishment is free as before" branch documented at lines
1932–1934. **The session re-establishes at an arbitrary, unbounded fresh ceiling.**

This is the *same class* as F-GS-1 — a state in which `contract_ceiling` fails to bound post-lift
re-establishment — reached through the ceiling-**record** failure rather than the token-**mint**
failure. Note the asymmetry that makes the point sharp: `_issuance_failure` at lines 897–899 was
*deliberately* hardened to write `Authority([], [])` "so the `_held` check fires"; the ALLOW path
at 1830–1836 has **no equivalent guarantee**, and its failure mode is strictly worse because the
ALLOW path also hands out a usable token. `None` (no entry) and `Authority([], [])` (empty entry)
are treated as opposite polarities by line 1936 — absent means unconstrained, empty means
maximally constrained — yet the exception handler produces the *unconstrained* one.

Additional concerns on the same lines:
- The only signal is `reasons.append("E-CEILING-RECORD-FAILED")` on an **ALLOW** record. This is
  advisory annotation where fail-closed discipline requires a terminal outcome. Nothing in the
  path denies, voids, or marks the session terminal.
- Emitting reason codes on an ALLOW receipt is itself anomalous relative to the DENY-carries-
  reasons convention visible throughout the gate, and should be checked against
  `schemas/authorization-receipt.schema.json` (closed schemas) — if `reason_codes` is
  non-empty-forbidden on ALLOW, this is also a schema-validity defect.
- CE175 asserts the *mint-fault* arm only (`mint_failed=True … cc_empty=True`). **No
  counterexample in the 175-item corpus covers the ceiling-record-failure arm**, and no
  `bssg_model_check.py` operation models it, so `BOUNDED-AUTH-INTRO` over 11,110 schedules cannot
  see it either. CE175 is a point fix; the surrounding invariant is unprobed.

**Reachability, stated honestly.** `ceiling_for_health` raising on a `contract_body` that has
already passed kernel evaluation is not demonstrated here, and I have not written a probe — a
producer-family seat should not be the one to establish a HIGH-class finding's reachability under
**SHV D6**. Under **SHUDP v0.5 Axiom 5 / no-default**, however, the reachability question does not
default to "unreachable": the code contains an explicit `except Exception` branch, which is a
producer assertion that the exception *is* considered possible. A defensive handler that, when it
fires, re-opens the exact bypass class the pass just closed is a defect on its face, regardless of
trigger frequency. **Recommended remedy (structural, not probe-dependent):** in the `except`
branch, write `self.state.contract_ceiling[_cc_sess] = Authority([], [])` — mirroring lines
897–899 — and/or route to `_issuance_failure(..., "E-CEILING-RECORD-FAILED")` so the ALLOW never
completes. Either makes the failure fail-closed. **A non-producer seat must reproduce and re-rate
this; this seat cannot assign HIGH.**

### 5.3 A-06 (advisory-HIGH-class — LEDGER INTEGRITY, REQUIRES NON-PRODUCER REPRODUCTION) — the historical pass-34 section appears retroactively edited

The **pass-34** section of `REPAIR_STATUS.md` contains two statements that cannot both have been
true when written:

- line 71: "**Battery state (repair34 resealed):** 345 tests OK — **173/173 CE GREEN** — MODEL
  CHECK PASS (… bounded-auth-intro(**2800 schedules**, K=4, **7-op alphabet**) …)"
- line 74: "**This document claims 175 counterexamples.**"

The pass-34 artifact had 173 counterexamples and a 7-op/2,800-schedule model check, by its own
adjacent sentence. The "175" figure is the **pass-35** corpus size. A historical, hash-sealed
ledger section therefore now asserts a number that was false at the time of that pass — the
signature of a **retroactive edit to a closed section**, most plausibly to satisfy a G12 numeric
check that scanned more than the current section.

Why this is load-bearing rather than cosmetic: `REPAIR_STATUS.md` is the **hash-verified substrate
of record** for the entire audit chain (`SHA256SUMS`: `REPAIR_STATUS.md: OK`), and the packet's own
discipline is append-only immutability — `PMD v1.2 §0.3` step 6 ("**Ledger** — append-only record
of the cycle; **immutability discipline enforced**"), echoed in the packet's own historical
sections ("Corrections on the record (append-only discipline)", `REPAIR_STATUS.md:664`; "recorded
per audit-chain immutability", `:1172`). If closed sections are mutable, then **every** historical
claim in this 1,179-line ledger — including the V32/V33 zero-BLOCKER records on which the entire
V32–V34 convergence argument rests — loses its evidentiary standing, because a reader cannot
distinguish a contemporaneous record from a later edit. That directly attacks **PMD §0.4**'s
"two consecutive cross-vendor rounds" premise: the evidence for those rounds is exactly this
ledger, and note that §2.2's "first and second consecutive" incoherence sits in the *same*
freshly-edited region. Note also that `SHA256SUMS` proves the file matches its manifest **now**;
it provides no evidence about what the file said at pass-34, so hash verification is not a defense
here.

Recommendation for the project lead: determine whether the pass-34 section was edited
post-seal; if so, restore the contemporaneous text and record the correction as a **new appended
entry** rather than an in-place edit; and add a verifier gate asserting that each historical
section's numeric corpus claim matches that pass's own stated battery state. Alternatively confirm
the benign reading — that the sentence is a fixed-format template line whose semantics are
"current corpus size," in which case the template is a trap and should be scoped per-section.
**A non-producer seat must adjudicate; a producer-family seat cannot rate a defect in the
producer's own ledger.**

### 5.4 A-07 (advisory-MEDIUM) — "MODEL CHECK: PASS" still overstates a bounded result

Register §6.1 keeps GP-R4/GP-R8 STILL BLOCKING ("Antitonicity is tested, not proved"; "no TLA+
model exists"), yet the shipped tool prints an unqualified `MODEL CHECK: PASS`. F-GS-3's repair
aligned spec §26 with the tool's existence but not the tool's *banner* with the tool's *scope*.
The honest string is "BOUNDED MODEL CHECK: NO COUNTEREXAMPLE at K≤4 over a 10-op alphabet" —
per **SHV Method v1.1 D5** (scale ladder: do not treat a claim proven at one scale as proven at
another) and **SHUDP Axiom 5** no-default. F-GS-2's own history is the argument: the 7-op/2,800
check printed PASS for many passes while being *vacuous* on target introduction. A PASS banner
whose scope is invisible is precisely how that went unnoticed.

### 5.5 A-08 (advisory-MEDIUM, process) — V33/V34 evidence is producer-narrated

See §2.2. The V32/V33/V34 records that carry the convergence argument exist in the substrate only
as producer prose inside a producer-authored section, not as deposited non-producer seat
artifacts. Under **SHV D6** ("Each must re-derive the load-bearing result from the primary source
rather than accept the producer's or another checker's number"), a council seat reading this packet
cannot re-derive the V32/V33 verdicts from a primary source — only from the producer's summary of
them. Compounded by A-06 if closed sections are mutable.

---

## 6. Dissenting angle — one substantive challenge to the pass-35 narrative

**The pass-35 narrative's implicit claim is that F-GS-1 was the 33rd and final instance of a
closing sequence. The ledger supports the opposite inference: the sequence is not converging, and
pass-35's own code contains the 34th instance-shaped hole.**

The gate's comments enumerate the recurrence explicitly. The V30 fix (`bssg_gate.py:1734–1748`)
restricted the `contract_ceiling` write to ALLOW decisions and closed the cross-contract vector.
The V31 K33-01 fix (`:1792–1798`) — labeled "**the 32nd instance**" — added `health == "HEALTHY"`
and closed the ALLOWed-degraded vector. The V34 F-GS-1 fix (`:1799–1807`) — "**the 33rd
instance**" — moved the write after mint and closed the mint-fault vector. Three consecutive
passes, three fixes, one line of code, three different *reasons why the write was wrong*. Each was
declared closed by a producer who had just declared the previous one closed.

Each fix narrowed a **precondition** on the write. None established the **invariant**. The
invariant is: *`contract_ceiling[session]` must, at every observable point, be a sound upper bound
on authority the session demonstrably and legitimately held; and its absence must never be
weaker than its emptiness.* Pass-35 does not state that invariant, does not test it as a
property, and does not model it in `bssg_model_check.py`. It adds one more precondition
(post-mint) plus one point-probe (CE175). A-05 (§5.2) is the immediate cost of that choice: the
very `except` handler protecting the newly-moved write, when it fires, restores `_held = None` and
hands the session the free-establishment branch — a 34th instance of the same shape, sitting
inside the 33rd instance's fix, shipped with `175/175 GREEN`.

Two further observations sharpen the dissent. First, **the shared blind spot was not diagnosed,
only patched.** V32, V33, and V34's first two seats all executed the shipped bytes across three
consecutive rounds and none saw the write-before-mint ordering; it took a specific probe from one
seat in an eight-seat council. Pass-35's response is to encode *that probe* (CE175). But a corpus
that grows one CE per discovered bypass is, by construction, always exactly one bypass behind —
and the V32/V33 "zero-BLOCKER" rounds are now known to have been zero-BLOCKER **on an artifact
containing a CRITICAL**, which is direct evidence that the panel's clean rounds do not measure
what PMD §0.4 needs them to measure. This is precisely why **SHV D6** demands "at least one
checker rotated in fresh, so that agreement is not an artifact of a fixed panel," and why V32–V34
cannot be extended by a producer repair.

Second, **the "platform limitations, not artifact defects" framing for the failed carry is now
falsified in the direction that matters.** That framing asks the council to treat the carry as
morally discharged because the obstacle was environmental. V34 then found a CRITICAL
authorization bypass in the artifact. The most defensible reading of the failed carry is therefore
not "the artifact was fine and the platform failed," but "**the artifact had not been audited
enough**" — the very hypothesis the carry exists to test. **SHVVP v0.8 §8.0** names this move: a
justification "constructed after seeing an audit finding" is postdiction and is refused. And
**SHUDP v0.5 Axiom 5**'s no-default rule is indifferent to the *reason* evidence is missing:
absent carry evidence yields no carry credit.

**Advisory bottom line.** F-GS-1, F-GS-2, and F-GS-3 are genuinely closed on shipped bytes, and
pass-35 is competent, honest repair work whose own banner ("DRAFT / NOT CARRIED", "SELF-CONSISTENT
DRAFT (not carried, not publication ready)") states its status correctly. But a producer cannot
convert its own repair into convergence: **SHV D6** ("No party certifies its own work"), the
rotation doc's producer-instance exclusion, **PMD §0.4**'s two-clean-cross-vendor-rounds and
zero-or-excepted-HIGH-residual clauses, **SHVVP §0.3**'s undischarged carry, and the corpus's own
self-applied precedent in **SHUDP v0.5** ("the v0.4 convergence does not extend to the v0.5
additions") all point one way. **A fresh non-producer audit round on pass-35 bytes is mandatory
before convergence may be re-claimed. Vote unchanged: QUALIFIED-NO (advisory, no weight).**

---

## 7. Citation index for load-bearing claims

| Claim | Source |
|---|---|
| Producer family = advisory only; no HALT, no CRITICAL/HIGH | `methodology/bayyinah_cross-vendor-rotation.md` § Producer-instance exclusion |
| Producer may advise but its vote does not certify; ≥2 clean rounds with ≥1 fresh-rotated checker | `methodology/SHV_Method_v1_1.txt` D6 (line 182 ff.) |
| Convergence = 2 consecutive cross-vendor rounds @ 0 CRITICAL; HIGH residual 0 or signed exception; standing-rule checks incl. substrate uniqueness | `methodology/PMD_v1_2_BAF_v3_0.md` §0.4 |
| Six-step cycle: Author / Audit / Adjudicate / **Absorb** / **Ledger (append-only, immutability enforced)** | `methodology/PMD_v1_2_BAF_v3_0.md` §0.3 |
| Mechanical-traceability exception; binary "any content beyond checklist → cross-instance audit blocking" (cited in prior council as "M1.5"; canonical text is §0.5 / rotation doc §0.1) | `methodology/PMD_v1_2_BAF_v3_0.md` §0.5; `bayyinah_cross-vendor-rotation.md` § Same-instance §0.1 named exception |
| No independent human peer review; cross-model consistency ≠ peer review; HALT from either carrying seat blocks deposit outright | `methodology/SHVVP_v0_8_flagship.txt` §0.3 (line 173 ff.), audit history (lines 33–49) |
| A justification constructed after seeing an audit finding is postdiction and is refused | `methodology/SHVVP_v0_8_flagship.txt` §8.0 (line 2540 ff.) |
| No-default rule: missing/unresolvable evidence → NOT EVALUABLE / UNKNOWN, never satisfaction | `methodology/SHUDP_v0_5_flagship.txt` Axiom 5 layer (lines 12–22, 78–85) |
| Producer revision does not inherit prior convergence absent fresh independent re-attestation | `methodology/SHUDP_v0_5_flagship.txt` § Author and authority (lines 25–26) |
| Scale ladder: a claim proven at one scale is not proven at another | `methodology/SHV_Method_v1_1.txt` D5 (lines 175–181) |
| 4 STILL BLOCKING items; freeze would misrepresent council disposition; CL-B4 = no non-producer second implementation | `packet/BSSG_v0_1_DECISION_REGISTER.md` line 7 and §6 |
| 12 unresolved OD-1…OD-12; verifier WARNs and does not FAIL on them | `packet/OPEN_DECISIONS.md` (header; OD-2, OD-11 blocking markers) |
| F-GS-1 fix ordering: mint → validate → collision → ceiling write; `_issuance_failure` writes empty Authority | `packet/bssg_gate.py:897–899, 1808–1836`; `_held` check at `:1935` |
| G12 current-section selector and clauses (1)–(6) | `packet/verify_bssg_v0_1.py:601–611, ~1195–1247` |
| pass-35 battery: 20/20 hashes, 345 tests, 175/175 GREEN, MODEL CHECK PASS (11,110 schedules), 12 PASS / 2 WARN / 0 FAIL, SELF-CONSISTENT DRAFT | `bssg_review_v2/COMMAND_OUTPUTS.txt` CMD 1–5 + EXTRA |
| Post-fix probe: `contract_ceiling.effects = []`; post-lift DELETE `DENY_FALSE`, `commit: null` | `bssg_review_v2/F_GS_1_REPROBE_OUTPUT.txt` |
| Pass-35 changelog incl. "G12 heading selector … restored to canonical (pass-N) format"; V32/V33/V34 records; pass-34 "173/173" vs "claims 175" | `packet/REPAIR_STATUS.md:1–47 (esp. 3–18, 26, 31), 48–73 (esp. 71, 74)` |
| F-GS-2 `_reg_c2w` broader allowed vs narrower degraded target scopes; 10-op alphabet | `packet/bssg_model_check.py:317–322` per `COUNCIL_INSTRUCTIONS.md`; `COMMAND_OUTPUTS.txt` CMD 4 |

**Seat status restated for the record: PRODUCER FAMILY (Anthropic / Claude Opus 5) — ADVISORY
ONLY. No vote weight. Advisory-CRITICAL/HIGH-class findings A-05 and A-06 require non-producer
reproduction and re-rating before they carry any severity.**

---

# Bismillah ir-Rahman ir-Rahim
