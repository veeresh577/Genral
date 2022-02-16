import matplotlib.pyplot
import cv2
import numpy as np


img = cv2.imread(r'C:\Users\vs6993\PycharmProjects\Open_CV\DATA\Nadia_Murad.jpg',0)

# ret,img = cv2.threshold(orimg,155,255,cv2.THRESH_BINARY)
img = cv2.adaptiveThreshold(img,50,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,9,5)

while(1):
    cv2.imshow("original image",img)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()
