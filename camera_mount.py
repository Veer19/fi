import RPi.GPIO as GPIO
import time
import curses
from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = (1024, 768)
#camera.start_preview()
# Camera warm-up time
#time.sleep(2)
#print("Capturing")
#camera.capture('foo.jpg')
#print("Done, stopping")
#camera.stop_preview()
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)            
GPIO.setmode(GPIO.BOARD)




GPIO.setup(11,GPIO.OUT)
mountLR = GPIO.PWM(11,50)
GPIO.setup(13,GPIO.OUT)
mountUD = GPIO.PWM(13,50)

mountLR.start(0)
mountUD.start(0)
dutyLR = 7
dutyUD = 0
mountLR.ChangeDutyCycle(dutyLR)
mountUD.ChangeDutyCycle(dutyUD)
try:
    while(True):
        char = screen.getch()
        if(char == curses.KEY_RIGHT):
            if(dutyLR > 0.1):
                dutyLR=dutyLR-0.1
            mountLR.ChangeDutyCycle(dutyLR)
        if(char == curses.KEY_LEFT):
            if(dutyLR < 12.0):
                dutyLR=dutyLR+0.1
            mountLR.ChangeDutyCycle(dutyLR)
        if(char == curses.KEY_UP):
            if(dutyUD < 12.0):
                dutyUD=dutyUD+0.1
            mountUD.ChangeDutyCycle(dutyUD)
        if(char == curses.KEY_DOWN):
            if(dutyUD > 0.1):
                dutyUD=dutyUD-0.1
            mountUD.ChangeDutyCycle(dutyUD)  
finally:
    mountLR.stop()
    mountUD.stop()
    GPIO.cleanup()
    #camera.stop_preview()
    print("Fuck off")
    
