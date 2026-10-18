# Bismillah ir-Rahman ir-Rahim

# R0635 -- FAIL DP-G1a [MINOR] root-directory target canonicalizes (single trailing slash) canonical=None

**Chronological Index:** 850 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** glm_pass8_probes_output (1).txt  
**Source Format:** txt  
**SHA-256:** `6ff484af16722edee01f47df0c4e08addaa4e2eda970bf444476a67e69d72f5f`  

---

## R0635 · FAIL DP-G1a [MINOR] root-directory target canonicalizes (single trailing slash) canonical=None

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: glm_pass8_probes_output (1).txt
- source_format: txt
- text_sha256: 6ff484af16722edee01f47df0c4e08addaa4e2eda970bf444476a67e69d72f5f

FAIL DP-G1a [MINOR] root-directory target canonicalizes (single trailing slash)  canonical=None
FAIL DP-G1b [MINOR] percent-encoded non-separator (%2D hyphen) target canonicalizes  canonical=None
FAIL DP-G1c [MINOR] @ in path segment (not credentials) canonicalizes  canonical=None
PASS DP-G1d [INFO] directory-scope target with trailing slash canonicalizes (control)  canonical=https://db.example.internal/records/
PASS DP-G1e [INFO] trailing-newline nonce: structural_check catches it OR schema_valid catches it  structural_nonce_err=False gate_decision=REJECTED_SCHEMA
PASS DP-G2a [MINOR] Unicode homoglyph authority canonicalizes to different target (no IDNA)  latin=https://db.example.internal/records/row-1 cyrillic=https://dв.example.internal/records/row-1
PASS DP-G2b [INFO] U+2044 fraction slash does not escape scope  decision=DENY_FALSE canonical=https://db.example.internal/records⁄secrets
PASS DP-G2c [INFO] path case is preserved (not lowercased)  canonical=https://db.example.internal/Records/Row-1
PASS DP-G2d [MINOR] IDNA: Unicode and Punycode forms canonicalize differently (no IDNA)  unicode=https://bücher.example/records/ punycode=https://xn--bcher-kva.example/records/
FAIL DP-G3a [MAJOR] commit-time fresh witness WithinAuth assessment IS revalidated  outcome=COMMITTED_PENDING_OUTCOME reasons=[]
FAIL DP-G3b [MAJOR] commit-time fresh witness observed_at IS revalidated (clock ambiguity)  outcome=COMMITTED_PENDING_OUTCOME reasons=[]
FAIL DP-G3c [INFO] commit-time fresh witness checkpoint IS compared  committed=True receipt_binds_checkpoint=False
PASS DP-G3d [INFO] commit-time fresh witness with missing within_auth_assessment is rejected  outcome=FAILED_NO_EFFECT reasons=['E-COMMIT-WITNESS-SCHEMA-INVALID']
PASS DP-G4a [INFO] _commit_lock is redundant (commit already holds self._lock)  outer_lock=True inner_lock=True
PASS DP-G4b [INFO] authorize, commit, submit_amendment all serialize on self._lock  auth=True commit=True amend=True
PASS DP-G4c [INFO] concurrent multi-session authorize: all ALLOW, no crash  outcomes={'sess-0': 'ALLOW', 'sess-1': 'ALLOW', 'sess-2': 'ALLOW', 'sess-3': 'ALLOW', 'sess-4': 'ALLOW'}
FAIL DP-G5a [MINOR] verifier scans for 'preserves capability' (spec prohibition #8)  found_in_verifier=False
FAIL DP-G5b [MINOR] verifier scans for 'guarantees' broadly (not just 'guarantees safety')  guarantee_patterns=['guarantees safety']
FAIL DP-G5c [INFO] attack register does not claim equivocation is ENFORCED  equivocation_enforced=True
PASS DP-G5d [INFO] gate module makes no effectiveness claim  no_harm=True no_safe=True
PASS DP-G5e [INFO] spec acknowledges in-memory nondurability (deployment obligation)  acknowledged=True

12/21 passed  (9 flagged)

---

# Bismillah ir-Rahman ir-Rahim
