# Bismillah ir-Rahman ir-Rahim

# R0039 -- Six-Element Findings Format

**Chronological Index:** 628 of 995  
**Date:** Undated  
**Section:** II. Analytical Frameworks & Methodology  
**Source File:** bayyinah_findings-format.md  
**Source Format:** md  
**SHA-256:** `5186e1300bc7cceb5e8fbc3f2fc8da0c265147a973a20a7d0bcc9bd63514e3d2`  

---

## R0039 · Six-Element Findings Format

- section: II. Analytical Frameworks & Methodology
- source_file: bayyinah_findings-format.md
- source_format: md
- text_sha256: 5186e1300bc7cceb5e8fbc3f2fc8da0c265147a973a20a7d0bcc9bd63514e3d2

# Six-Element Findings Format

Every finding under BayyinahEnterprise audit methodology must contain
all six elements below. Findings missing any element are themselves
findings.

## The six elements

1. **ID** -- unique identifier in the namespace `F-XX-N` where `XX` is
   the round / cycle namespace and `N` is the sequence number. Examples:
   `F-PA-3` (Round 38.5 finding 3), `F-TR-7` (al-Mursalat v1.5 -> v1.6
   round, finding 7), `F-PB-1` (next round's first finding).
2. **Severity** -- one of CRITICAL, HIGH, MEDIUM, LOW (uppercase). See
   `severity-rubric.md` for calibration.
3. **Locus** -- file path + line number(s) (or section/heading for
   prose) pinpointing where the finding lives. Generic loci ("somewhere
   in the prompt") are themselves findings.
4. **Substance** -- what is wrong, stated as a surface-substrate
   divergence. Not "X is bad" but "X claims Y but does Z."
5. **Disposition** -- the prescribed route to resolution. Either a
   specific code change ("rename Z to Y at line 47"), a documentation
   correction ("amend §3.2 to state the resolved state directly"), an
   ADR requirement ("removal of public API X requires ADR before
   merge"), or a HALT-and-escalate marker for CRITICAL findings.
6. **Cross-reference** -- the prior finding, methodology section, or
   substrate fact this finding relates to. Forward references to PMD
   sections, prior round finding IDs, or substrate line citations.

## Template

```
**F-XX-N** [SEVERITY] -- <one-sentence summary>

- **Locus:** <file>:<line> (or <section heading>)
- **Substance:** <surface claim> diverges from <substrate behavior>
  because <mechanism>.
- **Disposition:** <prescribed route>.
- **Cross-reference:** <related finding ID, methodology section, or
  substrate citation>.
```

## Worked example (from al-Mursalat Round 38.5)

```
**F-PA-3** HIGH -- T05 alphabetical-vs-end-append four-surface contradiction

- **Locus:** paste.txt lines 2984-3050 (T05 code block), 3088-3134
  (fixture #3 hash computation), plus comment at 2964 and fixture #1
  alphabetical assertion.
- **Substance:** T05 code block enumerates 19 entries in alphabetical
  order claiming "extend existing 16-entry tuple"; fixture #3
  hash literal computation appends new entries to end via
  `*V0_11_8_CHECKER_SOURCES + additions`; comment claims one ordering
  while fixture asserts another. Four surfaces present three orderings.
- **Disposition:** Option (alpha) -- restructure T05 to interleave gate11
  Go entries at canonical alphabetical positions #6/#7 between
  cli.py and manifest_schema.py; shift original gate11 entries to
  #8-#18; goast at #19 in go_adapter section. Fixture #3 hash
  literal must enumerate full 19-entry tuple in this interleaved order.
  Fixture #1 alphabetical assertion preserved.
- **Cross-reference:** F-TR-6 (alphabetical claim retired at v1.6) and
  F-PF-1 (T00 surfaced substrate-actual alphabetical). PMD v1.2 §X
  absorption-induced regression at retired surfaces.
```

## Findings-format compliance check

When auditing an audit deliverable, verify each finding entry against
this template. Common violations:

- Severity in sentence case ("High" instead of "HIGH") -- itself a
  finding, severity LOW.
- Missing cross-reference -- itself a finding, severity LOW.
- Locus stated as "the document" without line / section -- itself a
  finding, severity MEDIUM (auditor cannot reproduce without locus).
- Substance stated as judgment ("this is bad") without surface-substrate
  divergence framing -- itself a finding, severity MEDIUM.
- Disposition absent or stated as "needs to be fixed" without prescribed
  route -- itself a finding, severity HIGH (next absorption cycle has
  no instruction to follow).

## Findings batching and ordering

Within a single audit deliverable:

- Findings are ordered by severity (CRITICAL first, then HIGH, MEDIUM,
  LOW).
- Within a severity band, findings are ordered by locus (file path
  ascending, then line number ascending).
- Cross-references may forward-reference later findings within the same
  audit (e.g., F-PA-3 may reference F-PA-7) but never backward-edit
  prior findings.

## Namespace assignment

Audit cycles assign a two-letter namespace per round:

- `F-AL-N` -- al-Hujurat round
- `F-RM-N` -- as-Saff Route a1 round
- `F-RN-N` -- as-Saff Route a1-via-args round
- `F-TR-N` -- al-Mursalat v1.5 -> v1.6 round
- `F-PF-N` -- Co-work T00 pre-flight round
- `F-PA-N` -- al-Mursalat Round 38.5 (v1.7 audit)
- `F-PB-N` -- next round (al-Mursalat Round 39 or v1.8 audit)
- `F-PMD-N` -- methodology-document findings (PMD v1.x audit cycles)

New cycles pick the next unused two-letter combination. Never reuse a
prior namespace within a single chain.

---

# Bismillah ir-Rahman ir-Rahim
