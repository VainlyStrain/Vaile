#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import time
import os
import sys
sys.path.append('tmp/')
import requests
from core.Core.colors import *

final_links = []

info = "Find Links pointing to the target."
searchinfo = "Page Links"
properties = {}

def links(web):

    print(R+'\n   =====================')
    print(R+'    P A G E   L I N K S ')
    print(R+'   =====================\n')
    time.sleep(0.4)
    print('' + GR + color.BOLD + ' [!] Fetching links to the website...')
    time.sleep(0.4)
    print(GR +" [~] Result: "+ color.END)
    web0 = web.replace('http://','')

    domains = [web]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/pagelinks/?q=' + dom).text
        result = str(text)
        if 'error' not in result and 'no links found' not in result:

            woo = result.splitlines()
            for w in woo:
                if str(web0).lower() in w.lower():
                    final_links.append(w)

            print(O+'\n [!] Receiving links...')
            for p in final_links:
                print(G+' [+] Found link : '+O+p)
                time.sleep(0.06)

            if 'http://' in web:
                po = web.replace('http://','')
            elif 'https://' in web:
                po = web.replace('https://','')
            p = 'tmp/logs/'+po+'-logs/'+str(po)+'-links.lst'
            open(p, 'w+')
            print(B+' [!] Saving links...')
            time.sleep(1)
            for m in final_links:
                m = m + '\n'
                ile = open(p,"a")
                ile.write(m)
                ile.close()
            pa = os.getcwd()
            print(G+' [+] Links saved under '+pa+'/'+p+'!')
            print('')

        else:
            print(R+' [-] Outbound Query Exception!')
            time.sleep(0.8)

def attack(web):
    links(web)