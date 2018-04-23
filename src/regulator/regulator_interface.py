import worker
import message

class RegulatorInterface(worker.Worker):
    
    referencer_ = []
    sensor_ = []
    actuators_ = [] #list of all actuators
    
    name_ = 'regulator'
    
    solution_ = None
    
    def Job(self):
        self.solution_ = self.Solver()
        self.SendSolution()
    
    def Solver(self):
        return 0
    
    def SendSolution(self):
        if len(self.actuators_):
            message_out = message.Message(self.solution_)
            for actuator in self.actuators_:
                actuator.put(message_out)
        else:
            print('I am so useless, I do not have actuators!!!')