import socket
import os
from datetime import datetime
import cv2

cap = cv2.VideoCapture(0)

now = datetime.now()
current_time = now.strftime("%H_%M")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1002)) # 127.0.0.1

print(os.getcwd())
server.listen(2)

client_socket, client_addr = server.accept()

file = open('server_img.jpg','wb')
image_chunk = client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

print("receiving completed")
file.close()

