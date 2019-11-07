#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def varnish(headers, content):
    detect = False
    detect |= search(r'varnish|x-varnish', str(headers.values()), I) is not None
    if detect:
        return "Varnish FireWall (OWASP)"
