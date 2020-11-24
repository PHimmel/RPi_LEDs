"""
notes for using the onboard leds:

sys identifiers:
led0 = green activity
led1 = red power

locations:
main led directory = /sys/class/leds
toggle functionality = /boot/config.txt

they function primarily as system status indicators. This can lead to conflicting control over them(even when
active status is turned off). Especially led1.

Once in the 'trigger' state of programmic usability - they are effectively turned on and used by the system
as indicators
care must be taken when using them immediately after start-up or reboot. As they are susceptible to undesired events
(see below: Sleep)

Programs that rapidly alternate the states of these two leds must be very exact with their statements.
They should be clearly turned on and off as needed (but without *any* redundant commands, eg. red-on, red-on).
Otherwise they are prone to having their on/off states flipped (along with their required commands to do so).

sleep between state alternations is also important, without a period of rest(minimum ~0.2 seconds)
the brightness maybe significantly reduced, also response time and rate(failures occur)
"""

import os
from time import sleep

on = 'on'
off = 'off'

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

#flash_leds(red_pwr, 3, duration=.15)
#flash_leds(green_act, 3, duration=.15)

#onboard_leds(green_act, off)
#onboard_leds(red_pwr, off) # the red seems to be inverted (at least part time)
