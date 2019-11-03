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

info = "Displays the robots.txt/sitemap.xml file of the target."
searchinfo = "Robot/Sitemap Printer"
properties = {}

def robot(web):

    print(R+'\n   =============================')
    print(R+'    R O B O T S   C H E C K E R')
    print(R+'   =============================\n')

    url = web + '/robots.txt'
    print(' [!] Testing for robots.txt...\n')
    try:
        resp = requests.get(url).text
        m = str(resp)
        print(O+' [+] Robots.txt found!')
        print(GR+' [*] Displaying contents of robots.txt...')
        print(G+m)
    except:
        print(R+' [-] Robots.txt not found')

    print(' [!] Testing for sitemap.xml...\n')
    url0 = web + '/sitemap.xml'
    try:
        resp = requests.get(url0).text
        m = str(resp)
        print(O+' [+] Sitemap.xml found!')
        print(GR+' [*] Displaying contents of sitemap.xml')
        print(G+m)
    except:
        print(R+' [-] Sitemap.xml not found')

def attack(web):
    robot(web)