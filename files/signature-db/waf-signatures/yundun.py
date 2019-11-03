#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile


def yundun(headers, content):
    detect = False
    detect |= headers['server'] == 'YUNDUN'
    if 'x-cache' in headers.keys():
        detect |= headers['x-cache'] == 'YUNDUN'
    if detect:
        return "Yundun Web Application Firewall (Yundun)"
