#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def trafficshield(headers, content):
    detect = False
    detect |= headers['server'] == "F5-TrafficShield".lower()
    detect |= search(r'st8\(id|_wat|_wlf\)', str(headers.values()), I) is not None
    if detect:
        return "TrafficShield (F5 Networks)"
