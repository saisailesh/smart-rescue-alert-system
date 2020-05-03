import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # use board numbers
# define input pin
pin = 12
GPIO.setup(pin, GPIO.IN)

while 1:
  if GPIO.input(pin) == GPIO.LOW:
    print "i hear you"
    time.sleep(1)
