# Bismillah ir-Rahman ir-Rahim

# R0038 -- Em-Dash Policy

**Chronological Index:** 627 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_em-dash-policy.md  
**Source Format:** md  
**SHA-256:** `9cd41ddadcf9fa72c0690c8449440935e3da660d0b1ceb6057df731345dcde38`  

---

## R0038 · Em-Dash Policy

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_em-dash-policy.md
- source_format: md
- text_sha256: 9cd41ddadcf9fa72c0690c8449440935e3da660d0b1ceb6057df731345dcde38

# Em-Dash Policy

**Rule:** No em-dash characters (`--`-em, Unicode U+2014) anywhere in
artifacts produced under this skill. Use the double-hyphen `--` for
prose em-dash effect.

## Scope

The policy applies to:

- External prose (README, marketing copy, blog posts, business plans)
- Internal documents (audit prompts, methodology documents, ledger
  entries)
- Python source files (`.py`) -- comments and string literals included
- LaTeX sources (`.tex`) -- the `---` em-dash ligature must also become
  `--`
- Markdown sources (`.md`) -- with the explicit exception that `---`
  as a horizontal rule or table-row separator is permitted and required

## Why this rule

Three reasons converge:

1. **Cross-tool consistency.** Many text editors auto-substitute `--`
   into em-dash; many LLM outputs default to em-dash; many PDF renderers
   render em-dash differently across fonts. Strict double-hyphen
   eliminates substrate divergence between editing tools, model
   outputs, and rendering surfaces.
2. **Diff-friendliness.** Em-dash characters render identically to
   hyphen-minus in some fonts (especially monospace), making source
   diffs ambiguous. Double-hyphen is unambiguous in every font.
3. **Substrate uniqueness.** Em-dash and hyphen-minus claim the same
   visual surface but have different code points; this is itself a
   surface-substrate divergence pattern. The methodology refuses to
   instantiate the pattern it audits.

## Exceptions

Three explicit exceptions:

1. **Markdown horizontal rules.** `---` on its own line is a legitimate
   horizontal rule and required formatting.
2. **Markdown table separators.** `|---|---|` row separators in tables
   are legitimate and required.
3. **Documentation references to the rule itself.** Files that document
   this policy (this file; PMD §0.2; SKILL.md) may quote em-dash
   characters when explicitly demonstrating violations or the literal
   characters being prohibited. Wrap such quotations in backticks.

## Detection patterns

When auditing, search for:

- `—` (U+2014, em-dash) anywhere outside the three exceptions
- `–` (U+2013, en-dash) anywhere -- also prohibited; use `--` or `-`
- `―` (U+2015, horizontal bar) anywhere -- also prohibited
- `---` in LaTeX sources outside legitimate Markdown contexts

## Common violation sites

Empirical record across Rounds 31-38.5:

- LLM-generated prose almost always defaults to em-dash; producer
  cycles routinely surface em-dash violations during methodology-lint
  step.
- Copy-pasted text from web sources (especially news articles,
  documentation sites, and rich-text editors) carries em-dash.
- Markdown-to-PDF conversion tools sometimes substitute `--` -> em-dash
  during rendering; the source remains compliant but the rendered
  output diverges. Audit at the source layer.

## Disposition

Em-dash violations are LOW severity by default. They are detection-
trivial (regex `[\u2013-\u2015]`) and correction-trivial (substitute
to `--`). The reason they remain in scope is that they accumulate
across artifacts and undermine cross-document consistency at the brand
level.

In one specific case the severity escalates to MEDIUM: when the violation
appears in a published Zenodo deliverable with an assigned DOI. Per
§14.5 attribution-corrective immutability, the DOI-published version
cannot be edited; the next version must absorb and the v1.x -> v1.x+1
appendix must document the carry-forward.

## Quick check

The fastest violation check is:

```python
import re
def check_em_dash(text: str) -> list[tuple[int, str]]:
    """Return (line_number, context) tuples for em-dash violations."""
    violations = []
    for i, line in enumerate(text.split("\n"), start=1):
        if re.search(r"[\u2013\u2014\u2015]", line):
            violations.append((i, line))
    return violations
```

LaTeX additional check:

```python
def check_latex_em_dash(text: str) -> list[tuple[int, str]]:
    """Return (line_number, context) for --- outside Markdown contexts."""
    violations = []
    for i, line in enumerate(text.split("\n"), start=1):
        if "---" in line and not (line.strip() == "---" or "|---|" in line):
            violations.append((i, line))
    return violations
```

---

# Bismillah ir-Rahman ir-Rahim
