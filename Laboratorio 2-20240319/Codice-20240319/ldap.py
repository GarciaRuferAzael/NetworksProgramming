#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:52:39 2024

@author: apirodd
"""

from ldap3 import Server, Connection, SUBTREE

def ldap_search():
    ldap_server = "ldap.forumsys.com"
    server = Server(ldap_server) 

    # Connessione al server LDAP, traduce indirizzo sintattico in indirizzo IP
    ldap_conn = Connection(server, user="uid=tesla,dc=example,dc=com", password="password")
    #leggo informazioni all'interno di example.com e mi connetto con il server passando i parametri
    
    # Bind con l'utente e password specificati
    ldap_conn.bind()

    # Definizione della base di ricerca
    base_dn = "dc=example,dc=com"

    # Creazione della query di ricerca
    search_filter = "(objectclass=*)"
    #definisco che cosa voglio leggere, * cioè tutto, tutta la serie di utenti

    # Esecuzione della ricerca
    ldap_conn.search(base_dn, search_filter, SUBTREE)

    # Restituisci i risultati della ricerca
    return ldap_conn.response

# Esempio di utilizzo
search_result = ldap_search()
for entry in search_result:
    print("DN:", entry["dn"])
    print("Entry:", entry["attributes"])

