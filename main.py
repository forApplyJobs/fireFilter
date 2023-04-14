import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.waitKey(0)
while cap.isOpened():

    ret, frame = cap.read()
    cv2.waitKey(0)
    frame2=frame.copy()

    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (5, 5), 0)
    # mask limitss
    red_high = np.array([18, 166, 230])
    red_low = np.array([0, 74, 200])

    mask = cv2.inRange(hsv, red_low, red_high)
    result = cv2.bitwise_and(frame2, frame2, mask=mask)
    numberoftotal=cv2.countNonZero(mask)
    if numberoftotal>1000:
        cv2.putText(result, "firedetected", (0, 150), 1, 1, (0, 255, 0), 1)
        print("firedetected")
    else:
        cv2.putText(result, "notdetected", (0, 150), 1, 1, (0, 255, 0), 1)
    cv2.imshow("frame2", result)
    cv2.imshow