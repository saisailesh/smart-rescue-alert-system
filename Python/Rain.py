

#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
state = GPIO.input(23)

if (state == 0):
    print "its raining detected"
else:
    print "its not raining "
