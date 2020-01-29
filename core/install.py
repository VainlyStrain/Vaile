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

import os

print('''\033[1m
   ___                     _                _       _    
  |_ _|   _ _      ___    | |_    __ _     | |     | |   
   | |   | ' \\    (_-<    |  _|  / _` |    | |     | |   
  |___|  |_||_|   /__/_   _\\__|  \\__,_|   _|_|_   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
''') 


print(" [+] Installing dependencies (1/2): Package Manager")
os.system("apt-get install libncurses5 libxml2 nmap tcpdump libexiv2-dev build-essential python3-pip libmariadbclient18 libmysqlclient-dev tor")

print(" [+] Installing dependencies (2/2): pip3")
os.system("pip3 install -r requirements.txt")

print(" [+] Installing Vaile...")
os.system('mkdir -v -p /opt/Vaile/')
os.system('cp -r -v ../* /opt/Vaile/')
os.system('cp -v ../tmp/Vaile /usr/bin/Vaile')
os.system('chmod -R 755 /opt/Vaile/*')
os.system('chmod -v 755 /usr/bin/Vaile')

print("Installation process complete. Run 'Vaile' to launch the framework.\033[0m")
