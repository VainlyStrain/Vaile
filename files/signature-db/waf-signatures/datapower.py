#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def datapower(headers, content):
    detect = False
    for header in headers.items():
        detect |= search(r'x-backside-transport', header[1], I) is not None
        if detect: break
    if detect:
        return "IBM WebSphere DataPower (IBM)"
