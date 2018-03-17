from actuator_interface import ActuatorInterface
import RPi.GPIO as GPIO  
import time

class Switch(ActuatorInterface):
    
    pin_number_ = None
    pull_down_ = 1
    inverse_ = 0
    state_ = 0
    
    
    def GetData(self, data):
        #ActuatorInterface.GetData(self, data)
        if (data > 0) & (self.state_ <= 0):
            self.On()
            self.state_ = 1
        elif (data <= 0) & (self.state_ > 0):
            self.Off()
            self.state_ = 0
    
    def SendState(self):
        #ActuatorInterface.SendState(self)
        if not len(self.state_output_):
            for channel in self.state_output_:
                channel.put(self.state_)
        return self.state_
    
    def Configure(self, pin_number, pull_down = 1, inverse = 0):
        #ActuatorInterface.Configure(self)
        
        # another type is BCM
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_number, GPIO.OUT)
        
        self.pin_number_ = pin_number
        self.pull_down_ = pull_down
        self.inverse_ = inverse
        
        #now initialyse it
    
    def On(self):
        GPIO.output(self.pin_number_, GPIO.HIGH)
    
    def Off(self):
        GPIO.output(self.pin_number_, GPIO.LOW)
        
    def Test(self):
        # just blinking with pin
        for i_inc in range(5):
            self.On()
            time.sleep(5)
            self.Off()
            time.sleep(5)


if __name__ == '__main__':
    test_switch = Switch()
    pin = int(input())
    test_switch.Configure(pin)
    test_switch.Test()

