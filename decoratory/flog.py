"""File containing developer logging code."""
from __future__ import print_function

import logging
import sys


class FlogFormatter(logging.Formatter):
    """Format the meta data in the log message to fix string length."""

    datefmt = '%Y-%m-%d %H:%M:%S'

    def format(self, record):
        """Default formatter."""
        error_location = "%s.%s" % (record.name, record.funcName)
        line_number = "%s" % (record.lineno)
        location_line = error_location[:18] + ":" + line_number
        # s = "%.19s [%-8s] [%-36s] %s" % (self.formatTime(record, self.datefmt),
        #                                  record.levelname,  location_line, record.getMessage())
        s = "[%-5s] [%-21s] %s" % (record.levelname,  location_line, record.getMessage())
        return s


flogger = logging.getLogger('flog')

# Prevent recreation of handlers. Maintain a singleton.
if not len(flogger.handlers):
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(FlogFormatter())
    flogger.addHandler(handler)
    flogger.setLevel(logging.CRITICAL)


def flog(func):
    """Decorate functions to have control over whether to flog or not.

    The functions that are decorated by this decorater cannot have a kwarg
    named `flog` or `flogLevel`.

    Args:
        flog (bool): Extracted from kwargs. Default False.
        flogLevel (logging.Levels): Extracted from kwargs. Default logging.DEBUG.
    """
    def func_wrapper(*args, **kwargs):
        flog_ = kwargs.pop('flog', False)
        flogLevel = kwargs.pop('flogLevel', logging.DEBUG)
        if flog_:
            flogger.setLevel(flogLevel)
            # flogger.log(flogLevel, "============================================= {}".format(func.__name__))

        # Pass args and kwargs as is to the function.
        ret_val = func(*args, **kwargs)

        # Reset log level.
        flogger.setLevel(logging.CRITICAL)
        return ret_val

    return func_wrapper
