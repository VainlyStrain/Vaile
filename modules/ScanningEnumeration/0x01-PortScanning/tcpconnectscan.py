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

info = "TCP Connect Scanner."
searchinfo = "TCP Connect Scanner"
properties = {"INIT":["Start of port range to scan.", " "], "FIN":["End of the port range to scan.", " "], "VERBOSE":["Verbose Output? [1/0]", " "]}


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

def portloop(portlist, verbose, ip_host): # Function to scan a given port
    closed = []
    open = []
    try:
        for port in portlist:
            srcport = RandShort()
            conf.verb = 0
            if verbose:
                print(C+' [*] Sending SYN flagged packet to port : ' + str(port))
                print(GR+' [*] Trying handshake...')
            tcp_connect_scan_resp = sr1(IP(dst=ip_host)/TCP(sport = srcport, dport=port,flags="S"),timeout=5)
            if verbose:
                print(GR+' [*] Receiving incoming packet from port : ' + str(port))
                print(B+' [*] Extracting the received packet...')
            try:

                if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
                    closed.append(port)
                    if verbose:
                        print(''+R+" [!] Port %s detected Closed..." % port)

                elif(tcp_connect_scan_resp.haslayer(TCP)):

                    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
                        print("\033[1;92m [!] Port \033[33m%s \033[1;92mdetected Open..." % port)
                        open.append(port)
                        if verbose:
                            print(C+' [*] Sending back a ACK flag to confirm the connection...')
                        send_rst = sr(IP(dst=ip_host)/TCP(sport=srcport, dport=port, flags="AR"),timeout=5)

                    elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
                        closed.append(port)
                        if verbose:
                            print(R+" [!] Port %s detected Closed..." % port)
            except:
                pass
        
    except KeyboardInterrupt: # In case the user needs to quit
        print('\033[91m [*] User requested shutdown...')
        print(" [*] Exiting...")
        quit()
    return (open, closed)


def scan0x00(target):

    try:

        #print(R+'\n    =================================')
        #print(R+'     T C P   C O N N E C T   S C A N ')
        #print(R+'    =================================\n')
        from core.methods.print import pscan
        pscan("tcp connect scan")
        if properties["INIT"][1] == " ":
            min_port = input(O+' [#] Enter initial port :> ')
        else:
            min_port = properties["INIT"][1]
        if properties["FIN"][1] == " ":
            max_port = input(O+' [#] Enter ending port :> ')
        else:
            max_port = properties["FIN"][1]
        open_ports = []
        closed_ports = []
        ip_host = socket.gethostbyname(target)
        if properties["VERBOSE"][1] == " ":
            chk = input(C+' [#] Do you want a verbose output? (enter if not) :> ')
            verbose = chk is not ""
        else:
            verbose = properties["VERBOSE"][1] == "1"
        print(GR+' [*] Checking port range...')
        if int(min_port) >= 0 and int(max_port) >= 0 and int(max_port) >= int(min_port) and int(max_port) <= 65536:
            print('\033[1;32m [!] Port range detected valid...')
            time.sleep(0.3)
            print(GR+' [*] Preparing for the the Scan...')

            ports = range(int(min_port), int(max_port)+1) # Build range from given port numbers
            prtlst = listsplit(ports, round(len(ports)/processes))
            starting_time = time.time() # Start clock for scan time
            SYNACK = 0x12 # Set flag values for later reference
            RSTACK = 0x14

            checkhost(ip_host) # Run checkhost() function from earlier
            print(O+" [*] Scanning initiated at " + strftime("%H:%M:%S") + "!\n") # Confirm scan start

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
            print(O+' ——·+-------------+')
            print(O+'    [ SCAN REPORT ]    conscan')
            print(O+'    +-------------+   ----------')
            print(O+'             ')
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
                print('')
            else:
                print(R+' [-] No open ports found!')

            print(O+' [!] '+ str(len(closed_ports)) + ' closed ports not shown')
            print(C+" [!] Host %s scanned in %s seconds.\n" %(target, total_time))

        else: # If range didn't raise error, but didn't meet criteria
            print("\n\033[91m [!] Invalid Range of Ports")
            print(" [!] Exiting...")
            quit()
    except Exception as e: # If input range raises an error
        print(e)
        quit()

def tcpconnectscan(web):

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
    tcpconnectscan(web)