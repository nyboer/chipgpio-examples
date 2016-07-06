import time
import CHIP_IO.GPIO as GPIO

# Pin configuration.
pinA = "XIO-P4"
pinB = "XIO-P5"
pinC = "XIO-P6"

# Setup input for pin
GPIO.setup(pinA,GPIO.IN)
GPIO.setup(pinB,GPIO.IN)
GPIO.setup(pinC,GPIO.IN)

bcount = 0
start = 0
end = 0

#also shows time elapsed between presses
def fallcall(channel):
    global bcount
    global start
    global end
    flag = bcount%2
    if flag:
        end = time.time()
        print "up"+str(end - start)
    else:
        start = time.time()
        print "down"
    bcount = bcount + 1
    print "CALLBACK FALL "+channel

def risecall(channel):
    print "CALLBACK RISE"

def bothcall(channel):
    print "CALLBACK BOTH"


# Setup edge detects for pins. Rising and Both have different values for de-bounce time, for testing.
GPIO.add_event_detect(pinA,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinB,GPIO.RISING,risecall,200)
GPIO.add_event_detect(pinC,GPIO.BOTH,bothcall,400)

# make a loop
try:
    while True:
        print "press a button..."
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
