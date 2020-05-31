import RPi.GPIO as GPIO
import time

m1r1 = 16
m1r2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(m1r1, GPIO.OUT)
GPIO.setup(m1r2, GPIO.OUT)
while(True):
    print("ON")
    GPIO.output(m1r1, True)
    
    