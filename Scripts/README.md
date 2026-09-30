# Useful Scripts & Utilities

Useful shell and Python scripts for Linux/Unix automation and security hash generation.

## Permissions
Ensure scripts are executable before running:

```bash
chmod +x Scripts/*.sh Scripts/*.py
```

## Available Scripts

### 1. `generateMD5_SHA1_SHA256_SHA512_WithPython.py`
Generates MD5, SHA1, SHA256, or SHA512 hashes using Python. Supports both CLI arguments and interactive mode.

**CLI Usage:**
```bash
python3 Scripts/generateMD5_SHA1_SHA256_SHA512_WithPython.py -s "hello world" -a sha256
```

**Interactive Usage:**
```bash
python3 Scripts/generateMD5_SHA1_SHA256_SHA512_WithPython.py
```

### 2. `generateMD5.sh`
Generates an MD5 hash for a given string input.

```bash
./Scripts/generateMD5.sh "text to hash"
```

### 3. `atualizar.sh`
Updates system package lists and upgrades installed packages via `apt-get`.

```bash
./Scripts/atualizar.sh
```

### 4. `mysql.sh`
Manage MySQL system service status (start/stop/status/restart).

```bash
./Scripts/mysql.sh
```

### 5. `mongodb.sh`
Manage MongoDB system service status (start/stop/status).

```bash
./Scripts/mongodb.sh
```

### 6. `php.sh`
Manage Apache2 service status (start/stop/restart).

```bash
./Scripts/php.sh
```

### 7. `desligar.sh`
Shutdown or reboot system.

```bash
./Scripts/desligar.sh
```

## Running Tests

To run the automated test suite using pytest:

```bash
pytest -v
```
