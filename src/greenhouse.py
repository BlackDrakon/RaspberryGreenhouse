import threading
import queue
import time
import uuid

from ds18b20 import Ds18b20

import keyboard
import gpio_keyboard
from dht11_sensor import Dht11Sensor
from referencer import Referencer
from sql_saver import SqlSaver
from regulator import Regulator
from actuator import Actuator



def MotorWorker(commands_queue):#, motor):    
    while True:
        item = commands_queue.get()
        if item == 'kill':
            break
        #do_work(item)
        print('Motor Worker thread recived a command:', item)
        commands_queue.task_done()

def KeyboardWorker(commands_queue):    
    while True:
        command = keyboard.GetKeyboardCommand()
        print('Keyboard Worker thread sent a command:', command)
        commands_queue.put(command)
        print('kill',command,'kill'==command)
        if command == 'kill':
            break

def PinsInputWorker(commands_queue):
    while True:
        #command = GetKeyboardCommand()
        command = 'kill'
        print('Keyboard Worker thread sent a command:', command)
        commands_queue.put(command)
        if command is 'kill':
            break                

def EndProgramm(commands_queues):
    for commands_queue in commands_queues:
            commands_queue.put('kill')
    print('programm stoped, humanity saved')
    

def main():
    
    commands_queues = []
    threads = []
    
    led_pwr_on = Actuator('switch')
    led_water_low = Actuator('switch')
    led_water_hight = Actuator('switch')
    
    
    temp_line_ref = queue.Queue()
    temp_line_reg = queue.Queue()
    temp_line_sen = queue.Queue()
    light_line_ref = queue.Queue()  # data channel from reverencer
    light_line_reg = queue.Queue()  # data channel from reverencer
    
    sql_temp_line_ref = queue.Queue()
    sql_temp_line_reg = queue.Queue()
    sql_temp_line_sen = queue.Queue()
    sql_light_line_ref = queue.Queue()  # data channel from reverencer
    sql_light_line_reg = queue.Queue()  # data channel from reverencer
    
    
    # start SQL thread it recive all sensor and regulator data
    
    sql_thread =  SqlSaver(uuid.uuid4())
    sql_thread.name_ = 'SQL base saver'
    # add all input queues to the SQL worker
    sql_thread.AddSetInputChanels([sql_temp_line_ref, sql_temp_line_reg, sql_temp_line_sen, sql_light_line_ref, sql_light_line_reg])
    
    sql_commands_queue = queue.Queue()
    sql_worker = threading.Thread(target = sql_thread.Worker, args=(sql_commands_queue,))
    
    threads.append(sql_worker)
    commands_queues.append(sql_commands_queue)
    
    
    # create whole temperature line
    
    # create whole light line
    # start time referencer for light
    light_referencer = Referencer(uuid.uuid4())
    light_referencer.name_ = 'light referencer'
    referencer_commands_queue = queue.Queue()
    
    # data channels from referencer
    light_referencer.out_queues_.append(light_line_ref)
    light_referencer.out_queues_.append(sql_light_line_ref)
    
    referencer_worker = threading.Thread(target = light_referencer.Worker, args=(referencer_commands_queue,))
    threads.append(referencer_worker)
    commands_queues.append(referencer_commands_queue)
    
    # actuator part. switch
    light_switch = Actuator('switch')
    light_switch.Configure( pin_number = 22, pull_down = 1, inverse = 0)
    
    # regulator just repeater of reference signal
    light_repeater =  Regulator('repeater')
    light_repeater.id_ = uuid.uuid4()
    light_repeater.name_ = 'light repeater'
    light_repeater.referencer_.append(light_line_ref)
    light_repeater.actuators_.append(light_switch)
    
    commands_queue = queue.Queue()
    repeater_worker = threading.Thread(target = light_referencer.Worker, args=(commands_queue,))
    threads.append(repeater_worker)
    commands_queues.append(commands_queue)
    
    # start first DS18B20 sensor thread
    ds18b20_1 = Ds18b20(uuid.uuid4())
    ds18b20_1.Configure()
    ds18b20_1.name_ = 'outside tempreture'
    sensor_commands_queue = queue.Queue()
    sensor_worker = threading.Thread(target = ds18b20_1.Worker, args=(sensor_commands_queue,))
    threads.append(sensor_worker)
    commands_queues.append(sensor_commands_queue)
    
    # start first DHT11 sensor thread
    dht11_1 = Dht11Sensor(uuid.uuid4())
    dht11_1.Configure()
    dht11_1.name_ = 'outside temperature and humidity'
    sensor_commands_queue = queue.Queue()
    sensor_worker = threading.Thread(target = dht11_1.Worker, args=(sensor_commands_queue,))
    threads.append(sensor_worker)
    commands_queues.append(sensor_commands_queue)
    
    # start second DHT11 sensor thread
    dht11_2 = Dht11Sensor(uuid.uuid4())
    dht11_2.Configure()
    dht11_2.name_ = 'inside temperature and humidity'
    sensor_commands_queue = queue.Queue()
    sensor_worker = threading.Thread(target = dht11_2.Worker, args=(sensor_commands_queue,))
    threads.append(sensor_worker)
    commands_queues.append(sensor_commands_queue)
    
    
    # start all threads
    for thread in threads:
        thread.start()
    
    while True:
        print('wait your commands:', end = ' ')
        user_command = input()
        if user_command == 'kill':
            EndProgramm(commands_queues)
            break


if __name__ == '__main__':
    main()
    