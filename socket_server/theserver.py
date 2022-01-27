# importing socket
import socket
import threading


HostIPaddr = socket.gethostbyname(socket.gethostname())
print(HostIPaddr)
PORT = 9999
ADDR = (HostIPaddr, PORT)
HEADER = 64
DISCONNECTED_MSG = "!DISCONNECTED"
# Making a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = "UTF-8"


def client_handler(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    CONNECTED = True
    while CONNECTED:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED_MSG:
                CONNECTED = False
            print(f"[{addr}]: {msg}")

    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")


print("[STARTING] server is ready to coonnect....")
start()
