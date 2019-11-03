#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework      #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def safe3(headers, content):
    detect = False
    for header in headers.items():
        detect |= search(r'Safe3 Web Firewall|Safe3', header[1], I) is not None
        detect |= search(r'Safe3WAF', header[1], I) is not None
        if detect:
            break
    if detect:
        return "Safe3 Web Application Firewall"
