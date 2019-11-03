#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile


def wallarm(headers, content):
    detect = False
    detect |= headers['server'] == 'nginx-wallarm'
    if detect:
        return "Wallarm Web Application Firewall (Wallarm)"
