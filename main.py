import cv2, mediapipe as mp, time, atexit, threading
from judemath import *
from debugui import *
from drone import *
from handcontrol import *

def func():
    if not drone.testMode: drone.estop()

def thread():
    while True:
        drone.move(vec, threshold)

drone = Dronee()
handinput = handcontroller()
threshold = 15 #in pixels 
atexit.register(func)

vec = None

t1 = threading.Thread(target=thread)
t1.start()

while True:
    vec = handinput.update()