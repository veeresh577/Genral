import cv2
import numpy as np

def diplay_img(img):
    while True:
        cv2.imshow("I am",img)

        if cv2.waitKey(1) & 0xFF == 27 : # waiting for i msec and closeing the image by Esc button
            break
    cv2.destroyAllWindows()

img = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\giraffes.jpg")
img1 = cv2.resize(img,(0,0),img, fx = 0.5, fy = 0.5)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# ret,img = cv2.threshold(img1,155,255,cv2.THRESH_BINARY_INV)
img = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,9,5)

diplay_img(img)

