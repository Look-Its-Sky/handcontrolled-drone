import cv2, mediapipe as mp, time
from debugui import *

class handcontroller:
    cap = None

    hands = None
    mpHands = None
    mpDraw = None
    
    cTime = 0
    pTime = 0
    
    prevPointArr = []
    
    depths = {
            'depth': None,
            'prevDepth': None,
            'depthDiff': None
    }

    dirVec = []

    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

        self.pTime = 0
        self.cTime = 0


    def update(self):
        while True:
            success, img = self.cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                
                self.depths['depth'] = results.multi_hand_landmarks[0]

            self.cTime = time.time()
            fps = 1/(self.cTime - self.pTime)
            self.pTime = self.cTime

            img = cv2.flip(img, 1)
            
            cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

            #print all points
            if results.multi_hand_landmarks:
                if debugs['printHandPoints']:
                    printHandPoints()

                if debugs['printHandDirection']:
                    printHandDirection()
                
                if debugs['printHandLandmarkData']:
                    printHandLandmarkData(img=img, results=results)

                if debugs['printHandDepth']:
                    printHandDepth(img=img, results=results) 

            cv2.imshow("Hand Tracker", img)
            cv2.waitKey(1)

            #prepare for the next frame
            try:
                #return direction vector
                if self.prevPointArr and results.multi_hand_landmarks[0].landmark[0].x:  
                    self.dirVec = getDirVec(self.prevPointArr, results.multi_hand_landmarks[0].landmark[0])
            
                self.prevPointArr = results.multi_hand_landmarks[0].landmark[0]
            except:
                pass

            return self.dirVec