🔐 File Encryption & Decryption (Educational Project)

⚠️ IMPORTANT WARNING
This project encrypts and decrypts files directly on disk. Running it without full understanding may result in permanent data loss if the encryption key is lost.

This repository is provided strictly for educational and research purposes, to demonstrate:

symmetric cryptography concepts,

file system traversal,

basic network communication using sockets.

Do NOT use this code on real systems, personal data, or third-party machines.

📌 Project Overview

This project consists of two Python scripts:

Encripter

Recursively scans directories.

Encrypts files using Fernet (symmetric encryption).

Generates a cryptographic key.

Sends the key over a TCP socket.

Logs the encryption timestamp.

Desencripter

Reads the previously generated key.

Decrypts encrypted files in the current directory.

Restores original file contents (if the correct key is present).

Together, they form a controlled lab example to study encryption workflows.

📂 Scripts
🔒 Encripter (Encryption Script)

Main responsibilities:

Traverse directories recursively.

Skip specific project-related files.

Encrypt files using cryptography.Fernet.

Store the encryption key temporarily.

Send the key to a remote host using TCP.

Record the execution date and time.

⚠️ If the key is deleted or intercepted incorrectly, files cannot be recovered.

🔓 Desencripter (Decryption Script)

Main responsibilities:

Scan the current directory for encrypted files.

Load the encryption key from key.key.

Decrypt each file using the same Fernet key.

Restore original file content.

If the key does not match, decryption will fail.

📄 Files Excluded From Processing

Both scripts explicitly ignore the following files:

Encripter.py

EncripterLinux.py

desencripter.py

key.key

encrypt_time.txt

This prevents self-encryption and accidental corruption of control files.

📦 Dependencies

Python 3.8+

cryptography

Optional / unused imports may appear in the code but are not required for core functionality.

Install dependencies manually if needed:

pip install cryptography

🌐 Network Configuration (Encripter)

The encryption script contains placeholder network values:

IP = "192.168.x.xx"
port = 4444


These values are examples only and should be used exclusively in isolated test environments, such as virtual machines or closed labs.

🧪 Safe Usage Guidelines

✔️ Recommended environments:

Virtual machines

Test folders with disposable files

Offline laboratory setups

❌ Never run on:

Your main operating system

Personal or important data

Other people’s computers

Systems without backups

⚠️ Known Limitations

No file type filtering.

No user confirmation before encryption.

Minimal error handling.

No secure transport layer (plain TCP).

Loss of the key results in irreversible data loss.

🎓 Educational Purpose

This project can be used to learn about:

Symmetric encryption (AES via Fernet)

File system traversal in Python

Risks of automated file modification

Importance of backups and key management

Defensive security awareness

It is not intended as a real-world encryption tool.

⚖️ Legal Disclaimer

This software is provided “as is”, without warranty of any kind.
The author assumes no responsibility for misuse, data loss, or damage caused by this code.
