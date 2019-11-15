#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import json
import requests
import time
from core.Core.colors import *

info = "Find information about domains using CENSYS."
searchinfo = "CENSYS Domain Recon"
properties = {}

def censysdom(web):

    #print(R+'\n    =======================================')
    #print(R+'     C E N S Y S   D O M A I N   R E C O N')
    #print(R+'    =======================================\n')
    from core.methods.print import posintpas
    posintpas("censys domain recon") 

    time.sleep(0.6)
    print(GR+' [*] Importing API Key...')
    try:
        from files.API_KEYS import CENSYS_UID, CENSYS_SECRET
    except IOError as ImportError:
        print(R+' [-] Error while importing key...')

    web = web.split('//')[1]
    if "@" in web:
        web = web.split("@")[1]
    if CENSYS_SECRET != '' and CENSYS_UID != '':
        print(G+' [+] Found Censys UID Key : '+O+CENSYS_UID)
        print(G+' [+] Found Censys Secret Token : '+O+CENSYS_SECRET)
        base_url = 'https://www.censys.io/api/v1'
        print(GR+' [*] Looking up info...')
        time.sleep(0.7)
        resp = requests.get(base_url + "/view/websites/"+web, auth=(CENSYS_UID, CENSYS_SECRET))
        if 'quota_exceeded' in resp.text:
            print(R+' [-] Daily limit reached for this module. Use you own API key for CENSYS.')

        if resp.status_code == 200:

            print(G+' [+] Found domain info!')
            w = resp.text.encode('utf-8')
            asio = json.dumps(resp.json(), indent=4)
            quest = asio.splitlines()
            print(O+' [!] Parsing info...\n')
            time.sleep(1)
            for q in quest:
                q = q.replace('"','')
                if ':' in q and '[' not in q and '{' not in q:
                    q1 = q.split(':',1)[0].strip().title()
                    q2 = q.split(':',1)[1].strip().replace(',','')
                    print(C+'   [+] '+q1+' : '+GR+q2)
                    time.sleep(0.01)

                elif ('{' or '[' in q) and (':' in q):
                    w1 = q.split(':',1)[0].strip().upper()
                    w2 = q.split(':',1)[1].strip()
                    print(O+'\n [+] '+w1+' :-'+'\n')

                elif '{' not in q and '[' not in q and ']' not in q and '}' not in q:
                    print(GR+'   [+] '+q.replace(',','').strip())

            print(O+' [!] Saving retrieved CENSYS data...')
            time.sleep(1)
            with open('tmp/logs/'+web+'-logs/'+web+'-censys-data.json', 'w+') as file:
                json.dump(resp.json(), file, ensure_ascii=True,indent=4)
                eq = os.getcwd()
                print(G+' [+] Censys Data stored '+eq+'/tmp/logs/'+web+'-logs/'+web+'-censys-data.json')

        else:
            print(R+' [-] Did not find any info about domain '+O+web)
            print(R+' [+] Try with another one...')

    else:
        print(R+' [-] CENSYS API TOKENs not set!')
        print(R+' [-] This module cannot be used!')

def attack(web):
    censysdom(web)