import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1410))
s.listen(5)

msg = s.recv(1024)
print(msg.decode("utf-8"))
while True:
    clientsocket, address = s.accept()
    print(f"adres odbiorcy = {address}")
    clientsocket.send(bytes("send info", "utf-8"))