import os
from time import sleep

on = 'on'
off = 'off'

# Bash commands for accessing leds
red_pwr = '/sys/class/leds/led1/brightness'
green_act = '/sys/class/leds/led0/brightness'


def set_on(color):
    if color == red_pwr:
        return '0'
    return '1'


def set_off(color):
    if color == red_pwr:
        return '1'
    return '0'


def onboard_leds(color, state):
    if state == on:
        state = set_on(color)
    else:
        state = set_off(color)
    # MAIN PART
    return os.system('echo {} | sudo tee {} > /dev/null 2>&1'.format(state, color))


def flash_leds(color, flashes, duration=None, rest=None):
    for i in range(flashes):
        onboard_leds(color, on)
        if duration is not None:
            sleep(duration)
        else:
            sleep(.2)
        onboard_leds(color, off)
        if rest is not None:
            sleep(rest)
        else:
            sleep(.1)

# Basics uses:

# flash_leds(red_pwr, 3, duration=.15)
# flash_leds(green_act, 3, duration=.15)

# onboard_leds(green_act, off)
# onboard_leds(red_pwr, off) # the red seems to be inverted (at least part time)
