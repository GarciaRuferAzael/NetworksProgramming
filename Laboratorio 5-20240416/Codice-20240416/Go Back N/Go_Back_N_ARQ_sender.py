# GO-BACK-N-Automatic Repeat reQuest

# Sender.py
"""
Created on Thursday Apr 19 14:47:29 2023

@authors: Franco CALLEGATI, Andrea PIRODDi,Roberto GIRAU
"""
import time, socket, sys
# definizione funzione di conversione decimale in binario
def decimalToBinary(n):  
    return n.replace("0b", "0")

#definizione della funzione di trasposizione da utf-8 in binario
def binarycode(s):
    a_byte_array = bytearray(s, "utf8")
    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a
#messaggio di benvenuto
print("\n Benvenuti nella Chat Room\n")
print("Inizializzazione....\n")
time.sleep(1)
#creazione del socket utilizzando làip address reale della macchina
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1235
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Inserisci il tuo nome: "))
           
s.listen(1)
print("\n In attesa di connessioni in entrata...\n")
conn, addr = s.accept()
print("Ricevuta connessione dal", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
# recupero il nome di chi si è collegato in chat
s_name = s_name.decode()
print(s_name, "si è collegato alla chat room\n Usa [e] per uscire dalla chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Io : "))
    conn.send(message.encode())
    if message == "[e]":
        message = "Abbandona la chat room!"
        conn.send(message.encode())
        print("\n")
        break
    message=binarycode(message)
    print(message)
    f=str(len(message))
    conn.send(f.encode())
   
    i=0
    j=0
    j=int(input("Inserisci la dimensione della finestra -> "))
    
   
    b=""
   
    j=j-1
    f=int(f)
    k=j
    while i!=f:
        while(i!=(f-j)):
            conn.send(message[i].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Ack RICEVUTO! La finestra scorrevole è nel range da "+(str(i+1))+" a "+str(k+1))
                print("Ora inviamo il pacchetto successivo")
                i=i+1
                k=k+1
                time.sleep(1)
            else:
                time.sleep(1)
                print("Ack del data bit NON RICEVUTO! La finestra scorrevole resta nel range da "+(str(i+1))+" a "+str(k+1))
                print("Ora reinviamo lo stesso pacchetto")
                time.sleep(1)
        while(i!=f):
            
            conn.send(message[i].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Ack RICEVUTO! La finestra scorrevole è nel range da "+(str(i+1))+" a "+str(k))
                if ((str(i+1))!=str(k)):
                    print("Ora inviamo il pacchetto successivo")
                i=i+1
                time.sleep(1)
            else:
                time.sleep(1)
                print("Ack del data bit NON RICEVUTO! La finestra scorrevole resta nel range da "+(str(i+1))+" a "+str(k))
                print("Ora reinviamo lo stesso pacchetto")
                time.sleep(1)
            
     
