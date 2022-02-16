from distutils.command.bdist_dumb import bdist_dumb

import numpy as np
import cv2
# import matplotlib.pyplot as plt

img = cv2.imread(r"D:\UI images\zebra.jpg")
# print(img.shape)
# b,g,r = cv2.split(img)
# b[:2037,:1854] = 255
# img=cv2.merge((b,g,r))
img = cv2.resize(img,(76,17),img)
# img = cv2.calcHist([img],channels=[0],mask=None,histSize=[256])
# plt.imshow(img)
while True:
    cv2.imshow("my_drawing", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.imwrite(r'D:\UI images\zebra1.png',img)
cv2.destroyAllWindows()
