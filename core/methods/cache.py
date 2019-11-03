#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;    
    , ;   
     .   
           
       .    
     .;.    
     .;  
      :  
      ,   
       

┌─[Vaile]─[]
└──╼ VainlyStrain
"""


import core.variables as vars

def load(i):
    targets = []
    with open("core/sessioncache/{}".format(i),"r") as f:
        targets = [line.rstrip("\n") for line in f]
    for vic in targets:
        vars.targets.append(vic)

    
def save(i):
    with open("core/sessioncache/{}".format(i),"w") as f:
        for vic in vars.targets:
            f.write(vic)
            f.write("\n")
