#!/usr/bin/env python3
# coding:  utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import requests, time
from time import sleep
from core.Core.colors import *

info = "Enumerate subnets of the target's network."
searchinfo = "Subnet Enumeration"
properties = {}

def subnet(web):

    web = web.replace('http://','')
    web = web.replace('https://','')
    if "@" in web:
        web = web.split("@")[1]
    time.sleep(0.4)
    print(R+'\n   ====================================')
    print(R+'    S U B N E T  E N U M E R A T I O N')
    print(R+'   ====================================\n')
    print(GR + ' [!] Enumerating subnets in network...')
    time.sleep(0.4)
    print(GR+' [*] Getting subnet class infos...\n')
    domains = [web]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/subnetcalc/?q=' + dom).text
        #text = requests.get('https://steakovercooked.com/api/ping/?host=' + dom).text
        http = str(text)

        if 'error' not in http:
            result = http.splitlines()
            for r in result:
                print(G+' '+r.split('=')[0]+'='+O+r.split('=')[1])

        elif 'No results found' in http:
            print(R+' [-] No results found!')
        else:
            print(R+' [-] Outbound Query Exception!')

def attack(web):
    subnet(web)
