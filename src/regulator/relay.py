from regulator_interface import RegulatorInterface

class Relay(RegulatorInterface):
    
    state_ = 0
    hysteresis = 0.3
    
    def Solver(self):
        
        return_value = self.state_
        
        message = self.referencer_[0].get()
        if len(self.referencer_):
            reference_value = message.value_
            self.referencer_[0].task_done()
        else:
            print('no reference no honey')
            reference_value = 0
        
        
        message = self.sensor_[0].get()
        if len(self.sensor_):
            sensor_value = message.value_
            self.sensor_[0].task_done()
        else:
            print('no sensor no honey')
            sensor_value = 0
        
        if sensor_value > reference_value + self.hysteresis:
            return_value = 0
        elif sensor_value < reference_value - self.hysteresis:
            return_value = 1
            
        self.state_ = return_value
        
        return return_value