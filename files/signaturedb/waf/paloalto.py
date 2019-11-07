#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search


def paloalto(headers, content):
    detect = False
    detect |= search(r'Access[^<]+has been blocked in accordance with company policy', content) is not None
    if detect:
        return "Palo Alto Firewall (Palo Alto Networks)"
