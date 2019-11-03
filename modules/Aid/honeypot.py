#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import socket
import requests
import time
from core.Core.colors import *
from files.API_KEYS import SHODAN_API_KEY

info = "This module calculates the probability that the target is a honeypot using Shodan HoneyScore."
searchinfo = "HoneyScore Calculator"
properties = {}

def honeypot(web):

    print(R+'    ===================================')
    print(R+'     H O N E Y P O T   D E T E C T O R')
    print(R+'    ===================================')
    print(GR+' [*] Configuring APi request...')
    time.sleep(0.7)
    print(O+' [!] Reading APi Key...')
    if SHODAN_API_KEY != '':
        print(G+' [+] Key Found : '+O+SHODAN_API_KEY)
        web0 = web.split('//')[1]
        ip = socket.gethostbyname(web0)
        honey = "https://api.shodan.io/labs/honeyscore/"+ip+"?key="+SHODAN_API_KEY
        req = requests.get(honey).text
        read = float(req)
        if read < 5.0:
            print(G+' [+] Target does not seem to be a potential Honeypot...')
            print(G+' [+] Honey Score : '+O+str(read*100)+'%')

        else:
            print(R+' [-] Potential Honeypot Detected!')
            print(R+' [+] Honey Score : '+O+str(read*100)+'%')

    else:
        print(R+' [-] Shodan APi key not set!')
        print(R+' [-] Cannot use this module!')

def attack(web):
    honeypot(web)