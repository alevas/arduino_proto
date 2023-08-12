import pyfirmata

import time

board = pyfirmata.Arduino('/dev/ttyACM0')


def blink(duration, sleep_after=.5):
    board.digital[13].write(1)
    time.sleep(duration)
    board.digital[13].write(0)
    time.sleep(sleep_after)

while True:
    blink(1)
    blink(.2)
    blink(1)
    blink(.2)
    blink(3)
    blink(.1, sleep_after=0.2)
    blink(.1, sleep_after=0.2)
    blink(.1, sleep_after=0.2)
