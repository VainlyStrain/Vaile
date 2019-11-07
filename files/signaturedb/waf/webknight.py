#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile


def webknight(headers, content):
    detect = False
    detect |= headers['server'] == 'WebKnight'.lower()
    if detect:
        return "WebKnight Application Firewall (AQTRONIX)"
