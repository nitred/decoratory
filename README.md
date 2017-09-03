# About
Decoratory is a python library that provides decorators to make life easier especially during development.

Currently there are two decorators, namely the **Function Timer Decorator** `@ftime` and the **Function Logger/Debug Decorator** `@flog`.

*Disclaimer: Using decorators adds overhead and if your functions have complex behaviors or use other decorators then be sure to look at the implementation of the library before using it. This library is recommended to be used as a tool for development or testing and not for production.*

### Function Timer Decorator (@ftime)
By adding the `@ftime` decorator to a function, the execution time of the function will be printed out.

```python
# File: example_ftime.py
import time
from decoratory.ftime import ftime

@ftime
def wait_one_second_and_return():
    time.sleep(1.0)

if __name__ == "__main__":
    wait_one_second_and_return()
```
```
$ python example_ftime.py
Time elapsed: 1.00       sec
```

### Function Logger/Debug Decorator (@flog)
By adding the `@flog` decorator to a function, you will be able to control the log levels of the log/debug statements.

```python
# File: example_flog.py
from decoratory.flog import flog, flogger

@flog
def log_different_levels():
    flogger.debug("Entered the function.")
    flogger.warning("Exiting the function.")

if __name__ == "__main__":
    log_different_levels()
```
```
$ python example_flog.py
[DEBUG   ] [flog.log_different_le:7  ] Entered the function.
[WARNING ] [flog.log_different_le:8  ] Exiting the function.
```

# Installation
`pip install git+https://github.com/nitred/decoratory.git --upgrade`

# Run Complete Example
```python
git clone https://github.com/nitred/decoratory.git
cd decoratory
python example_complete.py
```
