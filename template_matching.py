import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def display(img):
    while True:
        cv2.imshow('deteced_image',img)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cv2.destroyAllWindows()

original = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\internal_external.png")
print(original.shape)
img1 = original[320:600,120:400,:]
original2=original[320:600,120:400,:]

res= cv2.matchTemplate(img1,original2,cv2.TM_CCORR_NORMED)
# if res:
print(res)
print("yes")

display(res)
