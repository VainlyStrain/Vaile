#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def netscaler(headers, content):
    detect = False
    for header in headers.items():
        detect |= search(r'(ns_af=|citrix_ns_id|NSC_)', header[1], I) is not None
        detect |= search(r'ns.cache', header[1], I) is not None
        if detect:
            break
    if detect:
        return "NetScaler (Citrix Systems)"
