# Bismillah ir-Rahman ir-Rahim

# R0310 -- Model Council Report: Claude Fable 5 (ADVISORY seat), BSSG v0.1 pass-35, Round 2

**Chronological Index:** 716 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** model-council-claude_fable_5-r2.md  
**Source Format:** md  
**SHA-256:** `4076c3e004a10f209751717fb2c5e1601cda46ef783d2d3fcabc04552f5ee810`  

---

## R0310 · Model Council Report: Claude Fable 5 (ADVISORY seat), BSSG v0.1 pass-35, Round 2

- section: V. BSSG & SHVVP Protocols
- source_file: model-council-claude_fable_5-r2.md
- source_format: md
- text_sha256: 4076c3e004a10f209751717fb2c5e1601cda46ef783d2d3fcabc04552f5ee810

# Model Council Report: Claude Fable 5 (ADVISORY seat), BSSG v0.1 pass-35, Round 2

## 0. Identity and producer-family disclaimer

- Model name (model-catalog friendly-name column): **Claude Fable 5** (Anthropic).
- Seat: **ADVISORY ONLY**, PRODUCER family, no vote weight (per COUNCIL_INSTRUCTIONS.md role
  table and `bayyinah_cross-vendor-rotation.md`). Per the round brief, no CRITICAL or HIGH
  may be recorded as my finding for panel-ledger purposes. Any escalation-grade issue I find
  is written as **ADVISORY-HIGH / ADVISORY-CRITICAL** and flagged for a non-producer
  (Gemini 3.1 Pro or GPT 5.6 Sol) to independently reproduce and record.
- I adjudicated on the round-2 bytes, not on Round 1 (Grok 4) or the v2 council rulings
  (PMD v1.2 §0.4 independent-re-derivation requirement).
- No effectiveness claims are made. The package is DRAFT / NOT CARRIED. No em or en dashes
  are used, per `bayyinah_em-dash-policy.md`.

**Format note (itself a minor observation):** the task brief calls for an "eight-element
Bayyinah format," but `methodology/bayyinah_findings-format.md` defines a **six-element**
format (ID, Severity, Locus, Substance, Disposition, Cross-reference). I use the six-element
format the methodology doc actually specifies. The brief-vs-doc mismatch is noted for the
orchestrator; per `bayyinah_findings-format.md` a spec that undercounts its own required
elements would itself be a finding.

---

## 1. Command outputs (executed verbatim, trimmed to tails)

All five mandated commands plus `bssg_gate.py` were executed by me in
`/home/user/workspace/bssg_round2/packet`. Results match the orchestrator's sealed ground
truth (COUNCIL_INSTRUCTIONS.md "Ground truth" block) exactly.

**`sha256sum -c SHA256SUMS`** -> all 20 files `OK` (20/20). Tail confirmed:
`test_bssg_gate.py: OK`, `verify_bssg_v0_1.py: OK`, all six `schemas/*.json: OK`.

**`python3 test_bssg_gate.py`**:
```
Ran 345 tests in 0.142s
OK (skipped=8)
```

**`python3 bssg_counterexamples.py`**:
```
GREEN CE175 [F-GS-1] F-GS-1 mint-fault ceiling-poison CLOSED: a FAILED_NO_EFFECT first-establish
  writes empty contract_ceiling; post-lift DELETE is DENIED; session never successfully held DELETE
  mint_failed=True no_delete=True cc_empty=True delete_denied=True
175/175 GREEN  (0 RED = open defects)
```

**`python3 bssg_model_check.py`**:
```
PASS REFINE every kernel-evaluated record satisfies decision == kernel_decision(conjuncts) ... records=7 inconsistent=0
PASS BOUNDED-AUTH-INTRO: over all schedules (len<=4, 10-op alphabet) no ALLOW authorizes an effect
  or target outside the established healthy ceiling ... schedules=11110 allows=7200
MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(11110 schedules)
  + operational refinement on the executable
```

**`python3 verify_bssg_v0_1.py`**:
```
G1 PASS ... G2 WARN jsonschema not installed; structural check only ; G2 PASS six schemas valid ...
G3 PASS 345 tests ; G9 PASS SHA256SUMS verified for 20 files
G10 WARN 12 open design decisions (OD-1..OD-12); decision register records STILL BLOCKING findings
G13 PASS counterexample corpus EXECUTED: 175/175 GREEN, 0 RED
SUMMARY: 14 gates, 12 PASS, 2 WARN, 0 FAIL
PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)
```

**`python3 bssg_gate.py`** (banner):
```
BSSG reference gate 0.1.0-draft, spec version 0.1
DRAFT / NOT CARRIED. No effectiveness claim is made by this software.
```

Structural invariants confirmed on my process: 243 kernel truth states, 729 antitone
contracts, 11110 schedules, 7200 allows, 175 counterexamples (CE175 = F-GS-1 closure).
The two WARNs are non-blocking-to-execution by design (G2 = jsonschema absent; G10 = 12 open
design decisions that the decision register itself flags STILL BLOCKING). Reason-from-bytes
per COUNCIL_INSTRUCTIONS.md anti-patterns: I re-derived, I did not trust the sealed values.

---

## 2. Deep code analysis

### 2a. `_issuance_failure` empty-Authority write (bssg_gate.py L879-916)

The V34 F-GS-1 fix is at L900-902:
```python
if session is not None and session not in self.state.contract_ceiling:
    self.state.contract_ceiling[session] = Authority([], [])
```

**Symmetry across the three failure modes.** All three post-kernel issuance faults route
through the SAME `_issuance_failure(...)` entry point (L1817-1825):
- `E-TOKEN-MINT-FAULT` (L1819, `new_token()` raised),
- `E-TOKEN-MINT-INVALID` (L1822, token fails the 8..128-length / prohibited-field check),
- `E-TOKEN-FACTORY-COLLISION` (L1825, `token_id in self.state.tokens`).

Because the empty-Authority write lives in the common `_issuance_failure` body (L900-902),
not at any one of the three call sites, the fail-closed write is **symmetric**: the empty
ceiling is written identically regardless of which of the three faults fired. This is
correct and is what CE175 exercises for `E-TOKEN-MINT-FAULT` (verified GREEN in section 1).

**Guard polarity is correct.** The write is conditional on
`session not in self.state.contract_ceiling`, i.e. it only fills the FIRST-establish gap. A
session that already legitimately demonstrated authority keeps its real (narrower) ceiling
and is not clobbered by an empty one on a later mint fault. The post-establish over-broaden
case is independently closed by `E-AUTHORITY-WIDENING` in `_apply_narrowing` (L1943-1953),
as the CE175 comment states. I confirmed the `_held` check at L1949-1952 reads
`contract_ceiling.get(session)` and terminalizes on `not (new_ceiling <= _held)`.

**Does any post-kernel failure path skip the empty write?** I traced every `return` between
the kernel decision (L1765) and the ALLOW receipt (L1922). The only post-kernel exits are
the three `_issuance_failure` calls (all covered) and the outer `except BaseException`
handler in `authorize()` (L1432-1513). The BaseException handler routes to
`_authorize_abort`, which does NOT write the empty Authority. This is the seam that section
3 and finding F-CF-1 examine: a post-mint mutation that raises escapes to the BaseException
abort, which by explicit design (L1436-1440 comment) does NOT rewind authority/ceiling state.

### 2b. Post-mint ceiling-write branch (Opus 5's A-05, L1830-1863)

The branch (L1830-1835):
```python
if _cc_pending is not None and health == "HEALTHY":
    _cc_sess, _cc_body = _cc_pending
    try:
        self.state.contract_ceiling[_cc_sess] = ceiling_for_health(_cc_body, "HEALTHY")
    except Exception:
        reasons.append("E-CEILING-RECORD-FAILED")
```

**The reason_codes DROP is confirmed on the bytes.** The ALLOW receipt template at L1863
hardcodes `"reason_codes": []`, and the ALLOW decision record at L1920 hardcodes
`"reason_codes": []` as well. `reasons` is a live local list that the ALLOW path DID append
to (L1835 on ceiling-record failure; also L1750 on the pending-capture failure). Neither
the receipt nor the record ever reads `reasons` on the ALLOW path. Therefore
**`E-CEILING-RECORD-FAILED` can never surface on an ALLOW receipt or ALLOW record.** This is
a genuine surface-substrate divergence: the code computes a reason code and then discards
it. Verified empirically in section 3 (`r1_receipt_reason_codes: []` and
`r1_record_reason_codes: []` while the ceiling write was forced to fail).

**Ordering of post-mint mutations.** After the successful mint at L1817, the ALLOW path
performs, in order:
1. L1833 `contract_ceiling[sess] = ceiling_for_health(...)` (the A-05 site),
2. L1837 `request_digest = digest(request)`,
3. L1838-1839 `expires_at = min(parse_rfc3339_utc(...), parse_rfc3339_utc(...))`,
4. L1840-1912 receipt dict construction (includes `digest(witness_receipt)`, `digest_bytes`,
   `ceiling.as_json()`),
5. L1914-1921 decision record construction,
6. L1922 `self.state.records.append(...)`,
7. L1923+ `self.state.tokens[token_id] = {...}` (includes `digest(receipt)`).

Everything in steps 1 through 6 executes AFTER the token counter has advanced (L1817) but
BEFORE the token is registered in `state.tokens` (step 7). Only steps 3 (`parse_rfc3339_utc`),
2 and 4 and 7 (`digest`) and the dict/`as_json` construction can plausibly raise; if any of
them does, control leaves through the outer `except BaseException` (L1432), which explicitly
does NOT rewind the L1833 ceiling broadening. This is the seam finding F-CF-1 documents.

---

## 3. Independent A-05 reproduction (ADVISORY)

I wrote my own probe (`/home/user/workspace/bssg_round2/fable5_a05_probe.py`), deliberately
using a DIFFERENT mechanism than the orchestrator's `a05_probe.py`. The orchestrator counts
HEALTHY `ceiling_for_health()` invocations and raises on the second. I instead replaced
`state.contract_ceiling` with a `dict` subclass whose `__setitem__` raises exactly once for
the target session, so the L1833 assignment itself throws inside its own try/except. The
token mint (L1817) succeeds, so only the ceiling RECORD fails. This isolates the A-05 arm
more precisely (it forces the assignment, not a downstream recompute).

**Probe output (verbatim):**
```
r1_decision: ALLOW
r1_issuance_status: (none)
r1_receipt_present: True
r1_receipt_reason_codes: []
r1_record_reason_codes: []
r1_token: token-00000001
contract_ceiling_present_sess: False
contract_ceiling_value: ABSENT
token_live: True
r3_delete_prelift_decision: DENY_FALSE
lift_status: submitted
r4_delete_postlift_decision: ALLOW
r4_token: token-00000003
ADJUDICATION: A-05 REPRODUCED
```

**Adjudication: A-05 REPRODUCED (mechanically), via an independent mechanism.** All four
mechanical claims hold on the round-2 bytes: (1) ALLOW issued with a live token despite the
ceiling-write fault; (2) `E-CEILING-RECORD-FAILED` silently dropped, receipt
`reason_codes: []`; (3) `contract_ceiling['sess-0001']` left ABSENT (not empty); (4) a
post-lift HEALTHY DELETE re-establishes to ALLOW. This matches the orchestrator's summary.

**Severity nuance I am obligated to raise (ADVISORY, for a non-producer to weigh).** The
"a DELETE the session never held" framing deserves scrutiny before a non-producer records
this as CRITICAL. The A-05 contract has `allowed_effects = [READ, WRITE, DELETE]` and its
HEALTHY ceiling therefore INCLUDES DELETE. On the NON-faulted path, a HEALTHY READ ALLOW
writes `contract_ceiling = ceiling_for_health(body, "HEALTHY") = {DELETE, READ, WRITE}` (the
V31 K33-01 design: a HEALTHY ALLOW records the full HEALTHY ceiling of that contract, not
just the requested effect). On that non-faulted path the post-lift DELETE would ALSO
re-establish to ALLOW, because `_held = {DELETE,READ,WRITE}` and `DELETE <= _held`. So the
end-state authority in the faulted (A-05) run and the clean run is IDENTICAL for this
contract. The A-05 fault therefore does not, for this contract shape, grant authority the
session would otherwise be denied; it reaches the same landing state by a different (absent
vs full) intermediate ceiling.

Where A-05 does bite, and where it is genuinely a defect regardless of the above, is the
**silent drop of `E-CEILING-RECORD-FAILED` from the audit surface** (section 2b) and the
**divergence between the two fail-closed polarities**: `_issuance_failure` writes an EMPTY
Authority (fail-closed to nothing, L900-902) whereas the L1833 arm leaves the ceiling ABSENT
(fail-open to free re-establishment via `_apply_narrowing._held is None`, L1946-1952). Two
sibling post-kernel failure arms use OPPOSITE fail-closed conventions. That asymmetry is the
real substrate finding, and it is a construct a non-producer should record. See F-CF-1.

---

## 4. ADVISORY findings (six-element `bayyinah_findings-format.md` format)

**F-CF-1** ADVISORY-HIGH -- post-mint ceiling-write failure is fail-OPEN (absent ceiling),
inconsistent with `_issuance_failure`'s fail-CLOSED (empty ceiling), and drops its own reason
code.

- **Locus:** `bssg_gate.py:1830-1835` (post-mint ceiling write + swallowed
  `E-CEILING-RECORD-FAILED`), `bssg_gate.py:1863` and `:1920` (receipt/record hardcode
  `reason_codes: []`), against `bssg_gate.py:900-902` (`_issuance_failure` empty-Authority
  write) and `bssg_gate.py:1946-1952` (`_apply_narrowing` `_held is None` free-establish).
- **Substance:** the code claims (L1793-1815 comments) that contract_ceiling records only
  demonstrably-held authority and that the F-GS-1 class is closed by the empty-Authority
  fail-closed default, but when `ceiling_for_health` raises at L1833 the session's ceiling is
  left ABSENT rather than EMPTY. Absent drives `_apply_narrowing` down the `_held is None`
  free-establishment branch (L1946), i.e. fail-OPEN, the opposite polarity from the sibling
  `_issuance_failure` arm which writes an EMPTY Authority to force fail-CLOSED. The appended
  `E-CEILING-RECORD-FAILED` is then discarded because the ALLOW receipt (L1863) and record
  (L1920) hardcode `reason_codes: []`, so the fault is invisible on every audit surface.
  Reproduced by my independent probe (section 3): ALLOW issued, token live, ceiling ABSENT,
  reason_codes empty.
- **Disposition:** in the L1834 `except`, write `self.state.contract_ceiling[_cc_sess] =
  Authority([], [])` (mirror `_issuance_failure` L900-902) so the failure is fail-closed to
  the empty ceiling, AND surface the reason by replacing the two hardcoded `reason_codes: []`
  at L1863 and L1920 with `sorted(set(reasons))` so `E-CEILING-RECORD-FAILED` reaches the
  audit plane. A non-producer (GPT 5.6 Sol or Gemini 3.1 Pro) should reproduce and, if
  confirmed, record at the severity the rubric dictates. Because I am producer-family, I
  cannot record this as CRITICAL/HIGH for the ledger; per `bayyinah_severity-rubric.md`
  CRITICAL-vs-HIGH calibration it turns on whether a security invariant is BROKEN (CRITICAL)
  versus a defense-in-depth / observability gap that does not, for the tested contract shape,
  actually broaden landing-state authority (HIGH). My read is HIGH on the audit-surface drop
  and polarity asymmetry; the CRITICAL claim is contract-shape-dependent (section 3 nuance)
  and needs a non-producer to construct a contract where absent-vs-full genuinely diverges.
- **Cross-reference:** Opus 5 A-05 (v2 council); F-GS-1 / CE175 (the empty-write fix this
  finding says is applied asymmetrically); PMD v1.2 §0.4 (a CRITICAL here would fail the
  two-consecutive-clean-rounds premise); `bayyinah_severity-rubric.md` CRITICAL-vs-HIGH.

**F-CF-2** ADVISORY-MEDIUM -- post-mint mutations after the L1833 ceiling write can raise into
the BaseException abort, leaving the ceiling broadened with no registered token.

- **Locus:** `bssg_gate.py:1837` (`digest(request)`), `:1838-1839` (`parse_rfc3339_utc`),
  `:1840-1912` (receipt construction, `as_json`, `digest_bytes`), `:1923+`
  (`state.tokens[token_id] = ...`), against the outer handler `bssg_gate.py:1432-1440`
  (`except BaseException`, explicit "do NOT rewind authority/epoch state").
- **Substance:** the ALLOW path broadens `contract_ceiling` at L1833 BEFORE steps 2-7
  (section 2b). If any later step raises (a hostile `state.tokens` on the L1923 assignment,
  or any dependency fault), control leaves via the outer BaseException handler, which by
  design does not rewind the L1833 broadening. The result is a broadened ceiling with either
  no live token (raise before L1923) or, if L1923 itself raises after L1922, an ALLOW record
  already appended to `state.records` referencing a `token_id` absent from `state.tokens`.
  The latter fails safe on redemption (the committer checks `state.tokens`, so an absent
  token cannot commit), so this is defense-in-depth, not a live bypass on the tested paths.
- **Disposition:** move the L1833 ceiling write to be the LAST post-mint mutation, after
  `state.tokens[token_id]` is successfully assigned, so ceiling broadening is atomic with a
  redeemable token (mirrors the L1811-1815 "write AFTER successful token creation" intent,
  extended to "after token REGISTRATION"). Alternatively, register the token first and write
  the ceiling last within a single try that fails closed. A non-producer should confirm the
  ordering claim.
- **Cross-reference:** F-CF-1 (same L1833 broadening, failure arm); F-GS-1 / CE175 (the
  "write AFTER mint" principle whose scope this finding extends); CE174 (AUDIT-V33-01,
  BaseException totality on the commit path, the analogous invariant on the commit side).

**F-CF-3 (probe-limitation disclosure, not a defect claim).** My section-2b edge hypothesis
that `digest(request)` raising at L1837 would demonstrate F-CF-2 empirically is reported as
**CANNOT-REPRODUCE via my probe**: `fable5_edge_probe.py` never triggered the raise
(`digest_req_shape_calls: 0`, `raise_fired: 0`), because my shape-based match on the
`_safe_copy`'d request object did not fire at the L1837 call site within the time budget. The
run therefore only shows normal HEALTHY behavior (ceiling `{DELETE,READ,WRITE}`, post-lift
DELETE ALLOW), which is by-design K33-01 semantics, NOT a new leak. F-CF-2 accordingly rests
on code review (ordering trace, section 2b), not on a passing probe. I disclose this rather
than present the normal-path run as if it demonstrated the edge case (per
`bayyinah_methodology-foundations.md` substrate-honesty and the task's "do NOT simulate
outputs" instruction).

**F-DOC-1** ADVISORY-LOW -- task brief cites an "eight-element" findings format that the
methodology doc defines as six-element.

- **Locus:** task brief ("eight-element Bayyinah format") vs
  `methodology/bayyinah_findings-format.md` heading "# Six-Element Findings Format".
- **Substance:** the brief's element count diverges from the authoritative doc; an auditor
  following the brief literally would look for two elements that do not exist.
- **Disposition:** correct the brief to "six-element," or, if an eight-element format is
  intended for this round, add the two new elements to `bayyinah_findings-format.md` first
  (immutability: format changes precede their citation).
- **Cross-reference:** `bayyinah_findings-format.md` "Findings-format compliance check";
  PMD v1.2 §0.4 independent-re-derivation (reason from the doc bytes, not the brief's claim
  about them).

---

## 5. A-06 adjudication (retroactive-edit signature in pass-34 REPAIR_STATUS.md)

Not in scope of my assigned deep-dive (Bilal asked me specifically for the `_issuance_failure`
empty-Authority write and the post-mint ceiling branch), and I reserved my tool budget for
the code-level A-05 work. I did not open a dedicated read of the pass-34 REPAIR_STATUS.md
subsection, so I record **A-06: NOT ADJUDICATED by this seat** and defer it to Gemini 3.1 Pro
(long-context meta-audit) and GPT 5.6 Sol, whose seats are scoped to that class. I note only
that CE175's GREEN self-report ("175/175") is consistent with a 10-op / 175-CE current state,
so any "173/173 ... 7-op" string in a pass-34 section would be a stale-or-edited HISTORICAL
subsection, which is the exact A-06 signature to check; I make no ruling on it.

---

## 6. Verdict

**ADVISORY-ISSUES-FOUND.**

- The five mandated commands reproduce the sealed ground truth exactly on my process
  (20/20 SHA, 345 tests OK, 175/175 GREEN, model check PASS, 14 gates 12 PASS 2 WARN 0 FAIL).
- **A-05 is REPRODUCED** (mechanically) via an independent mechanism: ALLOW issued, token
  live, `contract_ceiling` ABSENT, `E-CEILING-RECORD-FAILED` silently dropped. I flag it as
  **ADVISORY-HIGH (F-CF-1)** for a non-producer to reproduce and record; whether it rises to
  CRITICAL is contract-shape-dependent (section 3 nuance) and I explicitly do not assert
  CRITICAL from a producer seat.
- One additional ADVISORY-MEDIUM code seam (F-CF-2: post-L1833 mutations raising into the
  no-rewind BaseException abort), one probe-limitation disclosure (F-CF-3), and one
  ADVISORY-LOW doc mismatch (F-DOC-1).

Because I am PRODUCER family with no vote weight, my verdict does not count toward the
PMD v1.2 §0.4 two-consecutive-clean-rounds tally. My substantive recommendation to the
non-producer seats: **A-05 (F-CF-1) must be independently reproduced and, if a contract can
be constructed where the absent-vs-empty polarity genuinely broadens landing-state authority,
recorded as CRITICAL, which would break the clean-round premise (PMD v1.2 §0.4).** Until then
the audit-surface reason-code drop and the fail-open/fail-closed polarity asymmetry stand on
the bytes as at least HIGH-grade defects. Package remains DRAFT / NOT CARRIED; no
effectiveness claim is made.

---

### Methodology citations used
- PMD v1.2 §0.4 (two consecutive cross-vendor clean rounds; independent bytes re-derivation).
- `bayyinah_findings-format.md` (six-element format; compliance check).
- `bayyinah_severity-rubric.md` (CRITICAL-vs-HIGH calibration; producer-family recording
  constraint interpreted with the rubric's harm-invariant boundary).
- `bayyinah_cross-vendor-rotation.md` (producer-family advisory-only seat).
- `bayyinah_em-dash-policy.md` (no em/en dashes).
- `bayyinah_methodology-foundations.md` (substrate honesty; reason-from-bytes).

### Artifacts
- `/home/user/workspace/bssg_round2/fable5_a05_probe.py` (my independent A-05 probe).
- `/home/user/workspace/bssg_round2/fable5_edge_probe.py` (F-CF-2 edge probe; disclosed
  inconclusive, F-CF-3).

---

# Bismillah ir-Rahman ir-Rahim
