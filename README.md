# Raspberry Pi Onboard LEDs

# Foobar

Foobar is a Python lsdibrary for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

### Notes
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