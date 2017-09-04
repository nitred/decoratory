"""Example file to demonstrate simple ftime use."""
from decoratory.flog import flog, flogger


@flog
def log_different_levels():
    flogger.debug("Entered the function.")
    flogger.warning("Exiting the function.")


if __name__ == "__main__":
    log_different_levels()
