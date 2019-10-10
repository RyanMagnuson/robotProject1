#Ryan's Robot Project
#Ryan Magnuson
#File Modified from FreeNova Tutorial


import RPi.GPIO as GPIO
import time 

xAxis = (12, 16, 18, 22)    #define pins connected to four phase ABCD of stepper motor

yAxis = (13, 15, 19, 21)

CCWStep = (0x01,0x02,0x04,0x08) #define power supply order for coil for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  #define power supply order for coil for rotating clockwise




def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location


    for pin in xAxis:
        GPIO.setup(pin,GPIO.OUT)

    for pin in yAxis:
        GPIO.setup(pin,GPIO.OUT)


#as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps  
#axis assignment: 1 is x axis, 0 is y axis  
def moveOnePeriod(direction, ms, axis):    
    motorPins = xAxis if axis else yAxis
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
def moveSteps(direction, ms, steps, axis):
    for i in range(steps):
        moveOnePeriod(direction, ms, axis)

#Moves clockwise 2.8125 degrees (360 / 128)


def moveCW():
    moveSteps(1,10,2, 1)

def moveCCW():
    moveSteps(0,10,2, 1)

def moveDown():
    moveSteps(1,10,2, 0)

def moveUp():
    moveSteps(0,10,2, 0)

def destroy():
    GPIO.cleanup()             # Release resource

def keyCont():
    setup()
    while True:
        k = input()

        if k == 'w':
            moveUp()
        elif k == 'a':
            moveCCW()
        elif k == 's':
            moveDown()
        elif k == 'd':
            moveCW()
        else:
            break

    destroy()




# destroy()
# setup()

# while True:
#     for i in range(5):
#         moveDown()
#     for i in range(5):
#         moveCW()
#     for i in range(5):
#         moveUp()
#     for i in range(5):
#         moveCCW()
    


# destroy()



