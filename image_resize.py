import cv2

img = cv2.imread(r"C:\Users\vs6993\Downloads\Akatsuki.png")
img = cv2.resize(img, (320,240))
cv2.imwrite(r"C:\Users\vs6993\Downloads\Akatsuki2.png",img)
