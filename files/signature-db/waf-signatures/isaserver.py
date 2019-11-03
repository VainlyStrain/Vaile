#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search


def isaserver(headers, content):
    detect = False
    detect |= search(
        r'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.',
        content) is not None
    detect |= search(r'The ISA Server denied the specified Uniform Resource Locator (URL)', content) is not None
    if detect:
        return "ISA Server (Microsoft)"
