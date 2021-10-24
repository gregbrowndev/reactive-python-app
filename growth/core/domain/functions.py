import time

ENABLE_SLEEP = False


def do_some_work():
    if ENABLE_SLEEP:
        time.sleep(2)
    return
