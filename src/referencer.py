import time
import worker
import message

class Referencer(worker.Worker):
    
    def __init__(self):
        super().__init__()
        self.state_ = 0
        self.time_points_ = [[6, 1],[22, 0]]
        self.out_queues_ = []
        
        self.time_period_ = 1
    
    def Job(self):
        
        value = self.time_points_[-1][1]
        
        previus_time_point = self.time_points_[0]
        
        for time_point in self.time_points_:
            time_hour = list(time.gmtime())[3]
            if (time_hour < time_point[0]) & (time_hour > previus_time_point[0]):
                value = previus_time_point[1]
                break
            previus_time_point = time_point
        
        out_msg = message.Message(value)
        out_msg.sender_name_ = self.name_
        
        #print('referencer send msg', out_msg.message_id_)
        #print('number of out queues is ', self.out_queues_)
        
        for out_queue in self.out_queues_:
            #print('number of messages inside queue befor writing ',out_queue.qsize()) 
            out_queue.put(out_msg)
            
        