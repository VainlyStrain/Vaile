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

def sessionparse(i):
    victims = []
    modules = {}
    oneline = ""
    with open("core/sessioncache/{}".format(i), "r") as file:
        for line in file:
            oneline += line
    vicblocks = oneline.split("<victim ")[1:]
    for block in vicblocks:
        block = block.split("</victim>")[0]
        victim = block.split(">")[0].strip()
        victims.append(victim)
        vars.targets.append(victim)
        inter = block.replace(victim+">","")
        modblocks = inter.split("<module ")[1:]
        for modblock in modblocks:
            properties = {}
            module = modblock.split(">")[0].strip()
            modblock = modblock.split("</module>")[0]
            if ">" in modblock:
                modblock = modblock.split(">")[1]
            proplist = modblock.split(";")
            for proptuple in proplist:
                if ":" in proptuple:
                    prop = proptuple.split(":")[0].strip()
                    val = proptuple.split(":")[1].strip()
                    properties.update({prop : val})
            modules.update({module : properties})
    return (victims, modules)