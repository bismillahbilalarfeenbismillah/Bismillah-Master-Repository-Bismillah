# Bismillah ir-Rahman ir-Rahim

# R0307 -- Grok 4 (xAI) — Round 3 / pass-36 Class Fix Verification

**Chronological Index:** 713 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** Grok_audit.md  
**Source Format:** md  
**SHA-256:** `800d6a80b5738397aa5baa0893a7f2a4b9c9dc3fc6ea80205f7c5898d538fbc4`  

---

## R0307 · Grok 4 (xAI) — Round 3 / pass-36 Class Fix Verification

- section: V. BSSG & SHVVP Protocols
- source_file: Grok_audit.md
- source_format: md
- text_sha256: 800d6a80b5738397aa5baa0893a7f2a4b9c9dc3fc6ea80205f7c5898d538fbc4

**Grok 4 (xAI) — Round 3 / pass-36 Class Fix Verification**
Exact model: Grok 4 (built by xAI). Fresh nonce; everything re-derived from the bytes in packet/.


## 1. Command outputs + identity

### sha256sum -c SHA256SUMS

**20/20 OK.**

### python3 test\_bssg\_gate.py

text

```
`Ran 345 tests in 0.082s`

`OK (skipped=8)`
```

### python3 bssg\_counterexamples.py

text

```
`...`

`GREEN CE176 \[34TH-INSTANCE\] 34th instance (degraded-first ceiling-absence) CLOSED: a degraded-first session gets an empty contract\_ceiling entry; post-lift DELETE is DENIED; the class fix ensures \_held is NEVER None after an ALLOW  has\_entry=True is\_empty=True delete\_denied=True`


`176/176 GREEN  (0 RED = open defects)`
```

### python3 bssg\_model\_check.py

text

```
`MODEL CHECK: PASS -- kernel(243) + antitone(729) + bounded-auth-intro(11110 schedules) + operational refinement on the executable`
```

### python3 verify\_bssg\_v0\_1.py

text

```
`SUMMARY: 14 gates, 12 PASS, 2 WARN, 0 FAIL`

`PACKAGE STATUS: SELF-CONSISTENT DRAFT (not carried, not publication ready)`
```

### python3 bssg\_gate.py

text

```
`BSSG reference gate 0.1.0-draft, spec version 0.1`

`DRAFT / NOT CARRIED. No effectiveness claim is made by this software.`
```

### Identity values

text

```
`MANIFEST: 2eb51ed4d015805b65adec431cb2fe788e9c1be6c71d97ee1b687f62bcbad34c`

`CHALLENGE: 5897994516fd2a5bc474950f1cc8f9ebf83053dda38b4502fde5971221dbab68`

`EXECUTION\_ATTESTATION: ba330755b8e0727cdebc7820f2eef8c1e2e29c66b283d0840fca30f40e111612`
```


## 2. Class-fix verification

### ALLOW-path init (≈L1820)

Python

```
`\# CLASS FIX: initialize contract\_ceiling for this session if absent.`

`\# ... at the TOP OF THE ALLOW PATH, before any conditional (health check, mint, ceiling-write).`

`\_cc\_session = (request.get("session\_id") if isinstance(request, dict)`

`               and isinstance(request.get("session\_id"), str) else None)`

`if \_cc\_session is not None and \_cc\_session not in self.state.contract\_ceiling:`

`    self.state.contract\_ceiling\[\_cc\_session\] = Authority(\[\], \[\])`
```

This fires **unconditionally** for every path that has already decided ALLOW (i.e., after the if decision != DECISION\_ALLOW: return gate and before new\_token()).

- Degraded ALLOW → empty entry left in place.

- HEALTHY + successful mint → entry later **upgraded** by ceiling\_for\_health(..., "HEALTHY").

- Mint-fault / invalid / collision → returns via \_issuance\_failure **after** the empty init has already run; \_issuance\_failure also retains its defensive write.

- Ceiling-write exception → empty (or prior) entry survives.

### Gemini degraded-first probe (34th instance)

text

```
`R1: ALLOW | cc: \{'effects': \[\], 'target\_scopes': \[\]\}`

`cc is empty Authority: True`

`R3 DELETE after lift: DENY\_FALSE`

`34th instance CLOSED: True`
```

### R2 probes re-run (still closed)

| **Path** | **R1** | **cc empty?** | **Post-lift DELETE** | Closed? |
| :-: | :-: | :-: | :-: | :-: |
| MINT-FAULT | ALLOW / FAILED\_NO\_EFFECT | True | DENY\_FALSE | Yes |
| MINT-INVALID | ALLOW / FAILED\_NO\_EFFECT | True | DENY\_FALSE | Yes |
| COLLISION | ALLOW / FAILED\_NO\_EFFECT | True | DENY\_FALSE | Yes |
| Prior-ceiling + broader-registry mint-fault | ALLOW / FAILED\_NO\_EFFECT | prior survives unbroadened | — | Yes |

### The invariant

**\_held can never be None after any ALLOW decision on the pass-36 bytes.**

Trace of every path through the ALLOW branch:

1. Kernel reaches decision == DECISION\_ALLOW.

2. Control enters the ALLOW block.

3. Pending is captured and cleared.

4. **Empty-Authority init runs if the session is absent** (the class fix).

5. new\_token() is attempted.

   - Success + HEALTHY → upgrade write.

   - Success + DEGRADED → empty/prior left.

   - Fault / invalid / collision → \_issuance\_failure (entry already present).

6. Any subsequent post-lift re-establishment therefore sees \_held = self.state.contract\_ceiling.get(session) as a non-None Authority (empty or previously demonstrated HEALTHY). The \_held is not None guard in \_apply\_narrowing therefore always fires and bounds the re-establishment.

No ALLOW path returns without having executed the init. The 34-instance pattern (absence treated as “establishment free”) is structurally closed.


## 3. Verdict

**CLEAN.**

All commands match the expected battery (20/20, 345, 176/176 GREEN, 11110 schedules, 12 PASS / 0 FAIL). The class fix is present and unconditional at the top of the ALLOW path. The degraded-first vector is closed (CE176). All prior R2 vectors remain closed. The invariant holds: after any ALLOW, \_held is never None.

Artifact status remains **DRAFT / NOT CARRIED / NOT PUBLICATION-READY**. No effectiveness claim is made.

---

# Bismillah ir-Rahman ir-Rahim
