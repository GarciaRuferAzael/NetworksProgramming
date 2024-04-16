# GO-BACK-N-Automatic Repeat reQuest

# Receiver.py
"""
Created on Thursday Apr 19 14:47:29 2023

@authors: Franco CALLEGATI, Andrea PIRODDi,Roberto GIRAU
"""
import time, socket, sys
import random
#definisco la funzione per convertire il binario in testo utf-8
def bin2text(s): return "".join([chr(int(s[i:i+8],2)) for i in range(0,len(s),8)])


#messaggio di benvenuto
print("\n Benvenuto nella Chat Room\n")
print("Inizializzazione....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Inserisci indirizzo IP del server: "))
name = input(str("\n Inserisci il tuo nome: "))
port = 1235
print("\n Tentativo di connessione al ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connesso...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "si è unito alla Chat\n Usa [e] per uscire dalla chat room\n")

while True:

    m=s.recv(1024)
    m=m.decode()
    k=s.recv(1024)
    k=k.decode()
    k=int(k)
    i=0
    a=""
    b=""
    f=random.randint(0,1)
    message=""
    while i!=k:
       
       
       f=random.randint(0,1)
       if(f==0):
          b="ACK Lost"
          message = s.recv(1024)
          message = message.decode()
          s.send(b.encode())
         
       elif(f==1):
          b="ACK "+str(i)
          message = s.recv(1024)
          message = message.decode()
          print(a)
          s.send(b.encode())
          a=a+message
          i=i+1
          
       
    
    print("Il messaggio ricevuto è :", bin2text(a))
   
