#import wiringpi
import time
from actuator_interface import ActuatorInterface

# GPIO pin 12 = BCM pin 18 = wiringpi pin 1
MOTOR_PWM_PIN = 26

#wiringpi.wiringPiSetup()

#wiringpi.pinMode(MOTOR_PWM_PIN, 2)
#wiringpi.pwmWrite(MOTOR_PWM_PIN, 0)



def SpeedChange(pwm_value):
    print('speed',pwm_value)
    #wiringpi.pwmWrite(MOTOR_PWM_PIN, pwm_value)

class Motor(ActuatorInterface):
    None

# значение должно быть от 0 до 1024
def MotorTest():
    speed = 0
    change = 1
    try:
        while True:
            SpeedChange(speed)
            speed += change
            if speed == 1024:
                change = -1
            if speed == 0:
                change = 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('stop')