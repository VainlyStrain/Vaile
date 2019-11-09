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
from core.Core.colors import *

info = "Perform a WhoIS lookup on the target."
searchinfo = "WhoIS Lookup"
properties = {}

def whoischeckup(web):

    web = web.replace('http://','')
    web = web.replace('https://','')
    if "@" in web:
        web = web.split("@")[1]
    print(R+'\n   =========================')
    print(R+'    W H O I S   L O O K U P')
    print(R+'   =========================\n')
    time.sleep(0.4)
    print('' + GR + color.BOLD + ' [!] Looking Up for WhoIS Information...')
    time.sleep(0.4)
    print(""+ GR + color.BOLD + " [~] Result: \n"+ color.END)
    domains = [web]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/whois/?q=' + dom).text
        nping = str(text)
        if 'error' not in nping:
            print(G+ nping)
        else:
            print(R+' [-] Outbound Query Exception!')
            time.sleep(0.8)

def attack(web):
    whoischeckup(web)