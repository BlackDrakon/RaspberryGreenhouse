import worker

class RegulatorInterface(worker.Worker):
    
    referencer_ = []
    sensor_ = []
    
    time_period_ = 1 #time for worker in sec
    actuators_ = [] #list of all actuators
    solution_ = None
    
    def Job(self):
        self.solution_ = self.Solver()
        self.SendSolution()
    
    def Solver(self):
        return 0
    
    def SendSolution(self):
        if len(self.actuators_):
            for actuator in self.actuators_:
                actuator.GetData(self.solution_)
        else:
            print('I am so useless, I do not have actuators!!!')