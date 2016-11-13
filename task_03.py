#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """A CustomLogger object."""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A log function."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush function."""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log(IOError)
            raise IOError

        try:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                except IOError:
                    self.log(IOError)
                    break
                else:
                    handled.append(index)
        finally:
            fhandler.close()

        if handled != []:
            for index in handled[::-1]:
                try:
                    del self.msgs[index]
                except IOError:
                    break
                except StandardError:
                    self.log(StandardError)
