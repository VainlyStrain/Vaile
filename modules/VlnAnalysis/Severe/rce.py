#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import sys
import time
import re
import urllib
from urllib.request import FancyURLopener
from core.Core.colors import *
payloads = []

info = "This module probes the target for Command Injection vulnerabilities using Vaile's built-in payload dictionary."
searchinfo = "Command Injection Probe"
properties = {}

class UserAgent(FancyURLopener):
    verion = 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0'

useragent = UserAgent()

class HTTP_HEADER:
    HOST = "Host"
    SERVER = "Server"

def headread(url):
    print(GR+" [*] Testing site...\n")
    if "@" in url:
        if "https" in url:
            url2 = "https://" + url.split("@")[1]
        else:
            url2 = "http://" + url.split("@")[1]
    opener = urllib.request.urlopen(url2)
    if (opener.code == 200):
        print(G+" [+] Status: (200 - OK)")
    elif (opener.code == 401):
        print(G+" [*] Status: (401 - Unauthorized) (may be caused by temporar removal of credentials)")
    if (opener.code == 404):
        print(R+" [-] Status: Server maybe down (404)")
        sys.exit()

    Server = opener.headers.get(HTTP_HEADER.SERVER)
    Host = url.split("/")[2]
    print(C+" [+] Host: " + str(Host))
    print(B+" [+] Web server: " + str(Server))

def check0x00(url, payloads, check):

    vuln = 0

    print(GR+' [*] Starting command injection testing...')
    for params in url.split("?")[1].split("&"):
        for payload in payloads:
            vuln = False
            print(B+'\n [*] Trying payload :> '+C+str(payload))
            print(GR+' [!] Setting parameter value...')
            bugs = url.replace(params, params + str(payload).strip())
            print(O+' [*] Making the request...')
            request = useragent.open(bugs)
            print(GR+' [*] Reading response...')
            html = request.readlines()
            for line in html:
                checker = re.findall(check, line)
                if (len(checker) != 0):
                    vuln = True
                else:
                    vuln = False

            if vuln == True:
                print(G+" [+] Possible vulnerability found!")
                print(C+" [+] Payload: ", payload)
                print(R+" [+] Example PoC: " + bugs)
                vuln = vuln + 1
            else:
                print(R+' [-] No command injection flaw detected!')
                print(O+' [-] Payload '+R+payload+O+' not working!')


    if (vuln == 0):
        print(G+"\n [+] This website is damn secure. No vulnerabilities found. :)\n")
    else:
        print("\n [+] "+str(vuln)+" Bugs Found. Happy Hunting... :) \n")



def getPayloads(url):

    print(GR+' [*] Loading payloads...')
    time.sleep(0.8)
    try:
        with open('files/payload-db/rce_payloads.lst') as run:
            for p in run:
                p = p.replace('\n','')
                p = r'%s' % p
                payloads.append(p)
    except Exception as e:
        print(R+' [-] Exception: '+str(e))
    print(G+' [+] '+str(len(payloads)+1)+' Payloads loaded!')
    check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot|root|x:bin", re.I)
    check0x00(url, payloads, check)

def rce(web):

    print(R+'\n    =========================================')
    print(R+'     O S   C O M M A N D   I N J E C T I O N ')
    print(R+'    =========================================\n')
    web0 = input(O+' [#] Path Parameter '+R+'(eg. /ping.php?site=foo)'+O+' :> ')
    if "?" in web0 and '=' in web0:
        if web0.startswith('/'):
            m = input(GR+'\n [!] Your path starts with "/".\n [#] Do you mean root directory? (Y/n) :> ')
            if m == 'y' or m == 'Y':
                web00 = web + web0
            elif m == 'n' or m == 'N':
                web00 = web + web0
            else:
                print(R+' [-] U mad?')
        else:
            web00 = web + '/' + web0

        getPayloads(web00)
    else:
        print(R+" [-] Please enter the URL with parameters...")
        rce(web)

def attack(web):
    rce(web)