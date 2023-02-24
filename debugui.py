import cv2
from judemath import *

debugs = {
    'printHandPoints': False,
    'printHandDirection': False,
    'printHandLandmarkData': False,
    'printHandDepth': False,
}

def printHandPoints(results):
    #for i in range(len(pointArr)): # subsitute i for desired point in hand
    i = 0
    print(f"Point {i}: {results.multi_hand_landmarks[i]}")

def printHandDirection(img, results):
    direction = getDirection(results.multi_hand_landmarks[0], results.multi_hand_landmarks[0], 10)
    cv2.putText(img, str(direction), (10, 140), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

def printHandLandmarkData(img, results):
    cv2.putText(img, str(results.multi_hand_landmarks[0]), (10, 230), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    print(str(results.multi_hand_landmarks[0]))

def printHandDepth(img, results):
    cv2.putText(img, str(results.multi_hand_landmarks[0]), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 3)
    print(results.multi_hand_landmarks[0].landmark[0].z)