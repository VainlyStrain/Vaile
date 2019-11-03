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
from core.Core.colors import *
links = []

info = "Perform a reverse IP lookup using a free API."
searchinfo = "Reverse IP Lookup"
properties = {}

def revip(web):

    web = web.replace('http://','')
    web = web.replace('https://','')
    print(R+'\n   ===================================')
    print(R+'    R E V E R S E   I P   L O O K U P')
    print(R+'   ===================================\n')
    time.sleep(0.4)
    print('' + GR + color.BOLD + ' [!] Looking Up for Reverse IP Info...')
    time.sleep(0.4)
    print(""+ GR + color.BOLD + " [~] Result : \n"+ color.END)
    domains = [web]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/reverseiplookup/?q=' + dom).text
        result = str(text)
        res = result.splitlines()
        if 'error' not in result:
            for r in res:
                print(O+' [+] Site :> '+G+r)
                links.append(r)
                time.sleep(0.04)

            p = 'tmp/logs/'+web+'-logs/'+str(web)+'-reverse-ip.lst'
            open(p,'w+')
            print(B+' [!] Saving links...')
            time.sleep(1)
            for m in links:
                m = m + '\n'
                ile = open(p,"a")
                ile.write(m)
                ile.close()
            pa = os.getcwd()
            print(G+' [+] Links saved under '+pa+'/'+p+'!')
            print('')

        elif 'error' in result:
            print(R+' [-] Outbound Query Exception!')
            time.sleep(0.8)

def attack(web):
    revip(web)