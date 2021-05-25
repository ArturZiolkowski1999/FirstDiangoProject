import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1410))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"adres odbiorcy = {socket.gethostname()}")
    clientsocket.send(bytes("send info", "utf-8"))
