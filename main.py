import cv2, mediapipe as mp, time
from judemath import *

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

prevPointArr = []
pointArr = []

debugs = {
    'printHandPoints': False,
    'printHandDirection': True
}

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                #if id ==0:
                pointArr.append((cx, cy))
                cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    #print all points
    if pointArr and prevPointArr:
        #for i in range(len(pointArr)):
        if debugs['printHandPoints']: print(f"Point {i}: {pointArr[i]}")
        if debugs['printHandDirection']:
            direction = getDirection(pointArr[0], prevPointArr[0], 20)
            print(getDirection(pointArr[0], prevPointArr[0], 20))

    prevPointArr = pointArr
    pointArr = []
    
    cv2.imshow("Hand Tracker", img)
    cv2.waitKey(1)
