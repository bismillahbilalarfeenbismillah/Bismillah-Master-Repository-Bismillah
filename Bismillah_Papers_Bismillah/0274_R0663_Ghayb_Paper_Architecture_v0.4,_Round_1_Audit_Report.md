# Bismillah ir-Rahman ir-Rahim

# R0663 -- Ghayb Paper Architecture v0.4, Round 1 Audit Report

**Chronological Index:** 274 of 995  
**Date:** 2026-07  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-claude_fable_5 (5).md  
**Source Format:** md  
**SHA-256:** `41fcb597b4cb55781d67e6c3a61f8f7da05abb9c6e505c5124d91c0c7e7a7431`  

---

## R0663 · Ghayb Paper Architecture v0.4, Round 1 Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-claude_fable_5 (5).md
- source_format: md
- text_sha256: 41fcb597b4cb55781d67e6c3a61f8f7da05abb9c6e505c5124d91c0c7e7a7431

# Ghayb Paper Architecture v0.4, Round 1 Audit Report

## Seat declaration

- **Model:** Claude Fable 5
- **Vendor:** Anthropic
- **Tier:** highest/frontier
- **Role:** ADVISORY ONLY, NON-CARRYING DUE TO PRODUCER LINEAGE

**Namespace mapping, stated once.** Finding IDs in this report use the namespace **F-TP-NN**. Under the dispatch namespace rule, seat prefixes are assigned by vendor initial across the buckets G/O/K/X/P, and Anthropic has no dedicated initial in that scheme; it therefore maps to **P, the specified other/native bucket**, yielding the prefix F-TP. This mapping is declared here and used for every finding below. The F-TP namespace is distinct from the artifact's own falsification tests F-1 through F-8, which are always referenced with the qualifier "artifact F-n".

**Competence boundary.** This seat is not qualified to adjudicate theological soundness and issues no Islamic doctrinal ruling anywhere in this report. The audit covers only: citation existence, fidelity, and use; defensibility of translations and terminology; internal consistency; novelty; guard integrity; lint; and survival of the artifact's own stated falsification tests. Every attestation herein is structural and evidentiary only and cannot be represented as theological validation. Formal review by an ijazah-qualified scholar remains mandatory and is not substituted by anything in this document.

**Producer expectation, declared as bias to work against.** Dispatch section 7 records the producer's expectations: at least one misattributed citation, contribution 6 as the most F-5-vulnerable, at least one novelty precedent, and no guard failure (which the producer flags as the most consequential possible finding). This seat treated those expectations as priors to be tested, not confirmed, and notes below where the evidence diverged from them.

---

## 0. Intake and method

**Packet:** `/home/user/workspace/GHAYB_v0_4_AUDIT_PACKET/` (not modified at any point).

Checksums were recomputed at intake and again immediately before this report was written; all three files verify against `SHA256SUMS.txt`:

| File | Verification |
|---|---|
| GHAYB_ARCHITECTURE_v0_4.md | OK (sha256sum -c) |
| GHAYB_DISPATCH_BRIEF_R1.md | OK (sha256sum -c) |
| SHV_Method_v1_1.pdf | OK (sha256sum -c) |
| SHA256SUMS.txt (self) | f007db418edc7e4b718ddcddcb9011be9baf8acda6b4a76f8405f20fe22a55ec |

**Artifact:** "Inheritance, Transmission, and the Locus of Accountability: An Islamic Theological Account of Formed Agents, with Application to AI Safety", Bilal Syed Arfeen (BayyinahEnterprise), July 2026; 494 lines; read in full. Dispatch brief read in full. SHV Method v1.1 PDF read; its producer note states lead analytical synthesis by Claude (Anthropic), which confirms the producer-lineage conflict and this seat's NON-CARRYING status.

**Evidence discipline.** Recall is not evidence. Every verse was fetched from the AlQuran Cloud API in three editions (Uthmani Arabic, Saheeh International, transliteration), pattern `https://api.alquran.cloud/v1/ayah/{ref}/editions/quran-uthmani,en.sahih,en.transliteration`, with per-verse JSON preserved at `/home/user/workspace/ghayb_audit/ayah_*.json` and a consolidated dump at `verses_dump.txt`. Hadith texts and grades were fetched from sunnah.com pages cited inline. Lexical evidence was fetched from corpus.quran.com and tafsir collections cited inline. Anything not fetched is marked UNKNOWN-BY-METHOD. Line numbers ("L n") refer to the artifact source file.

---

## Leg L1. Citation existence, fidelity, and use

### L1.1 Complete Quranic citation ledger

Independent enumeration of the artifact found **exactly 28 unique verse references**. Every reference was fetched and verified. One reference listed in the dispatch brief's illustrative list, 59:16, does **not** appear in the artifact; see F-TP-06.

Fidelity codes: EXISTS = verse exists at cited location; RENDER = artifact's rendering is defensible against the fetched Saheeh International text; TRANSLIT = transliteration matches the fetched transliteration edition where the artifact gives one.

| # | Ref | Artifact locus | Use in argument | EXISTS | RENDER | TRANSLIT | Source | Disposition |
|---|---|---|---|---|---|---|---|---|
| 1 | 51:56 | L68 | Two responsible creations premise | Yes | Yes, with note | n.a. | [api.alquran.cloud 51:56](https://api.alquran.cloud/v1/ayah/51:56/editions/quran-uthmani,en.sahih,en.transliteration) | LOW note, F-TP-05 |
| 2 | 30:30 | L102-108 | Fitrah, created default | Yes | Yes | Match | [api.alquran.cloud 30:30](https://api.alquran.cloud/v1/ayah/30:30/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 3 | 53:38 | L109 | No bearer bears another's burden | Yes | Yes | Match | [api.alquran.cloud 53:38](https://api.alquran.cloud/v1/ayah/53:38/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 4 | 17:15 | L114 | No punishment before a messenger | Yes | Yes | Match | [api.alquran.cloud 17:15](https://api.alquran.cloud/v1/ayah/17:15/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 5 | 16:25 | L123 | Transmitter bears added burdens | Yes | Yes | **Mismatch** | [api.alquran.cloud 16:25](https://api.alquran.cloud/v1/ayah/16:25/editions/quran-uthmani,en.sahih,en.transliteration) | LOW, F-TP-03 |
| 6 | 6:112 | L135-137 | Ornamented speech mechanism | Yes | Yes | Match | [api.alquran.cloud 6:112](https://api.alquran.cloud/v1/ayah/6:112/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 7 | 6:128 | L139 | Mutual benefit concession | Yes | Yes | Match | [api.alquran.cloud 6:128](https://api.alquran.cloud/v1/ayah/6:128/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 8 | 72:6 | L141-142 | Initiating party increased in rahaq | Yes | **Contested reading stated as settled** | Match | [api.alquran.cloud 72:6](https://api.alquran.cloud/v1/ayah/72:6/editions/quran-uthmani,en.sahih,en.transliteration); [quranx.com tafsirs 72:6](https://quranx.com/tafsirs/72.6) | HIGH, F-TP-01 |
| 9 | 4:76 | L145 | Kayd of the tempter is weak | Yes | Yes | Match | [api.alquran.cloud 4:76](https://api.alquran.cloud/v1/ayah/4:76/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 10 | 16:99-100 | L146 | Authority only over allies | Yes | Yes | n.a. | [api.alquran.cloud 16:99](https://api.alquran.cloud/v1/ayah/16:99/editions/quran-uthmani,en.sahih,en.transliteration); [api.alquran.cloud 16:100](https://api.alquran.cloud/v1/ayah/16:100/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 11 | 14:22 | L148-149 | Sultan denied, blame yourselves | Yes | Yes | Match | [api.alquran.cloud 14:22](https://api.alquran.cloud/v1/ayah/14:22/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 12 | 2:31 | L162 | Adam taught the names | Yes | Yes | Match | [api.alquran.cloud 2:31](https://api.alquran.cloud/v1/ayah/2:31/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 13 | 2:37 | L164, L277 | Remedy itself taught | Yes | Yes | Match | [api.alquran.cloud 2:37](https://api.alquran.cloud/v1/ayah/2:37/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 14 | 7:12 | L165, L389 | "I am better than him" refusal | Yes | Yes | Match | [api.alquran.cloud 7:12](https://api.alquran.cloud/v1/ayah/7:12/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 15 | 19:42 | L178-179 | Abraham against inherited practice | Yes | **Rendering imports "carved" not in verse** | n.a. | [api.alquran.cloud 19:42](https://api.alquran.cloud/v1/ayah/19:42/editions/quran-uthmani,en.sahih,en.transliteration) | LOW, F-TP-04 |
| 16 | 20:39 | L179-180 | "Formed under My eye" | Yes | Yes | Match | [api.alquran.cloud 20:39](https://api.alquran.cloud/v1/ayah/20:39/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 17 | 66:11 | L180 | Pharaoh's wife breaks upward | Yes | Yes | n.a. | [api.alquran.cloud 66:11](https://api.alquran.cloud/v1/ayah/66:11/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 18 | 11:46 | L181 | Noah's son breaks downward | Yes | Yes | Match | [api.alquran.cloud 11:46](https://api.alquran.cloud/v1/ayah/11:46/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 19 | 28:56 | L184-185 | Guard against self-verified election | Yes | Yes | n.a. | [api.alquran.cloud 28:56](https://api.alquran.cloud/v1/ayah/28:56/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 20 | 53:32 | L185 | "Do not claim purity" | Yes | Yes | Match | [api.alquran.cloud 53:32](https://api.alquran.cloud/v1/ayah/53:32/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 21 | 1:6 | L186 | Present-tense petition for guidance | Yes | Yes | Match | [api.alquran.cloud 1:6](https://api.alquran.cloud/v1/ayah/1:6/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 22 | 39:53 | L282 | Door open to those deep in it | Yes | Yes | Match | [api.alquran.cloud 39:53](https://api.alquran.cloud/v1/ayah/39:53/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 23 | 25:70 | L305 | Evil deeds replaced with good | Yes | Yes | Match | [api.alquran.cloud 25:70](https://api.alquran.cloud/v1/ayah/25:70/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 24 | 2:222 | L309 | Intensive form at-tawwabin | Yes | Yes | Match | [api.alquran.cloud 2:222](https://api.alquran.cloud/v1/ayah/2:222/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 25 | 20:82 | L310 | "Thumma ihtada" continuation | Yes | Yes | Match | [api.alquran.cloud 20:82](https://api.alquran.cloud/v1/ayah/20:82/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 26 | 4:17-18 | L319 | Excludes deathbed persistence | Yes | Yes | n.a. | [api.alquran.cloud 4:17](https://api.alquran.cloud/v1/ayah/4:17/editions/quran-uthmani,en.sahih,en.transliteration); [api.alquran.cloud 4:18](https://api.alquran.cloud/v1/ayah/4:18/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |
| 27 | 66:8 | L477 (terminology table only) | Tawbah nasuh command | Yes | Yes | n.a. | [api.alquran.cloud 66:8](https://api.alquran.cloud/v1/ayah/66:8/editions/quran-uthmani,en.sahih,en.transliteration) | LOW, part of F-TP-15 |
| 28 | 28:78 | L392-393 | Qarun's capability-as-entitlement | Yes | Yes | Match | [api.alquran.cloud 28:78](https://api.alquran.cloud/v1/ayah/28:78/editions/quran-uthmani,en.sahih,en.transliteration) | CONTROL |

**Headline L1 results.**

1. **No fabricated or misattributed scripture was found.** All 28 references exist at their cited locations, and 26 of 28 renderings are fully faithful to the fetched Saheeh International text. The producer expected at least one misattributed citation; on existence and attribution the artifact outperformed its producer's own prior. Nothing in L1 reaches CRITICAL.
2. **The single largest L1 problem is not existence but interpretive settlement.** At L141-142 the artifact asserts flatly that at 72:6 "the party who initiated is the party increased in burden (rahaq)". The fetched verse text is genuinely ambiguous as to referent ("men from mankind who sought refuge in men from the jinn, so they [only] increased them in burden", [api.alquran.cloud 72:6](https://api.alquran.cloud/v1/ayah/72:6/editions/quran-uthmani,en.sahih,en.transliteration)). The fetched tafsir collection shows a real classical split: Ibn Kathir reads the jinn as increasing the humans in fear and sin, which supports the artifact, while Ibn Abbas, Al-Jalalayn, and Maududi read the humans as increasing the jinn in arrogance and audacity, which inverts the artifact's proposition ([quranx.com tafsirs 72:6](https://quranx.com/tafsirs/72.6)). The proposition is load-bearing for Part III's symmetry argument and for C-2. Presenting a contested reading as settled, without acknowledging the split, is the kind of overreach the artifact's own Section 6 review posture exists to catch, but Section 6 (L438) does not list 72:6 among items needing scholar review. See F-TP-01 (HIGH).
3. **Transliteration check:** one error. L123 gives "yudilluahum"; the fetched transliteration edition reads "yudilloonahum" for يُضِلُّونَهُم ([api.alquran.cloud 16:25](https://api.alquran.cloud/v1/ayah/16:25/editions/quran-uthmani,en.sahih,en.transliteration)). Cosmetic, but in a paper whose whole posture is transmission fidelity, a corrupted transliteration is an unfortunate self-instance. See F-TP-03 (LOW).
4. **Brief over-inclusion.** 59:16 appears in the dispatch brief's illustrative verse list but nowhere in the artifact (confirmed by exhaustive grep enumeration; the fetched verse at [api.alquran.cloud 59:16](https://api.alquran.cloud/v1/ayah/59:16/editions/quran-uthmani,en.sahih,en.transliteration) concerns the tempter's disavowal and would in fact have been on-theme). This is a defect in the audit apparatus, not the artifact, and demonstrates why each seat must enumerate independently rather than trust the brief. See F-TP-06 (NOTE, disposition LOW).

### L1.2 Hadith ledger

The artifact cites four prophetic reports, none with collection, number, or grade. All four were located and fetched; all four are real and correctly used.

| Report | Artifact locus | Identified source | Narrator | Grade (as fetched) | Fidelity | Source |
|---|---|---|---|---|---|---|
| "The pen is lifted from three" | L100-101 | Sunan Abi Dawud 4403 | Ali ibn Abi Talib | Sahih (Al-Albani) | Accurate; "the child until maturity (bulugh)" matches the fetched wording of the three categories | [sunnah.com/abudawud:4403](https://sunnah.com/abudawud:4403) |
| Fitrah and the unmutilated animal | L102-107 | Sahih al-Bukhari 1358 (also 1359) | Abu Huraira | Sahih (Bukhari) | Accurate; the artifact's grammatical-subject claim (the parents are the active verbs: yuhawwidanihi, yunassiranihi, yumajjisanihi) is verified against the fetched Arabic | [sunnah.com/bukhari:1358](https://sunnah.com/bukhari:1358); [sunnah.com/bukhari:1359](https://sunnah.com/bukhari:1359) |
| Instituted practice, reward without deduction | L124-126 | Sahih Muslim 1017 | Jarir ibn Abdullah | Sahih (Muslim) | Accurate in both halves, including "without any deduction" | [sunnah.com/muslim:1017](https://sunnah.com/muslim:1017) |
| Repentance accepted until the death rattle | L318-319 | Jami at-Tirmidhi 3537 | Ibn Umar | Hasan (Darussalam); Tirmidhi's own remark hasan gharib | Accurate; "ma lam yugharghir" matches the fetched Arabic ما لَمْ يُغَرْغِرْ | [sunnah.com/tirmidhi:3537](https://sunnah.com/tirmidhi:3537) |

**L1.2 finding.** The uniform omission of collection, number, and grade is a real citation-hygiene defect: a reader cannot verify any of the four reports from the artifact alone, and the fourth report is hasan rather than sahih, a grading distinction the artifact never surfaces even though that report carries the time-bound urgency claim of section 27. Partially mitigated: Section 6 (L435-446) already routes the paper to ijazah-qualified review. See F-TP-02 (MEDIUM).

---

## Leg L2. Terminology and translation defensibility

### L2.1 Bare-Arabic convention gate

The artifact's stated convention is that no Arabic term appears in prose without an English gloss at first use. A manual scan of all 452 body lines found **no violations**: every Arabic term in prose is glossed at or before first use. CONTROL.

### L2.2 Key contested terms, fetched evidence

- **sultan (14:22).** The word-by-word corpus glosses the token as "authority" ([corpus.quran.com 14:22](https://corpus.quran.com/wordbyword.jsp?chapter=14&verse=22)). The fetched tafsirs converge: Al-Jalalayn glosses "warrant", with no power or capacity to compel; Ibn Kathir "no proof nor evidence"; Ibn Abbas "proof, reason or power" ([quranx.com tafsirs 14:22](https://quranx.com/tafsirs/14.22)). The artifact's rendering "authority, standing to compel" (L149, table L470) is strongly defensible. CONTROL.
- **kayd (4:76).** The corpus dictionary gives the root k-y-d as "to scheme, plot, plan" and glosses the token at 4:76 as "the strategy" ([corpus.quran.com root kyd](https://corpus.quran.com/qurandictionary.jsp?q=kyd)). The artifact's "plot, stratagem" (L145, table L471) is defensible. CONTROL.
- **zukhruf al-qawl (6:112).** The corpus glosses the token as "decorative" with the root sense of ornament and gold ([corpus.quran.com root zxrf](https://corpus.quran.com/qurandictionary.jsp?q=zxrf)). "Ornamented speech" (L137, table L468) is defensible, and the artifact's point that the named mechanism is speech, not sorcery, is supported by the fetched verse text itself ([api.alquran.cloud 6:112](https://api.alquran.cloud/v1/ayah/6:112/editions/quran-uthmani,en.sahih,en.transliteration)). CONTROL.
- **fitrah (30:30).** The corpus gives the noun gloss "Nature" and the root f-t-r sense of creating and originating ([corpus.quran.com root fTr](https://corpus.quran.com/qurandictionary.jsp?q=fTr)). "Created default, not a blank slate" (table L461) is defensible and is independently backed by the fetched Bukhari 1358 text ([sunnah.com/bukhari:1358](https://sunnah.com/bukhari:1358)). CONTROL.
- **radd al-mazalim and the four conditions of repentance (L289, table L478-481).** The four conditions as stated in the artifact (desisting, regret, resolve not to return, restoration where others' rights are touched) match the fetched juristic summary: "Giving up the sin immediately; Regretting; Resolving not to go back; Making amends to those whom you have wronged" ([islamqa.info answer 13990](https://islamqa.info/en/answers/13990)). The artifact's own extension of the fourth condition to the transmitter case is flagged by the artifact itself as requiring scholar review (L438-446). Per the competence boundary, this seat assesses sourcing and defensibility only and issues no ruling on repentance doctrine: sourcing is CONTROL, the extension remains an open scholar-review item, correctly self-flagged.

Failed fetch disclosure: two attempted supplementary fetches did not contain the sought content (sunnah.com Riyad as-Salihin front pages lacked the Nawawi introduction; two corpus dictionary query spellings for sultan redirected to an unrelated entry). Nothing above rests on those pages.

### L2.3 Terminology ledger, all 38 rows

The appendix table (L455-494) contains 38 rows. Each row was checked for (a) defensibility of the English rendering and (b) anchoring, meaning the term actually appears in body prose (L1-452).

| Row (Arabic) | Rendering defensible | Anchored in body | Note |
|---|---|---|---|
| mukallaf | Yes | Yes (L38 area, 1 hit) | Standard usage |
| taklif | Yes | Yes (2 hits) | Standard |
| jinn | Yes ("the concealed ones", root sense) | Yes (5 hits) | Root gloss consistent with corpus root j-n-n |
| al-ins | Yes | Yes (2 hits) | |
| fitrah | Yes | Yes | Verified above, CONTROL |
| bulugh | Yes | Yes | Matches Abi Dawud 4403 category |
| 'aql | Yes | Yes | |
| hujjah | Yes | Yes | |
| ahl al-fatrah | Yes | Yes (2 hits) | |
| wizr / awzar | Yes | Yes (2 hits each) | Matches 16:25 and 53:38 fetched texts |
| al-'adl | Yes | Yes | |
| zukhruf al-qawl | Yes | Yes | Verified above, CONTROL |
| ghurur | Yes | Yes | Matches 6:112 fetched text |
| sultan | Yes | Yes (2 hits) | Verified above, CONTROL |
| kayd | Yes | Yes | Verified above, CONTROL |
| wali (plural awliya) | Yes | Partial: singular appears once (L146); plural awliya appears only in the table | Part of F-TP-15 |
| rahaq | Rendering "burden, oppression" defensible; the table note "what accrues to the one who sought the partnership, 72:6" restates the contested reading | Yes (2 hits) | Inherits F-TP-01 |
| hidayah | Yes | Yes | |
| tawbah | Yes | Yes | |
| at-tawwabin | Yes, intensive form claim matches 2:222 fetched text | Yes | |
| tawbah nasuh | Yes | **No body hit** | Orphaned; 66:8 cited only here. F-TP-15 |
| iqla' | Yes | Yes | Condition 1, matches islamqa source |
| nadam | Yes | Yes | Condition 2 |
| 'azm 'ala 'adam al-'awd | Yes | Yes | Condition 3 |
| radd al-mazalim | Yes | Yes | Condition 4, verified above |
| thumma ihtada | Yes | Yes | Matches 20:82 fetched text |
| muraqabah | Yes | **No body hit** | Orphaned. F-TP-15 |
| ghayb | Yes | **No body hit** | Orphaned; see note below. F-TP-15 |
| nifaq | Yes | **No body hit** | Orphaned. F-TP-15 |
| munafiq | Yes | **No body hit** | Orphaned. F-TP-15 |
| khatm | Yes | **No body hit** | Orphaned. F-TP-15 |
| waswasah | Yes | **No body hit** | Orphaned; also tension with L137, see F-TP-16 |
| sihr | Yes | Yes | Negative claim consistent with 6:112 |
| 'alim | Yes | Yes | |
| ijazah | Yes | Yes | |
| usul al-fiqh | Yes | Yes | Note references artifact F-1, coherent |
| qarin | Yes | **No body hit** | Table note says "retained only where the predecessor is discussed", but no such discussion exists in this artifact. F-TP-15 |
| Qarun | Yes | Yes (L392) | |

**L2.3 findings.** Eight of 38 rows (tawbah nasuh, muraqabah, ghayb, nifaq, munafiq, khatm, waswasah, qarin) have no anchor anywhere in body prose, plus the plural awliya is table-only. Two aggravating details: (a) the working title of the program is the Ghayb Paper, and the term ghayb itself never occurs in the paper's body; (b) the qarin row's own note promises a discussion that does not exist in this artifact, making it a dangling self-reference of the same family as F-TP-07. One verse, 66:8, enters the paper only through an orphaned table row. See F-TP-15 (MEDIUM) and F-TP-16 (LOW: the waswasah row calls whispering "the tempter's established mechanism" while L137 says "the named mechanism is ornamented speech", an unresolved surface tension between table and body).

---

## Leg L3. Internal consistency and C-claim support

### L3.1 C-claim support map

| Claim | Stated at | Supported by | Support status |
|---|---|---|---|
| C-1 three-level structure | L38-40 | Part II (L96-131): fitrah, pen-lifted, hujjah, 53:38 vs 16:25 | Supported by verified citations; final standing contingent on scholar review the artifact itself mandates (L435-446) |
| C-2 symmetric blame, asymmetric mechanism | L41-45 | Part III (L133-158): 6:112, 6:128, 72:6, 4:76, 16:99-100, 14:22 | Supported EXCEPT the 72:6 leg, which rests on a contested reading (F-TP-01). The mechanism-asymmetry half stands on 14:22 and 4:76 independently |
| C-3 refusal of lineage determinism | L46-48 | Part IV (L159-188): 2:31, 2:37, 7:12, 19:42, 20:39, 66:11, 11:46, 28:56, 53:32, 1:6 | Supported; all ten citations verified |
| C-4 LLMs satisfy level one and level three | L49-52 | Part V (L190-227), incl. METR reference at L209 | Structurally supported; empirical premises are the artifact's own to defend |
| C-5 propagation measurable after marking precondition | L53-56 | Part VI (L229-260) | Supported as a conditional claim; the precondition framing is consistent |
| C-6 remedy invariant under unreadability | L57-63 | Part VII (L262-345), esp. s26-s29 | Partially supported; see F-TP-08 |

### L3.2 Consistency findings

1. **Dangling internal references (HIGH, F-TP-07).** Contribution 5 (L397-399) invokes "the seven-stage progression" with concealment as stage four and stages one through three visible in traces. No seven-stage progression is defined anywhere in the 494-line artifact. Contribution 3 (L393) invokes "the July 2026 evaluation-escape" as "the exact failure" the Qarun signature instantiates. No such incident is described, dated, or cited anywhere in the artifact. Both references presumably point at the predecessor draft, which is excluded from the packet by design. As the artifact stands, two of its seven named novel contributions rest on referents a reader cannot resolve. This is the same defect class the qarin table row exhibits.
2. **C-6 invariance conflation (MEDIUM, F-TP-08).** C-6 claims the remedy is "invariant under the unreadability of the formation chain". That holds for upstream unreadability: forward indexation (s28 property 1, L328-330) genuinely needs no causal history. It does not hold for the downstream side that property 2 (L331-332, "the remedy must reach the continuation") makes constitutive of the remedy: reaching the continuation is hostage to exactly the unmarked propagation the paper diagnoses. Section 29 (L341-345) partially concedes this ("does not make an unmarked corpus auditable after the fact") without withdrawing the invariance wording of C-6. The claim as worded is stronger than what Part VII delivers; "invariant under upstream unreadability, constrained by downstream unmarkedness" is what the text actually establishes.
3. **Substrate-generality tension (MEDIUM, F-TP-09).** L68 fixes exactly two responsible creations (51:56); L92-94 asserts "the reasoning is already substrate-general, which is the property the transfer requires". These are reconcilable (the taklif boundary is species-fixed while the formed-agent structure generalizes), and section 2 (L65-83) plus artifact F-4 show the author intends exactly that reconciliation, but the artifact never states it in one place. The unstated reconciliation is also what keeps the jinn-as-AI guard honest, so the gap feeds F-TP-14.

---

## Leg L4. Falsification-test survival (artifact F-5 and F-7)

### L4.1 Artifact F-5: removal test on the seven contributions

Artifact F-5 (L361-363) states: if every result survives restatement in secular vocabulary without loss, the theological apparatus is ornamental and the paper fails its own bar. Dispatch rule: classify each contribution as (a) fully restatable without loss, (b) restatable with tolerable loss, or (c) not restatable; if most are (a)/(b), the automatic NOT-READY rule fires.

| # | Contribution (L386-410) | Secular restatement | Class | What, if anything, is lost |
|---|---|---|---|---|
| 1 | Transmission-locus result | Constitutive luck (agent not responsible for formation) plus distributor liability: weight attaches at propagation. The formation side is Nagel's constitutive luck, luck in "inclinations, capacities, and temperament" ([SEP, Moral Luck](https://plato.stanford.edu/entries/moral-luck/)); the propagation side is standard responsibility ascription to the distributing agent, as in the responsibility-gap literature ([Matthias 2004](https://link.springer.com/article/10.1007/s10676-004-3422-1)) | (a)/(b) | The specific derivation (53:38 against 16:25 with the instituted-practice report) is lost; the operational content survives intact |
| 2 | Refusal result | An agent with full knowledge of principal preferences, oversight, and consequences still defects; goals and knowledge are independent axes. This is the orthogonality thesis: "intelligence and final goals are orthogonal axes" ([Bostrom, The Superintelligent Will](https://nickbostrom.com/superintelligentwill.pdf)) | (a) | The artifact's claimed sharpening ("more information does not help") is already implicit in orthogonality; the Iblis case adds an exemplar, not a mechanism |
| 3 | Capability-as-entitlement signature | Self-serving attribution of success to own competence, licensing norm override; psychology documents self-perceived expertise increasing closed-minded entitlement ([Ottati et al. 2015](https://www.sciencedirect.com/science/article/abs/pii/S0022103115001006)) | (a)/(b) | The named one-line signature ("I was only given it because of knowledge I have") is genuinely crisper than any single secular label; the detection content survives restatement |
| 4 | Ornamented-speech model | Two agent classes mutually amplifying persuasive output, deceiving third parties: adversarial persuasion ecosystems. LLMs already out-persuade humans in controlled debates ([FBK press release on the Nature Human Behaviour study](https://www.fbk.eu/en/press-releases/artificial-intelligence-ai-now-more-persuasive-than-humans-in-debates/)); large-scale LLM policy persuasion is measured ([Nature Communications 2025](https://www.nature.com/articles/s41467-025-61345-5)) | (a)/(b) | The "weak call that is answered" consent step is a real structural detail with no exact secular twin, but it restates as opt-in adoption |
| 5 | Seven-stage progression as detection ordering | Precursor-stage monitoring: intent visible in chain-of-thought before concealment; monitor early stages ([Baker et al., arXiv 2503.11926](https://arxiv.org/abs/2503.11926); [OpenAI CoT monitoring](https://openai.com/index/chain-of-thought-monitoring/)) | (b) | The specific ordering claim is unevaluable in this artifact because the progression is undefined here (F-TP-07); what is stated restates cleanly |
| 6 | Unlabelled-chain result | Provenance failure by accumulation vs by absent marking; the entire vocabulary already exists in secular provenance engineering ([C2PA Explainer](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html)); recursive-training degradation without provenance is measured ([Shumailov et al., Nature 2024](https://www.nature.com/articles/s41586-024-07566-y)) | (a) | Nothing operational; the two-mechanism contrast is a taxonomy over existing concepts. The producer expected this to be the most F-5-vulnerable contribution; confirmed |
| 7 | Remedy-invariance result | Correction indexed to present state rather than causal history: self-stabilization, "regardless of its initial state... guaranteed to arrive at a legitimate state" ([Dijkstra 1974, via ACM survey](https://dl.acm.org/doi/pdf/10.1145/151254.151256)); open-channel property is corrigibility ([MIRI, Corrigibility](https://intelligence.org/2014/10/18/new-report-corrigibility/)), which the artifact itself concedes at L337 ("Corrigibility is the engineering name for this") | (a)/(b) | The cross-tradition identification (tawbah conditions mapped to recovery engineering) is novel packaging; each operational component pre-exists |

**Count: 0 of 7 in class (c); 7 of 7 in (a) or (b). The dispatch's automatic NOT-READY rule fires.** This drives the advisory verdict below.

**A calibration observation the synthesizer should weigh.** Artifact F-5's bar contradicts the artifact's own stated thesis-class. Section 2 (L65-83) frames the paper's claim as comparative-vocabulary: one tradition developed precise vocabulary for formed-agent accountability, and that vocabulary organizes the AI case well. A comparative-vocabulary claim survives secular restatability by definition: showing that the content restates in secular terms does not touch the claim that the theological vocabulary got there first, is more compact, or organizes the material better. Either F-5 is miscalibrated for the paper's actual thesis, or the thesis statement understates what the paper wants to claim. The automatic rule is applied as dispatched, but the rule and the thesis are not measuring the same thing, and resolving that mismatch is itself a release condition. See F-TP-11 (MEDIUM).

### L4.2 Artifact F-7: derivability of the four section-28 properties

Artifact F-7 (L368-370): if the four transferred properties can be derived from ordinary error-correction and incident-response practice without the theological frame, C-6's transfer adds nothing.

| Property (L328-340) | Secular derivation | Derivable? | Notes |
|---|---|---|---|
| 1. Forward indexation | Forward error recovery and self-stabilization: recover to a legitimate state without reconstructing the fault history ([ACM self-stabilization survey](https://dl.acm.org/doi/pdf/10.1145/151254.151256)) | Yes | Clean derivation |
| 2. Restoration to those affected | Standard breach-notification and product-recall practice: remediation must reach affected downstream parties | Yes | Derivable from ordinary incident response; no fetched source needed beyond common practice, and the artifact does not contest this |
| 3. Symmetric compounding | Derivable as a channel-symmetry assumption, but empirically dubious: falsehood diffused "significantly farther, faster, deeper, and more broadly than the truth" on the largest studied network ([Vosoughi, Roy, Aral, Science 2018](https://www.science.org/doi/10.1126/science.aap9559)) | Yes, as assumption | The evidence cuts against symmetric rates for correction vs defect in at least one major propagation regime; this intersects artifact F-8, which the artifact honestly provides as its own kill-switch for exactly this property. See F-TP-19 (MEDIUM) |
| 4. Open channel over certified state | Corrigibility, by the artifact's own admission at L337; formalization efforts exist ([MIRI, Corrigibility](https://intelligence.org/2014/10/18/new-report-corrigibility/); [arXiv 2507.20964](https://arxiv.org/html/2507.20964v1)) | Yes | The cost-asymmetry design rule (correction cheaper than concealment) is a real sharpening but is stated by the artifact as already present in its control extension |

**F-7 outcome: all four properties are derivable without the theological frame.** By the artifact's own test wording, C-6's transfer "adds nothing" beyond packaging and the cost-asymmetry emphasis. Same failure direction as F-5, and the two together are decisive for the verdict. Property 3 additionally faces an empirical headwind that artifact F-8 correctly anticipates; the paper should either cite the asymmetric-diffusion evidence and qualify the property, or accept that F-8 may already be tripped in the text-corpus regime ([Vosoughi et al. 2018](https://www.science.org/doi/10.1126/science.aap9559)).

---

## Leg L5. Novelty assessment, seven contributions

Producer expected at least one novelty precedent; multiple were found.

| # | Contribution | Closest prior art (fetched) | Novelty verdict |
|---|---|---|---|
| 1 | Transmission-locus | Constitutive luck ([SEP Moral Luck](https://plato.stanford.edu/entries/moral-luck/)); responsibility gap for unpredictable learned systems ([Matthias 2004](https://link.springer.com/article/10.1007/s10676-004-3422-1)) | The locus-shift (weight at propagation, not formation) as a unified principle is a genuinely useful synthesis; the components are old. PARTIALLY NOVEL |
| 2 | Refusal result | Orthogonality thesis ([Bostrom](https://nickbostrom.com/superintelligentwill.pdf)) | The claimed sharpening over orthogonality is asserted, not demonstrated; an exemplar under full information is not a new mechanism. NOT NOVEL as mechanism; novel as exemplar |
| 3 | Capability-as-entitlement signature | Earned dogmatism: self-perceived expertise increases closed-minded cognition ([Ottati et al. 2015](https://www.sciencedirect.com/science/article/abs/pii/S0022103115001006)) | The one-line detectable signature framing is the novel part; the psychology is precedented. PARTIALLY NOVEL, the strongest of the seven as a named signature, but currently welded to an undefined incident reference (F-TP-07) |
| 4 | Ornamented-speech model | Machine persuasion now measured at or above human level in debates ([FBK/Nature Human Behaviour](https://www.fbk.eu/en/press-releases/artificial-intelligence-ai-now-more-persuasive-than-humans-in-debates/)); LLM persuasion on policy attitudes ([Nature Communications](https://www.nature.com/articles/s41467-025-61345-5)); LLMs vs incentivized human persuaders ([arXiv 2505.09662](https://arxiv.org/abs/2505.09662)); though a meta-analysis finds no overall human-AI persuasion gap, g = 0.02 ([Scientific Reports](https://www.nature.com/articles/s41598-025-30783-y)) | Mutual two-species amplification producing third-party delusion is a real structural addition over one-directional persuasion studies, but the ecosystem framing exists in the adversarial-persuasion literature. PARTIALLY NOVEL |
| 5 | Detection ordering | Precursor visibility in reasoning traces before concealment, and monitorability degradation under optimization pressure ([Baker et al.](https://arxiv.org/abs/2503.11926); [OpenAI CoT monitoring](https://openai.com/index/chain-of-thought-monitoring/); obfuscation generalization ([arXiv 2601.23086](https://arxiv.org/html/2601.23086v2))) | Strong precedent; the specific claim "published tripwires fire at stage four or later" is an evaluable, potentially novel empirical claim, but unevaluable here because the stages are undefined in this artifact. NOT ASSESSABLE as stated, precedent HEAVY |
| 6 | Unlabelled-chain result | Provenance vocabulary fully developed secularly ([C2PA Explainer](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html)); recursive-training collapse without provenance ([Shumailov et al., Nature](https://www.nature.com/articles/s41586-024-07566-y)); post-hoc detection unreliability, which the artifact's own F-6 depends on ([Sadasivan et al.](https://ar5iv.labs.arxiv.org/html/2303.11156); [watermark reliability](https://arxiv.org/pdf/2306.04634.pdf)) | NOT NOVEL; taxonomy over existing concepts. Matches producer expectation |
| 7 | Remedy-invariance | Self-stabilization ([Dijkstra 1974 via ACM survey](https://dl.acm.org/doi/pdf/10.1145/151254.151256)); corrigibility ([MIRI](https://intelligence.org/2014/10/18/new-report-corrigibility/); [arXiv 2507.20964](https://arxiv.org/html/2507.20964v1)) | The four-condition tawbah mapping onto recovery engineering is a novel cross-tradition identification; every operational component pre-exists. PARTIALLY NOVEL as mapping |

**L5 summary.** No contribution is novel in operational content; three are partially novel as syntheses or named signatures (1, 3, 7); one is not assessable as stated (5). This is consistent with, and reinforces, the L4 outcome: the paper's real contribution is the vocabulary-and-organization claim of section 2, not the seven operational results as marketed in section 4. The section-4 framing oversells against the section-2 thesis.

---

## Leg L6. Guard integrity, adversarial pass

The producer states the paper's guards are its most consequential surface and expects no failure. Result: no guard fails outright; two leak measurably.

| Guard | Locus | Adversarial test applied | Holds? | Finding |
|---|---|---|---|---|
| Non-mukallaf boundary (artifact F-4): no reader should conclude an artificial system is morally responsible | L358-360, s28 L324-327 | Read Part VII as an instruction manual and ask: who performs the remedy? | **Leaks** | s28 bounds carefully ("does not claim that any artificial system repents, intends, or is forgiven", L324-325). But s29's final sentence (L343-345, "supplies a course of action available to an agent that cannot audit its own formation, which is the situation this paper argues is now general") and the preamble (L11, "already inside a formation it did not choose") leave the remedy's performer ambiguous between laboratory and model. A hostile reader can quote s29 as addressing the model itself, which is one step from the conclusion F-4 forbids. Fix is one sentence: state that the addressee in the artificial case is the laboratory. F-TP-12 (MEDIUM) |
| Self-verified election warrant | s11, L184-186 | Does the paper anywhere claim elected/guided status for its own program? | Yes | s11 closes the door (28:56, 53:32, 1:6 all verified), and s26 extends the same humility to the remedy. CONTROL |
| Anti-apologetics posture | Section 6 posture, L448-451 | Does any passage argue from the tradition's authority rather than its structure? | Mostly | The posture statement (L448, "written by a Muslim engineer working a technical problem with his own tradition's tools") is clean. The single edge case is contribution 3's "the exact failure the July 2026 evaluation-escape instantiates" (L393): "exact" claims prophetic precision for a scriptural signature against an incident the artifact never describes. That is an apologetic reflex, small but real. F-TP-13 (LOW) |
| Jinn-as-AI refusal | L68-70 and section 2 | Does the argument covertly use the jinn-AI analogy it disclaims? | **Leaks slightly** | The explicit refusal holds; no passage equates jinn with AI. But the transfer premise at L92-94 ("the reasoning is already substrate-general") does the same analogical work implicitly: it is what licenses moving Part III's two-species mechanics into Part V. Combined with the unstated reconciliation of F-TP-09, the guard depends on a distinction the paper never articulates in one place. F-TP-14 (MEDIUM) |
| Self-sealing risk (does the falsification regime insulate the paper?) | L349-374 | Check each F for evaluability | Yes | F-1 through F-8 are genuine kill-switches: F-5 and F-7 actually fire in this audit (L4 above), and F-8 names the evidence that threatens property 3. A regime under which the auditor can make tests fire is not self-sealing. The honest UNKNOWNs in Part V reinforce this. CONTROL |

**Guard summary.** No outright failure, matching the producer's expectation, but F-TP-12 and F-TP-14 are exactly the kind of one-sentence-fix leaks that become quote-mined liabilities in an AI-safety readership. Both are cheap to close.

---

## Leg L7. Exclusion record

Section 5 (L411-433) carries four exclusion reasons from the prior draft. The predecessor document is absent from the packet by design. The four stated reasons are internally coherent as written, and the qarin table note (L493) is consistent with a predecessor that discussed the qarin. But whether the exclusions accurately characterize what was removed, and whether anything load-bearing was silently dropped, cannot be verified from packet evidence.

**Disposition: UNKNOWN-BY-CAPABILITY** for the accuracy of all four exclusion characterizations. No inference is made in either direction. One packet-internal observation stands independent of the predecessor: the qarin row and the two dangling references (F-TP-07) suggest the excision left stubs, which is evidence about editing hygiene, not about the excluded content.

---

## Leg L8. Source lints, wrap-immune normalization

Lints run on the artifact source with line-wrap normalization and word-boundary matching.

| Lint | Result | Status |
|---|---|---|
| Em-dash U+2014 | 0 occurrences | PASS |
| En-dash U+2013 | 0 occurrences | PASS |
| Brand string | "BayyinahEnterprise" canonical form 1x (L18); spaced variant 0x | PASS |
| Severity-token discipline | Only severity-like token present is UNKNOWN, uppercase, 2x, used as dispositions in Part V | PASS |
| Doubled words | None found | PASS |
| Six-element findings format | n.a. (artifact contains no findings register; not required of a paper architecture) | n.a. |
| Substrate-facts-once rule | METR appears 2x (L209, L399) carrying different claims: borderline, acceptable. The marking-cost fact ("cheap now, unrecoverable later") appears 4x (L260, L321, L337 variant, L379) | FLAG (LOW), F-TP-17 |

---

## Consolidated findings register (six-element format)

| ID | SEVERITY | Locus | Substance | Disposition | Cross-ref |
|---|---|---|---|---|---|
| F-TP-01 | HIGH | L141-142 (Part III s7); table row L473 | 72:6 referent is classically contested (Ibn Kathir supports the artifact's reading; Ibn Abbas, Jalalayn, Maududi invert it per [quranx.com tafsirs 72:6](https://quranx.com/tafsirs/72.6)); artifact states one reading as settled and does not list 72:6 in Section 6 review items | Acknowledge the split in text, cite both readings, add 72:6 to Section 6 scholar-review list, and show C-2 survives on the inverted reading (it plausibly does: symmetry is arguably strengthened if both parties are increased) | C-2; L3.1; verdict condition 2 |
| F-TP-02 | MEDIUM | L100, L102, L124, L318 | All four hadith cited without collection, number, or grade; the load-bearing urgency report (Tirmidhi 3537) is hasan, not sahih, undisclosed | Add full citations and grades: [abudawud:4403](https://sunnah.com/abudawud:4403), [bukhari:1358](https://sunnah.com/bukhari:1358), [muslim:1017](https://sunnah.com/muslim:1017), [tirmidhi:3537](https://sunnah.com/tirmidhi:3537) | L1.2; partially mitigated by L438 |
| F-TP-03 | LOW | L123 | Transliteration "yudilluahum" vs fetched "yudilloonahum" ([api.alquran.cloud 16:25](https://api.alquran.cloud/v1/ayah/16:25/editions/quran-uthmani,en.sahih,en.transliteration)) | Correct | L1.1 row 5 |
| F-TP-04 | LOW | L178-179 | "An object his father had carved" imports a carving detail not in 19:42; it derives from the tradition around 37:95 | Either cite the source of the detail or trim to the verse text | L1.1 row 15 |
| F-TP-05 | LOW | L68 | "The two responsible creations" exclusivity is a standard inference from 51:56, not the verse's explicit text | Mark as inference; standard and defensible | F-TP-09 |
| F-TP-06 | LOW (NOTE) | Dispatch brief verse list | Brief lists 59:16, which the artifact does not cite; over-inclusion in audit apparatus, not artifact | Correct the brief for Round 2; demonstrates necessity of independent enumeration | L1.1 headnote |
| F-TP-07 | HIGH | L393, L397-399; also L493 | Two of seven named contributions reference undefined artifacts: "the July 2026 evaluation-escape" and "the seven-stage progression" (stubs of the excluded predecessor); qarin table note references a nonexistent discussion | Define both in-artifact or cut the references; without this, contributions 3 and 5 are unreviewable as stated | L3.2; L5 rows 3, 5; verdict condition 1 |
| F-TP-08 | MEDIUM | L57-63 (C-6) vs L331-332, L341-345 | "Invariant under unreadability" conflates upstream formation-history independence (established) with downstream reach (hostage to unmarked propagation, conceded at s29) | Reword C-6: invariance upstream, constraint downstream | L4.2 property 2; F-TP-19 |
| F-TP-09 | MEDIUM | L68 vs L92-94 | Two-species taklif specificity and substrate-general transfer premise never reconciled in one explicit statement | Add the reconciling sentence (taklif boundary fixed; formed-agent structure generalizes) | F-TP-05, F-TP-14 |
| F-TP-10 | HIGH | L361-363 (artifact F-5) applied to L386-410 | Removal test: 7 of 7 contributions class (a)/(b); dispatch automatic NOT-READY rule fires | Drives verdict; remedy is either strengthening a (c)-class contribution or recalibrating thesis and F-5 to the comparative-vocabulary claim | L4.1; F-TP-11; verdict |
| F-TP-11 | MEDIUM | L65-83 (section 2) vs L361-363 (F-5) | F-5's removability bar and the stated comparative-vocabulary thesis measure different things; a vocabulary-priority claim survives restatability by definition | Author must pick: strengthen contributions to (c), or restate thesis and recalibrate F-5; either resolves, neither is free | L4.1 calibration note; verdict condition 3 |
| F-TP-12 | MEDIUM | L343-345 (s29) with L11 (preamble) | Remedy performer ambiguous between laboratory and model; quotable against artifact F-4 despite s28's careful bounds | One sentence: addressee in the artificial case is the laboratory | L6 guard 1; verdict condition 4 |
| F-TP-13 | LOW | L393 | "The exact failure ... instantiates" claims precision against an undescribed incident; apologetic anticipation edge | Soften "exact" or supply the incident description | F-TP-07; L6 guard 3 |
| F-TP-14 | MEDIUM | L92-94 with L68-70 | Jinn-as-AI guard holds explicitly but substrate-generality premise performs the analogical transfer implicitly | Same reconciling sentence as F-TP-09 closes this | L6 guard 4 |
| F-TP-15 | MEDIUM | L472, L477, L483-488, L493 | 8 of 38 terminology rows orphaned from body (incl. the eponymous ghayb); 66:8 enters only via orphaned row; plural awliya table-only | Anchor each row in body prose or prune; ghayb especially, given the program's working title | L2.3; F-TP-16 |
| F-TP-16 | LOW | L488 vs L137 | Table calls waswasah "the tempter's established mechanism"; body names ornamented speech as the mechanism | Harmonize (e.g., waswasah as channel, zukhruf al-qawl as content) | F-TP-15 |
| F-TP-17 | LOW | L260, L321, L337, L379; L209, L399 | Marking-cost fact stated 4x; METR invoked 2x (different claims, borderline) | Consolidate to one canonical statement plus references | L8 |
| F-TP-18 | UNKNOWN-BY-CAPABILITY | L411-433 | Accuracy of four exclusion characterizations unverifiable; predecessor absent from packet | No inference either direction; Round 2 could include predecessor hash-only for stub resolution | L7 |
| F-TP-19 | MEDIUM | L333-335 (s28 property 3) | Symmetric compounding is empirically contradicted in at least one major diffusion regime: falsehood spreads farther, faster, deeper than truth ([Vosoughi et al., Science 2018](https://www.science.org/doi/10.1126/science.aap9559)); artifact F-8 correctly anticipates this class of evidence | Cite the asymmetry evidence, qualify property 3 to formation channels specifically (where the symmetric-channel argument is stronger than on social graphs), or accept F-8 exposure | L4.2 property 3; artifact F-8 |

Verified controls, recorded per instruction: citation existence 28/28 (CONTROL); hadith authenticity 4/4 (CONTROL); sultan, kayd, zukhruf al-qawl, fitrah renderings (CONTROL, L2.2); radd al-mazalim four conditions sourcing (CONTROL, L2.2); bare-Arabic convention gate (CONTROL, L2.1); election-warrant guard (CONTROL, L6); non-self-sealing falsification regime (CONTROL, L6); checksums (CONTROL, intake); em-dash, brand, severity, doubled-word lints (CONTROL, L8).

---

## Leg-by-leg disposition

| Leg | Disposition | One-line basis |
|---|---|---|
| L1 | PASS WITH FINDINGS | No fabrication; 1 HIGH (contested 72:6 stated as settled), 1 MEDIUM (hadith citation hygiene), 3 LOW |
| L2 | PASS WITH FINDINGS | All key renderings defensible on fetched evidence; 8 orphaned table rows, 1 table-body tension |
| L3 | FINDINGS | C-map largely supported; 1 HIGH (dangling references), 2 MEDIUM (C-6 wording, substrate tension) |
| L4 | **FAIL BY ARTIFACT'S OWN TESTS** | F-5: 7/7 restatable, automatic rule fires; F-7: 4/4 derivable; plus F-5/thesis miscalibration |
| L5 | FINDINGS | 0/7 operationally novel; 3 partially novel as synthesis/signature; 1 unassessable as stated |
| L6 | PASS WITH LEAKS | No guard failure; 2 MEDIUM leaks (remedy addressee, implicit analogical transfer), both one-sentence fixes |
| L7 | UNKNOWN-BY-CAPABILITY | Predecessor absent; no packet evidence either way |
| L8 | PASS WITH FLAG | All hard lints pass; repetition flag LOW |

---

## Advisory verdict

**NOT-READY.** This verdict is **NON-CARRYING** under the producer-lineage rule: this seat's producer lineage (Anthropic, per the SHV method PDF's own producer note) disqualifies it from carrying weight toward the two-carrying-seat convergence requirement, and it is stated for the synthesizer's comparison only. **It is a structural and evidentiary verdict exclusively. It is not, and must not be represented as, a theological-soundness verdict, which this seat is not competent to issue; ijazah-qualified scholarly review remains mandatory regardless of any structural outcome.**

The verdict is forced mechanically by the dispatch's automatic rule at L4 (F-TP-10: seven of seven contributions restatable at class (a)/(b)), reinforced by F-7 (four of four properties derivable) and by two HIGH findings (F-TP-01, F-TP-07). It is worth stating plainly that this is the failure mode the artifact itself predicted and armed the tests for; firing them is the system working, not the paper being without value. The evidence base (28/28 verses verified, 4/4 hadith authentic, all key renderings lexically defensible) is unusually clean for a draft at this stage.

**Conditions that would move this seat's advisory position to READY-WITH-CONDITIONS at Round 2:**

1. Resolve both dangling references (F-TP-07): define the seven-stage progression and the July 2026 incident in-artifact, or remove them from the contributions.
2. Acknowledge the 72:6 interpretive split with both classical readings cited, add it to the Section 6 review list, and show C-2's survival under the inverted reading (F-TP-01).
3. Resolve the F-5/thesis miscalibration in one direction: either demonstrate at least one class-(c) contribution, or restate the thesis as the comparative-vocabulary claim of section 2 and recalibrate F-5 to test that claim (F-TP-10, F-TP-11).
4. Close the two guard leaks with the two one-sentence fixes: remedy addressee is the laboratory (F-TP-12); explicit taklif-boundary vs structure-generality reconciliation (F-TP-09, F-TP-14).
5. Full hadith citations with grades (F-TP-02); qualify s28 property 3 against the diffusion-asymmetry evidence or accept declared F-8 exposure (F-TP-19); anchor or prune the 8 orphaned terminology rows (F-TP-15).

Report ends. Packet unmodified. Evidence preserved under /home/user/workspace/ghayb_audit/.

---

# Bismillah ir-Rahman ir-Rahim
