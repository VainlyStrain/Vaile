#!/usr/bin/env python3
# coding:  utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os, requests, time
from time import sleep
from core.Core.colors import *

info = "Ping/NPing Enumeration."
searchinfo = "(N)Ping Enumeration"
properties = {}

def piwebenum(web):

    time.sleep(0.4)
    web = web.split('//')[1]
    #print(R+'\n   =============================================')
    #print(R+'    P I N G / N P I N G   E N U M E R A T I O N')
    #print(R+'   =============================================\n')
    from core.methods.print import posintact
    posintact("(n)ping enumeration") 
    print(GR + ' [!] Pinging website...')
    time.sleep(0.5)
    print(O+' [*] Using adaptative ping and debug mode with count 5...')
    time.sleep(0.4)
    print(GR+' [!] Press Ctrl+C to stop\n'+C)
    os.system('ping -D -c 5 '+ web)
    print('')
    time.sleep(0.6)
    print(O+' [*] Trying NPing (NMap Ping)...')
    print(C+" [~] Result: \n")
    print('')
    text = requests.get('http://api.hackertarget.com/nping/?q=' + web).text
    nping = str(text)
    print(G+ nping +'\n')

def attack(web):
    piwebenum(web)