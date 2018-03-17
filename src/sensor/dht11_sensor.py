import sensor

class Dht11Sensor(sensor.Sensor):
    
    pin_num_ = None
    
    def GetData(self):
        # sensor.Sensor.GetData(self)
        
        # here we will have a logic to collect data from sensor
        return 1
    
    def Configure(self):
        #sensor.Sensor.Configure(self)
        None