import picamera 
from camera_pi import Camera
import socket 
import io 

from app import app
from flask import request,jsonify,render_template,Response,Flask
# from bson.json_util import dumps,loads
# from json import load
from flask_cors import CORS
from time import time
import datetime  
from time import sleep

# from . import db
import requests
import json
CORS(app)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
mountX = GPIO.PWM(11,50)
GPIO.setup(13,GPIO.OUT)
mountY = GPIO.PWM(13,50)

mountX.start(0)
mountY.start(0)



@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
                    
                   
@app.route("/cameraX", methods=["POST"])
def move_mount_x():
    print("Called X")
    if request.method == "POST":
        x = request.get_json()['camera_mount_x']
        timestamp = request.get_json()['timestamp']
        if(int(time()) - timestamp < 5):

            mountX.ChangeDutyCycle(x)
            sleep(1)
            mountX.ChangeDutyCycle(0)
        # mountY.ChangeDutyCycle(y)1590679410152
    return "Ok"

@app.route("/cameraY", methods=["POST"])
def move_mount_y():
    print("Called Y")
    if request.method == "POST":
        y = request.get_json()['camera_mount_y']
        mountY.ChangeDutyCycle(y)
        sleep(1)
        mountY.ChangeDutyCycle(0)
        # mountY.ChangeDutyCycle(y)
    return "Ok"