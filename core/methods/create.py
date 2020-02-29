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

import argparse
import os

p = argparse.ArgumentParser()
p.add_argument('intype',
                   help='Installation Type',
                   metavar='ITP'
                   )
p.add_argument('user',
                   help='Unprivileged user',
                   metavar='USR'
                   )

args = p.parse_args()
print(args.intype)
if args.intype == "OPT":
    os.system("touch /opt/Vaile/core/sessioncache/syn.val && chown {0}:{0} /opt/Vaile/core/sessioncache/syn.val".format(args.user))
else:
    os.system("touch /home/{0}/Vaile/core/sessioncache/syn.val && chown {0}:{0} /home/{0}/Vaile/core/sessioncache/syn.val".format(args.user))
