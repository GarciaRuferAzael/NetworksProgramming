#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:55:48 2024

@author: apirodd
"""

import socket
import tqdm
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# definiamo le chiavi
key = b"TheBestRandomKey"
nonce = b"TheBestRandomNce"

# crea un oggetto AES cipher
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=backend)

filename1 = "Cartel3.csv"
# IP address del server ricevente
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# riceve 4096 bytes ogni trance
BUFFER_SIZE = 1024 * 4
SEPARATOR = "<SEPARATOR>"
# creiamo il socket del server
# TCP socket
s = socket.socket()
# facciamo il bind del socket all'ip address locale
s.bind((SERVER_HOST, SERVER_PORT))

# abilitiamo il nostro server ad accettare connessioni
# 5 è il numero di connessioni in attesa che il sistema
# processerà prima, le altre saranno rifiutate

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accetta la connessione se presente

client_socket, address = s.accept()
# se il codice che segue viene eseguito significa che il mittente è connesso
print(f"[+] {address} is connected.")
# riceve le informazioni sul file
# riceve usandi il socket del client, non il socket del server

received = client_socket.recv(BUFFER_SIZE).decode("utf-8", "ignore")
pippo = [filename, filesize] = received.split(SEPARATOR)
# rimuove il percorso assoluto se presente

filename = os.path.basename(pippo[0])
# converte in un intero
filesize = int(pippo[1])
# comincia a ricevere il file dal socket
# e lo scrive sul file stream

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename1, "wb") as f:
    decryptor = cipher.decryptor()
    while True:
        # legge 1024 bytes dal socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # non riceve nulla
            # la trasmissione del file è completa
            break

        # decifra i bytes ricevuti
        # decrypted_bytes = decryptor.update(bytes_read)
        # scrive nel file i bytes che abbiamo ricevuto
        f.write(bytes_read)
        # aggiorna la barra di avanzamento
        progress.update(len(bytes_read))
        # progress.update(len(decrypted_bytes))
        if bytes_read[-5:] == b"<END>":
            break
# chiude il client socket
client_socket.close()
# chiude il server socket
s.close()
