#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import lxml
import os
from core.methods.tor import session
import re
import requests as wrn
import time
from bs4 import BeautifulSoup
import sys
from core.Core.colors import *
found = 0x00
urls = []
links = []

info = "This module hunts down comments in the source code. It is recommended to run the crawlers before using this module."
searchinfo = "Comment Scraper"
properties = {}

def commentssrc(web):
    requests = session()
    #print(R+'\n    =================================')
    #print(R+'     C O M M E N T S   S C R A P E R')
    #print(R+'    =================================')
    from core.methods.print import posintact
    posintact("comment scraper") 
    print(C+' [It is recommended to run ScanEnum/Crawlers')
    print(C+'       before running this module]\n')
    print(GR+' [*] Importing links...')
    po = web.split('//')[1]
    p = 'tmp/logs/'+po+'-logs/'+po+'-links.lst'
    links = [web]

    for w in links:
        print(GR+' [*] Making the request...')
        req = requests.get(w).content
        print(C+' [!] Setting parse parameters...')
        comments = re.findall('<!--(.*)-->',req)
        print(O+" [+] Searching for comments on page:"+C+color.TR3+C+G+web+C+color.TR2+C+'\n')
        for comment in comments:
            print(C+'   '+comment)
            time.sleep(0.03)
            found = 0x01

    soup = BeautifulSoup(req,'lxml')
    for line in soup.find_all('a'):
        newline = line.get('href')
        try:
            if newline[:4] == "http":
                if web in newline:
                    urls.append(str(newline))
            elif newline[:1] == "/":
                combline = web+newline
                urls.append(str(combline))
        except:
            pass
            print(R+' [-] Unhandled Exception Occured!')

    try:
        for uurl in urls:
            print(O+"\n [+] Searching for comments on page: "+C+color.TR3+C+G+uurl+C+color.TR2+C+'\n')
            req = requests.get(uurl)
            comments = re.findall('<!--(.*)-->',req.text)
            for comment in comments:
                print(C+'   '+comment)
                time.sleep(0.03)

    except wrn.exceptions:
        print(R+' [-] Outbound Query Exception...')

    if found == 0x00:
        print(R+' [-] No comments found in source code!')

    print(G+' [+] Comments Scraping Done!'+C+color.TR2+C)

def attack(web):
    commentssrc(web)