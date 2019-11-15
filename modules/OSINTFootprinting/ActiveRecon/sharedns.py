#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import time
import requests
import os
from os import system
from core.Core.colors import *

info = "Discovers hosts on the same DNS server."
searchinfo = "DNS Shared Hostnames"
properties = {}

def sharedns(web):

    web = web.split('//')[1]
    #print(R+'\n    =========================================')
    #print(R+'     S H A R E D   D N S   H O S T N A M E S ')
    #print(R+'    =========================================\n')
    from core.methods.print import posintact
    posintact("shared dns hostnames") 
    print(O+' [!] Looking up for name servers on which website is hosted...\n'+G)
    time.sleep(0.7)
    system('dig +nocmd '+web+' ns +noall +answer')
    h = input(O+'\n [*] Enter any DNS Server from above :> ')
    time.sleep(0.4)
    print(GR + ' [!] Discovering hosts on same DNS Server...')
    time.sleep(0.4)
    print(GR +" [~] Result: \n"+ color.END)
    domains = [h]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/findshareddns/?q=' + dom).text
        dns = str(text)
        if 'error' in dns:
            print(R+' [-] Outbound Query Exception!\n')
            time.sleep(0.8)
        elif 'No results found' in dns:
            print(R+' [-] No shared DNS nameserver hosts...')
        else:
            p = dns.splitlines()
            for i in p:
                print(O+' [+] Site found :> '+G+i)
                time.sleep(0.02)

def attack(web):
    sharedns(web)