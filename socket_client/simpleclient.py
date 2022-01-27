import socket


HEADER = 64
DISCONNECTED_MSG = "!DISCONNECTED"
FORMAT = "UTF-8"
Host = socket.gethostbyname(socket.gethostname())
port = 9999

ADDR = (Host, port)

newClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newClient.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    newClient.send(send_length)
    newClient.send(message)


send("HELLO WORLD!")
send(DISCONNECTED_MSG)
