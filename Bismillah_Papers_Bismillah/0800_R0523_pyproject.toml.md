# Bismillah ir-Rahman ir-Rahim

# R0523 -- pyproject.toml

**Chronological Index:** 800 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** pyproject.toml  
**Source Format:** toml  
**SHA-256:** `3bfbf2b42c6e350d42e941868caa194a260c4a171b7bb37b635d29f4faa79404`  

---

## R0523 · pyproject.toml

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: pyproject.toml
- source_format: toml
- text_sha256: 3bfbf2b42c6e350d42e941868caa194a260c4a171b7bb37b635d29f4faa79404

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "bayyinah"
version = "1.5.0"
description = "Bayyinah Scanner: file integrity verification through surface/substrate parity (ARINC-653 + Munafiq self-detect, avionics advisory tier)"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "Proprietary" }
authors = [
    { name = "Bilal Syed Arfeen", email = "bayyinahenterprises@tuta.com" },
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent",
    "Topic :: Security",
    "Topic :: Software Development :: Quality Assurance",
]
# Runtime dependencies: stdlib-only for v1.2.5 (csv, json modules).
# Optional scipy used by the F1 harness for exact Clopper-Pearson bounds.
dependencies = []

[project.optional-dependencies]
# Per dependency-manifest discipline (memory): new third-party imports go in
# BOTH requirements.txt AND pyproject.toml in the same patch, capped at current major.
f1 = [
    "scipy>=1.11,<2",
]
dev = [
    "pytest>=7,<9",
    "ruff>=0.5,<1",
    "mypy>=1.8,<2",
    "black>=24,<26",
]

[project.scripts]
bayyinah = "bayyinah.cli.main:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-dir]
"" = "src"

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B"]
ignore = ["E501"]  # let black/ruff-format handle line length

[tool.mypy]
python_version = "3.9"
strict = true
ignore_missing_imports = true
files = ["src/bayyinah"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-q"

---

# Bismillah ir-Rahman ir-Rahim
