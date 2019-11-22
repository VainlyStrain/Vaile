#!/usr/bin/env python3
# -*- coding : utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This script is a part of Vaile Framework
#https://github.com/VainlyStrain/Vaile


from scapy.all import *
import sys
from datetime import datetime
import time
import socket
from time import sleep
from time import strftime
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from multiprocessing import Pool, TimeoutError
from core.methods.multiproc import listsplit
from core.variables import processes
from core.Core.colors import *

info = "XMAS Scanner."
searchinfo = "XMAS Scanner"
properties = {}

def scanport(port, verbose, ip_host): # Function to scan a given port
    closed = []
    filtered = []
    open = []
    try:
        srcport = RandShort()
        conf.verb = 0
        if verbose:
            print(C+' [*] Sending FIN flagged packet to port : ' + str(port))
        xmas_scan_resp = sr1(IP(dst=ip_host)/TCP(sport = srcport, dport=port,flags="FPU"),timeout=10)
        if verbose:
            print(B+' [*] Receiving incoming packet from port : ' + str(port))
            print(B+' [*] Extracting the received packet...')
        try:

            if (str(type(xmas_scan_resp))=="<type 'NoneType'>"):
                print("\033[1;92m [+] Port \033[33m%s \033[1;92mdetected Open..." % port)
                open.append(port)

            elif(xmas_scan_resp.haslayer(TCP)):
                if(xmas_scan_resp.getlayer(TCP).flags == 0x14):
                    if verbose:
                        print(R+" [!] Port %s detected Closed..." % port)
                    closed.append(port)
                    pass

            elif(xmas_scan_resp.haslayer(ICMP)):
                if(int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                    if verbose:
                        print("\n\033[1;32m [!] Port \033[33m%s \033[1;92mdetected Filtered !" % port)
                    filter.append(port)
        except:
            pass

    except KeyboardInterrupt: # In case the user needs to quit

        print('\033[91m [*] User requested shutdown...')
        print(" [*] Exiting...")
        quit()
    return (open, filtered, closed)

def portloop(portlist, verbose, ip_host):
    closed = []
    open = []
    filtered = []
    for port in portlist:
        res = scanport(port, verbose, ip_host)
        closed += res[2]
        filtered += res[1]
        open += res[0]
    return (open, filtered, closed)

def scan0x00(target):
    try:

        #print(R+'\n        ===================')
        #print(R+'         X M A S   S C A N ')
        #print(R+'        ===================\n')
        from core.methods.print import pscan
        pscan("xmas scan")
        print(R+'   [Reliable only in LA Networks]\n')
        min_port = input(O+" [#] Enter Minumum Port Number -> ")
        max_port = input(O+" [#] Enter Maximum Port Number -> ")
        openfil_ports = []
        filter_ports = []
        closed_ports = []
        ip_host = socket.gethostbyname(target)
        chk = input(C+' [#] Do you want a verbose output? (enter if not) :> ')
        verbose = chk is not ""

        try:
            print(GR+' [*] Checking port range...')
            if int(min_port) >= 0 and int(max_port) >= 0 and int(max_port) >= int(min_port) and int(max_port) <= 65536:
                print(G+'\033[1;32m [+] Port range detected valid...')
                time.sleep(0.3)
                print(GR+' [*] Preparing for the the FIN Scan...')
                pass
            else:
                print(R+"\n [!] Invalid Range of Ports")
                print(" [!] Exiting...")
                quit()
        except Exception: # If input range raises an error
            print("\n\033[91m [!] Invalid Range of Ports")
            print(" [!] Exiting...")
            quit()


        ports = range(int(min_port), int(max_port)+1) # Build range from given port numbers
        prtlst = listsplit(ports, round(len(ports)/processes))
        starting_time = time.time() # Start clock for scan time
        SYNACK = 0x12 # Set flag values for later reference
        RSTACK = 0x14

        def checkhost(ip): # Function to check if target is up
            conf.verb = 0 # Hide output
            try:
                ping = sr1(IP(dst = ip)/ICMP()) # Ping the target
                print("\n\033[1;32m [!] Target server detected online...")
                time.sleep(0.6)
                print(' [*] Beginning scan...')
            except Exception: # If ping fails
                print("\n\033[91m [!] Couldn't Resolve Target")
                print(" [!] Exiting...")
                quit()

        checkhost(ip_host) # Run checkhost() function from earlier
        print(G+" [*] Scanning initiated at " + strftime("%H:%M:%S") + "!\n") # Confirm scan start

        with Pool(processes=processes) as pool:
            res = [pool.apply_async(portloop, args=(l,verbose,ip_host,)) for l in prtlst]
            #res1 = pool.apply_async(portloop, )
            for i in res:
                j = i.get()
                openfil_ports += j[0]
                filter_ports += j[1]
                closed_ports += j[2]

        print("\n [!] Scanning completed at %s" %(time.strftime("%I:%M:%S %p")))
        ending_time = time.time()
        total_time = ending_time - starting_time
        print(GR+' [*] Preparing report...\n')
        time.sleep(1)
        #print(O+'    +-------------+')
        #print(O+'    | '+R+'SCAN REPORT '+O+'|')
        print(O+'      '+R+'SCAN REPORT '+O+' ')
        #print(O+'    +-------------+')
        print(O+'    ––·‹›·––·‹›·–––')
        #print(O+'    |')
        print()
        print(O+'    +--------+------------------+')
        print(O+'    |  '+GR+'PORT  '+O+'|       '+GR+'STATE      '+O+'|')
        print(O+'    +--------+------------------+')

        if openfil_ports:
            for i in sorted(openfil_ports):

                c = str(i)
                if len(c) == 1:
                    print(O+'    |   '+C+c+O+'    |       '+G+'OPEN       '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 2:
                    print(O+'    |   '+C+c+'   '+O+'|       '+G+'OPEN       '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 3:
                    print(O+'    |  '+C+c+'   '+O+'|       '+G+'OPEN       '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 4:
                    print(O+'    |  '+C+c+'  '+O+'|       '+G+'OPEN       '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 5:
                    print(O+'    | '+C+c+'  '+O+'|       '+G+'OPEN       '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)

        if filter_ports:
            for i in sorted(filter_ports):
                c = str(i)
                if len(c) == 1:
                    print(O+'    |   '+C+c+O+'    |     '+GR+'FILTERED     '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 2:
                    print(O+'    |   '+C+c+'   '+O+'|     '+GR+'FILTERED     '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 3:
                    print(O+'    |  '+C+c+'   '+O+'|     '+GR+'FILTERED     '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 4:
                    print(O+'    |  '+C+c+'  '+O+'|     '+GR+'FILTERED     '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)
                elif len(c) == 5:
                    print(O+'    | '+C+c+'  '+O+'|     '+GR+'FILTERED     '+O+'|')
                    print(O+'    +--------+------------------+')
                    time.sleep(0.2)

        else:
            print(''+R+" [-] No filtered ports found.!!"+O+'')
        print(B+"\n [!] " + str(len(closed_ports)) + ' closed ports not shown')
        print(O+" [!] Host %s scanned in %s seconds\n" %(target, total_time))


    except KeyboardInterrupt: # In case the user wants to quit
        print("\n\033[91m [*] User Requested Shutdown...")
        print(" [*] Exiting...")
        quit()

def xmasscan(web):
    print(GR+' [*] Loading scanner...')
    time.sleep(0.5)
    if 'http://' in web:
        web = web.replace('http://','')
    elif 'https://' in web:
        web = web.replace('https://','')
    else:
        pass
    scan0x00(web)

def attack(web):
    xmasscan(web)