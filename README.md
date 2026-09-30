# Useful Commands and Automation Scripts (Comandos e Scripts Úteis)

Repository for reference guides, cheat sheets, and production-grade utility scripts across various DevOps tools, database engines, and programming languages.

* **Team / Contributors:**
  * [Marcos](https://github.com/MarcosAllysson) - Full Stack Developer
  * [Douglas](https://github.com/douglasshibata) - Full Stack Developer

---

## Table of Contents
- [Project Overview & Architecture](#project-overview--architecture)
- [Setup & Installation Instructions](#setup--installation-instructions)
- [Environment Variables Required](#environment-variables-required)
- [How to Run the Test Suite](#how-to-run-the-test-suite)
- [Security Considerations & Vulnerabilities Resolved](#security-considerations--vulnerabilities-resolved)
- [Directory Structure & Guides](#directory-structure--guides)

---

## Project Overview & Architecture

This repository organizes development cheat-sheets and standalone automation scripts into dedicated technology modules:

```text
├── Scripts/               # Bash & Python automation scripts
│   ├── generateMD5_SHA1_SHA256_SHA512_WithPython.py  # Python Hash Generator
│   ├── generateMD5.sh     # Bash MD5 generator
│   ├── atualizar.sh        # System package updater script
│   ├── mysql.sh            # MySQL service controller
│   ├── mongodb.sh          # MongoDB service controller
│   ├── php.sh              # Apache2 service controller
│   └── desligar.sh         # System power/reboot utility
├── tests/                 # Comprehensive test suite
│   └── test_hash_generator.py # Pytest unit & integration tests
├── Postgres/              # PostgreSQL cheat-sheets
├── Django Framework/      # Django commands guide
├── Docker/                # Docker reference & compose files
├── Kubernetes/            # K8s manifest examples
├── Elasticsearch/         # Docker-compose configuration for ES
└── ...                    # Language & framework guides (Python, Git, Angular, Rasa, Windows)
```

---

## Setup & Installation Instructions

### Prerequisites
- **Python**: Python 3.8+
- **Bash**: GNU Bash (for Linux/Unix shell scripts)
- **Pytest**: For running tests

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/douglasshibata/useful.git
   cd useful
   ```

2. (Optional) Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install test dependencies:
   ```bash
   pip install pytest
   ```

4. Make scripts executable:
   ```bash
   chmod +x Scripts/*.sh Scripts/*.py
   ```

---

## Environment Variables Required

No external environment variables or third-party secret credentials are required to run the utility scripts. Standard Linux systems with standard `systemctl` / `apt-get` utility permissions (e.g., `sudo` access) are expected for system management shell scripts.

---

## How to Run the Test Suite

The project includes an automated test suite using `pytest` covering execution paths, CLI arguments, interactive mode fallbacks, edge cases, and security warnings.

To run all tests:

```bash
pytest -v
```

Output example:
```text
tests/test_hash_generator.py::TestHashGenerator::test_cli_mode_sha256 PASSED
tests/test_hash_generator.py::TestHashGenerator::test_cli_mode_weak_algorithm_warning PASSED
tests/test_hash_generator.py::TestHashGenerator::test_generate_hash_md5 PASSED
tests/test_hash_generator.py::TestHashGenerator::test_generate_hash_sha1 PASSED
tests/test_hash_generator.py::TestHashGenerator::test_generate_hash_sha256 PASSED
tests/test_hash_generator.py::TestHashGenerator::test_generate_hash_sha512 PASSED
...
```

---

## Security Considerations & Vulnerabilities Resolved

### Security Remediations Made
1. **Cryptographic Algorithm Warnings**:
   - MD5 and SHA-1 are cryptographically vulnerable to collision attacks. The Python hashing utility (`generateMD5_SHA1_SHA256_SHA512_WithPython.py`) now explicitly issues security warnings when MD5 or SHA-1 is selected and defaults to SHA-256 for non-specified operations.
2. **Shell Injection and Word Splitting Fixes**:
   - Resolved unquoted positional parameter `$1` expansions in `generateMD5.sh` by switching to `printf '%s' "$1"`.
   - Quoted user input variables (`"$resposta"`) across all shell scripts to prevent field splitting and globbing vulnerabilities.
3. **Privilege & Command Hardening**:
   - Standardized system management commands to use `systemctl` and added missing `sudo` checks for reboot/shutdown operations (`desligar.sh`).
4. **Input Validation & Exception Handling**:
   - Replaced infinite unhandled loops in Python scripts with structured exception handling (`KeyboardInterrupt`, `EOFError`, `ValueError`).
   - Added parameter validation checks in shell scripts to handle missing arguments cleanly.

---

## Directory Structure & Guides

### Postgres
* [Comandos úteis do Postgres](Postgres/PsqlComandos.md)

### Scripts
* [Como usar Scripts](Scripts/README.md)
* [Script de apoio para atualizar o sistema debian](Scripts/atualizar.sh)
* [Desligar o computador via terminal](Scripts/desligar.sh)
* [Gerenciar serviço do mongodb](Scripts/mongodb.sh)
* [Gerenciador do serviço mysql](Scripts/mysql.sh)
* [Gerenciador do serviço apache](Scripts/php.sh)
* [Gerador de MD5](Scripts/generateMD5.sh)
* [Gerador de MD5/SHA1/SHA256/SHA512 Com Python](Scripts/generateMD5_SHA1_SHA256_SHA512_WithPython.py)

### Python
* [Manual Básico do Python](Python/Python.md)

### Git
* [Comandos Básico do Git](Git/GitComandos.md)

### Django Framework
* [Comandos Básicos do Django](Django%20Framework/DjangoComandos.md)

### MongoDB
* [Comandos Básicos do MongoDB](MongoDB/MongoDBComandos.md)
* [Comandos Básicos do MongoDB com Docker](MongoDB/MongoDBWithDocker.md)

### Rasa Framework
* [Comandos Básicos do Rasa](Rasa%20Framework/RasaComandos.md)

### Docker
* [Comandos Básicos do Docker](docker/dockerComandos.md)

### CRON
* [CRON](Cron/CRON.md)

### Angular
* [Angular](Angular/Angular.md)

### Windows
* [CMD](Windows/Cmd.md)
* [Power Shell](Windows/powershell.md)

### Apache
* [Linux](Apache/ForLinux.md)
* [Windows](Apache/ForWindows.md)

### Kubernetes
* [Kubernetes Guide](Kubernetes/Kubernetes.md)

### Elasticsearch
* [Elasticsearch Config](Elasticsearch/docker-compose.yml)
