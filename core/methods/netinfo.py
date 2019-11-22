

import os
import platform
import socket
import time
from urllib.request import urlopen

from core.Core.colors import *
from core.variables import interface

mac_address = os.popen("cat /sys/class/net/{}/address".format(interface)).read()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
localaddr = s.getsockname()[0]  # local subnet
ipaddr = urlopen('http://ip.42.pl/raw').read()
def_gw_device = os.popen("route | grep '^default' | grep -o '[^ ]*$'").read()


def info():
    print("\n" + O + "                     +======================================================+" + color.END)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  Mac Address: " + mac_address)
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  Local address: " + localaddr)
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  IP: " + str(ipaddr).split("'")[1])
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  Operating System: " + platform.system())
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  Name: " + platform.node())
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+")
    time.sleep(0.1)
    print("                               |" + O + color.BOLD + "  Interface: " + def_gw_device)
    # time.sleep (0.1)
    print("" + GR + "                             +------------------------------------+" + color.END)
    print("" + O + "                     +=======================================================+\n")
