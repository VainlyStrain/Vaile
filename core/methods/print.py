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

import os
import time
from time import sleep

from core import variables as vars
from core.Core.colors import *


def loadstyle():
    os.system('clear')
    red_bold = R
    reset = W
    loading = "Vaile Attack Load."
    action = 0
    while action < 2:
        for i, char in enumerate(loading):
            if i == 0:
                print("%s%s%s%s" % (red_bold, char.swapcase(), reset, loading[1:]))
            elif i == 1:
                old_loading = loading[0].swapcase()
                print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[2:]))
            elif i == i:
                # old_loading = loading[-0:i].swapcase()
                old_loading = loading[-0:i]
                print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[i + 1:]))
            time.sleep(0.1)
            os.system('clear')
        action += 1



vaile = """\033[1m
                      .   
                      .   
                      .   
                      .   
                      .   
\033[0m____, __          \033[1m \033[0m \033[1m ..   
   + ;               ..   
   .:,                       
     ’                      
    .              ;      
    + ;           :,      
    ;.           ,,       
     ;          ,;, ' .   
     ;         .;;. ;     
     ’      ;  . ;..      
          ';. '           
         .;...,           
    ~   Vaile Attack : saarsec   ~        
    \033[1;31m~  fork from\033[0m\033[1m Infected Drake  ~    
              .'.         
  5 Phases  |  \033[1;31mv {}  |  \033[0m\033[1m108 Modules
                ;.        
                 .,.      
                   .'.    
                  ''.;:     
                    ...   
                     : .  
                     .    
""".format(vars.version)


def banner():
    os.system("clear")
    print(vaile)


def bannerbelow():
    print("\n")
    # print(B+'  [       '+C+'The Vaile Framework  \033[36m|  \033[1;37mVersion '+open('doc/Version_Num').read().strip()+'       \033[1;34m]  ')
    # sleep(0.2)
    # print(B+'  [                                                  ]  ')
    print(B + '  [           ~   Vaile Attack : saarsec   ~         ]  ')
    sleep(0.1)
    print(B + '  [           ' + O + '\033[1;31m~  fork from\033[0m\033[1m Infected Drake  ~         ]  ')
    sleep(0.1)
    print(B + '  [                                                  ]  ')
    sleep(0.1)
    print(B + '  [    5 Phases  |  \033[1;31m14 Sub-Phases  |  \033[0m\033[1m108 Modules    ]  ')
    sleep(0.1)
    print('')
    sleep(0.1)
    print(B + '         Vaile Attack Framework Console ({})'.format(vars.version))
    sleep(0.1)
    print(B + '      Vaile Attack is a fork of TIDoS by ' + R + 'Vainly(saarsec)\n\033[0m\033[1m')


def printLegal():
    print("[!] Legal disclaimer: Usage of Vaile for "
          "attacking targets without prior mutual consent is illegal. It is the end "
          "user's responsibility to obey all applicable local, state and federal "
          "laws. Developers assume no liability and are not responsible for any "
          "misuse or damage caused by this program.\n")


def info():
    print('''
 \033[4mVaile\033[4;1m Attack \033[0m\033[1m

  Avail. Cmds (M needs loaded modvle):

    attack    Attack specified target(s)             [M]
    clear     Clear terminal.                         :
    creds     Handle target credentials.              
    find      Search a module.                        :
    help      Show help message.                      :
    info      Show description of current module.    [M]
    intro     Display Intro.                          :
    ip        Show network information.               :
    leave     Leave module.                          [M]
    list      List all modules of a category.         :
    load      Load module.                            :
    opts      Show options of current module.        [M]
    phpsploit Load the phpsploit framework.           :
              (needs to be downloaded externally)
    q         Terminate Vaile session.                :
    sessions  Interact with cached sessions.          :
    set       Set option value of module.            [M]
    vicadd    Add Target to list.                     :
    vicdel    Delete Target from list.                :
    viclist   List all targets.                       :
''')


def disclaimer():
    print("""
DISCLAIMER
----------

Vaile Attack was provided as an open-source, royalty-free penetration testing toolkit. It has capable modules in various phases which can unveil potential dangerous flaws in various web-applications which can further be exploited maliciously. Therefore the author as well as the contrbutors assume no liability for misuseof this toolkit. Usage of Vaile Attack for testing or exploiting websites without prior mutual consent can be considered as an illegal activity. It is the final user's responsibility to obey all applicable local, state and federal laws.  
            """)
