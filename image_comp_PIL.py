from PIL import Image, ImageChops

im1 = Image.open(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\barcode1.jpg")
im2 = Image.open(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\barcode2.jpg")

diff = ImageChops.difference(im1,im2)

diff.show()
