#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import sys
import requests as wrn
from core.methods.tor import session
import re
import time
from core.Core.colors import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

wrn.packages.urllib3.disable_warnings(InsecureRequestWarning)

info = "This module tries to find the domain for a given email address."
searchinfo = "Find domain from email"
properties = {}

def getRes0x00():
    requests = session()
    email = input(O+' [#] Enter the email :> '+R)
    if '@' in email and '.' in email:
        pass
    else:
        email = input(O+' [#] Enter a valid email :> '+R)

    print(GR+' [*] Setting headers... (behaving as a browser)...')
    time.sleep(0.7)
    headers =   {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
                 'Accept-Language':'en-US;',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;',
                 'Connection':'close'}
    print(O+' [!] Making the no-verify request...')
    time.sleep(0.5)
    url = "https://whoisology.com/search_ajax/search?action=email&value="+email+"&page=1&section=admin"
    result = ''
    try:
        result = requests.get(url, headers=headers, verify=False, timeout=10).content
        if result != '':
            regex = re.compile('whoisology\.com\/(.*?)">')
            stuff = regex.findall(result)
            if len(stuff) > 0:
                for line in stuff:
                    if line.strip() != '':
                        if '.' in line:
                            print(G+' [+] Received Domain : '+O+line)
            else:
                print(R+ " [-] Empty domain result for email : "+O+email)
    except:
        print(R+" [-] Can't reach url...")
        print(R+' [-] Request timed out!')

def mailtodom():

    print(GR+' [*] Loading module...')
    time.sleep(0.6)
    #print(R+'\n    ===============================')
    #print(R+'     E M A I L   T O   D O M A I N ')
    #print(R+'    ===============================\n')
    from core.methods.print import posintpas
    posintpas("email to domain")
    time.sleep(0.7)
    getRes0x00()

def attack(web):
    mailtodom()