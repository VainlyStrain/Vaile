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

import importlib as imp
import os
import platform
import sys
import time
from cmd import Cmd

import core.methods.inputin as addtarget
import core.methods.print as prnt
import core.methods.select as select
import core.variables as vars
from core.Core.colors import R, B, C, color
from core.methods.cache import *
from core.methods.creds import creds


class VainShell(Cmd):
    # prompt = "\033[1;31m──·»\033[0m\033[4mVaile\033[0m\033[1;31m]─[\033[0m{}\033[1;31m]\033[0m\033[1m –› \033[
    # 0m".format(vars.module)
    intro = ""
    prompt = '\033[0m\033[1m vaile > '
    ruler = "—-"
    doc_header = "Docvmented:"
    misc_header = "Misc.:"
    undoc_header = "NoDocs:"

    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(VainShell, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                if vars.module == "":
                    print("^C\n" + R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Command 'q' to end session.")
                else:
                    print("^C")
                    self.do_leave("")

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""
        if arg:
            # XXX check arg syntax
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            prnt.info()

    def help_help(self):
        print("""
  help [?]
  ----------

  Vaile help menu.
  Syntax: ? [CMD]

    CMD: command for which more detailed help should be shown.

  If CMD is omitted, a list of all commands with its function will be shown.
""")

    def do_q(self, inp) -> bool:
        return True

    def help_q(self):
        print("""
  q
  ---

  Terminate current session and quit the program.
  [!] The session is not cached, use command 'sessions' for this.
""")

    def do_sessions(self, inp):
        if "load" in inp:
            b = vars.targets
            vars.targets = []
            #for i in vars.targets:
            #    vars.targets.remove(i)
            session = inp.split("load")[1].strip()
            if session == "":
                print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Syntax: sessions [load|save <SESS_ID>] [list]")
                vars.targets = b
            else:
                try:
                    load(session)
                    print(" [+] Restored session: {}.".format(session))
                except FileNotFoundError:
                    print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "{}: no such session file.".format(session))
                    vars.targets = b
        elif "save" in inp:
            session = inp.split("save")[1].strip()
            if session == "":
                print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Syntax: sessions [load|save <SESS_ID>] [list]")
            else:
                save(session)
        elif "list" in inp:
            os.system("\\ls core/sessioncache")
        else:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Syntax: sessions [load|save <SESS_ID>] [list]")


    def help_sessions(self):
        print("""
  sessions
  ----------

  Interact with cached sessions.
  Available commands:

    list     list all available sessions to load.
    load ID  restore session ID
    save ID  save current session as ID.
""")

    def do_clear(self, inp):
        os.system('clear')

    def help_clear(self):
        print("""
  clear
  -------

  Clear the terminal using the native 'clear' command.
""")

    def do_ip(self, inp):
        try:
            import core.methods.netinfo as netinfo
            netinfo.info()
        except:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Something went wrong. Try again later.")

    def help_ip(self):
        print("""
  ip
  ----

  Provides current network information, such as

    + your local IP
    + your public IP
    + your MAC address
""")

    def do_creds(self, inp):
        creds(inp)
        
    def help_creds(self):
        print("""
  creds
  -------

  Add or remove credentials from a specific target.
  Syntax: creds add|del target

    target: the URL which shall be operated on

  [!] the target must be formatted as in viclist.
""")

    def do_find(self, inp):
        if inp == "":
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Please enter a search term.")
        else:
            select.search(inp)

    def help_find(self):
        print("""
  find
  ------

  Search a module by providing a search term.
  The command will return any module containing the term in

    + its name
    + its description
""")

    def do_list(self, inp):
        select.list(inp,True)

    def help_list(self):
        print("""
  list
  ------

  List all modules in a specified category.
  Providing no category, list will output all availbale categories.
  Available categories:

    all           all available modules
    aid           additional tools (e.g. honeypot check)
    infdisc       information disclosure modules
    osint-active  modules for active reconnaissance
    osint-passive modules for passive reconnaissance
    scan          modules for scanning and enumeration
    sploit        exploits (in progress)
    vlnysis       modules useful for vulnerability analysis
""")

    def do_attack(self, inp):
        if vars.module == "":
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "No module loaded.")
            return None
        elif len(vars.targets) <= 0:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "No target(s) set.")
            return None
        else:
            print("\n Attack")
            print(" --------")
            for i in vars.targets:
                if len(vars.targets) > 1:
                    print( "\n [i] Target: {}\n".format(i))
                select.attack(i)

    def help_attack(self):
        print("""
  attack
  --------

  unleash the loaded module on the specified target(s)
  if no options have been specified

    + default options will be applied
    + if above not possible, user will be prompted for live input.
""")

    def do_vicadd(self, inp):
        addtarget.inputin(inp)

    def help_vicadd(self):
        print("""
  vicadd
  --------

  Add the specified URL to the target list.
""")

    def do_phpsploit(self, inp):
        try:
            # print(" [!] phpsploit is an external toolkit we cannot guarantee the benignity of.")
            # choice = input(" [?] Do you want to run phpsploit with restricted privileges? :> ")
            # if (choice.lower().startswith("n")):
            if inp == "":
                os.system("python3 {}".format(vars.phpsploit))
            else:
                os.system("sudo -u {} python3 {}".format(inp, vars.phpsploit))
        except SystemExit:
            pass
        except:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "phpsploit crashed.")

    def help_phpsploit(self):
        print("""
  phpsploit
  -----------

  Load the phpsploit post-exploitation and control framework.
  Syntax: phpsploit [user]

    user  the user who will execute phpsploit (e.g. a non-privileged user)
  
  [!] you need to change the phpsploit path in core/variables.py to point at your installation.
""")

    def do_vicdel(self, inp):
        if inp == "all":
            vars.targets = []
            print(" [+] Cleared target list.")
        else:
            old = vars.targets
            vars.targets = list(filter(lambda a: a != inp, vars.targets))
            found = old != vars.targets
            if found:
                print(" [+] Deleted Target: {}".format(inp))
            else:
                print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Could not find specified target: {}".format(inp))

    def do_viclist(self, inp):
        for i in vars.targets:
            print(i)

    def help_viclist(self):
        print("""
  viclist
  ---------

  List all targets specified for attack.
""")

    def do_intro(self, inp):
        prnt.banner()
        #prnt.bannerbelow()
        print()

    def help_intro(self):
        print("""
  intro
  -------

  Display the intro banner.
""")

    def help_vicdel(self):
        print("""
  vicdel
  --------

  Remove a target from the list.
  Syntax: vicdel TARGET

    TARGET  target to be removed

  To delete all targets, use TARGET = all.
""")

    def emptyline(self):
        pass

    def do_set(self, inp):
        listed = inp.split(" ")
        if len(listed) != 2:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Entry must contain exactly 1 space.")
        else:
            param = listed[0]
            value = listed[1]
            if vars.module != "":
                select.set(vars.module, param, value)
            else:
                print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "No module loaded.")

    def help_set(self):
        print("""
  set
  -----

  Set an attack option for the current module.
  Syntax: set OPT VAL

    OPT  name of the option to be modified
    VAL  value the option will take
""")

    def do_info(self, inp):
        if vars.module == "":
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "No module loaded.")
        else:
            select.information(vars.module)

    def help_info(self):
        print("""
  info
  ------

  Displays the description of the current module, as well as all available options.
""")

    def do_opts(self, inp):
        if vars.module == "":
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "No module loaded.")
        else:
            select.opts(vars.module)

    def help_opts(self):
        print("""
  opts
  ------

  Displays the options of the current module.
""")

    def do_load(self, inp):
        try:
            success = False
            impmod = inp
            if "modules" in impmod:
                imp.import_module(impmod)
                success = True
            else:
                p = select.bareimport(impmod)
                success = p[0]
                impmod = p[1]
                imp.import_module(impmod)
            if success:
                vars.module = impmod
                self.prompt = '\033[0m\033[1m vaile(\033[1;31m{}\033[0m\033[1m) > '.format(vars.module.split(".")[-1])
        except ImportError:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Not a valid module: {}".format(inp))
        except ValueError:
            print(R + " [-] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Please enter a module.")

    def help_load(self):
        print("""
  load
  ------

  Load a module.
  Syntax: load MODULE

    MODULE: module to be loaded

  The full path, as well as the name can be used ('.' as separator)
""")

    def do_leave(self, inp):
        vars.module = ""
        self.prompt = '\033[0m\033[1m vaile > '

    def help_leave(self):
        print("""
  leave
  -------

  Leave the current module.
""")

    do_EOF = do_q


# help_EOF = help_q

if __name__ == '__main__':
    os.system('clear')
    if str(platform.system()) != "Linux":
        sys.exit(
            R + " [!] " + color.UNDERLINE + "\033[1m" + "You are not using a Linux Based OS! Linux is a must-have for "
                                                        "this script!" + color.END)
    if not os.geteuid() == 0:
        sys.exit(R + " [!] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Must be run as root." + B + " :)" + color.END)
    if 'no' in open('core/doc/choice').read():
        prnt.disclaimer()

        a1 = input(B + ' [?] Do you agree to these terms and conditions? :> ' + C)
        if a1.lower().startswith('y'):
            print(B + ' [+] That\'s awesome! Move on...')
            time.sleep(3)
            FILE = open("core/doc/choice", "w")
            FILE.write('yes')
            FILE.close()

        else:
            print(R + ' [!] ' + B + 'You have to agree!')
            time.sleep(1)
            sys.exit(0)
   
    prnt.loadstyle()
    prnt.banner()
    #prnt.bannerbelow()
    VainShell().cmdloop()
    print(R + "[Vaile] " + "\033[0m" + color.UNDERLINE + "\033[1m" + "Session finished." + color.END)
