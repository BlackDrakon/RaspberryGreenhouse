import time

class Worker():
    
    time_period_ = 1 #time for worker in sec
    id_ = None
    name_ = None
    
    def Job(self):
        None
    
    def __init__(self, id_in = None):
        self.id_ = id_in
    
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