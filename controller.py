#Ryan's Robot Project
#Ryan Magnuson
#File Modified from FreeNova Tutorial


import RPi.GPIO as GPIO
import time 

motorPins = (12, 16, 18, 22)    #define pins connected to four phase ABCD of stepper motor
CCWStep = (0x01,0x02,0x04,0x08) #define power supply order for coil for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  #define power supply order for coil for rotating clockwise




def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT)


#as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):      #cycle for power supply order
        for i in range(0,4,1):  #assign to each pin, a total of 4 pins
            if (direction == 1):#power supply order clockwise
                GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              #power supply order anticlockwise
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       #the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)  

#continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)

#Moves clockwise 2.8125 degrees (360 / 128)
def moveCW():
    moveSteps(1,3,4)

def moveCCW():
    moveSteps(0,3,4)

def destroy():
    GPIO.cleanup()             # Release resource



