# importing socket
import socket


def EstablishedConnection():
    HOST = '127.0.0.1'
    PORT = 9999
    newConnnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding the connection with host and the port

    newConnnection.bind((HOST, PORT))
    print("Establishing Connection")
    newConnnection.listen(2)

    conn, addr = newConnnection.accept()

    with conn:
        print("connected by", addr)

        while True:
            data = conn.recv(1024)

            if not data:
                break
            conn.sendall(data)


EstablishedConnection()
