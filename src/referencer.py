import time
import worker

class Referencer(worker.Worker):
    
    state_ = 0
    time_points_ = [[6, 1],[22, 0]]
    out_queues_ = []
    
    
    
    def Job(self):
        
        value = self.time_points_[-1][1]
        
        previus_time_point = self.time_points_[0]
        
        for time_point in self.time_points_:
            time_hour = list(time.gmtime())[3]
            if (time_hour < time_point[0]) & (time_hour > previus_time_point[0]):
                value = previus_time_point[1]
                break
            previus_time_point = time_point
        
        for out_queue in self.out_queues_:
            out_queue.put(value) 
            
    
    