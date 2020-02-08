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
import random
from time import sleep
from datetime import datetime

from core import variables as vars
from core.Core.colors import *


def loadstyle():
    os.system('clear')
    red_bold = R
    cursive = color.END + "\033[3m"
    reset = cursive
    loading = "Loading console.."
    swappy = "Loading console.."
    display = """





____, __{}
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}V A I L E{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
    """.format(color.END, R, color.END, RB, color.END, R, C, cursive, swappy, color.END)
    #loading = "——·‹› Vaile ‹›·——"
    action = 0
    while action < 2:
        for i, char in enumerate(loading):
            if i == 0:
                swappy = "%s%s%s%s" % (red_bold, char.swapcase(), reset, loading[1:])
                #print("%s%s%s%s" % (red_bold, char.swapcase(), reset, loading[1:]))
            elif i == 1:
                old_loading = loading[0].swapcase()
                swappy = "%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[2:])
                #print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[2:]))
            elif i == i:
                old_loading = loading[-0:i]
                swappy = "%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[i + 1:])
                #print("%s%s%s%s%s" % (old_loading, red_bold, char.swapcase(), reset, loading[i + 1:]))
            display = """





____, __{}
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}V A I L E{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
            """.format(color.END, R, color.END, RB, color.END, R, C, cursive, swappy, color.END)
            print(display)
            time.sleep(0.1)
            os.system('clear')
        action += 1



vaile = '''{}                      |
                      :   
                      |   
                      .   
                      .   
                      .   
____, __             .|   
   + ;               .|   
   .{}:,                       
     ’                      
    .              /      
    + ;           :,      
    ;.           /,       
   {}  ;          /;' ;    
     ;         /;{}|{}  : ^  
     ’      /  . ;..  °   
          '/; '           
         ./ '.        
          '.  ’
         {}   '.
              \\
              .\\.    
                \\.               
                 .,.      
                   .'.    
                  ''.;:     
                    .|.   
                     | .  
                     .    
'''.format(color.END, color.BOLD, color.END, color.CURSIVE, color.END, color.BOLD)

vaile = '''{}                      |
                      :   
                      |   
                      .   
                      .   
                      .   
____, __             .|   
   + ;               .|   
   .{}:,                       
     ’                      
    .              /      
    + ;           :,      
    ;.           /,       
   {}  ;          /;' ;    
     ;         /;{}|{}  : ^  
     ’      / {}:{}  ;..  °   
          '/; \\           
         ./ '. \\      {}|{}
          '.  ’·    __\\,_
         {}   '.      {}\\{}`{};{}{} 
              \\      {}\\ {}
              .\\.     {}V{}   
                \\.               
                 .,.      
                   .'.    
                  ''.;:     
                    .|.   
                     | .  
                     .    
'''.format(color.END, color.BOLD, color.END, color.CURSIVE, color.END, color.CURSIVE, color.END, color.CURSIVE, color.END, color.BOLD, color.END, color.BOLD, color.CURSIVE, color.END, color.BOLD, color.END, color.BOLD, color.END, color.BOLD)

sp00k70b3r = """
      ___
     /   \\
    / O O \\       _ __         
   |   O   |     /// / _   _   _ _ __ 
 , |       | ,  / ` /,'o| /o| /o|\\V / 
  \\/(     )\\/  /_n_/ |_,7/_,'/_,' )/  
   | )   ( |            //  //   //    
   |(     )|      ___
   ||   | |'    ,' _/ _   _   _   /7  /7  _   /7  __ _ 
   `|   | |    _\\ `. /o|,'o|,'o| //_7/_7,'o| /o\\,'o///7
    |   | |   /___,'/_,'|_,'|_,'//\\\\//  |_,'/_,'|_(//  
    |   /-'        //        
    |_.'    
""" 

christmas = """\033[1m
               ,--.
              (:.. )
           ,--.`--'
          (:.. )'""`.
           `--/`.__,'
             f f                      .-.   .-..----..----. .----..-.  .-. 
            ,'.`.                     |  `.'  || {_  | {}  }| {}  }\\ \\/ / 
        _,-'  :  `-._                 | |\\ /| || {__ | .-. \\| .-. \\ }  {  
        `-._ .:. _,-'                 `-' ` `-'`----'`-' `-'`-' `-' `--' 
            ) :.(          .---. .-. .-..----. .-. .----..---. .-.   .-.  .--.   .----.
        _,-' .:  `-._     /  ___}| {_} || {}  }| |{ {__ {_   _}|  `.'  | / {} \\ { {__  
       '-._  .:.  _,-`    \\     }| { } || .-. \\| |.-._} } | |  | |\\ /| |/  /\\  \\.-._} }
           )  :  (         `---' `-' `-'`-' `-'`-'`----'  `-'  `-' ` `-'`-'  `-'`----' 
       _,-'..::.  `-._
       `-._  .:   _,-'
           `. : ,'
         _,-' : `-._
         `-. .:. ,-'
            \\ . /
             `v' 

"""

currentMonth = datetime.now().month
currentDay = datetime.now().day

def f00l():
    return

def banner():
    os.system("clear")
    if currentMonth == 10:
        print(sp00k70b3r)
    elif currentDay == 1 and currentMonth == 4:
        f00l()
    elif currentDay in [24,25,26] and currentMonth == 12:
        print(christmas)
    else:
        print(vaile)

def randomsg():
    with open("files/ms.lst","r") as msg_list:
        return random.choice(msg_list.readlines()).strip()

def bannerbelownew():
    #print("   Vaile {}{}{}".format(color.END, RB, vars.e_version) + C)
    print("   Vaile{}{}{}{}{}{}{}{}{}{}".format(color.END, color.TR6, color.END, RB, vars.e_version.split("#")[0],C,color.TR3,G,vars.e_version.split("#")[1],color.TR2) + C)
    print("  {}{}{}".format(RC, randomsg(), color.END))

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
  print('''\033[4m  \033[0m\033[1m                                                    \033[4m  \033[0m\033[1m
 !  attack    Attack specified target(s)              M
 :  clear     Clear terminal.                         :
 V  creds     Handle target credentials.              
 :  fetch     Check for and install updates.          :
 :  find      Search a module.                        :
    help      Show help message.                      :
    info      Show description of current module.     M
 :  intro     Display Intro.                          :
 :  leave     Leave module.                           M
    list      List all modules of a category.         :
 :  load      Load module.                            :
 :  netinfo   Show network information.               :
 :  opts      Show options of current module.         M
    phpsploit Load the phpsploit framework.           :
              (needs to be downloaded externally)
 :  processes Set number of processes in parallelis.  :
    q         Terminate Vaile session.                :
 :  sessions  Interact with cached sessions.          :
 :  set       Set option value of module.             M
 :  tor       Pipe Attacks through the Tor Network.   :
    vicadd    Add Target to list.                     :
    vicdel    Delete Target from list.                :
    viclist   List all targets.                       :

  \033[4mAvail. Cmds\033[0m\033[1m
    M needs loaded modvle
    V [! potentially] need loaded target(s)
''')


def disclaimer():
    print("""
DISCLAIMER
----------

Vaile Attack was provided as an open-source, royalty-free penetration testing toolkit. It has capable modules in various phases which can unveil potential dangerous flaws in various web-applications which can further be exploited maliciously. Therefore the author as well as the contrbutors assume no liability for misuseof this toolkit. Usage of Vaile Attack for testing or exploiting websites without prior mutual consent can be considered as an illegal activity. It is the final user's responsibility to obey all applicable local, state and federal laws.  
            """)

def title(mod):
    return " ".join(mod[i].upper() for i in range(0, len(mod)))

def posintpas(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T   P A S S I V E{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def posint(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def posintact(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}O S I N T   A C T I V E{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\    
""".format(color.END, C, RC, title(mod), C))

def psploit(mod):
    print("""
      ,--.!,
   __/   -*-    {}S P L O I T{}
 ,d08b.  '|`
 0088MM     {}{}{}
 `9MMP'  
""".format(color.END, C, RC, title(mod), C))

def pvln(mod):
    print("""
   (
   '\\
  '  )       {}V L N Y S I S{}
##-------->     
  .  )       {}{}{}
   ./
   (
""".format(color.END, C, RC, title(mod), C))

def pscan(mod):
    print("""
       /\\
      /  \\
     /    \\   {}S C A N N I N G   &{}
    /      \\
   /        \\   {}E N U M E R A T I O N{}
  /          \\
 / /\\/\\  /\\/\\ \\   {}{}{}
/ /    \\/    \\ \\
\\/            \\/
""".format(color.END, C, color.END, C, RC, title(mod), C))

def pbrute(mod):
    print("""
 .--.
/.-. '----------.   {}B R U T E F O R C E{}
\\'-' .--"--""-"-'       {}{}{}
 '--'
""".format(color.END, C, RC, title(mod), C))

def pleak(mod):
    print("""
   ,_       
 ,'  `\\,_   
 |_,-'_)    
 /##c '\\  (   {}I N F D I S C{}
' |'  -{{.  )
  /\\__-' \\[]        {}{}{}
 /`-_`\\     
 '     \\ 
""".format(color.END, C, RC, title(mod), C))

def cprint(text1, text2):
    print(RC + text1 + color.END + RB + text2 + color.END)


def progressbar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s [%s] %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def summary(module, msg):
    display = """





{}____, __
   + ;    
   .:,    
     ’    
    .     {}‹›{}  {}{}{}  {}‹›{}
    + ;   {}{}{}
    ;.    
     ;
     ;
     ’   
    """.format(color.END, R, color.END, RB, title(module), color.END, R, C, color.CURSIVE, msg, color.END)
    print(display)
