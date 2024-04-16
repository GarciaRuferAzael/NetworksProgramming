#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:47:29 2023

@authors: Andrea PIRODDi, Franco CALLEGATI, Roberto GIRAU
"""

# Importiamo il modulo socket
import socket           
#definiamo la funzione XOR 
def xor(a, b):
 
    # initializziamo la lista che chiamiamo result
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
 
# Funzione usata dal lato ricevente per calcolare il resto
# della divisione.
def decodeData(codeword, key):
     
    remainder = mod2div(codeword, key)
    return remainder   
     
# Creiamo un oggetto socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       
key = "1001"
# Definiamo la porta su cui vogliamo metterci in ascolto
port = 12345           
server_address = ('localhost',port)
print ('\n\r starting up on %s port %s' % server_address)
s.bind(server_address) 

while True:
    print('\n\r waiting to receive message...')
    data, address = s.recvfrom(1024)

    print('received %s bytes from %s' % (len(data), address))
    print (data.decode())
    print(decodeData(data.decode(),key))
    if decodeData(data.decode(),key)=='0'*(len(key)-1):
        ans="it's ok"
        print(ans)
        s.sendto(ans.encode(),(address))
    else:
        print("it's not ok")


 
# chiudiamo la connessione
s.close()