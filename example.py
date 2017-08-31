"""Example file to demonstrate the use of ftime, flog and flogger features."""
import logging
import time

from decoratory import flog, flogger, ftime


#############################
# @ftime Example
#############################


@ftime
def test_ftime(foo):
    """Wait one second and print `foo` argument."""
    time.sleep(1.0)
    print("foo: {}".format(foo))


print("---------------------------------------------------------")
print("Test FTIME NAIVELY                 : Time elapsed PRINTED")
test_ftime(foo="bar")

print("---------------------------------------------------------")
print("Test FTIME DISABLED                : Time elapsed IGNORED")
test_ftime(foo="bar", ftime=False)

print("---------------------------------------------------------")
print("Test FTIME ENABLED                 : Time elapsed PRINTED")
test_ftime(foo="bar", ftime=True)


#############################
# @flog Example
#############################

@flog
def test_flog():
    """Use flogger to log messages with different levels."""
    time.sleep(0.25)  # This delay is purely for user experience.
    flogger.critical("This is a critical message.")
    flogger.warning("This is a warning message.")
    flogger.info("This is a info message.")
    flogger.debug("This is a critical message.")


print("---------------------------------------------------------")
print("Test FLOG NAIVELY                  : Default DEBUG level")
test_flog()

print("---------------------------------------------------------")
print("Test FLOG NAIVELY, WARNING level   : WARNING level ")
test_flog(flogLevel=logging.WARNING)

print("---------------------------------------------------------")
print("Test FLOG ENABLED, DEBUG level     : DEBUG level")
test_flog(flog=True, flogLevel=logging.DEBUG)

print("---------------------------------------------------------")
print("Test FLOG ENABLED, WARNING level   : WARNING level")
test_flog(flog=True, flogLevel=logging.WARNING)

print("---------------------------------------------------------")
print("Test FLOG DISABLED                 : DISABLED")
test_flog(flog=False)

print("---------------------------------------------------------")
print("Test FLOG DISABLED, WARNING level  : DISABLED")
test_flog(flog=False, flogLevel=logging.WARNING)


#############################
# @ftime and @flog Example
#############################

@ftime
@flog
def test_ftime_and_flog(foo):
    """Test ftime and flog combined."""
    time.sleep(1.0)
    flogger.info("ENTRY")
    for i in range(3):
        flogger.debug("ITER: {}".format(i))

    try:
        raise Exception
    except Exception:
        flogger.critical("ERROR!")

    flogger.info("EXIT")

    print("foo: {}".format(foo))


print("---------------------------------------------------------")
print("Test FTIME & FLOG NAIVELY           : EVERYTHING ENABLED")
test_ftime_and_flog(foo="bar")

print("---------------------------------------------------------")
print("Test FTIME & FLOG ENABLED           : EVERYTHING ENABLED")
test_ftime_and_flog(foo="bar", ftime=True, flog=True, flogLevel=logging.DEBUG)

print("---------------------------------------------------------")
print("Test FTIME & FLOG DISABLED          : EVERYTHING DISABLED")
test_ftime_and_flog(foo="bar", ftime=False, flog=False, flogLevel=logging.DEBUG)


if __name__ == '__main__':
    pass
