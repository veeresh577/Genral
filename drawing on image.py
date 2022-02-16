import cv2
import numpy as np
import random
global initial
global pointx , pointy

pointer_stack = []

initial = 0

def circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:

        global initial, pointx, pointy
        initial = initial + 1
        colour= random.randrange(100,250)
        cv2.circle(img,(x,y),58,(0,colour,256 ),4)
        cv2.putText(img, str(initial), (x,y), cv2.FONT_HERSHEY_PLAIN, 4,(65,20,255), 6)
        pointer_stack.append((x,y))
        print(x,y)

    if event == cv2.EVENT_RBUTTONDOWN :

        pointx,pointy = pointer_stack.pop()
        cv2.circle(img,(pointx,pointy),50,(0,0,0),3)
        cv2.putText(img, str(initial), (pointx,pointy), cv2.FONT_HERSHEY_PLAIN, 4,(0,0,0), 4)
        initial = initial - 1



cv2.namedWindow('my_drawing', cv2.WINDOW_NORMAL)


cv2.setMouseCallback('my_drawing',circle)

img = np.zeros((512,512,3))
# img = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\areca3.jpg")
# img = cv2.resize(img,(0.5 , 0.5))
while True:
    cv2.imshow("my_drawing", img)

    if cv2.waitKey(10) & 0xFF == 27:
        cv2.circle(img,(150 , 150 ),80,(0,0,256 ),6)
        cv2.putText(img, str(initial), (150 , 150 ), cv2.FONT_HERSHEY_PLAIN, 8,(50,0,10), 8)
        cv2.imwrite("countings3.png",img)
        break
cv2.destroyAllWindows()
