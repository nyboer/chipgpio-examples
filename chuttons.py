import time
import CHIP_IO.GPIO as GPIO

# cheeper buttons
class chuttons:
    def __init__(self):
        self.nom = ''
        # Pin configuration.
        self.LS = "XIO-P2" #left side
        self.RS = "XIO-P3" #right side
        self.TL = "XIO-P4" #top left
        self.MD = "XIO-P5" #top mid
        self.TR = "XIO-P6" #top right
        self.lookup = {"XIO-P2":"leftside","XIO-P3":"rightside","XIO-P4":"topleft","XIO-P5":"mid","XIO-P6":"topright"}
        # array makes setup a bit easier:
        self.buttons = [self.RS,self.LS,self.TL,self.MD,self.TR]
        for b in self.buttons:
            # Setup input for pin
            GPIO.setup(b,GPIO.IN)
            # Setup edge detects for pins. Rising and Both have different values for de-bounce time, for testing.
            GPIO.add_event_detect(b,GPIO.FALLING,self.fallcall,300)

    # how do I subscribe to this result outside of the class?
    def fallcall(self,channel):
        self.nom = self.lookup[channel]
        print 'self '+self.nom
        return self.nom

    def cleanup(self):
        GPIO.cleanup()

# Test
if __name__ == "__main__":
    bz = chuttons()
    try:
        while True:
            print "press a button..."
            time.sleep(1)

    except KeyboardInterrupt:
        bz.cleanup()       # clean up GPIO on CTRL+C exit
    bz.cleanup()           # clean up GPIO on normal exit
