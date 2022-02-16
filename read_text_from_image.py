import cv2
import pytesseract
import os,fnmatch

def find_popup_text():
    text= ""
    pytesseract.pytesseract.tesseract_cmd=r'C:\Users\vs6993\AppData\Local\Tesseract-OCR\tesseract.exe'

    def find(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    """get all the screen shots named with setting_beeper_volume.png """
    files= find('setting_*.png',os.getcwd())

    """loop through all the fils for text extraction"""
    for file in files:
        img = cv2.imread(file,0) #converting image to gray
        img=img[1000:1150,150:550] # croping the image to get only popup screen
        texts=pytesseract.image_to_string(img) #text extraction
        if texts:
            text=texts

    print(text)











# while True:
#
#     cv2.imshow("Naruto",img)
#
#     if cv2.waitKey(1) & 0xFF == 27 : # waiting for i msec and closeing the image by Esc button
#         break
# cv2.destroyAllWindows()
