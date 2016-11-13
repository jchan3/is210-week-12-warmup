#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """A function that checks var1 for a valid index or key."""
    try:
        var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist'
        return var1
    return var1[var2]
