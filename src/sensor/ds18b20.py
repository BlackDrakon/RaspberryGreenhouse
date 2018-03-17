import sensor

class Ds18b20(sensor.Sensor):
    
    pin_num_ = None
    
    def GetData(self):
        # sensor.Sensor.GetData(self)
        
        # here we will have a logic to collect data from sensor
        return 18.8
    
    def Configure(self):
        #sensor.Sensor.Configure(self)
        None