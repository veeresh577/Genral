import numpy as np
import cv2
# import matplotlib as plt


img = np.zeros([600,600,3])

cv2.rectangle(img,pt1=(100,200),pt2=(400,500),color=(0,255,0),thickness=-1)

cv2.circle(img,center=(300,300),radius=100,color=(0,0,150),thickness= 5)

while True:
    cv2.imshow("drawing",img)

    if cv2.waitKey(1) & 0xFF == 27 : # waiting for i msec and closeing the image by Esc button
        break
cv2.destroyAllWindows()
