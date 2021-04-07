import cv2
import mediapipe as mp
import time
 
cap = cv2.VideoCapture(0)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0
collect = []


ct=0
while ct<100:
    #input('Press Enter to capture')

    
    
    t_end =time.time() + 3
    #success, img = cap.read()
    success, img = cap.read()
    cv2.imshow("Image", img)
    while time.time() < t_end:
        success, img = cap.read()
        print("-----------------------------------------------------")
            
        cv2.putText(img, str(int(t_end-time.time())), (10, 130), cv2.FONT_HERSHEY_PLAIN, 3,
            (255, 0, 255), 3)
        #cv2.imshow("Image", img)

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        cl =[]
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    #print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx,cy)
                    cl.extend([cx,cy])
                    # if id == 4:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
    
        cv2.imshow("Image", img)
        
        cv2.waitKey(1)
    collect.append(cl)
    ct=ct+1

print(collect)
len(collect)
for i in collect:
    print(len(i))

import csv
with open(r'/home/akshay/data/personal/Python_projects/Hand_gesture/data/thumbsup.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    
    write.writerows(collect)

# import time
# import cv2
# t_end =time.time() + 4
#     #success, img = cap.read()
# while time.time() < t_end:
#     print(t_end-time.time())