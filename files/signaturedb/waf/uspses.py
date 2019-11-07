#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile


def uspses(headers, content):
    detect = False
    detect |= headers['server'] == 'Secure Entry Server'.lower()
    if detect:
        return "USP Secure Entry Server (United Security Providers)"
