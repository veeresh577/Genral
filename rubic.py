import cv2
import numpy as np
import imutils

# lower bound and upper bound for Green color


lower_bound = np.array([20, 80, 80])
upper_bound = np.array([30, 255, 255])


# rubic = cv2.imread(r'C:/Users/vs6993/Pictures/Camera Roll/rubic.jpg')

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read(0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    segmented_img = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours from the mask
    contours, hierarchy = cv2.findContours( mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    cnts = imutils.grab_contours(contours)
    output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)


    # Showing the output
    cv2.imshow("Output", output)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

