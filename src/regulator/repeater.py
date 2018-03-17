from regulator_interface import RegulatorInterface

class Repeater(RegulatorInterface):
    
    state_ = 0
    
    def Solver(self):
        #regulator.RegulatorInterface.Solver(self)
        return_value = self.state_
        
        while not self.referencer_.empty():
            return_value = self.referencer_.get()
            self.referencer_.task_done()
            self.state_ = return_value 
        
        
        return return_value
            