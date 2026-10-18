# Bismillah ir-Rahman ir-Rahim

# R0661 -- Seat Report — Claude Fable 5 (ADVISORY) — Narrow Re-Attestation, Structural Honesty Dissertation v1.3 → v1.4

**Chronological Index:** 273 of 995  
**Date:** 2026-07  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-claude_fable_5 (3).md  
**Source Format:** md  
**SHA-256:** `6a7608981ce4faf1dea1587e13eeb3d3b37388d04c56490dbcab5f2a144848a6`  

---

## R0661 · Seat Report — Claude Fable 5 (ADVISORY) — Narrow Re-Attestation, Structural Honesty Dissertation v1.3 → v1.4

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-claude_fable_5 (3).md
- source_format: md
- text_sha256: 6a7608981ce4faf1dea1587e13eeb3d3b37388d04c56490dbcab5f2a144848a6

# Seat Report — Claude Fable 5 (ADVISORY) — Narrow Re-Attestation, Structural Honesty Dissertation v1.3 → v1.4

**Round:** R2b-class narrow re-attestation, July 22–23, 2026 (brief dated July 23, 2026)
**Seat disclosure (per rev-2 rule as recovered from the in-packet round record):** Anthropic Claude-family seat, "Claude Fable 5" designation per brief; **ADVISORY tier** under Ruling 3 (Anthropic drafting-instrument producer lineage; Anthropic seats advisory). Executed independently inside Perplexity Computer model-council mode; no other seat's report was inspected or relied upon. **This seat's vote does not control convergence.** Convergence for this round = PASS-DELTA from both returning carrying seats (GPT 5.5, OpenAI; Gemini 3.1 Pro, Google) — named per the re-attestation plan in the ledger v1.4 section and the in-packet `DELTA_ATTESTATION_BRIEF_v1_4.md`.

**Finding namespace:** `F-DF-<NN>` (this seat).
**Instruments:** immutable audit packet at `attestation_brief/audit/` (byte-identical to `Dissertation_v1_4_audit_trail.zip`, SHA-256 `2a36201f81c898d6f8e3d09fb84c658bddccaff815b3946b9a9ffeabcf6947da`) and publication packet at `attestation_brief/publication/Dissertation_v1_4_PUBLICATION/` (byte-identical to `Dissertation_v1_4_PUBLICATION.zip`, SHA-256 `86bb2d791e1ef5697d617b793a8d99f85cbddb1eba7c7f77cb36522024e1a59f`; identity confirmed by extracting both zips and diffing per-file SHA-256 tables). No packet file was modified; all working artifacts live in `fable_work/`.

---

## 0. Prerequisite recovery and explicitly unavailable prerequisites

Recovered from in-packet evidence: the governing **ledger v1.4 section** (round record, adjudications, repair register R-1..R-6, receipts, re-attestation plan) — present **only in the publication packet's ledger** (`Structural_Honesty_Dissertation_audit_ledger.md`, lines 5630–5653, SHA-256 `cb7e498964a1fe5fae0791b586be2634147b50f5ea0630fad585b19c24aba566`); the v1.3 D-register section (both ledgers, line 5601 ff.); the delta brief; README; build corrigendum; deposit metadata; punch list.

Explicitly **unavailable** in-packet (identified, not assumed):
1. **The rev-2 brief itself** — its Section 1 convergence naming and its six-element finding-label schema do not ship in either packet. I therefore operationalized six labels (§4 below) and state them explicitly, as the brief permits.
2. **The v1.3 canon** (receipt `4467dd1e5e9c…` per the ledger v1.3 section) — not shipped; only `canon_v1_2_baseline.md` ships. Canon-side v1.3→v1.4 deltas were verified by composite bounding (v1.2 canon → v1.4 canon diff) plus byte-exact literal probes, not by a direct v1.3-canon diff (see F-DF-04).
3. Prior-round seat reports — not available and, per independence instruction, not sought.

---

## 1. L1' — Baseline/source hash verification and bounded diff

**Hashes (re-derived with `sha256sum`, both packets):**

| File | Re-derived SHA-256 | Expected | Match |
|---|---|---|---|
| `…v1_3_baseline_source.md` | `56178d29e01967e51aa4541a48fa737fc66438b170820a113299b7319945b8c5` | `56178d29…` (brief + ledger) | YES |
| `…v1_4_source.md` | `92ac1f1d88dc50c94d433a8b5e53e026260244e8710ce75ce5109421c5146e17` | `92ac1f1d…` (brief prefix; full value in ledger receipts) | YES |

**Command:** `diff -u Structural_Honesty_Dissertation_v1_3_baseline_source.md Structural_Honesty_Dissertation_v1_4_source.md` → **exactly 10 hunks**, at baseline lines 6, 134, 142, 163, 1409, 3163, 3562, 4253, 5288, 5337. Full mapping to the register as quoted in the ledger v1.4 section:

| Hunk (v1.3 line) | Register item | Content verified |
|---|---|---|
| @6 (front matter) | **R-1a** + R-4 (2 tokens) | `"Version 1.2 canonical"` → `"Version 1.4 canon"`; `(Arfeen 2026, forthcoming)` → `(Arfeen 2026, doi 10.5281/zenodo.21500700)`; Ch1 status v1.3→v1.4 |
| @134 | **R-4** (2 tokens) | "concluded at the v1.4 public deposit" / "satisfied at the v1.4 deposit" |
| @142 | **R-4** (1) | "(v1.4 working research monograph, July 2026)" |
| @163 | **R-4** (1) | Ch2 status v1.3→v1.4 |
| @1409 | **R-3** | calibration clause inserted at T83 locus 2 (byte-exact, §2) |
| @3163 | **R-1b** (1 of 2) | Ch15 companion note flagship ref → DOI |
| @3562 | **R-4** (2) + **R-5** | `[v1.3 corrigendum:` → `[v1.4 corrigendum:` ×2; literal `\"…\"` → typographic `“…”` at the D-3b bracket (hex-verified: `5C 22` bytes → `E2 80 9C / E2 80 9D`) |
| @4253 | **R-4** (1) | Ch22 status v1.3→v1.4 |
| @5288 | **R-1b** (2 of 2) | Appendix D flagship ref → DOI |
| @5337 | **R-2** | public-deposit record inserted at head of Appendix E |

**No hunk falls outside R-1a/R-1b/R-2/R-3/R-4/R-5.** Token accounting: baseline contained exactly **9** `v1.3` tokens (all producer v1.3-staging insertions per the D-register) — all swept, matching "R-4 (canon+body, 9 each)"; the canon likewise carries 9 swept `v1.4` version tokens. The only pre-existing `v1.4` literal in the baseline ("PMD v1.4 methodology codification", baseline line 4262, a methodology-document reference, not a dissertation-version token) is preserved untouched — the register's "no pre-v1.3 text contained the token" holds on the correct (dissertation-version-token) reading; see clarification note F-DF-05. The 2 `v1.3` tokens present in v1.4 source are both inside the new R-2 historical deposit record — legitimate history, not staleness. **L1': PASS.**

## 2. L2' — Per-finding discharge (byte-level, wrap-immune)

All literal gates were run byte-exact against source and canon, then wrap-immune (whitespace-normalized, tag-stripped, hyphenation-healed) against HTML, DOCX (`word/document.xml`), and PDF (`pdftotext`).

- **F-DO-01 / F-DG-08 → R-1a.** `"Version 1.2 canonical"` count: v1.3 baseline **1**; v1.4 source **0**, canon **0**, HTML **0**, DOCX **0**, PDF **0**. The producer's layering refinement verifies: `canon_v1_2_baseline.md` count **0** (the stale string was build-layer front matter only). **DISCHARGED.**
- **F-DP-01 / F-DO-02 → R-2.** The deposit record sits immediately under the body-layer heading `# Publication History and Version Amendments` (source line 5340; heading occurs in source **1×**, canon **0×** — bounding at the appendix heading confirmed, not at any front-matter mention). It enumerates v1.0 (superseded, never deposited), v1.2 (withheld), v1.3 (staging + NON-PASS round, not deposited), v1.4 (public-deposit version). Both Chapter 1/Chapter 2 pointers — "the versioned public-deposit line recorded in Appendix E" — occur exactly **2×** and the record's own parenthetical names them, so both resolve. Present 1× in HTML/DOCX/PDF (wrap-immune). **DISCHARGED.**
- **F-DG-10 → R-3.** The T83 framing phrase "corresponds to what operational practitioners call structural honesty" occurs exactly **3×** in source and canon (source lines 1326, 1412, 1472) — confirming the adjudication's "three loci, not two." Locus 1 (1326) carries the v1.3 D-6 span; locus 2 (1412) now carries the R-3 clause, byte-identical to the ledger quotation: "That correspondence is likewise evaluated as finite judgment-set adequacy relative to the named set $J$ (principally author-selected and author-labeled, with several constructed scenarios), not as broad independent practitioner validation." Locus 3 (1472) I verified myself, byte-identical to the ledger's quoted sentence ("T83's definitional-adequacy claim---…---is empirical-relative to a judgment-case set, not provable in a context-free sense.") — it is inline self-calibrating and needs no clause. HTML/DOCX show 3 loci; the PDF initially probed 2 because pdftotext interleaves a Chapter-7 running header ("CHAPTER 7. AXIOM 4 … 91") mid-word ("corre/sponds") at a page boundary — resolved by sub-phrase probes ("operational practitioners call" = 3×): all 3 loci present in the PDF; extraction artifact, not a defect. **DISCHARGED.**
- **F-DG-11.** The ledger v1.4 section's quoted APPLIED D-6 span — including "with several constructed scenarios" — matches the substrate **byte-for-byte** (Python `str.count` of the full 331-char literal: ledger 1, source 1, canon 1). **DISCHARGED.**
- **R-5 / R-6 (this seat's absorbed prior-round items).** R-5 hex-verified (above); zero `\"` residue in source/canon/HTML. R-6: PDF title page reads "July 23, 2026". Absorption of the Fable-5 advisory items (quote glyphs, canon shipped in-packet, title-page date) **CONFIRMED**.

## 3. L3' — Canon receipt and layering

`sha256sum` re-derivation: `Structural_Honesty_Dissertation_v1_4_canon.md` = `d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416` — matches the `d4f1da36…` prefix in the brief and the full ledger receipt, **identical in both packets**. The canon ships in-packet, discharging this seat's prior-round item.

**Layering note CONFIRMED structurally:** `diff -u canon.md source.md` = 25 hunks, all accounted for as (a) front-matter block (canon-only amendment notes at top vs body-only author note/abstract/companion line — the R-1a "Version 1.4 canon" string occurs **0×** in canon, 1× in body), (b) 23 deterministic chapter-heading transforms (`# === Chapter N: Title ===` → `# Title`), (c) the disclosed `\appendix`/`\setcounter{chapter}{3}` build insertion and the disclosed Chapter-8 blank-line normalization, and (d) body-only Appendix E (heading count: canon 0, source 1) carrying the R-2 record. Appendix E and front matter are body-layer, exactly as the ledger's layering clarification states. Composite bounding: `diff canon_v1_2_baseline.md v1_4_canon.md` = 10 hunks, all within D-register ∪ R-register loci. **L3': PASS** (with the v1.3-canon availability caveat in F-DF-04).

## 4. L4' — Verifier execution and manifest re-derivation

**Command/status:** `python3 verify_dissertation_v1_4.py` run inside byte-identical extractions of each kit:
- audit-trail kit: `VERIFIER: ALL PASS`, exit 0 — **control result only**: with no PDF member, the stale-version/forthcoming/propagation-count/deposit-record gates are skipped by construction (lines 14–40 of the verifier run only `if os.path.exists(pdf)`), leaving just manifest + author-note parity.
- publication kit: `VERIFIER: ALL PASS`, exit 0 — full gate set exercised against the PDF.

The four new gates are confirmed present in the shipped verifier source (lines 32–35: `"Version 1.2 canonical"`, `"(Arfeen 2026, forthcoming)"`, propagation count `== 2` of "finite judgment-set adequacy relative to the named set", deposit-record literals). I did **not** accept ALL PASS as absence evidence; every gated property was independently re-probed (§2).

**Manifests re-derived:** `sha256sum -c SHA256SUMS.txt` → all OK in both packets; independent per-file recomputation matches every manifest line. Render receipts vs ledger v1.4 receipts: PDF `cfe04c4de6fad5c0365ed9446c8c0aad0a16b8f4fd6ef70492522a212768877f` (324 pp confirmed) ✓; DOCX `da61eafc8682d69764faf89bc9e1efa27dcbb82c60780b74ebf7540905797883` ✓; HTML `b11114777f393617188c05d4c1bb4af9a5ef1b861020852ab24cc569db39c5d1` ✓; refs.bib `545e00bb58fa63146cb49b17cdd29667138502deb9145a496b5991e62ce165d4` unchanged ✓; v1.2 canon baseline `38dfa91d…` ✓.

**However, the mandated audit-vs-publication comparison surfaced three cross-packet divergences** (basis of F-DF-01):

| Member | Audit packet SHA-256 | Publication packet SHA-256 |
|---|---|---|
| audit ledger | `f7e539bb3733c128…` (1,261,500 B — **ends at line 5627; NO v1.4 section**) | `cb7e498964a1fe5f…` (1,267,019 B — v1.4 section at 5630–5653) |
| punch list | `c3ae1859e86329fd…` (no v1.4 STATE block) | `64aed7daf4a6805d…` (v1.4 STATE block present) |
| SHA256SUMS.txt | `6e9214c6ba212718…` (lists the stale hashes) | `b1c36f8ab685e0e9…` |

The audit ledger is an exact byte-prefix of the publication ledger (verified by `diff` on the first 1,261,500 bytes): the audit packet simply lacks the appended governing section.

## 5. L5' — R-1b and live Zenodo verification (Ruling 4: no absence-credit)

Per Ruling 4 the producer-registered R-1b repair was verified affirmatively, not credited. `"Arfeen 2026, forthcoming"`: baseline **3×** → v1.4 source/canon/HTML/DOCX/PDF **0×**. Flagship DOI `10.5281/zenodo.21500700`: source **4×** (front matter R-1a, Ch15 R-1b, Appendix D R-1b, Appendix E R-2), canon **2×** (the two R-1b canon loci — matching "canon+body, 2 each"), HTML/DOCX/PDF **4×** each.

**Live authoritative check:** the [Zenodo REST record for id 21500700](https://zenodo.org/api/records/21500700) (fetched July 22, 2026, HTTP 200) shows a **published** record: title *"Structural Honesty: Axioms for Detecting Surface-Substrate Divergence in AI Systems"* — byte-matching the flagship title quoted at all R-1b loci; creator Arfeen, Bilal Syed; DOI `10.5281/zenodo.21500700`; publication date 2026-07-22; version v0.13; files `Flagship_paper_v0_13.pdf`, `Flagship_v0_13_PUBLICATION.zip`, `Flagship_v0_13_audit_trail.zip`. The [DOI resolver](https://doi.org/10.5281/zenodo.21500700) returns HTTP 302 to `https://zenodo.org/doi/10.5281/zenodo.21500700`. The "forthcoming" → DOI repair is therefore factually warranted: the flagship is deposited and live. Observation for the record: the flagship record's `related_identifiers` is currently **empty** — the reciprocal `IsSupplementedBy` edit is (correctly) still pending this monograph's deposit, so the flagship's in-text companion-monograph language does not yet resolve archivally; this matches the plan and is not a finding. **L5': VERIFIED (no absence-credit taken or given).**

---

## 6. Findings (namespace F-DF-NN)

The rev-2 six-element labels are not recoverable in-packet (§0). I operationalized these six, chosen to preserve the evident intent of the inherited discipline (identifiability, byte-level locatability, expected-vs-actual separation, reproducibility, register traceability, and verdict impact): **(1) ID & severity; (2) Locus; (3) Expected (per governing register/gate); (4) Observed (substrate-actual); (5) Evidence & reproduction; (6) Disposition.**

### F-DF-01 — Audit-trail kit ships a pre-rebuild governance layer; the governing ledger v1.4 section is absent from the packet of record
1. **ID & severity:** F-DF-01, **HIGH** (auditability- and deposit-gating; not an R-register instrument defect).
2. **Locus:** `Dissertation_v1_4_audit_trail.zip` (SHA-256 `2a36201f…`) members `Structural_Honesty_Dissertation_audit_ledger.md`, `Structural_Honesty_Dissertation_punch_list.md`, `SHA256SUMS.txt`; identically the extracted immutable audit packet.
3. **Expected:** The brief declares "audit ledger v1.4 section governs"; the ledger's own process note states the crash-affected zips "were rebuilt"; both kit manifestations should carry the governing section.
4. **Observed:** The audit-packet ledger (`f7e539bb…`, 1,261,500 B) is an exact byte-prefix of the publication ledger (`cb7e4989…`, 1,267,019 B) ending at line 5627 — the **entire v1.4 section (round record, adjudications, R-register, receipts, re-attestation plan) is missing**. The punch list likewise lacks the "v1.4 STATE (July 23)" block. The audit kit's `SHA256SUMS.txt` was regenerated (00:52 timestamp, same as the rebuilt publication manifest) **against the stale members**, so the manifest self-verifies and masks the staleness. The producer assertion "the failed zips were rebuilt" is contradicted at the governance layer for one of the two kits.
5. **Evidence & reproduction:** `sha256sum` tables §4; `diff <(head -c 1261500 pub_ledger) audit_ledger` → empty (exact prefix); `unzip -l Dissertation_v1_4_audit_trail.zip` (ledger 1,261,500 B at 00:51, SHA256SUMS at 00:52); `sha256sum -c` OK in both kits.
6. **Disposition:** Blocking **for the deposit step this round authorizes**: `DEPOSIT_METADATA_v1_4.md` uploads exactly this audit-trail zip to Zenodo, and the deposit description's pointer "recorded in the accompanying audit ledger" would dangle — the public archival record would omit the very register being attested. Structurally this is a recurrence, at the kit-assembly layer, of the WL21 cross-artifact-propagation / per-fix-persistence class that produced the v1.3 NON-PASS, and a live instance of the ledger's own recorded lesson ("assembly must gate on governance-layer completion") failing to propagate into the artifact recording it — an Axiom-4-style projection inconsistency between the two kit projections of one governance substrate. Repair: rebuild the audit-trail zip with the current ledger + punch list, regenerate its manifest, re-receipt the zip hash in the ledger.

### F-DF-02 — Stale "version 1.3" in the Zenodo deposit description block
1. **ID & severity:** F-DF-02, **MEDIUM** (STATUS-CURRENCY class, pre-deposit surface).
2. **Locus:** `DEPOSIT_METADATA_v1_4.md` line 15 (identical bytes in both packets, SHA-256 `9af0f522…`).
3. **Expected:** R-4/R-6 discipline and the STATUS-CURRENCY standing gate (ledger v1.3 section) require zero stale current-status version claims on publication surfaces; the file's own Version field says v1.4.
4. **Observed:** The paste-whole-block description opens: `Status: working research monograph, version 1.3.` — the block Zenodo would publish states v1.3 while the record deposits v1.4.
5. **Evidence & reproduction:** `grep -n "version 1.3" DEPOSIT_METADATA_v1_4.md` → line 15; contrast line 11 (`**Version:** v1.4`) and line 19 ("the v1.4 revision applying…").
6. **Disposition:** Non-blocking for the R-register (the file is not a register locus), but blocking-for-deposit under the producer's own STATUS-CURRENCY gate; one-token repair. Note the R-4 sweep was scoped to canon+body only — this is exactly the adjacent-artifact residue class (WL22/WL21) the council flagged at v1.3.

### F-DF-03 — Verifier gate coverage is PDF-conditional; audit-kit ALL PASS is vacuous for the new gates
1. **ID & severity:** F-DF-03, **LOW** (gate-design observation; no false assertion in-packet — the round record itself treats ALL PASS as a control result).
2. **Locus:** `verify_dissertation_v1_4.py` (SHA-256 `7d2cde9b…`), lines 14–40.
3. **Expected:** The ledger receipts line says the verifier "gains stale-version, forthcoming-reference, propagation-count, and deposit-record" gates for the kit.
4. **Observed:** All four new gates execute only inside `if os.path.exists(pdf)`. In the audit-trail kit (no PDF member) the verifier prints `ALL PASS` after checking only manifest hashes and source/HTML author-note presence; none of the four advertised gates fire. The gates also scan only the PDF text layer — not source, canon, HTML, DOCX, or `DEPOSIT_METADATA_v1_4.md` (which is how F-DF-02 survives an ALL PASS).
5. **Evidence & reproduction:** Verifier source lines quoted §4; both executions recorded (`ALL PASS`, exit 0 each).
6. **Disposition:** Advisory. Recommend lifting the four literal gates to run against source+canon+metadata members whenever present, so the audit-kit invocation is non-vacuous.

### F-DF-04 — Unavailable prerequisite: v1.3 canon not in-packet; canon-side delta verified only by composite bounding
1. **ID & severity:** F-DF-04, **LOW** (disclosed verification-limit, per the brief's instruction to identify unavailable prerequisites).
2. **Locus:** Kit contents (both packets); ledger v1.3 receipts (`canon.md 4467dd1e…`).
3. **Expected:** L1'/L3' ideally verify the canon-side R-1b/R-3/R-4/R-5 deltas ("canon+body, N each") by direct diff of v1.3 canon → v1.4 canon.
4. **Observed:** Only `canon_v1_2_baseline.md` (38dfa91d…) ships. Canon-side repairs were instead verified by (a) `diff canon_v1_2 → canon_v1_4` = 10 hunks, all within D∪R register loci; (b) byte-exact literal probes for every R-item in the canon; (c) token counts matching the register's per-layer counts (9 R-4 tokens, 2 R-1b DOIs, 1 R-3 clause, 0 backslash-quote residues).
5. **Evidence & reproduction:** `fable_work/canon12_vs_canon14.txt`; probe outputs §§1–3.
6. **Disposition:** No defect asserted; residual risk is negligible given the composite bound plus receipts, but a future kit should ship the immediately-prior canon for R2b-class rounds.

### F-DF-05 — Clarifying note on the R-4 register phrasing (no defect)
1. **ID & severity:** F-DF-05, **NOTE**.
2. **Locus:** Ledger v1.4 section, R-4 entry ("no pre-v1.3 text contained the token").
3. **Expected/Observed:** Read literally against the token "v1.4", pre-v1.3 text does contain one instance ("PMD v1.4 methodology codification", baseline line 4262 — a methodology-document version, canon line 4333). Read as intended (the swept dissertation-version token "v1.3"), the claim verifies exactly: baseline carried 9 `v1.3` tokens, all v1.3-staging insertions, all swept; the pre-existing "PMD v1.4" literal was correctly left untouched by the sweep.
4. **Evidence:** `grep -c/-n "v1\.3" / "v1\.4"` outputs §1.
5–6. **Disposition:** No repair needed; suggest the next ledger increment disambiguate "the token" to avoid a false-positive audit trip on the PMD reference.

---

## 7. Advisory verdict and its relation to convergence

**Per-item scope result:** every item of the bounded R-register **VERIFIED-DISCHARGED on the instrument** — L1' diff exactly R-1a/R-1b/R-2/R-3/R-4/R-5 with zero out-of-register hunks; L2' all four finding-discharge gates pass byte-exact and wrap-immune across source, canon, HTML, DOCX, PDF; L3' canon receipt re-derived `d4f1da36…` with the layering note confirmed; L4' verifier ALL PASS (exit 0) in both kits with all listed hashes recomputed; L5' the R-1b repair verified against the live Zenodo record with no absence-credit taken (Ruling 4).

**Seat ruling: NON-PASS (ADVISORY).** The ruling does not attach to the R-register instrument, which this seat found clean; it attaches to what this round's convergence would authorize. Deposit follows convergence, and the deposit as currently staged would (a) upload an audit-trail zip whose ledger **omits the governing v1.4 section** while carrying a self-consistent manifest that masks the omission (F-DF-01, HIGH), and (b) publish a Zenodo description asserting "version 1.3" (F-DF-02, MEDIUM) — both recurrences of the status-currency / cross-artifact-propagation class that produced the v1.3 NON-PASS, now one layer up at kit assembly. Under the dissertation's own standing gates (STATUS-CURRENCY; the per-fix-persistence lesson recorded in the very section that failed to ship), this seat cannot advise that the corrected instrument's packet-of-record is deposit-ready.

**Distinction from convergence:** Convergence is determined solely by PASS-DELTA from the two carrying seats (GPT 5.5, Gemini 3.1 Pro) on the bounded R-register. A carrying seat confining itself strictly to the six register items on the source/canon/render layers could defensibly return PASS-DELTA; this advisory NON-PASS is non-controlling and is routed to the lead as a pre-deposit condition set: (1) rebuild `Dissertation_v1_4_audit_trail.zip` with the current ledger and punch list and re-receipt it; (2) correct the deposit-description version token; (3) optionally harden the verifier per F-DF-03. All three are mechanical; none touches canon or body, so no new attestation round on the R-register would be triggered by their application.

**Auditability:** every command, hash, count, and literal above is reproducible from the two packets alone plus the two cited live URLs ([Zenodo API record 21500700](https://zenodo.org/api/records/21500700); [DOI resolver](https://doi.org/10.5281/zenodo.21500700)). Working artifacts: `fable_work/source_diff.txt`, `fable_work/canon_vs_body.txt`, `fable_work/canon12_vs_canon14.txt`, `fable_work/pdf.txt`, extraction trees `fable_work/z_audit/`, `fable_work/z_pub/`.

---

# Bismillah ir-Rahman ir-Rahim
