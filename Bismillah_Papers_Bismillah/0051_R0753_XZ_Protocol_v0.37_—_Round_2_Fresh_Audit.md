# Bismillah ir-Rahman ir-Rahim

# R0753 -- XZ Protocol v0.37 — Round 2 Fresh Audit

**Chronological Index:** 51 of 995  
**Date:** 2024  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R2_F3_KIMI_COBWEB.md.txt  
**Source Format:** txt  
**SHA-256:** `655e2cf0488a14a34bb81aa863ed5a2cf96bfb5dfc54c0c008a4d08c0bd0bde0`  

---

## R0753 · XZ Protocol v0.37 — Round 2 Fresh Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R2_F3_KIMI_COBWEB.md.txt
- source_format: txt
- text_sha256: 655e2cf0488a14a34bb81aa863ed5a2cf96bfb5dfc54c0c008a4d08c0bd0bde0

# XZ Protocol v0.37 — Round 2 Fresh Audit

```
SEAT: Kimi K3 (carrying, binding), Round 2 Fresh, Cobweb/Composition
ROUND: 2 of 4 (fresh instance)
QUANTUM STATE: n=3, l=2, ml=+1 (Cobweb), ms=-1/2 (Family B), t=-1/2 (fresh)
PAIRED WITH: GLM-5.2 continuous Cobweb (same framework, different family, continuous)
VERDICT: CONDITIONAL PASS
```

Bismillah ar-Rahman ar-Rahim.

**Execution record (byte-level verification first, per dispatch anti-patterns):** `.txt` suffixes stripped (22 files); `sha256sum -c PACKET_SHA256SUMS` → 16/16 OK; `python3 build.py` → BUILD PASSED, all checks GREEN (after installing pytest, an environment gap, not a packet defect); direct seat execution of the canonical invocation → **186 passed in 11.50s**; default pytest discovery collects only 117, confirming the §0.1 claim that the explicit invocation is load-bearing. Manifest digest recomputed equals trust-roots digest `f09873e4…`. HISTORY seals verify all 37 entries; PRIOR_HISTORY derivation matches (`d073d096…`). Provenance gate [9c]: COMPUTED 0 / EXTERNAL 1 / ASSERTED 11 = 91.7% (inside the 87–93% bound). Build gate [5]: AST count 186 == collected 186.

Six-element format used below: **(1) ID·Severity (2) §22.3 Class (3) Evidentiary Tier (4) Finding (5) Evidence (6) Disproof.**

## FINDINGS

**F-K3R2-01 — §2.2 claim-boundary cardinal mismatch ("Three consequences" introduces four)**
1. **Severity:** MEDIUM — condition of this CONDITIONAL PASS.
2. **Class:** B-adjacent at discovery (undisclosed error), carried as a condition rather than HALT per the calibrated reading in Verdict Basis below; becomes Class C once disclosed.
3. **Tier:** 1 (byte-verifiable).
4. **Finding:** §2.2 line 91 reads "Three consequences are drawn now, before data:" and introduces a four-item enumeration (items 1–4, lines 93–96). Item 4 — *No composition inference*, the exact locus of this audit's composition-gap task — was added at v0.31 (v0.31 entry: "Section 2.2 consequence 4 added — composition-gap limitation inherited from deposited BSSG v0.1 §7.1"); the intro cardinal was never propagated. The defect is therefore a propagation residue spanning six versions (v0.31–v0.37), surviving the 11-seat v0.36 advisory round and the v0.37 amendment, undisclosed in all 37 entries.
5. **Evidence:** lines 91–96 (intro vs. four items); v0.31 entry (addition narrated, cardinal update absent); no entry v0.31–v0.37 dispositions it (grep: zero "consequence" dispositions in the record). Gate [9e] "Cardinal-range consistency" covers only the pattern `N consecutive … (v0.A through v0.B)` inside the current entry; it emitted zero checks on v0.37 bytes and cannot see body-prose cardinals.
6. **Disproof:** show that "Three" is intentional — e.g., a sentence marking item 4 as inherited-not-drawn. No such sentence exists; the enumeration presents four co-equal numbered consequences under a "Three" cardinal.

**F-K3R2-02 — v0.36 sealed ring-closure cites the consequence list at a wrong locus ("Section 0.2")**
1. **Severity:** MEDIUM — condition of this CONDITIONAL PASS.
2. **Class:** as F-01.
3. **Tier:** 1 (byte-verifiable).
4. **Finding:** the v0.36 ring-closure paragraph verifies "Section 0.2 consequence 1 … consequence 4" against shipped bytes. The consequence list resides in §2.2; §0.2 ("What this document is and is not," lines 24–30) contains no numbered consequences. The verification claims are real and their targets exist, but all four citations carry a wrong section locus — inside a paragraph that asserts "Verified on shipped bytes [ASSERTED]." v0.36 is HISTORY-sealed, so the locus error is immutable; v0.37's disposition of that paragraph (item 3, F-OP36G-01/F-OP36H-02, HIGH NOTED) repaired the FB-7b contradiction but not the locus error.
5. **Evidence:** line 1116 (four "Section 0.2 consequence N" citations); §0.2 lines 24–30 (zero numbered items); v0.37 entry item (3) (paragraph dispositioned without the locus error). Adjacent to disclosed boundary NC-5 ("no closure-reference validation in [9f]") but a distinct locus: no gate validates body-prose section cross-references.
6. **Disproof:** exhibit a numbered consequence list in §0.2. None exists.

**F-K3R2-03 — Slingshot context diverges from the canonical standing-boundary list (same count 19, membership 15/19)**
1. **Severity:** LOW.
2. **Class:** E (process observation; the slingshot is context, not canonical bytes).
3. **Tier:** 1 (diff-verifiable).
4. **Finding:** SLINGSHOT_PACKAGE.md's 19 boundaries match the v0.37 canonical list in count but differ in membership. Slingshot-only: EXTERNAL count = 1 (seat reports unbound); register scoping anchored to unregistered prose literal; [9f] NC-prefixed duplicate-severity gap; §22 item 7 operative clause ungated as a standalone item (canonical folds it into item 16's parenthetical at v0.37). Canonical-only: fresh-execution non-reproducibility; [9c] DOI-resolution blindspot; [9c] quoted-tag inflation in immutable correction (u). Two-sided significance: fresh seats calibrate on non-canonical context, and one slingshot-only item is *true of the shipped gate code yet absent from the canonical list* — [9f] does scope its register parse on the unregistered prose literal "defect register disposition" (build.py line 409), a genuine boundary the canonical record has not disclosed.
5. **Evidence:** slingshot §"Standing boundaries" vs. v0.37 entry's "Disclosed standing boundaries" list (both reproduced by parse; 15 shared / 4+4 divergent); build.py [9f] anchor at line 409.
6. **Disproof:** a byte-identical membership match between the two lists. The diff above stands.

**F-K3R2-04 — Gate [9e] emitted zero checks on v0.37 bytes; no per-gate check-count surface exists**
1. **Severity:** LOW.
2. **Class:** D (gate limitation), disclosed by this report.
3. **Tier:** 1 (output-verifiable).
4. **Finding:** build output prints the header "[9e] Cardinal-range consistency" followed by zero check lines, then aggregates into "BUILD PASSED: all checks GREEN." A gate that ran zero checks at this locus is externally indistinguishable from a gate that ran many (Differentiator §7.2 Pattern 2, completeness conflation; Principle 9, Observability Parity). Mitigating: per-check print lines make the absence human-visible. No machine-readable per-gate counter exists. This matters precisely because F-01 is a live cardinal defect at an ungated locus of the same class [9e] names.
5. **Evidence:** build.py lines 391–401 (pattern requires "consecutive" + parenthesized version range, current-entry scope only; `range_claims` empty on v0.37); build transcript ([9e] header, zero PASS lines).
6. **Disproof:** a per-gate check counter in the build output showing [9e] executed N>0 checks on v0.37 bytes. None exists.

**F-K3R2-05 — The v2 discipline files named as "ship in every dispatch" did not ship in this dispatch**
1. **Severity:** INFO.
2. **Class:** E.
3. **Tier:** 1 (absence is byte-verifiable).
4. **Finding:** the v0.19 entry states PRODUCER_SELF_DISCIPLINE_v2_DELTA.md, AUDIT_DISPATCH_DISCIPLINE_v2.md, and SEAT_STANDING_ORDERS_v1.md (S-0 through S-9) "ship in every dispatch as methodological context." This Round-2 dispatch shipped R2_FRESH_KIMI_COBWEB.md + SLINGSHOT_PACKAGE.md only. The R2 markdown embeds distilled discipline content (byte-verification-first, Selection Bias Check, Cow Episode), so the methodological function is partially preserved, but the literal "ship in every dispatch" claim is falsified on this packet, and S-0's normative text is unavailable to this seat (see fractal task for the consequence).
5. **Evidence:** packet file list (22 files; the three named files absent); v0.19 entry text.
6. **Disproof:** none available — absence is total.

**F-K3R2-06 — Severity-register onset at v0.15 is a measurement-onset artifact, not a quiescent epoch**
1. **Severity:** INFO.
2. **Class:** E (denominator honesty, Guardrail 2).
3. **Tier:** 1.
4. **Finding:** severity tokens exist only from v0.15 onward; v0.1–v0.14 carry none. The INFO band therefore partly records the absence of a severity register, not measured quiescence. Consequence for the oscillation analysis: the v0.14→v0.15 +4 step is a regime-break/instrumentation artifact and is excluded from swing-amplitude classification; the slingshot itself flags this ("no explicit severity tokens").
5. **Evidence:** per-entry severity-token counts (0 for v0.1–v0.14; first token at v0.15); slingshot §"Severity trajectory."
6. **Disproof:** locate explicit severity tokens in v0.1–v0.14 entries. None exist.

## PRIORITY-TASK ANALYSES (grounded in the shipped 37-entry series)

**1. Cobweb dynamics classification (Layer 8).** Per-entry max-severity ordinal series (INFO=0…CRITICAL=4), extracted independently and matching the slingshot's six bands 7/7: `[0×14, 4×8, 3×7, 2×1, 3×6, 4×1]`. Excluding the v0.14→v0.15 instrumentation step (F-06), phase-level swing amplitudes are `[1, 1, 1, 1]` — constant, one phase-step, around a HIGH equilibrium (ordinal 3). Per-entry |Δsev| windowed means: 0.57 during the Axiom-3 crisis (v0.15–21), 0.14 through gate-hardening, 0.29 at the freeze arc; first-half mean 0.222 = second-half mean 0.222. Finding-generation volume damps: severity-token counts peak 35 at v0.21, band means 15.5 (v0.15–22) → 9.3 (v0.31–37), terminal run 15→15→13→8→7→2 then 5 at v0.37. **Classification: STABLE** — bounded, constant-amplitude oscillation around a HIGH attractor, with convergent finding volume and a terminal ceiling contact (v0.37 CRITICAL). Not divergent (no amplitude growth in 22 post-onset entries); not convergent to a low-severity equilibrium (the series ends at the ceiling). Layer 8's trajectory-over-position rule keeps this out of HALT territory; the elevated equilibrium is what the TNF task weighs.

**2. TNF-α homeostasis — gate-limitation findings: physiological or pathological?** The standing-boundary stock (the inflammation marker) grows 5→4→5→7→12→13→15→16→17→19→19 across v0.27–v0.37: near-monotone, with two retirements-by-resolution ("PDF unbound" resolved at v0.28; "EXTERNAL count zero" resolved when the Zenodo anchors raised EXTERNAL to 1) and a first plateau at 19 (v0.36→v0.37). Per-item severity is bounded (all Class C/D/E, non-blocking per §22.3); no super-CRITICAL class has emerged; the one terminal CRITICAL (v0.37 register: 1 CRITICAL / 3 HIGH / 1 MEDIUM) was detected by 11/11 seats and closed in-entry. **Reading: physiological-chronic.** The ledger is the Known-Limits mechanism functioning (Guardrail 8; Layer 6 Rice boundary published, not hidden). The chronicity marker: **no gate-limitation boundary has ever been retired by remediation** — every retirement traces to an external resolution, never to a shipped gate extension. Inflammation is bounded, disclosed, and non-escalating (physiological), but resolution is exogenous (chronic). Pathology threshold (cytokine-storm analog: escalating severity per entry, undisclosed accumulation, or boundary growth outpacing body hardening) is not met on shipped data; the 59.2% ungated §27 share with 27.0% semantic-gate body coverage is the standing condition to watch, already disclosed as boundary #4/#3.

**3. Composition-gap sufficiency — does §2.2 consequence 4 suffice for CVE-2024-3094?** Consequence 4 declares composition inference OUT OF MODEL: the kernel evaluates each boundary independently; the XZ compromise was built through individually plausible contributions. The shipped code confirms this at **type level**: `evaluate_kernel(vector)` accepts exactly one frozen `ConjunctVector` — "the five conjunct values for one boundary evaluation" (kernel.py); no sequence, history, or trajectory parameter exists in the input type, so compositional campaigns are not merely unhandled but unrepresentable. Sufficiency, stated exactly: **sufficient for the protocol's declared estimand** (E-S1 mechanical divergence of frozen decision functions on committed packets at enumerated boundaries — the release boundary's tarball-vs-git byte anomaly is an endpoint state the seam can score), **structurally insufficient for CVE-2024-3094 as a compositional campaign** (trust accumulation across years of plausible contributions is invisible to any per-boundary evaluation) — and the protocol says so itself, in the same sentence, before data. The insufficiency is disclosed, scoped, and claim-limited; that is the honest form of sufficiency. Two defects attach to this locus, not to the scoping: the cardinal mismatch that introduces the list (F-01) and the wrong-locus citations of it in the sealed record (F-02). Tier 2 (structural assessment over Tier-1 evidence).

**4. Lag-N autocorrelation of finding types.** Severity-ordinal proxy, N=37, pair counts stated per lag (Guardrail 2): lag-1 r=0.903 (36 pairs), decaying monotonically to r=0.093 at lag 10 (27 pairs) — strong positive persistence, no sign-flip. Severity-token volume: lag-1 r=0.791, crossing zero near lag 8 (−0.037), i.e., positive short-memory with no negative regime. Finding-ID count: lag-1 r=0.636, slow irregular decay to 0.333 at lag 10. **Classification: POSITIVE.** Finding types persist within arcs (the Axiom-3 CRITICAL band v0.15–22 and the HIGH freeze arc v0.31–36 are the load-bearing runs) and decorrelate across arc distances; there is no alternation regime. Hurst R/S on the token-volume series yields H≈0.90, reported as **QUESTION-tier only**: the Cross-Text Thesis v1.1 excludes N=39 from R/S estimation as below reliable length, and N=37 here falls under the same caveat (§3.2: wide confidence intervals on short series; the qualitative persistence read, not the point estimate, is the defensible content).

**5. Standing-boundary monotone growth — pathology or honesty?** Series (canonical, per-entry "Disclosed standing boundaries" lists): 5, 4, 5, 7, 12, 13, 15, 16, 17, 19, 19 over v0.27–v0.37. Monotone modulo two exogenous retirements; first plateau at the terminal pair. **Reading: HONESTY, with a chronicity caveat.** This is Guardrail 8's Known-Limits Disclosure operating as designed — Layer 6 demands the approximation boundary be published, and every item is named, scoped, and severity-bounded. The alternative (pathology) reading would require silent retirement (none — append-only holds; both retirements are narrated) or escalation (none — all items remain Class C/D/E). The caveat, carried from task 2: growth is one-way because remediation is exogenous; a boundary stock that only disclosure — never engineering — retires is physiological-chronic, and the terminal plateau (19, 19) is the first homeostatic signal in the series.

**6. Fractal self-similarity — does the S-0 invariant repeat at multiple scales?** S-0's normative text does not ship (F-05), so the test is run against the invariant the dispatch operationalizes: verify → recompute → disclose. Measured at three scales. *Entry scale:* six-field template conformance per entry (version stamp / digest recompute / test-count+GREEN / status declaration / boundary disclosure / provenance tags) rises 0.17→1.00 and saturates at 1.00 for the final 11 consecutive entries (v0.27–v0.37); phase-scale means 0.30 → 0.73 → 0.90 → 1.00 → 1.00 → 1.00. *Gate scale:* build.py gates [1]–[12] recompute the same six field classes (existence≈stamp, [3] digests, [5]/[8] test counts, [2] version/status, [11] boundary/coverage share, [9c] provenance). *Seat scale:* the R2 dispatch and this seat's own execution re-instantiate the motif (sha256 → build → direct pytest → disclose, with denominators stated). **Result: SELF-SIMILAR AT 3 SCALES**, with entry-scale conformance saturated (11/11 perfect entries) — persistence confirmed structurally, not by the underpowered R/S estimate (see task 4 caveat).

## OSCILLATION MEASUREMENTS

```
  Cobweb: stable (constant amplitude-1 phase swings around HIGH equilibrium;
          finding-volume damping 15.5→9.3 band means; terminal ceiling
          contact v0.37 CRITICAL; instrumentation step v0.14→15 excluded)
  Finding-type autocorrelation: positive (lag-1 r=0.903 → 0.093 at lag 10,
          N=37, pairs 36→27; no negative regime at any lag 1-10)
  Boundary-to-finding ratio: diverging (boundary stock 5→19 vs finding-flow
          decay; TNF read: physiological-chronic, zero remediation retirements)
  S-0 fractal test: self-similar at 3 scales (entry / gate / seat; entry
          conformance 1.00 for final 11 entries, v0.27-v0.37)
```

## VERDICT BASIS (why CONDITIONAL PASS, not HALT)

No Class A basis exists: every sealed claim this seat executed verified on the shipped bytes — 16/16 digests, manifest = trust roots, 186/186 GREEN direct, 37-entry ascending order, all seals, PRIOR_HISTORY derivation, 91.7% ASSERTED within bound. F-01 and F-02 are genuine, undisclosed errors (a strict letter-reading of §22.3 Class B would say HALT-grade), and this seat rejects that reading on three grounds: **(1)** the CONDITIONAL PASS vehicle's existence precedent — if any undisclosed error auto-HALTed, no seat could ever carry findings as conditions, yet the v0.31 carrying round's CONDITIONAL PASS conditions counted as non-HALT; Class B's paradigm is concealment that defeats verification of what the bytes claim to be (the v0.4 erased-HALT), not locus-visible prose slips whose substrate (four enumerated items; the only numbered consequence list in the document) is co-present at the locus. **(2)** Neither finding contradicts status, a digest, a count of record, or any sealed object; §22 item 7's exception explicitly preserves HALT for Class A/B, and for that carve-out to have operative meaning the A/B boundary must sit at sealed-claim substance. **(3)** Converting disclosable, non-status defects into freeze-blockers is the non-converging re-HALT loop the v0.37 amendment was written to break, and the Cow-Episode failure mode this dispatch warns against (v0.37 item 4: cumulative specification is real but misapplied against correct rule-application). Conditions, all disclosure/amendment-class, executable in one version: **(C1)** amend §2.2's cardinal or mark consequence 4 as inherited, with append-only entry (F-01); **(C2)** disclose the v0.36 ring-closure locus error as a standing boundary (F-02); **(C3)** reconcile the slingshot boundary list against the canonical list each round, and absorb "register scoping anchored to unregistered prose literal" into the canonical list (F-03); **(C4)** emit per-gate check counters in build output (F-04).

## TOOL PRODUCTIVITY

```
TOOL PRODUCTIVITY: 6/6 productive (every priority task produced genuine,
  entry-grounded findings; no tool run for narration)
Selection Bias Check (denominators): 43 tool calls total — 42 productive,
  1 unproductive (native ODT read failed; content recovered via zip/XML
  extraction). Analytical tools: 36 (ipython 25, shell 6, read_file 5);
  process overhead: 7 (todo_write 5, write_file 2).
  Patterns tested before accepting the oscillation classification: 3
  (severity-ordinal swings, token-volume decay, finding-ID persistence);
  the per-entry severity parse was cross-checked against the slingshot's
  6-band trajectory (7/7 agreement) before any classification was drawn.
Cow Episode check: 4 conditions, all disclosure/amendment-class; no new
  gate, schema, or specification is demanded of the producer.
```

Wa ma tawfiqi illa billah.

---

# Bismillah ir-Rahman ir-Rahim
