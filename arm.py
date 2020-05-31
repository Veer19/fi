import RPi.GPIO as GPIO
import time
import curses
from picamera import PiCamera

#camera = PiCamera()
#camera.stop_preview()
#camera.start_preview()
# Camera warm-up time
#time.sleep(2)
#print("Capturing")
#camera.capture('foo.jpg', use_video_port=True)
#print("Done, stopping")
#camera.stop_preview()
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)            
GPIO.setmode(GPIO.BOARD)




GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

arm1 = GPIO.PWM(3,50)
arm2 = GPIO.PWM(5,50)
arm3 = GPIO.PWM(7,50)

arm1.start(0)
arm2.start(0)
arm3.start(0)
duty1 = 7
duty2 = 0
arm1.ChangeDutyCycle(duty1)
# arm2.ChangeDutyCycle(duty2)
#arm3.ChangeDutyCycle(6)
w = 119
a = 97
s = 115
d = 100
j = 106
l = 108
try:
    while(True):
        arm1.ChangeDutyCycle(2)
        print("Waiting")
        time.sleep(1)

        arm1.ChangeDutyCycle(7)
        time.sleep(1)
        # char = screen.getch()
        # #print(char)
        # if(char == a):
        #     print("Turning Left")
        #     if(duty1 > 0.1):
        #         duty1=duty1-0.1
        #     arm1.ChangeDutyCycle(duty1)
        # if(char == d):
        #     print("Turning Right")
        #     if(duty1 < 12):
        #         duty1=duty1+0.1
        #     arm1.ChangeDutyCycle(duty1)
        # if(char == w):
        #     print("Up")
        #     if(duty2 < 12.0):
        #         duty2=duty2+0.1
        #     arm2.ChangeDutyCycle(duty2)
        # if(char == s):
        #     print("Down")
        #     if(duty2 > 0.1):
        #         duty2=duty2-0.1
        #     arm2.ChangeDutyCycle(duty2)  
finally:
    arm1.stop()
    arm2.stop()
    GPIO.cleanup()
    #camera.stop_preview()
    print("Fuck off")
    
