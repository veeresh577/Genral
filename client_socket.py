import socket
from datetime import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',1002))

client.sendall(b"get image")


now = datetime.now()
current_time = now.strftime("%H_%M")

file = open("image_server"+current_time+".jpg", 'wb')

image_chunk = client.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client.recv(2048)


print("receiving completed")
file.close()
client.close()
