# Bismillah ir-Rahman ir-Rahim

# R0490 -- bayyinah-validator

**Chronological Index:** 780 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** bayyinah-validator-README.pdf  
**Source Format:** pdf  
**SHA-256:** `62e154b1f276519702de75669ae16f282e47a1bda08d60a83dad619d94c806c1`  

---

## R0490 · bayyinah-validator

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: bayyinah-validator-README.pdf
- source_format: pdf
- text_sha256: 62e154b1f276519702de75669ae16f282e47a1bda08d60a83dad619d94c806c1

bayyinah-validator
Cross-vendor orchestrator for the Bayyinah Audit Framework §5.2 validator-by-differentinstance protocol.
Fans an artifact out to multiple LLM providers in parallel. Each loads the framework as
system prompt and audits independently. The aggregator computes consensus (multiple
validators agree) and solo findings (one validator only) and renders a Round-N report in
canonical Bayyinah format.

Why cross-vendor
Same-vendor validation is weaker than cross-vendor. A second Claude instance shares
architectural priors with the first. A Claude+GPT+Gemini panel does not. Disagreement
across vendors is informative; agreement across vendors is much harder to dismiss.

Quick start
# Install with all providers
pip install -e ".[all]"
# Or pick what you need
pip install -e ".[anthropic,openai]"
# Set keys
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...
# Audit a doc with the default validator set (anthropic + openai)
bayyinah-validate path/to/artifact.md \
--framework-prompt path/to/SKILL.md \
--output round-1.md

Components
bayyinah-validator/
├── bayyinah_validator/
│

├── core.py

(Finding, Artifact, Validator base class)


│

├── orchestrator.py

(parallel fan-out)

│

├── aggregator.py

(consensus and solo grouping)

│

├── report.py

(markdown rendering)

│

├── cli.py

(command-line interface)

│

└── validators/

│

├── anthropic_validator.py

│

├── openai_validator.py

│

├── gemini_validator.py

│

├── grok_validator.py

│

└── mock_validator.py

(no-API testing)

├── examples/
│

└── run_with_mocks.py

(smoke run without keys)

├── tests/
│

└── test_pipeline.py

(end-to-end with mocks)

├── pyproject.toml
├── requirements.txt
└── README.md

How findings get grouped
Each finding has a stable signature combining its normalized category and reproducer.
Findings sharing a signature across validators are treated as referring to the same
underlying gap. Within a group, the finding with the highest severity is the representative.
This means: if Claude grades a citation gap as HIGH and GPT grades it as MED, they form
one consensus finding (representative HIGH, with the disagreement preserved in the pervalidator detail block). The signature collapses them; the severity distribution preserves the
disagreement.

Cost and rate-limit notes
Each validator runs the full audit independently. A 4-validator run costs roughly 4x a single
audit. For routine audits, 2 validators (anthropic + openai) are usually sufficient. Reserve 3
or 4 for high-stakes artifacts (release candidates, framework updates, public-facing
pitches).
Validators run in parallel via asyncio.gather, so wall-clock time is dominated by the slowest
provider, not the sum.

Exit codes (CLI)
0 No consensus findings at HIGH or MED severity


1 Consensus MED findings present
2 Consensus HIGH findings present, OR a fatal error before audit ran

Solo findings do not affect exit codes by design. Solo findings are signals worth
investigating, not gates worth blocking on.

Connection to the rest of the audit infrastructure
Lane #1 (skill bundle): Provides the framework prompt that this orchestrator passes to
each validator. Use the SKILL.md from the skill bundle as the --framework-prompt
argument.
Lane #2 (CI pipeline): Can invoke this orchestrator as a deeper audit when a HIGH
finding emerges in CI, escalating from single-vendor to cross-vendor.
Lane #4 (MCP server, future): This orchestrator can be wrapped as an MCP tool, so
any MCP-compliant agent can request a cross-vendor audit on demand.

Smoke test (no API keys)
python tests/test_pipeline.py

Should print All smoke tests passed. and a sample report.

Three placeholders to confirm before production
1. Default models per validator. The defaults are claude-opus-4-7 , gpt-4o , gemini1.5-pro , and grok-2-latest . Confirm these exist and are appropriate for audit work;

override via --model VALIDATOR=MODEL .
2. Framework prompt source. The CLI loads framework text from --framework-prompt .
Point it at the SKILL.md from the skill bundle, or any other framework reference text.
3. Provider auth model. Each validator reads its key from a default environment variable
( ANTHROPIC_API_KEY , OPENAI_API_KEY , GOOGLE_API_KEY , XAI_API_KEY ). For
programmatic use, pass api_key to the constructor.

License
Inherits BayyinahEnterprise terms. Confirm before public distribution.

---

# Bismillah ir-Rahman ir-Rahim
