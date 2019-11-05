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

from core.methods.select import list as modules
from core.Core.colors import R, B, C, color
import importlib as imp

info = "Launch all scan modules."
searchinfo = "ALL: scan"
properties = {}

modlist = modules("scan",False)

def attack(web):
    for module in modlist:
        try:
            if "-all" not in module:
                mod = imp.import_module(module)
                mod.attack(web)
        except ImportError:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Failed to import module: {}".format(module))
            
