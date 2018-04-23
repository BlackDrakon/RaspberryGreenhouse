import uuid
import time

class Message:
    
    def __init__(self, value = None, sender_name = None, sender_id = None, dimension = None, value_name = None):
        if sender_name == None:
            sender_name = 'Anonimus'
        
        self.time_ = time.time()
        self.sender_name_ = sender_name
        self.sender_id_ = sender_id
        self.value_name_ = value_name
        self.dimension_ = dimension
        self.message_id_ = uuid.uuid4().hex
        self.value_ = value