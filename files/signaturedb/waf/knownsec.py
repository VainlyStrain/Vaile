#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search


def knownsec(headers, content):
    detect = False
    detect |= search(r"url\('/ks-waf-error\.png'\)", content) is not None
    if detect:
        return "KS-WAF (Knownsec)"
