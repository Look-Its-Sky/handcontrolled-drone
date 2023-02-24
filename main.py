import cv2, mediapipe as mp, time
from judemath import *
from debugui import *
from drone import *
from handcontrol import *

#connect to drone
#drone = Drone()
handinput = handcontroller()

while True:
    vec = handinput.update()
    #drone.move(vec)