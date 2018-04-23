class ActuatorInterface():
    
    state_output_ = []
    name_ = 'actuator'
    
    def Configure(self):
        None
    
    def GetData(self, data):
        None
    
    # same interface as for queue
    def put(self, msg_data):
        self.GetData(msg_data)
    
    def SendState(self):
        None