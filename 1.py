import sys
import time


def blink_once():
    sys.stdout.write('\rTEXT')
    time.sleep(0.5)
    b = ("Loading")
    sys.stdout.write('\r     ')
    time.sleep(0.5)


def blink(number):
    for x in range(0, number):
        blink_once()


blink(3)
3333