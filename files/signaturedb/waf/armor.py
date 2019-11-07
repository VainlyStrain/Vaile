#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def armor(headers, content):
    detect = False
    detect |= search(r'This request has been blocked by website protection from Armor', content, I) is not None
    if detect:
        return "Armor Protection (Armor Defense)"
