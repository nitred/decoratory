"""Example file to demonstrate simple ftime use."""
import time

from decoratory.ftime import ftime


@ftime
def wait_one_second_and_return():
    time.sleep(1.0)


if __name__ == "__main__":
    wait_one_second_and_return()
