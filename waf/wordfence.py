#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Wordfence (Feedjit)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, _, _ = get_page(get=vector)
        retval |= any(_ in (page or "") for _ in ("A potentially unsafe operation has been detected in your request to this site", "Generated by Wordfence", "Your access to this site has been limited", "This response was generated by Wordfence"))
        if retval:
            break

    return retval
