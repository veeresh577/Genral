import socket


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)  # listening through the port
    c, addr = s.accept()

    print("connection from:" + str(addr))

    while 1:
        data = c.recv(1024)  # receiving data max size of 1024byte
        if not data:
            break
        print("conneted from:" + str(data))
        data = str(data).upper()
        print("sending;" + str(data))
        c.send(data)
    c.close()


if __name__ == '__main__':
    main()
