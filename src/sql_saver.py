import sqlite3
import time
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
        print(data)
        None
    
    def AddInputChanel(self,queue_in):
        self.queues_input_data_.append(queue_in)
    
    def AddSetInputChanels(self, input_set):
        for chanel in input_set:
            self.AddInputChanel(chanel)
    
    def Job(self):
        
        #worker.Worker.Job(self)
        
        for in_queue in self.queues_input_data_:
            while not in_queue.empty():
                data = in_queue.get()
                in_queue.task_done()
                self.SaveDataToBase(data)
    
    def SaveMarketStateToBase(self, json_ticker, time_str):
        #return_value = "error"
        
        self.DataBaseConnection()
        
        # time table
        
        self.cursor_.execute("CREATE TABLE IF NOT EXISTS time (time_id integer PRIMARY KEY, year, month, day, hour, min, sec, week_day, year_day, isdst) ")
        self.cursor_.execute("INSERT INTO time (year, month, day, hour, min, sec, week_day, year_day, isdst) VALUES (?,?,?,?,?,?,?,?,?)",tuple(time_str))
        
        self.cursor_.execute("SELECT time_id FROM time ORDER BY time_id desc LIMIT 1")
        last_time_id = int(self.cursor_.fetchall()[0][0])
        
        # coin table
        
        for pair in json_ticker:
            
            self.cursor_.execute('''CREATE TABLE IF NOT EXISTS '''+ pair +'''
            (time, percentChange, high24hr, baseVolume, highestBid, lowestAsk, isFrozen, id, low24hr, last, quoteVolume,
            FOREIGN KEY (time) REFERENCES time(time_id) ) ''')
            
            
            self.cursor_.execute('''INSERT INTO '''+ pair +''' 
            (time, percentChange, high24hr, baseVolume, highestBid, lowestAsk, isFrozen, id, low24hr, last, quoteVolume ) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?)''', [last_time_id, json_ticker[pair]['percentChange'],json_ticker[pair]['high24hr'],
            json_ticker[pair]['baseVolume'],json_ticker[pair]['highestBid'],json_ticker[pair]['lowestAsk'],
             json_ticker[pair]['isFrozen'],json_ticker[pair]['id'],json_ticker[pair]['low24hr'],
              json_ticker[pair]['last'],json_ticker[pair]['quoteVolume']])
        
        # CREATE TABLE IF NOT EXISTS info (PRIMARY KEY id int, username text, password text)
        
        self.DataBaseConnectionClose()
        
        return_value = "ok"
        return return_value
    
