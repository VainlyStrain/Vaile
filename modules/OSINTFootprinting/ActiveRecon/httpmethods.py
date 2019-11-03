#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import http.client
import time
from core.Core.colors import *

info = "Lists allowed HTTP methods."
searchinfo = "HTTP Methods Lister"
properties = {}

def httpmethods(web):

    try:
        print(R+'\n    =========================')
        print(R+'     H T T P   M E T H O D S ')
        print(R+'    =========================\n')

        print(GR+' [*] Parsing Url...')
        time.sleep(0.7)
        web = web.replace('https://','')
        web = web.replace('http://','')
        print(O+' [!] Making the connection...')
        conn = http.client.HTTPConnection(web)
        conn.request('OPTIONS','/')
        response = conn.getresponse()
        q = str(response.getheader('allow'))
        if 'None' not in q:
            print(G+' [+] The following HTTP methods are allowed...')
            methods = q.split(',')
            for method in methods:
                print(O+'     '+method)
        else:
            print(R+' [-] HTTP Method Options Request Unsuccessful...')

    except Exception as e:
        print(R+' [-] Exception Encountered!')
        print(R+' [-] Error : '+str(e))

def attack(web):
    httpmethods(web)