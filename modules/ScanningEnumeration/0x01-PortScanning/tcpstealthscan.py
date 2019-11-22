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
from time import sleep
from time import strftime
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from multiprocessing import Pool, TimeoutError
from core.methods.multiproc import listsplit
from core.variables import processes
from core.Core.colors import *

info = "TCP Stealth Scanner."
searchinfo = "TCP Stealth Scan"
properties = {}


def checkhost(ip): # Function to check if target is up
    conf.verb = 0 # Hide output
    try:
        ping = sr1(IP(dst = ip)/ICMP()) # Ping the target
        print("\n\033[1;32m [+] Target server detected online...")
        time.sleep(0.6)
        print(O+' [*] Beginning scan...')
    except Exception: # If ping fails
        print("\n\033[91m [!] Couldn't Resolve Target")
        print(" [!] Exiting...")
        quit()

def scanport(port, verbose, target):
    try:
        SYNACK = 0x12
        RSTACK = 0x14
        ret = False
        srcport = RandShort()
        conf.verb = 0
        if verbose:
            print(GR+' [*] Sending SYN flagged packet to port : ' + str(port))
        SYNACKpkt = sr1(IP(dst = target)/TCP(sport = srcport, dport = port, flags = "S"), timeout=5)
        if verbose:
            print(C+' [*] Receiving incoming packet from port : ' + str(port))
            print(B+' [*] Extracting the received packet...')
        try:
            pktflags = SYNACKpkt.getlayer(TCP).flags
            if pktflags == SYNACK:
                print(G+' [+] Cross Reference Flag SYN-ACK detected!')
                ret = True
            else:
                if verbose:
                    print(R+' [!] No cross reference flag detected, port possibly closed...'+R+'')
                ret = False
        except:
            pass
        if verbose:
            print(O+' [!] Constructing the RST flagged packet to be sent to reset the connection...')
            time.sleep(0.2)
        RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flags = "R")
        if verbose:
            print(C+' [!] Sending RST packet to reset the connection...')
        send(RSTpkt)
        return ret
    except KeyboardInterrupt:
        print(''+R+' [-] User requested shutdown...')
        time.sleep(0.2)
        print(O+' [*] Stopping jobs...')
        RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flags = "R")
        send(RSTpkt)
        print(R+" [*] Exiting...")
        quit()

def portloop(ports, verbose, target):
    open = []
    closed = []
    for port in ports:
        status = scanport(port, verbose, target)
        if status == True:
            print(G+" [+] Port " + O + str(port) + G+" detected Open !")
            open.append(port)
        else:
            if verbose:
                print(''+R+' [!] Port ' + str(port) + ' Closed')
            closed.append(port)
    return (open, closed)

def scan0x00(target):

    try:

        #print(R+'\n    =================================')
        #print(R+'     T C P   S T E A L T H   S C A N ')
        #print(R+'    =================================\n')
        from core.methods.print import pscan
        pscan("tcp stealth scan")
        min_port = input(O+" [#] Enter Minumum Port Number -> ")
        max_port = input(O+" [#] Enter Maximum Port Number -> ")
        open_ports = []
        closed_ports = []
        ip_host = socket.gethostbyname(target)
        chk = input(C+' [#] Do you want a verbose output? (enter if not) :> ')
        verbose = chk is not ""

        try:
            print(GR+' [*] Checking port range...')
            if int(min_port) >= 0 and int(max_port) >= 0 and int(max_port) >= int(min_port) and int(max_port) <= 65536:
                print('\033[1;32m [!] Port range detected valid...')
                time.sleep(0.3)
                print(GR+' [*] Preparing for the the Scan...')
                pass
            else:
                print("\n\033[91m [!] Invalid Range of Ports")
                print(" [!] Exiting...")
                quit()
        except Exception:
            print("\n\033[91m [!] Invalid Range of Ports")
            print(" [!] Exiting...")
            quit()

        ports = range(int(min_port), int(max_port)+1)
        prtlst = listsplit(ports, round(len(ports)/processes))
        starting_time = time.time()
        SYNACK = 0x12
        RSTACK = 0x14

        checkhost(target)
        print(O+" [*] Scanning initiated at " + strftime("%H:%M:%S") + "!\n")

        with Pool(processes=processes) as pool:
            res = [pool.apply_async(portloop, args=(l,verbose,ip_host,)) for l in prtlst]
            #res1 = pool.apply_async(portloop, )
            for i in res:
                j = i.get()
                open_ports += j[0]
                closed_ports += j[1]

        print(O+"\n [!] Scanning completed at %s" %(time.strftime("%I:%M:%S %p")))
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

        if open_ports:

            for i in sorted(open_ports):

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

        else:
            print(''+R+" [-] Sorry, No open ports found.!!")
        print(O+'\n [!] ' + str(len(closed_ports)) + ' closed ports not shown')
        print(C+" [!] Host %s scanned in %s seconds" %(target, total_time))

    except KeyboardInterrupt:
        print(R+"\n [-] User Requested Shutdown...")
        print(" [*] Exiting...")
        quit()

def tcpstealthscan(web):

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
    tcpstealthscan(web)