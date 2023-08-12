import pyfirmata

import time

board = pyfirmata.Arduino('/dev/ttyACM0')


def blink(duration):
    board.digital[13].write(1)
    time.sleep(duration)
    board.digital[13].write(0)
    time.sleep(.5)

while True:
    blink(1)
    blink(.2)
    blink(1)
    blink(.2)
    blink(3)
    blink(.1)
    blink(.1)
    blink(.1)
