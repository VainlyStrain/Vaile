#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;.    
    , ;.    
     . :,  
     ;'.    
      ..    
     .;.    
      .;  
       :  
       ,   
       

┌─[Vaile]─[]
└──╼ VainlyStrain
"""

import os

global modir
global sploidir
global aidir
global pasdir
global acdir
global vlndir
global scadir
global infdir
global phpsploit

global ai
global op
global oa
global od
global sc
global sc1
global sc2
global sp
global vam
global vao
global vas

global dlist
global interface

version = "2.1"
e_version = "2.1.5-1#dev"
module = ""
targets = []
processes = 8
interface = "wlp4s0"
tor = False
initip = ""

modir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/"
sploidir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/SploitLoot/"
scadir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/ScanningEnumeration/"
pasdir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/OSINTFootprinting/PassiveRecon/"
acdir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/OSINTFootprinting/ActiveRecon/"
infdir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/OSINTFootprinting/InfoDisclose/"
vlndir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/VlnAnalysis/"
aidir = os.path.dirname(os.path.realpath(__file__)) + "/../modules/Aid/"
phpsploit = os.path.dirname(os.path.realpath(__file__)) + "/../../phpsploit/phpsploit"

ai = "modules.Aid."
op = "modules.OSINTFootprinting.PassiveRecon."
oa = "modules.OSINTFootprinting.ActiveRecon."
od = "modules.OSINTFootprinting.InfoDisclose."
sc = "modules.ScanningEnumeration."
sc1 = "modules.ScanningEnumeration.0x01-PortScanning."
sc2 = "modules.ScanningEnumeration.0x02-WebCrawling."
sp = "modules.SploitLoot."
vam = "modules.VlnAnalysis.Misconfig."
vao = "modules.VlnAnalysis.Other."
vas = "modules.VlnAnalysis.Severe."

dlist = [ai, op, oa, od, sc, sc1, sc2, sp, vam, vao, vas]
