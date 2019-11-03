#!/usr/bin/env python3
# coding: utf-8

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile



import os
import socket
import time

import core.variables as vars
from core.Core.colors import *


def inputin(target):
    try:
        web = target
        if not str(web).startswith('http'):
            mo = input(GR + ' [?] Does this website use SSL? (y/n) :> ')
            if mo == 'y' or mo == 'Y':
                web = 'https://' + web
            elif mo == 'n':
                web = 'http://' + web
        if 'http://' in web:
            po = web.split('//')[1]
        elif 'https://' in web:
            po = web.split('//')[1]
        else:
            po = ''
        if str(web).endswith('/'):
            web = po[:-1]
            po = po[:-1]
        print(GR + ' [*] Checking server status...')
        time.sleep(0.6)

        try:
            ip = socket.gethostbyname(po)
            print(G + ' [+] Site seems to be up...')
            time.sleep(0.5)
            print(G + ' [+] IP Detected : ' + O + ip)
            time.sleep(0.5)
            print('')
            os.system('cd tmp/logs/ && rm -rf ' + po + '-logs && mkdir ' + po + '-logs/')
            user = input(" [?] Enter username (leave blank if none): ")
            passwd = input(" [?] Enter password (leave blank if none): ")
            webfin = web
            if user != "" and passwd != "":
                wl = web.split("://")
                webfin = wl[0] + "://" + user + ":" + passwd + "@" + wl[1]
            vars.targets.append(webfin)
            print(" [+] Target added: {}".format(webfin))

        except socket.gaierror:
            print(R + ' [-] Site seems to be down...')
            pass

    except KeyboardInterrupt:
        pass
