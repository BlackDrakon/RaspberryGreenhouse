import uuid
import time

class Worker():
    
    def __init__(self, id_in = None):
        if id_in == None:
            id_in = uuid.uuid4()
        
        self.id_ = id_in
        self.time_period_ = 10 #time for worker in sec
        self.name_ = None
    
    def Job(self):
        None
    
    def Worker(self, command_queue):
        while True:
            if not command_queue.empty():
                command = command_queue.get()
                command_queue.task_done()
                if command is 'kill':
                    print('thread name:', self.name_, ' thread id:', self.id_, ' ended correctly')
                    break
            self.Job()
            time.sleep(self.time_period_)