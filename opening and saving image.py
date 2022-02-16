import cv2

img = cv2.imread('buffer_place/images.jpg')
img = cv2.resize(img,(0,0),img,4,4)  # resizing the image

while True:

    cv2.imshow("Naruto",img)

    if cv2.waitKey(1) & 0xFF == 27 : # waiting for i msec and closeing the image by Esc button
        break
cv2.destroyAllWindows()
