import time
import CHIP_IO.GPIO as GPIO

# Pin configuration.
pin = "XIO-P4"


# Setup input for pin
GPIO.setup(pin,GPIO.IN)

# Poll the pin in a loop
try:
    while True:
        # read the pin every half a second
        btn = GPIO.input(pin)
        print btn
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
