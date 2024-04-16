#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:45:43 2023

@authors: Andrea PIRODDi, Franco CALLEGATI, Roberto GIRAU
"""

# Importiamo il modulo socket
import socket           
 
def xor(a, b):
 
    # initializziamo la lista result
    result = []
 
    # Scorriamo tutti i bits, se ci sono bits uguali
    # allora XOR è 0, altrimenti 1 (vedi tabella di verità nelle slide)
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
 
# Definiamo la funzione che calcola il resto della divisione binaria
def mod2div(dividend, divisor):
 
    # Numero di bits su cui applicare la XOR (dimensione del divisore).
    pick = len(divisor)
 
    # applichiamo lo Slicing al dividendo in funzione della
    # lunghezza appropriata per ciascun passo
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
 
            # rimpiazziamo il dividendo con il risultato della
            # XOR e tiriamo giù 1 bit
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else: # se il bit più a sinistra è '0'
 
            # se il bit più a sinistra del dividendo (o la parte
            # usata in ciascuno step) è 0, non possiamo
            # usare il divisore regolare; dobbiamo usare un divisore
            # all-0s.
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
        # incrementiamo pick per muoverci in avanti
        pick += 1
 
    # Per gli ultimi n bits, eseguiamo l'operazione
    # conclusiva onde evitare di avere un errore del tipo Index Out of Bound
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword
 
# Funzione usata dal lato mittente per applicare il CRC
# appendendo il resto della divisione
# al termine del messaggio.
def encodeData(data, key):
 
    l_key = len(key)
 
    # Appende n-1 zeri al termine del messaggio
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    # Appende il resto al messaggio originale
    codeword = data + remainder
    return codeword   
     
server_address = ('localhost', 10000)   
# Creiamo il socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Definiamo la porta su cui collegarci
port = 12345           
 

 
input_string = input("Enter data you want to send->")
#s.sendall(input_string)
data =(''.join(format(ord(x), 'b') for x in input_string))
print("Entered data in binary format :",data)
key = "1001"
 
ans = encodeData(data,key)
print("Encoded data to be sent to server in binary format :",ans)
s.sendto(ans.encode(),('127.0.0.1', port))
 

# receviamo i dati dal server
print("Received feedback from server :",s.recv(1024).decode())
 
# chiudiamo la connessione
s.close()