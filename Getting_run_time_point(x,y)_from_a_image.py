import cv2


""" Function """
def getRunTimePosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y) # printing the position of point when the mouse pointer clicks on the images

cv2.namedWindow(winname='pannel')
cv2.setMouseCallback('pannel', getRunTimePosition)


""" Display images """

image = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\giraffes.jpg")
image = cv2.resize(image,(0,0),image, 0.5,0.5)

while True:
    cv2.imshow("pannel",image)

    if cv2.waitKey(1) & 0xff == 27 :
        break
cv2.destroyAllWindows()
