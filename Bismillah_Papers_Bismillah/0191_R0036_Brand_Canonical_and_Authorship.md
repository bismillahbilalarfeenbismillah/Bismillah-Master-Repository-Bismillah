# Bismillah ir-Rahman ir-Rahim

# R0036 -- Brand Canonical and Authorship

**Chronological Index:** 191 of 995  
**Date:** 2026-05  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_brand-canonical.md  
**Source Format:** md  
**SHA-256:** `5ccd9faca8373065e11455c7f1075733d722099b4847f1dd4b110668f80a3a23`  

---

## R0036 · Brand Canonical and Authorship

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_brand-canonical.md
- source_format: md
- text_sha256: 5ccd9faca8373065e11455c7f1075733d722099b4847f1dd4b110668f80a3a23

# Brand Canonical and Authorship

## Brand

**Canonical brand name:** `BayyinahEnterprise` -- one word, no space.

**Forbidden variants:**

- `Bayyinah Enterprise` (with space) -- ALL OCCURRENCES are findings.
- `Bayyinah Enterprises` (plural) -- ALL OCCURRENCES are findings.
- `bayyinahenterprise` (lowercase) -- acceptable only in URLs, email
  addresses, domain names, and code identifiers where casing is
  enforced by external systems (e.g., `bayyinahenterprises@tuta.com`,
  `github.com/BayyinahEnterprise`).
- `Bayyinah` alone -- acceptable only when modifying a product name
  ("Bayyinah Audit Framework v3.0", "Bayyinah Integrity Scanner") or
  when contextually clear inside a document whose title already
  carries the full canonical brand.

## Product names

These are canonical product names; do not abbreviate or rephrase:

| Product | Canonical name |
|---|---|
| Code analysis tool | `furqan-lint` (lowercase, hyphenated) |
| Document integrity scanner | `Bayyinah Integrity Scanner` |
| Methodology document | `Bayyinah Audit Framework v3.0` |
| Predictive modeling doctrine | `Predictive Modeling Discipline` (PMD) |
| Four-lane platform | `BayyinahEnterprise platform` or `the platform` |
| Skill bundle (Lane 1) | `bayyinah-audit` (lowercase) |
| CI pipeline (Lane 2) | `bayyinah-ci` (lowercase) |
| Cross-vendor validator (Lane 3) | `bayyinah-validator` (lowercase) |
| MCP server (Lane 4) | `bayyinah-mcp` (lowercase) |

## Authorship attribution

**Project lead and methodology author:**

> Bilal Syed Arfeen (BayyinahEnterprise)

Bilal is referenced as "project lead" or "founder" depending on
context. In academic / Zenodo contexts, "author" or "co-author." Never
"CEO" without entity-formation confirmation (Indiana LLC was planned
per business plan as of May 2026 but is not yet formed at time of this
skill version).

**Methodology co-developer:**

> Fraz Ashraf (audit methodology co-developer)

Fraz contributes the engineering-discipline practices from 15+ years
in renewable energy and safety-critical infrastructure systems.
Co-author on Audit Framework v3.0 and the Application Brief.

**Infrastructure partner:**

> Patrick Estes (Estes Strategy Insights, LLC)

Patrick built the four-lane deployment infrastructure (skill compiler,
CI pipeline, cross-vendor validator, MCP server) -- now under
construction per Phase 1-4 of the build prompt. Perpetual, non-exclusive,
royalty-free license to BayyinahEnterprise.

**Domain advisor:**

> Devin (Domain Advisor, Supply Chain Analytics)

10 years at Hanson Logistics / Lineage Logistics. Potential collaborator
on predictive analytics track.

**Mentor:**

> Paul Yadron (SCORE Mentor, NW Central Indiana)

Co-Chair, NW Indiana SCORE Chapter. Advisory on entity formation,
pricing, and go-to-market.

## Joint-authorship convention

For co-authored work:

- Audit Framework v3.0 -- "Bilal Syed Arfeen and Fraz Ashraf
  (BayyinahEnterprise)"
- Code repositories -- "Bilal Syed Arfeen (BayyinahEnterprise)" unless
  Fraz contributed code (then joint)
- Platform infrastructure -- "Patrick Estes (Estes Strategy Insights,
  LLC), licensed to BayyinahEnterprise"

## Casing in code identifiers

Per existing repository conventions:

- Package names: `furqan-lint`, `bayyinah-ci`, `bayyinah-validator`,
  `bayyinah-mcp`, `bayyinah-audit` (lowercase, hyphenated)
- Python module names: `bayyinah_ci`, `bayyinah_validator`,
  `bayyinah_mcp` (lowercase, underscored)
- GitHub org: `BayyinahEnterprise` (canonical casing)
- DOI prefix: `10.5281/zenodo.20017335` (Zenodo-assigned; never edit)

## Detection

Quick check for brand violations:

```python
import re

FORBIDDEN_BRAND_PATTERNS = [
    r"Bayyinah Enterprise\b",       # with space
    r"Bayyinah Enterprises\b",      # plural
    r"\bbayyinah enterprise\b",     # lowercase with space (URLs OK)
]

def check_brand(text: str) -> list[tuple[int, str]]:
    violations = []
    for i, line in enumerate(text.split("\n"), start=1):
        for pat in FORBIDDEN_BRAND_PATTERNS:
            if re.search(pat, line):
                # Allow inside URLs / email addresses
                if "@" in line or "://" in line or "github.com" in line:
                    continue
                violations.append((i, line))
                break
    return violations
```

## Severity

Brand-canonical violations are LOW severity in internal artifacts,
MEDIUM severity in customer-facing artifacts (pitches, website,
business plan, README, published papers), and HIGH severity in
Zenodo-DOI-published deliverables (per §14.5 immutability discipline,
brand errors in DOI-published versions cannot be edited; only absorbed
into the next version with explicit appendix entry).

---

# Bismillah ir-Rahman ir-Rahim
