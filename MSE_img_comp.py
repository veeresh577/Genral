import numpy as np
import cv2
import os
import matplotlib as plt
from template_matching import display



def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


imageA = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\dog_backpack.jpg")
imageB = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\dog_backpack.png")

display(imageA)


