
from switch import Switch
from motor import Motor

def Actuator(type_of_actuator):
    
    return_value = None    
    #print('__call_ in actuator')
    
    if type_of_actuator == 'switch':
        return_value = Switch()
    elif type_of_actuator == 'motor':
        return_value = Motor()
        None
    else:
        print('type of actuator is underfined')
    
    return(return_value)
        
            
    
    
    