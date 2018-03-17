import sensor_data
import time
import queue
import worker



class Sensor(worker.Worker):
    
    data_queues_ = []
    
    def SendData(self, value):
        data = sensor_data.SensorData()
        data.time_ = time.time()
        data.sensor_id_ = self.id_
        data.value_ = self.GetData();        
        
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
        
