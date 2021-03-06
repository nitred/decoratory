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
        location_line = error_location[:21] + ":" + line_number
        # s = "%.19s [%-8s] [%-36s] %s" % (self.formatTime(record, self.datefmt),
        #                                  record.levelname,  location_line, record.getMessage())
        s = "[%-8s] [%-25s] %s" % (record.levelname,  location_line, record.getMessage())
        return s


flogger = logging.getLogger('flog')

# Prevent recreation of handlers. Maintain a singleton.
if not flogger.hasHandlers():
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(FlogFormatter())
    flogger.addHandler(handler)
    flogger.setLevel(logging.DEBUG)
    # flogger.warning("No external logging handlers found for FLOGGER. FLOGGER will use its own logging handler:"
    #                 "\"logging.StreamHandler(stream=sys.stdout)\", with default logLevel set to DEBUG.")

flogLevel_lookup = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "CRITICAL": logging.CRITICAL,
}


def flog(func):
    """Decorate functions to have control over whether to flog or not.

    The functions that are decorated by this decorater cannot have a kwarg
    named `flog` or `flogLevel`.

    Args:
        flog (bool): Extracted from kwargs. Default False.
        flogLevel (logging.Levels): Extracted from kwargs. Default logging.DEBUG.
    """
    def func_wrapper(*args, **kwargs):
        flog_ = kwargs.pop('flog', True)
        flogLevel = kwargs.pop('flogLevel', logging.DEBUG)
        if isinstance(flogLevel, str):
            flogLevel = flogLevel_lookup[flogLevel.upper()]  # Wrong key will throw error
        if flog_:
            flogger.setLevel(flogLevel)
        else:
            flogger.setLevel(logging.CRITICAL + 10)

        # Pass args and kwargs as is to the function.
        ret_val = func(*args, **kwargs)

        # Reset log level.
        flogger.setLevel(logging.DEBUG)
        return ret_val

    return func_wrapper
