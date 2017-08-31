"""File that contains methods for timing a function."""
from __future__ import print_function

import time


def ftime(func):
    """Decorate the function that you want to time."""
    def func_wrapper(*args, **kwargs):
        ftime_ = kwargs.pop('ftime', True)
        if ftime_:
            start = time.time()
            ret_val = func(*args, **kwargs)
            end = time.time()
            print("Time elapsed: {:<10.2f} sec".format((end - start)))
        else:
            ret_val = func(*args, **kwargs)

        return ret_val
    return func_wrapper
