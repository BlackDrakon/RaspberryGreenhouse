import message
import queue
import worker

class SensorInterface(worker.Worker):
    
    data_queues_ = []
    sensor_name_ = 'Sensor'
    dimension_ = None
    
    def SendData(self, value):
        # value, sender_name=None, sender_id=None, dimension=None
        data = message.Message(self.GetData(), self.sensor_name_, self.id_, self.dimension_ )
                
        # send data to all queues wich we have for this sensor
        for out_queue in self.data_queues_:
            out_queue.put(data)
        
    def AddQueue(self, queue_in):
        self.data_queues_.append(queue_in)
    
    def GetData(self):
        
        None
    
    def Configure(self):
        None
    
    def Job(self):
        value = self.GetData()
        self.SendData(value)
        
