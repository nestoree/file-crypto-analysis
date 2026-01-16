# 🔐 File Encryption & Decryption (Educational Project)

⚠️ IMPORTANT WARNING

This project encrypts and decrypts files directly on disk.  
Running it without proper understanding may lead to permanent data loss if the encryption key is lost or corrupted.

This repository is provided strictly for educational and research purposes to demonstrate:
- Symmetric cryptography concepts
- File system traversal in Python
- Basic TCP socket communication

DO NOT use this code on real systems, personal data, or third-party machines.

---

## 📌 Project Overview

This repository contains two Python scripts that work together:

- Encripter → Encrypts files and generates a cryptographic key  
- Desencripter → Decrypts files using the previously generated key  

Together, they form a controlled lab example to study encryption and decryption workflows.

---

## 📂 Scripts Included

### 🔒 Encripter (Encryption Script)

Main features:

- Recursively scans directories for files
- Excludes critical project files from encryption
- Encrypts file contents using cryptography.Fernet
- Automatically generates a symmetric encryption key
- Stores the key temporarily in key.key
- Sends the key over a TCP socket
- Logs the encryption date and time in encrypt_time.txt

⚠️ If the key is lost or deleted, encrypted files cannot be recovered.

---

### 🔓 Desencripter (Decryption Script)

Main features:

- Scans the current directory for encrypted files
- Loads the encryption key from key.key
- Decrypts files using the same Fernet key
- Restores original file contents only if the correct key is used

If the key is invalid or missing, decryption will fail.

---

## 🚫 Excluded Files

The following files are intentionally excluded to prevent self-encryption:

- Encripter.py
- EncripterLinux.py
- desencripter.py
- key.key
- encrypt_time.txt

---

## 📦 Requirements

- Python 3.8+
- cryptography library

Install dependency:

```
pip install cryptography
```

---

## 🌐 Network Configuration (Encripter)

The encryption script uses placeholder network values:

```
IP = "192.168.x.xx"  
port = 4444
```

These values are examples only and should be used exclusively in isolated test environments such as virtual machines or private labs.

---

## 🧪 Safe Usage Guidelines

Recommended:
- Virtual machines
- Isolated test folders
- Files without real value
- Cybersecurity labs or learning environments

Never use on:
- Your main operating system
- Personal or important files
- Computers you do not own
- Systems without backups

---

## ⚠️ Known Limitations

- No file type filtering
- No user confirmation before encryption
- Minimal error handling
- Plain TCP communication (no encryption)
- Loss of the encryption key results in irreversible data loss

---

## 🎓 Educational Purpose

This project is designed to help understand:

- Symmetric encryption (AES via Fernet)
- File traversal and manipulation in Python
- Encryption key management risks
- Importance of backups and secure key handling
- Why this design should not be used in real-world software

This is not intended as a production-ready encryption tool.

---

## ⚖️ Legal Disclaimer

This software is provided “as is”, without warranty of any kind.  
The author assumes no responsibility for misuse, damage, or data loss caused by this code.
