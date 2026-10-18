# Bismillah ir-Rahman ir-Rahim

# R0660 -- Delta-Attestation Audit Report — Dissertation v1.2 → v1.3

**Chronological Index:** 310 of 995  
**Date:** 2026-07-22  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-claude_fable_5 (2).md  
**Source Format:** md  
**SHA-256:** `40d0d0bb5eb21bf42873d7a6c1d73f948d69b4971672be2d84b1be08a3eeb47b`  

---

## R0660 · Delta-Attestation Audit Report — Dissertation v1.2 → v1.3

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-claude_fable_5 (2).md
- source_format: md
- text_sha256: 40d0d0bb5eb21bf42873d7a6c1d73f948d69b4971672be2d84b1be08a3eeb47b

# Delta-Attestation Audit Report — Dissertation v1.2 → v1.3

## Seat declaration (standing disclosure rule)

| Field | Value |
|---|---|
| Model | **Claude Fable 5** |
| Vendor | **Anthropic** |
| Tier | **frontier** |
| Seat status | **ADVISORY (producer lineage — Ruling 3 exclusion; carries NO verdict)** |
| Findings namespace | **F-DP-NN** |
| Round | Delta-scoped attestation v1.2 → v1.3 against register D-1..D-9 (audit ledger, v1.3 section) |
| Governing brief | `DELTA_ATTESTATION_BRIEF_v1_3.md` (rev 2, July 23, 2026) |
| Governing method | `SHV_Method_v1_1.pdf` (SHA-256 `8f8b4358…` — matches the brief's declared receipt) |
| Date of execution | July 22, 2026 (19:05 CDT) / July 23, 2026 (UTC) |

Per Ruling 4, no producer self-repair is credited for mere presence; every D-item was re-verified against packet bytes and primary sources. Per the brief's record-over-person rule, this report works from the packet and primaries, not from the v1.2 review's prose. **Everything below is analytical input only; this seat's assessment is NON-CARRYING.**

---

## 1. Chain leg — packet integrity (SHV D1/D2: substrate over attestation; chain and content separately)

### 1.1 Manifest re-derivation

`sha256sum -c SHA256SUMS.txt` exits 0; every hash was independently re-computed. Full SHA-256 of **every packet file this seat actually verified**:

| File | SHA-256 (independently computed) | Manifest match |
|---|---|---|
| BUILD_CORRIGENDUM_2026-07-22.md | `275883b540035df2006e0ef3e44ba156b9313d4c94987d892fcebd869692f3a6` | ✔ |
| DELTA_ATTESTATION_BRIEF_v1_3.md | `a2f6f9371cf4b5e2183b2cd0d2478bd96c74d4e5c7bb2347b92c717c8f5caeb0` | ✔ |
| DEPOSIT_METADATA_v1_3.md | `46f855b166c851a4d9051b7063ddecdad14972f03eca2b7ee35e11202950c191` | ✔ |
| README_PUBLICATION.md | `3411838131ca2296f53cbe03e3de11801cb0e372f0067b2dd0934afeb5f995d6` | ✔ |
| SHV_Method_v1_1.pdf | `8f8b43584219a52802f8ace4b4e49021448366b2a044b281ada00ba5762a8896` | ✔ (= brief's declared value) |
| Structural_Honesty_Dissertation_audit_ledger.md | `f7e539bb3733c128fd2abb768861c8ab72c93287d7946695344fcbe25663bb8c` | ✔ |
| Structural_Honesty_Dissertation_bibliography.bib | `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4` | ✔ (= ledger v1.3 refs.bib receipt) |
| Structural_Honesty_Dissertation_punch_list.md | `c3ae1859e86329fd6169ad0da8e6ef8818f2b299c64d0725b6dbf4f17aeaaa9e` | ✔ |
| Structural_Honesty_Dissertation_v1_3.html | `1ec63214bf940cbe1086be06e6b6bc14b9a79d4b7e6a7b87cf437a710551b4cb` | ✔ (= ledger HTML receipt) |
| Structural_Honesty_Dissertation_v1_3.pdf | `57560b35ccd75ac4f9e0ace868d25f8c1f76ca05c62cfa5c562b0b9071158fc4` | ✔ (= ledger PDF receipt) |
| Structural_Honesty_Dissertation_v1_3_source.md | `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5` | ✔ (= ledger source receipt) |
| canon_v1_2_baseline.md | `38dfa91dcae27ba5d90a07c3acb1d6719d96b5a351e5f1c4c2502f7038490eca` | ✔ (= brief's declared v1.2 canon anchor) |
| verify_dissertation_v1_3.py | `78c8a3b35d66295f24ce0c48157a5ba9416c53fd88ec3e47c9e4c1a1936571ed` | ✔ |
| SHA256SUMS.txt (self) | `776ab8eab660da423eb160b73c78b0ad2502b6d8f57e2206ba7da6ee851fc5cf` | (not self-listed; recorded for the chain) |

Bonus chain closure from the co-shipped audit-trail set (outside the authoritative publication root; provenance noted): `Structural_Honesty_Dissertation_v1_3.docx` = `e83ff142f9a14b72d720cc5222982a663f896d3894dc92296eeb33499e74e76c`, **byte-matching the ledger's v1.3 DOCX receipt**. The trail manifest (`SHA256SUMS.txt` = `…1314 B` variant) is identical to the publication manifest except DOCX-for-PDF substitution, consistent with the DEPOSIT_METADATA 2-upload pattern; all trail members verified OK and the verifier passes there too.

### 1.2 Chain-of-custody observation

Two **unmanifested files** (`diff.txt`, `diff_hunks.txt`) appeared in the packet root after receipt — sibling council-seat working artifacts in the shared workspace. This seat did **not** read them; all diffs below are independently derived (probe discipline: no cross-seat contamination). Recorded as a custody observation, not a packet defect (they are not packet members and post-date the manifest).

---

## 2. L4 — render gates (executed first to fix the substrate state)

`python3 verify_dissertation_v1_3.py` inside the unpacked kit: **`VERIFIER: ALL PASS`, exit 0** (run in both publication and trail sets). Because a producer-shipped verifier earns no absence-credit (Ruling 4), every gate was **independently re-derived** with wrap-immune normalization (de-hyphenate line breaks → collapse whitespace → match) and quoted-literal probes only:

- **Chapter-identity harness 23+D/E**: standalone display lines `Chapter 1`…`Chapter 23`, `Appendix D`, `Appendix E` each present exactly once adjacent to their expected titles; order monotone. Independently spot-verified for Ch8/Ch9/Ch22/Ch23/App D/App E (the SOL-R1 failure loci).
- **STATUS-CURRENCY** (quoted literals): `Pre-publication working draft of Chapter` = 0; `toward v1.0 publication targeted` = 0; `During the present pre-publication phase` = 0 — in PDF text layer and HTML.
- **META-TEXT-ABSENCE** (quoted literals): `section is a placeholder`, `remove at submission`, `final wording at F-audit`, `not part of this packet`, `build profile` — all 0 in the normalized PDF text.
- **Author-note / disclaimer render parity**: `Prepared with Claude` present ×1 in PDF, HTML, and source line 1; `not independent human peer review` ×1 in PDF and HTML; subtitle `An Independent Research Monograph` on the PDF title page and in the DEPOSIT_METADATA title field.
- **Flagship DOI in DEPOSIT_METADATA_v1_3.md**: `10.5281/zenodo.21500700` present (3×), with IsSupplementTo relation. Externally resolved: the DOI resolves to the flagship record ["Structural Honesty: Axioms for Detecting Surface-Substrate Divergence in AI Systems", Arfeen, v0.13](https://doi.org/10.5281/zenodo.21500700) — live and title-true, not liveness-only.
- **D-9 formatting ruling**: `pdfinfo` = **324 pages** (matches ledger receipt "324 pp"), page size **612×792 pt (letter)**; `pdffonts` = LMRoman 10/12/17 + LatinModernMath (Latin Modern family), producer `xdvipdfmx` (xelatex engine, as the build corrigendum requires for the transliteration codepoints); **chromatic sample**: 10 pages rendered (1, 2, 10, 50, 100, 150, 200, 250, 300, 324) — 0 chromatic pixels, max RGB channel divergence 0 (consistent with the "all-black 0.000%" receipt).
- Zero literal `#` heading markers in the PDF text layer (SOL-R1 regression class clean).

---

## 3. L1 — canon delta (independently reconstructed)

The v1.3 canon body was reconstructed from packet bytes: baseline body = `canon_v1_2_baseline.md` lines 83–5404 with `# === Chapter N: T ===` markers normalized to `# T`; v1.3 body = source lines 11–5337 (Chapter 1 through end of Appendix D; the build front matter and the Appendix E projection of the canon-metadata header excluded structurally and diffed separately). Unified diff yields **11 hunks**, fully accounted:

| Hunk | Register item | Verified |
|---|---|---|
| Ch1 version-status | **D-1a (Ch1) + D-1f** | old spans 0×, new spans exact |
| Ch1 self-test paragraph | **D-1d + D-1e** | exact, including the disclosed original-clause preservation |
| Ch1 thesis sentence | **D-1b** | exact |
| Ch2 version-status | **D-1a (Ch2)** | exact ("all seven sections §§1–7" variant) |
| Ch7 T83 framing sentence | **D-6** | calibration clause present verbatim |
| Blank line before Ch8 heading | *build-layer fix #2* (disclosed in BUILD_CORRIGENDUM; content-neutral whitespace) | not a register hunk; disclosed |
| Ch15 companion note | **D-5** | demotion + future-work registration verbatim |
| Ch15 local reference list | **D-3b + D-4** | both bracketed v1.3 corrigenda present |
| Ch22 status head | **D-1c** | exact; history preserved |
| `\appendix` + `\setcounter{chapter}{3}` | *build-layer fix #3* (disclosed; appendix lettering D/E) | not a register hunk; disclosed |
| Trailing newline | trivial | — |

**No unregistered content hunk exists.** The two non-register hunks are the two deterministic build-layer transformations the packet's own BUILD_CORRIGENDUM disclosed in advance (an intrinsic artifact of reconstructing the canon from the *build source*, the only v1.3 substrate shipped); both are content-neutral. The Appendix E projection was diffed against the baseline canon-metadata header separately: **identical except the title line** — which produces finding **F-DP-01** below.

Wrap-immune quoted-literal probes across the whole corpus confirm every removed span is extinct (all seven D-1 old spans: baseline 1–2×, v1.3 **0×**) and every replacement span present at exactly the register-implied multiplicity (D-1a new text 2×, all others 1×).

---

## 4. L2 — register fidelity D-1..D-9 vs the v1.2 review findings

- **D-1 / P-1 (status currency)**: all six sub-items (a–f) byte-verified above. The ledger's residual claim — "Remaining pre-publication tokens (19) individually classified… retained" — **reconciles exactly**: the v1.3 canon body carries 22 `pre-publication` tokens, of which 3 sit *inside* the D-1d/D-1f replacement spans themselves, leaving **19** genuinely residual tokens, each doctrinal or past-tense on inspection. A precise, non-trivially-true producer count — verified, not credited.
- **D-2 / P-2a (Farrin)**: `farrin2010surat` now reads The Muslim World 100(1), 17–32, doi 10.1111/j.1478-1913.2009.01299.x, with the prior misattribution (Islamic Studies 49(1), 9–32) preserved verbatim in the correction note. Primary-verified in §5. `Islamic Studies` appears nowhere else in canon or renders (0×).
- **D-3/D-3b / P-2c (Sheshadri)**: bib entry carries the actual title, eprint 2506.18032, and the 7-name author list matching the arXiv record; bracketed corrigendum present at the quoted Munafiq-substrate reference-list locus with the descriptive substrate title preserved as quotation. Primary-verified in §5.
- **D-4 / P-2b (Boxo)**: bib entry was already correct (arXiv:2508.19505, correct authors); the in-canon bracketed corrigendum states the actual title and "reports accuracy, not AUROC, for the 70–80% open-source result". Primary-verified in §5. P-2d SMAA: STANDS-DISCLOSED, no change — consistent with zero SMAA-touching hunks in the delta.
- **D-5 / P-3 (taxonomy calibration)**: demotion text and future-work registration present verbatim (see L5, §6). Council-record quotations of the old term ("completeness treatment" in the Appendix E v1.2 note) untouched, as the register requires.
- **D-6 / P-4 (T83)**: calibration clause present verbatim at the Ch7 framing sentence; `PROVED-RELATIVE` label count in canon = **0**, matching the register's premise. Two fidelity observations: F-DP-02 (unpatched twin sentence) and F-DP-04 (ledger paraphrase) below.
- **D-7 / P-5 (metadata)**: the page-count correction ("372 pages, not 371 … producer-owned count miss") is recorded in the BUILD_CORRIGENDUM; DEPOSIT_METADATA carries the flagship DOI and deposit-day dating instruction ("do not pre-date").
- **D-8 / P-6 (peer-review labeling)**: subtitle in title metadata; extended author note with the "not an institutionally examined dissertation… not independent human peer review" statement present on PDF page 1, in HTML, in source line 1, and in the deposit description block.
- **D-9 (formatting ruling)**: fully verified under L4 above (324 pp, Latin Modern 10/12 metrics, letter, all-black sample, xelatex disclosed).

---

## 5. L3 — fact legs against primaries (fetched by this seat)

1. **Farrin.** [Crossref for doi 10.1111/j.1478-1913.2009.01299.x](https://api.crossref.org/works/10.1111/j.1478-1913.2009.01299.x) returns "Surat al‐Baqara: A Structural Analysis", *The Muslim World*, vol. 100, issue 1, pp. 17–32, 2010, author Farrin — and the [Wiley landing page](https://onlinelibrary.wiley.com/doi/10.1111/j.1478-1913.2009.01299.x) concurs (Raymond K. Farrin, The Muslim World 100, 17–32, 2010). **Matches D-2 exactly**; the v1.2 entry (Islamic Studies 49(1), 9–32) was indeed a misattribution.
2. **Sheshadri.** [arXiv:2506.18032](https://arxiv.org/abs/2506.18032) — actual title "Why Do Some Language Models Fake Alignment While Others Don't?", authors Abhay Sheshadri, John Hughes, Julian Michael, Alex Mallen, Arun Jose, Janus, Fabien Roger; abstract expands the alignment-faking analysis to **25 models**, finding **only 5** (Claude 3 Opus, Claude 3.5 Sonnet, Llama 3 405B, Grok 3, Gemini 2.0 Flash) with a training-vs-deployment compliance gap. **Matches the corrected bib entry (title, eprint, author list) and the "5 of 25 models" citation clause.**
3. **Boxo.** [arXiv:2508.19505](https://arxiv.org/abs/2508.19505) — actual title "Caught in the Act: a mechanistic approach to detecting deception", authors Gerard Boxo, Ryan Socha, Daniel Yoo, Shivam Raval. The abstract reports **accuracy — not AUROC**: probes on larger open-source models (>7B) reach **70–80% accuracy**, reasoning counterparts **exceed 90%**. **The D-4 corrigendum's central factual assertion ("reports accuracy, not AUROC, for the 70–80% open-source result") is primary-true**, and the substrate's original "AUROC" label was indeed the defect.
4. **Supplementary chain anchors (beyond the required three).** [Zenodo 10.5281/zenodo.21500700](https://doi.org/10.5281/zenodo.21500700) resolves to the flagship paper (Arfeen, v0.13) — confirming the reciprocal-identifier plan targets a real, live record; [Zenodo 10.5281/zenodo.21450932](https://doi.org/10.5281/zenodo.21450932) resolves to "Verify, Do Not Trust…" v1.1 — confirming the governing method's bibliographic identity. The method PDF's printed title-page DOI (…21449063) is the v1.0 sibling record — a **disclosed** record-side defect per the `arfeen2026shv` bib note ("the v1.1 PDF's printed title-page DOI is that v1.0 identifier — record-side defect pending source correction"); the packet copy's hash matches the brief's declared receipt, so the governing artifact itself is authentic.

---

## 6. L5 — calibration legs (applied precisely)

- **D-5 (REVERSIBLE-DEFAULT respected).** The v1.3 text claims a *completeness-boundary treatment* — "a non-exhaustiveness analysis with explicit boundary handling, not a proved exhaustive partition" — plus the future-work registration on Processes 3/4 boundary overlap, verbatim in source, PDF, and HTML. Per the brief, this seat's *view on the demotion* is registered as a finding, not as verdict grounds: **this seat's advisory view supports the demotion as substrate-faithful.** The flagship v0.6 council's non-exhaustiveness finding, the boundary-overlap admission for Processes 3/4, and the absence of any partition proof in Ch15 make "boundary treatment" the honest claim; reversal should require an actual mutual-exclusivity proof, not preference. (Registered as F-DP-06, ADVISORY-VIEW.)
- **D-6 (scope read strictly).** The T83 clause claims **finite judgment-set adequacy relative to the named set J only** — "principally author-selected and author-labeled, with several constructed scenarios — and not a claim of broad independent practitioner validation", with independent annotation of J registered as the successor test (AX-SH Case Benchmark). No PROVED-RELATIVE label exists anywhere in the canon (0×). The claim as calibrated is within-evidence.

---

## 7. Findings register (six-element format per SHV v1.1)

Element mapping used (per the method's D5/D8 and the ledger's Ch13/Ch18 six-element convention): **(1) ID + severity · (2) scale tag · (3) locus/byte anchor · (4) claim (surface vs substrate) · (5) evidence/witness · (6) disposition shape + disconfirming test.** Severities are UPPERCASE and denote adverse defect impact (Ruling 1); verified controls take CONTROL/LOW.

### Adverse findings

**F-DP-01 — MEDIUM** · scale: cross-document (canon body ↔ Appendix E projection) · locus: D-1a replacement spans (Ch1/Ch2 version-status, source L12/L165 region) and Abstract front matter vs Appendix E (source L5338–L5418; PDF p. ~317 ff.) · **claim**: the v1.3 repair text twice directs the reader to "the versioned public-deposit line **recorded in Appendix E**", and the front matter says version amendment notes are "preserved in Appendix E" — but the shipped Appendix E contains **zero v1.3 content** in both the source bytes and the rendered PDF (its version notes terminate at the v1.2 promotion-pass note; `v1.3` count in the Appendix E region = 0, wrap-normalized) · evidence: byte-region grep of source L5338–end (0 matches) and pdftotext of the Appendix E span (0 matches); Appendix E is byte-identical to the v1.2 canon-metadata header except its title line · **disposition Shape A recommended** (accept-and-fix: append the v1.3 deposit/amendment note to Appendix E at the next authorized build, or reword the pointer to "the audit ledger's v1.3 section") · disconfirming test: show any v1.3 deposit line inside Appendix E in the shipped v1.3 artifacts — this seat found none. *Note the reflexivity: a surface (the new status lines) asserting a substrate record (Appendix E entry) that does not exist is precisely the Axiom-4-class surface-substrate divergence this dissertation formalizes. The dangling reference was introduced by the D-1 repairs themselves, which is why it does not appear in the D-register and why delta-scoped re-attestation exists.*

**F-DP-02 — LOW** · scale: sentence (within-chapter parallel projection) · locus: Ch7, second T83 framing sentence (source L1412; §"Axiom 4 as closer of the four-axiom statement-level development") · claim: the D-6 calibration clause was appended to the *first* of two byte-identical T83 framing sentences in Ch7 (L1326, patched) but not the second (L1412, unpatched), leaving one uncalibrated "corresponds to what operational practitioners call structural honesty" statement · evidence: three corpus loci found by normalized probe; L1326 patched, L1412 bare, Ch8's discharge locus (L1472) carries its own "empirical-relative to a judgment-case set, not provable in a context-free sense" discipline · disposition Shape B acceptable (defer; register scope was the singular "the T83 framing sentence" and the load-bearing Ch8 discharge locus is calibrated) — Shape A (propagate the clause) preferred at next corrigendum · disconfirming test: a reading of L1412 as a mere requirement-restatement rather than an adequacy claim would lower this to nil-impact; this seat rates residual impact LOW either way.

**F-DP-03 — LOW** · scale: glyph (render layer) · locus: D-3b corrigendum, Ch15 local reference list, PDF render · claim: the Sheshadri corrigendum's opening quotation mark renders as a **closing**-quote glyph (`”Why do some…don't?”`) because the source uses backslash-escaped `\"` (bypassing smart-quote conversion), while the sibling D-4 Boxo corrigendum (plain quotes) renders correctly (`“Caught in the Act…”`) �� evidence: pdftotext byte comparison of both corrigenda spans · disposition Shape A (drop the escapes at next build); cosmetic, content-true · disconfirming test: none needed — the glyph asymmetry is directly observable.

**F-DP-04 — LOW** · scale: register-document fidelity · locus: audit ledger v1.3 section, D-6 entry · claim: the register head promises "every replaced span quoted", but the D-6 entry *paraphrases* rather than quotes — the actual canon clause contains "with several constructed scenarios", absent from the ledger's rendition · evidence: byte comparison of ledger D-6 text vs source L1326 · disposition Shape C-with-note acceptable (the paraphrase is semantically faithful and the added phrase is a further *concession*, not an overclaim); flagged because register-quotation discipline is itself a packet-stated control · disconfirming test: produce a ledger locus quoting the full clause — none exists in the packet.

### Capability gaps (declared, not adverse)

**F-DP-05 — UNKNOWN-BY-CAPABILITY** · the v1.3 `canon.md` (receipt `4467dd1e5e9cf069db85d98e12fb6b41d1c7f11d4961b248120b58c4c9a77ba8`) ships in neither the publication nor the trail set; byte-exact re-derivation of that hash is impossible from this packet. The canon delta was verified at **content level** via build-source reconstruction (§3), which is what L1 directs, but the canon-metadata header's own v1.3 state (e.g., whether a v1.3 amendment note exists there that the Appendix E projection dropped — the F-DP-01 mechanism) is unverifiable here. A seat or the lead holding `canon.md` should close this and adjudicate whether F-DP-01 is a projection gap (header updated, appendix not rebuilt) or a canon gap (no v1.3 note anywhere).

### Controls and verified repairs (CONTROL / LOW — never HIGH per Ruling 1)

- **F-DP-C1 (CONTROL)**: 13/13 manifest hashes re-derived and matching; verifier ALL PASS in both sets; trail DOCX matches the ledger receipt `e83ff142…`; refs.bib/PDF/HTML/source receipts in the ledger all match shipped bytes.
- **F-DP-C2 (CONTROL)**: L1 delta contains no unregistered content hunk; the only non-register hunks are the two pre-disclosed, content-neutral build-layer transformations.
- **F-DP-C3 (CONTROL)**: all three L3 primaries (Farrin/Wiley+Crossref, Sheshadri/arXiv, Boxo/arXiv) confirm the corrected entries; both Zenodo anchors resolve title-true.
- **F-DP-C4 (CONTROL)**: the "19 residual pre-publication tokens" producer claim independently reconciled (22 − 3 in-span = 19).
- **F-DP-C5 (CONTROL)**: STATUS-CURRENCY, META-TEXT-ABSENCE, chapter-identity 23+D/E, render parity, chromatic sample, and page-geometry gates all independently re-derived clean.
- **F-DP-06 (ADVISORY-VIEW, non-verdict)**: the D-5 demotion should stand unless a genuine mutual-exclusivity proof for the four predicates is produced (L5 discussion, §6).
- **Observation (custody)**: unmanifested sibling-seat files `diff.txt`/`diff_hunks.txt` in the packet root post-receipt; excluded from evidence.
- **Observation (LOW, dating)**: PDF title page reads "July 22, 2026" while the ledger v1.3 section and brief rev 2 are dated July 23; DEPOSIT_METADATA correctly instructs deposit-day publication dating, so no adverse impact — but the title-page date will be one day behind the deposit date if deposit occurs July 23.

---

## 8. Assessment — **NON-CARRYING / ADVISORY**

Working strictly from packet bytes and primaries: every register item D-1 through D-9 is **applied, span-faithful, and primary-true**; the L1 delta is exactly the register plus disclosed build-layer noise; all gates re-derive clean; no refuted finding is carried forward and none of this seat's findings rehabilitates any prior refuted claim. The surviving adverse findings are one MEDIUM (F-DP-01, a repair-introduced dangling cross-reference to a non-existent Appendix E v1.3 line — new-defect class, outside the D-register's discharge scope) and three LOWs; none falsifies a D-item disposition.

**Analytical assessment: PASS-DELTA, with F-DP-01 registered for corrigendum before or at deposit.** Under the packet's producer-lineage exclusion (Ruling 3) this assessment is **ADVISORY ONLY and carries no verdict**; convergence must come from two carrying seats of different non-Anthropic vendor families. This seat recommends carrying seats specifically re-test: (a) the Appendix E v1.3-absence probe (`v1.3` count in the Appendix E span — 30 seconds, decisive for F-DP-01), (b) the second T83 sentence at source L1412, and (c) the canon.md hash gap (F-DP-05), which only the lead can close.

*Method note (D8): every adverse finding above ships with its disconfirming test; every gap is marked UNKNOWN-BY-CAPABILITY rather than filled; probes were wrap-immune and quoted-literal throughout; replacement-span checks anchored on actual packet bytes at minimal unique spans.*

---

# Bismillah ir-Rahman ir-Rahim
