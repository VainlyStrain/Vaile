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

import importlib as imp
import os
import re
from pathlib import Path
from socket import gaierror

import texttable as table

import core.variables as vars

from core.Core.colors import R, B, C, color

info = "Core methods for module handling."
searchinfo = ""
properties = {}

catlist = """
  all
  -----
  aid
  infdisc
  osint-active
  osint-passive
  scan
  sploit
  vlnysis  
"""

def attack(target):
    try:
        j = imp.import_module(vars.module)
        j.attack(target)
    except ImportError:
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Invalid module: {}".format(vars.module))
    except SystemExit:
        pass
    except gaierror:
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Socket Error received. This may be caused by credentials. Try creds del {}".format(target))
    except Exception as e:
        mod = vars.module.split(".")[-1]
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Module {} failed on target {}:".format(mod,target)+"\033[0m"+ color.CURSIVE +"\n{}".format(e) + C)


def set(mod, param, value):
    try:
        try:
            j = imp.import_module(vars.module)
            j.properties[param][1] = value
            print("{} > {}".format(param, value))
        except ImportError:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Incorrect module: 'properties' dictionary missing.")
    except KeyError:
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Module {} has no property {}".format(mod, param))


def display(i, names: list, descriptions: list, values: list):
    for k in i:
        names.append(k)
        descriptions.append(i[k][0])
        values.append(i[k][1])

    t = table.Texttable()
    headings = ["Name", "Desc.", "Val"]
    t.header(headings)
    t.set_deco(table.Texttable.BORDER)
    for row in zip(names, descriptions, values):
        t.add_row(row)
    s = t.draw()
    print(s + "\n")
    return names, descriptions, values


def information(mod):
    names = []
    descs = []
    vals = []
    try:
        j = imp.import_module(vars.module)
        i = j.info
        print("\n\033[4m{}\033[0m\n".format(vars.module))
        print(i + "\n\n\033[4mOptions\033[0m\n")
        i = j.properties
        names, descs, vals = display(i, names, descs, vals)
    except ImportError:
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Incorrect module: 'info' string missing.")


def opts(mod):
    names = []
    descs = []
    vals = []
    try:
        j = imp.import_module(vars.module)
        i = j.properties
        print("\n\033[4m{}\033[0m\n".format(vars.module))
        names, descs, vals = display(i, names, descs, vals)
    except ImportError:
        print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Incorrect module: 'properties' dictionary missing.")


def list(arg,display):
    names = []
    descs = []
    dir = ""

    if arg == "all":
        dir = vars.modir
    elif arg == "aid":
        dir = vars.aidir
    elif arg == "osint-passive":
        dir = vars.pasdir
    elif arg == "osint-active":
        dir = vars.acdir
    elif arg == "scan":
        dir = vars.scadir
    elif arg == "sploit":
        dir = vars.sploidir
    elif arg == "vlnysis":
        dir = vars.vlndir
    elif arg == "infdisc":
        dir = vars.infdir
    else:
        print(catlist)
        return

    for filen in Path(dir).glob("**/*.py"):
        module1 = str(filen).split(".py")[0]
        if os.name == 'nt':
            module2 = module1.split("modules/")[-1]
        else:
            module2 = module1.split("modules/")[-1]
        module2 = module2.replace("/", ".")
        module2 = module2.replace("\\", ".")
        module2 = "modules." + module2
        try:
            if (
                    "__init__" not in module2 and "colors" not in module2 and "wafimpo" not in module2 and "DNSDumpsterAPI" not in module2 and "Form" not in module2 and "uri" not in module2 and "Crawler" not in module2 and "subdom0x00" not in module2 and "errorsql" not in module2 and "blindsql" not in module2 and "files.subdom" not in module2 and "fileo.subdom" not in module2):
                j = imp.import_module(module2)
                i = j.searchinfo
                names.append(module2)
                descs.append(i)
        except ImportError:
            pass
    if display:
        t = table.Texttable()
        headings = ["Modvle", "Desc."]
        t.header(headings)
        t.set_deco(table.Texttable.BORDER)
        for row in zip(names, descs):
            t.add_row(row)
        s = t.draw()
        print("\n" + s + "\n")
    return names


def search(inp):
    names = []
    descs = []

    def filematch(id, filenames):
        patt = '.*{}.*'.format(id)
        found = []
        for filename in filenames:
            if (re.match(patt, os.path.basename(filename))):
                found.append(filename)
        return found

    filenames = []
    foundfiles = []

    idlist = inp.split(" ")
    for filen in Path(vars.modir).glob("**/*.py"):
        filenames.append(str(filen))
    for id in idlist:
        foundfiles += filematch(id, filenames)
    for filen in filenames:
        module1 = filen.split(".py")[0]
        if os.name == 'nt':
            module2 = module1.split("modules/")[-1]
        else:
            module2 = module1.split("modules/")[-1]
        module2 = module2.replace("/", ".")
        module2 = module2.replace("\\", ".")
        module2 = "modules." + module2
        # print(module2)
        try:
            if (
                    "__init__" not in module2 and "colors" not in module2 and "wafimpo" not in module2 and "DNSDumpsterAPI" not in module2 and "Form" not in module2 and "uri" not in module2 and "Crawler" not in module2 and "subdom0x00" not in module2 and "errorsql" not in module2 and "blindsql" not in module2 and "files.subdom" not in module2 and "fileo.subdom" not in module2):
                module = imp.import_module(module2)
                j = module.info
                for id in idlist:
                    if id.lower() in str(j).lower():
                        if filen not in foundfiles:
                            foundfiles.append(str(filen))
        except ImportError:
            pass
    for file in foundfiles:
        if os.name == 'nt':
            list1 = file.split("\\modules\\")
        else:
            list1 = file.split("/modules/")
        if len(list1) != 2:
            print("[-] PathError. Length: {}, expected: 2".format(len(list1)))
        else:
            parsedfile = list1[1].split(".py")[0]
            parsedfile = "modules." + parsedfile
            parsedfile = parsedfile.replace("/", ".")
            parsedfile = parsedfile.replace("\\", ".")
            try:
                if (
                        "__init__" not in parsedfile and "colors" not in parsedfile and "wafimpo" not in parsedfile and "DNSDumpsterAPI" not in parsedfile and "Form" not in parsedfile and "uri" not in parsedfile and "Crawler" not in parsedfile and "subdom0x00" not in parsedfile and "errorsql" not in parsedfile and "blindsql" not in parsedfile and "files.subdom" not in parsedfile and "fileo.subdom" not in parsedfile):
                    j = imp.import_module(parsedfile)
                    i = j.searchinfo
                    names.append(parsedfile)
                    descs.append(i)
            except ImportError:
                pass

    t = table.Texttable()
    headings = ["Modvle", "Desc."]
    t.header(headings)
    t.set_deco(table.Texttable.BORDER)
    for row in zip(names, descs):
        t.add_row(row)
    s = t.draw()
    print("\n" + s + "\n")

def bareimport(inp):
    success = False
    for i in vars.dlist:
        try:
            mod = imp.import_module(i+inp)
            #print(i+inp)
            success = True
            break
        except ImportError:
            pass
    return [success, i+inp]
