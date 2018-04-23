import sqlite3
import worker

class SqlSaver(worker.Worker):
    
    queues_input_data_ = []
    data_base_name_ = "greenhouse.db"
    connector_ = ""
    cursor_ = "" 
    
    
    def DataBaseConnection(self):
        self.connector_ = sqlite3.connect(self.data_base_name_)
        self.cursor_  = self.connector_.cursor()
        return "ok"
    
    def DataBaseConnectionClose(self):
        self.connector_.commit()
        self.connector_.close()
        return "ok"
    
    def SaveDataToBase(self, data):
        #print('debug print from sql:', data.value_)
        print('debug print from sql:', 'sender ',data.sender_name_, 'value ',data.value_, 'time ', data.time_)
        None
    
    def AddInputChanel(self,queue_in):
        self.queues_input_data_.append(queue_in)
    
    def AddSetInputChanels(self, input_set):
        for chanel in input_set:
            self.AddInputChanel(chanel)
    
    def Job(self):
        
        #worker.Worker.Job(self)
        self.DataBaseConnection()
        for in_queue in self.queues_input_data_:
            while not in_queue.empty():
                data = in_queue.get()
                in_queue.task_done()
                self.SaveDataToBase(data)
                self.SaveMessageToBase(data)
        self.DataBaseConnectionClose()
    
    def SaveMessageToBase(self, message):
        
        return_value = "error"
        
#         time_ = None
#         dimension_ = None
#         value_name_ = None
#         value_ = None
#         sender_id_ = None
#         message_id_ = None
#         sender_name_ = None
              
        self.cursor_.execute("CREATE TABLE IF NOT EXISTS messages (integer PRIMARY KEY, time, dimension, value_name, value, sender_id, message_id, sender_name) ")
        
        
        self.cursor_.execute('''INSERT INTO messages 
            ( time, dimension, value_name, value, sender_id, message_id, sender_name ) 
            VALUES (?,?,?,?,?,?,?)''', (message.time_, message.dimension_,
            message.value_name_, message.value_, message.sender_id_, message.message_id_, 
            message.sender_name_))
        
        
        return_value = "ok"
        return return_value
    
