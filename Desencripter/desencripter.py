import os
import sys
import subprocess
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "Encripter.py" or file == "key.key" or file == "desencripter.py" or file == "encrypt_time.txt" or file == "EncripterLinux.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("key.key", "rb") as key_file:
    key = key_file.read()

for file in files:
    try:
        with open(file, "rb") as f:
            data = f.read()
        data_decrypted = Fernet(key).decrypt(data)
        with open(file, "wb") as f:
            f.write(data_decrypted)
    except:
        print("Hubo un error al desencriptar los archivos")
