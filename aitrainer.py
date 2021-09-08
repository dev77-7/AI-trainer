import cv2
import numpy as np
import time
import posemodule as pm

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("Video Directory/Name.ext") can be used  for capturing a video

# importing the poseDetector class of posemodule to create a object
detector = pm.poseDetector()
count = 0
dir1 = 0
pTime = 0
while True:
    success, img = cap.read()
    # resizing the video
    img = cv2.resize(img, (1280, 720))
    # detecting pose in the video
    img = detector.findPose(img, False)
    # getting the landmarks values and appending them on the list
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # getting the angle by using landmark values of right arm
        angle = detector.findAngle(img, 12, 14, 16)
        # similarly for left arm
        # angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        # calculating reps for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir1 == 0:
                count += 0.5
                dir1 = 1
        if per == 0:
            color = (0, 255, 0)
            if dir1 == 1:
                count += 0.5
                dir1 = 0
        print(count)

        # drawing the intensity bar on (right_size_of) screen
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # printing rep counts on (left_side of) screen
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)
    # printing fps on screen
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Final_Run", img)
    # making the video/camera feed stay & then quitting the program by pressing "q" key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break