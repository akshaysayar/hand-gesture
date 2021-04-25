from cv2 import cv2
import mediapipe as mp
import time
import os
import csv



def generate_data():
    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    
    pTime = 0
    cTime = 0
    collect_data = []


    ct=0
    while ct<100:
        #input('Press Enter to capture')
        t_end =time.time() + 3
        #success, img = cap.read()
        success, img = cap.read()
        img = cv2.flip(img,1)
        cv2.imshow("Image", img)
        while time.time() < t_end:
            success, img = cap.read()
            print("-----------------------------------------------------")
                
            cv2.putText(img, str(int(t_end-time.time())), (10, 130), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            #cv2.imshow("Image", img)
            imgRGB = img
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
        collect_data.append(cl)
        ct=ct+1

    len(collect_data)
    return(collect_data)

def write_data(collect_data,gesture):
    filepath = 'data/raw_'+gesture+'.csv'
    with open(filepath, 'w') as f:
        write = csv.writer(f)
        write.writerows(collect_data)

def main(gesture):
    os.chdir(os.path.join(os.path.split(os.path.abspath(__file__))[0],".."))
    
    data_collected = generate_data()
    write_data(data_collected,gesture)

if __name__== "__main__":
    gesture = "stop"
    main(gesture)