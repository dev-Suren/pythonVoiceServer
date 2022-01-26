import socket


def clientSide():
    Host = '127.0.0.1'
    port = 9999

    newClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    newClient.connect((Host, port))

    newClient.sendall(b"this is just a test")

    data = newClient.recv(1024)

    print('Received', repr(data))


clientSide()
