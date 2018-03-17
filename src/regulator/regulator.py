import repeater
import relay

def Regulator(reg_type):
    
    return_value = None
    if reg_type == 'repeater':
        return_value = repeater.Repeater()
    elif reg_type == 'relay':
        return_value = relay.Relay()
    else:
        print('type of regulator is underfined')
    return return_value
    
    