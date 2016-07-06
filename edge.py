import time
import CHIP_IO.GPIO as GPIO

# Pin configuration.
pinA = "XIO-P0"
pinB = "XIO-P1"
pinC = "XIO-P2"
pinD = "XIO-P3"
pinE = "XIO-P4"
pinF = "XIO-P5"
pinG = "XIO-P6"
pinH = "XIO-P7"

# Setup input for pin
GPIO.setup(pinA,GPIO.IN)
GPIO.setup(pinB,GPIO.IN)
GPIO.setup(pinC,GPIO.IN)
GPIO.setup(pinD,GPIO.IN)
GPIO.setup(pinE,GPIO.IN)
GPIO.setup(pinF,GPIO.IN)
GPIO.setup(pinG,GPIO.IN)
GPIO.setup(pinH,GPIO.IN)

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
        print "up "+str(end - start)
    else:
        start = time.time()
        print "down "+channel
    bcount = bcount + 1
    print "CALLBACK FALL "+channel

def risecall(channel):
    print "CALLBACK RISE "+channel

def bothcall(channel):
    print "CALLBACK BOTH "+channel


# Setup edge detects for pins. Rising and Both have different values for de-bounce time, for testing.
GPIO.add_event_detect(pinA,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinB,GPIO.RISING,risecall,200)
GPIO.add_event_detect(pinC,GPIO.BOTH,bothcall,400)
GPIO.add_event_detect(pinD,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinE,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinF,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinG,GPIO.FALLING,fallcall)
GPIO.add_event_detect(pinH,GPIO.FALLING,fallcall)

# make a loop
try:
    while True:
        print "press a button..."
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
