#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """A Custom Exception object."""
    pass


def get_age(birthyear):
    """A function that checks for a valid age."""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
