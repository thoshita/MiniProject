from flask import Flask, render_template,request, redirect, url_for
import cv2
from pyduino import *
from imageai.Detection.Custom import CustomObjectDetection
import time


app = Flask(__name__)
a = Arduino(serial_port='COM3',baud_rate=9600) 
time.sleep(3)
# declare the pins we're using
LED_PIN = 13
# initialize the digital pin as output
a.set_pin_mode(LED_PIN,'O')
print('Arduino initialized')
@app.route("/")
def index():
    return render_template("myMain.html")

@app.route("/mySecond.html")
def second():
    for _ in range(3):
        a.digital_write(LED_PIN,1)
        time.sleep(0.5)
        a.digital_write(LED_PIN,0)
        time.sleep(0.5)
    a.digital_write(LED_PIN,1)
    return render_template("mySecond.html")

@app.route("/myPayment.html")
def payment():
    for _ in range(3):
        a.digital_write(LED_PIN,1)
        time.sleep(0.5)
        a.digital_write(LED_PIN,0)
        time.sleep(0.5)
    a.digital_write(LED_PIN,0)
    return render_template("myPayment.html")

@app.route("/myMain.html")
def myMain():
    for _ in range(3):
        a.digital_write(LED_PIN,1)
        time.sleep(0.5)
        a.digital_write(LED_PIN,0)
        time.sleep(0.5)
    a.digital_write(LED_PIN,0)
    return render_template("myMain.html")

@app.route("/imageProcessing")
def process():
    print("babu sona")
    detector = CustomObjectDetection()