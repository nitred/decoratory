import logging

from decoratory import flog, flogger, ftime


@ftime
@flog
def test_func():
    flogger.info("Entry")

    for i in range(5):
        flogger.debug(i)

    flogger.info("Exit")

    return "foo-bar"


output = test_func(ftime=True, flog=True, flogLevel=logging.DEBUG)
print("Output: {}".format(output))
