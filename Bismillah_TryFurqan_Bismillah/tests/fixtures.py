# Bismillah ir-Rahman ir-Rahim
# 
# Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
#   Allah -- The God
#   Ar-Rahman -- The Most Merciful
#   Ar-Rahim -- The Most Compassionate
#   Al-Malik -- The King
#   Al-Quddus -- The Most Holy
#   As-Salam -- The Source of Peace
#   Al-Mu'min -- The Guardian of Faith
#   Al-Muhaymin -- The Protector
#   Al-Aziz -- The Almighty
#   Al-Jabbar -- The Compeller
#   Al-Mutakabbir -- The Supreme
#   Al-Khaliq -- The Creator
#   Al-Bari -- The Evolver
#   Al-Musawwir -- The Fashioner
#   Al-Ghaffar -- The Forgiver
#   Al-Qahhar -- The Subduer
#   Al-Wahhab -- The Bestower
#   Ar-Razzaq -- The Provider
#   Al-Fattah -- The Opener
#   Al-Alim -- The All-Knowing
#   Al-Qabid -- The Restrainer
#   Al-Basit -- The Expander
#   Al-Khafid -- The Abaser
#   Ar-Rafi -- The Exalter
#   Al-Mu'izz -- The Bestower of Honor
#   Al-Mudhill -- The Humiliator
#   As-Sami -- The All-Hearing
#   Al-Basir -- The All-Seeing
#   Al-Hakam -- The Judge
#   Al-Adl -- The Just
#   Al-Latif -- The Subtle One
#   Al-Khabir -- The All-Aware
#   Al-Halim -- The Forbearing
#   Al-Azim -- The Magnificent
#   Al-Ghafur -- The All-Forgiving
#   Ash-Shakur -- The Appreciative
#   Al-Ali -- The Most High
#   Al-Kabir -- The Most Great
#   Al-Hafiz -- The Preserver
#   Al-Muqit -- The Sustainer
#   Al-Hasib -- The Reckoner
#   Al-Jalil -- The Majestic
#   Al-Karim -- The Generous
#   Ar-Raqib -- The Watchful
#   Al-Mujib -- The Responsive
#   Al-Wasi -- The All-Encompassing
#   Al-Hakim -- The Perfectly Wise
#   Al-Wadud -- The Loving One
#   Al-Majid -- The Most Glorious
#   Al-Ba'ith -- The Resurrector
#   Ash-Shahid -- The Witness
#   Al-Haqq -- The Truth
#   Al-Wakil -- The Trustee
#   Al-Qawiyy -- The Most Strong
#   Al-Matin -- The Firm One
#   Al-Waliyy -- The Protector
#   Al-Hamid -- The Praiseworthy
#   Al-Muhsi -- The Accounter
#   Al-Mubdi -- The Originator
#   Al-Mu'id -- The Restorer
#   Al-Muhyi -- The Giver of Life
#   Al-Mumit -- The Creator of Death
#   Al-Hayy -- The Ever Living
#   Al-Qayyum -- The Self-Subsisting
#   Al-Wajid -- The Finder
#   Al-Majid -- The Noble
#   Al-Wahid -- The Unique
#   Al-Ahad -- The One
#   As-Samad -- The Eternal
#   Al-Qadir -- The Able
#   Al-Muqtadir -- The Powerful
#   Al-Muqaddim -- The Expediter
#   Al-Mu'akhkhir -- The Delayer
#   Al-Awwal -- The First
#   Al-Akhir -- The Last
#   Az-Zahir -- The Manifest
#   Al-Batin -- The Hidden
#   Al-Wali -- The Governor
#   Al-Muta'ali -- The Most Exalted
#   Al-Barr -- The Source of Goodness
#   At-Tawwab -- The Acceptor of Repentance
#   Al-Muntaqim -- The Avenger
#   Al-Afuww -- The Pardoner
#   Ar-Ra'uf -- The Most Kind
#   Malik-ul-Mulk -- Owner of Sovereignty
#   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
#   Al-Muqsit -- The Equitable
#   Al-Jami -- The Gatherer
#   Al-Ghaniyy -- The Self-Sufficient
#   Al-Mughni -- The Enricher
#   Al-Mani -- The Preventer
#   Ad-Darr -- The Distresser
#   An-Nafi -- The Propitious
#   An-Nur -- The Light
#   Al-Hadi -- The Guide
#   Al-Badi -- The Originator
#   Al-Baqi -- The Everlasting
#   Al-Warith -- The Inheritor
#   Ar-Rashid -- The Guide to the Right Path
#   As-Sabur -- The Patient
# 
"""Mirror of the playground.js FIXTURES and DIFF_FIXTURES tables.

Single-source-of-truth would require parsing JS at test time; we accept
the duplication for clarity and lock both with a sync test
(test_fixtures_sync.py) that asserts every id present here is also
present in playground.js. Drift fails CI.
"""
from __future__ import annotations

CHECK_FIXTURES: dict[str, dict[str, str]] = {
    "python": {
        "py-clean": (
            "def get_email(uid: int) -> str | None:\n"
            "    if uid <= 0:\n"
            "        return None\n"
            "    return \"user@example.com\"\n"
            "\n"
            "def send_welcome(uid: int) -> str | None:\n"
            "    e: str | None = get_email(uid)\n"
            "    return e\n"
        ),
        "py-status-collapse": (
            "def get_email(uid: int) -> str | None:\n"
            "    if uid <= 0:\n"
            "        return None\n"
            "    return \"user@example.com\"\n"
            "\n"
            "def send_welcome(uid: int) -> bool:\n"
            "    e: str = get_email(uid)\n"
            "    return True\n"
        ),
        "py-parse-error": (
            "def f(x: int -> int:\n"
            "    return x\n"
        ),
        "py-no-may-fail": (
            "def double(x: int) -> int:\n"
            "    return x * 2\n"
            "\n"
            "def quad(x: int) -> int:\n"
            "    return double(double(x))\n"
        ),
    },
    "rust": {
        "rs-clean": (
            "pub struct Config { pub name: String }\n"
            "pub struct Service;\n"
            "\n"
            "pub enum ConfigError { NotFound }\n"
            "\n"
            "pub fn fetch_config(path: &str) -> Result<Config, ConfigError> {\n"
            "    Ok(Config { name: path.to_string() })\n"
            "}\n"
            "\n"
            "pub fn init_service(path: &str) -> Result<Service, ConfigError> {\n"
            "    let config = fetch_config(path)?;\n"
            "    let _ = config;\n"
            "    Ok(Service)\n"
            "}\n"
        ),
        "rs-unwrap-collapse": (
            "pub struct Config { pub name: String }\n"
            "pub struct Service;\n"
            "impl Service { pub fn new(_c: Config) -> Self { Service } }\n"
            "\n"
            "pub enum ConfigError { NotFound }\n"
            "\n"
            "pub fn fetch_config(path: &str) -> Result<Config, ConfigError> {\n"
            "    Ok(Config { name: path.to_string() })\n"
            "}\n"
            "\n"
            "pub fn init_service(path: &str) -> Service {\n"
            "    let config = fetch_config(path).unwrap();\n"
            "    Service::new(config)\n"
            "}\n"
        ),
        "rs-parse-error": (
            "pub fn broken(x: i32 -> i32 {\n"
            "    x\n"
        ),
    },
    "go": {
        "go-clean": (
            "package main\n"
            "\n"
            "import (\n"
            "\t\"encoding/json\"\n"
            "\t\"os\"\n"
            ")\n"
            "\n"
            "type Config struct{ Name string }\n"
            "\n"
            "func LoadConfig(path string) (*Config, error) {\n"
            "\tdata, err := os.ReadFile(path)\n"
            "\tif err != nil {\n"
            "\t\treturn nil, err\n"
            "\t}\n"
            "\tvar cfg Config\n"
            "\terr = json.Unmarshal(data, &cfg)\n"
            "\treturn &cfg, err\n"
            "}\n"
            "\n"
            "func ReadConfig(path string) (*Config, error) {\n"
            "\tcfg, err := LoadConfig(path)\n"
            "\tif err != nil {\n"
            "\t\treturn nil, err\n"
            "\t}\n"
            "\treturn cfg, nil\n"
            "}\n"
        ),
        "go-blank-collapse": (
            "package main\n"
            "\n"
            "import (\n"
            "\t\"encoding/json\"\n"
            "\t\"os\"\n"
            ")\n"
            "\n"
            "type Config struct{ Name string }\n"
            "type Server struct{}\n"
            "\n"
            "func NewServer(c *Config) *Server { return &Server{} }\n"
            "\n"
            "func LoadConfig(path string) (*Config, error) {\n"
            "\tdata, err := os.ReadFile(path)\n"
            "\tif err != nil { return nil, err }\n"
            "\tvar cfg Config\n"
            "\terr = json.Unmarshal(data, &cfg)\n"
            "\treturn &cfg, err\n"
            "}\n"
            "\n"
            "func StartServer(path string) *Server {\n"
            "\tcfg, _ := LoadConfig(path)\n"
            "\treturn NewServer(cfg)\n"
            "}\n"
        ),
        "go-parse-error": (
            "package main\n"
            "\n"
            "func broken( {\n"
        ),
    },
}


DIFF_FIXTURES: dict[str, dict[str, tuple[str, str]]] = {
    "python": {
        "py-additive-pass": (
            "def alpha(x: int) -> int:\n    return x\n\ndef beta(x: int) -> int:\n    return x + 1\n",
            "def alpha(x: int) -> int:\n    return x\n\ndef beta(x: int) -> int:\n    return x + 1\n\ndef gamma(x: int) -> int:\n    return x + 2\n",
        ),
        "py-additive-marad": (
            "def alpha(x: int) -> int:\n    return x\n\ndef beta(x: int) -> int:\n    return x + 1\n",
            "def alpha(x: int) -> int:\n    return x\n",
        ),
    },
    "rust": {
        "rs-additive-pass": (
            "pub fn alpha(x: i32) -> i32 { x }\n",
            "pub fn alpha(x: i32) -> i32 { x }\npub fn beta(x: i32) -> i32 { x + 1 }\n",
        ),
        "rs-additive-marad": (
            "pub fn alpha(x: i32) -> i32 { x }\npub fn beta(x: i32) -> i32 { x + 1 }\n",
            "pub fn alpha(x: i32) -> i32 { x }\n",
        ),
    },
    "go": {
        "go-additive-pass": (
            "package main\n\nfunc Alpha(x int) int { return x }\n",
            "package main\n\nfunc Alpha(x int) int { return x }\n\nfunc Beta(x int) int { return x + 1 }\n",
        ),
        "go-additive-marad": (
            "package main\n\nfunc Alpha(x int) int { return x }\n\nfunc Beta(x int) int { return x + 1 }\n",
            "package main\n\nfunc Alpha(x int) int { return x }\n",
        ),
    },
}

# Bismillah ir-Rahman ir-Rahim