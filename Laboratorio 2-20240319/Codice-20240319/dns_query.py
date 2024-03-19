#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:26:20 2024

@author: apirodd
"""

import dns.resolver

def query_dns(domain_name):
    try:
        # Eseguire la query DNS per ottenere gli indirizzi IP associati al nome di dominio
        answers = dns.resolver.resolve(domain_name, 'A')

        # Stampare gli indirizzi IP ottenuti
        for answer in answers:
            print("Indirizzo IP per", domain_name, ":", answer.address)
    except dns.resolver.NXDOMAIN:
        print("Il dominio", domain_name, "non esiste.")
    except dns.resolver.NoAnswer:
        print("Non ci sono record associati al dominio", domain_name)
    except dns.resolver.Timeout:
        print("La query DNS per", domain_name, "è scaduta.")
    except dns.resolver.NoNameservers:
        print("Nessun server DNS disponibile per risolvere il dominio", domain_name)

def query_mx(domain_name):
    try:
        answers = dns.resolver.resolve(domain_name, 'MX')
        
        for rdata in answers:
            print("Mail exchange server for ", domain_name, ":" , rdata.exchange)
    except dns.resolver.NoAnswer:
        print("No MX records found for ", domain_name)
    except dns.resolver.NXDOMAIN:
        print("The domain ", domain_name, "does not exist")
    except dns.resolver.Timeout:
        print("DNS query for ", domain_name, "timed out")
    except dns.resolver.NoNameServers:
        print("No DNS servers avaible to resolve the domain", domain_name)

# Esempio di utilizzo
domain_name = "google.com"
query_dns(domain_name)
query_mx(domain_name)