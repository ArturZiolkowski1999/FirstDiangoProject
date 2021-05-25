from network import Network

run = True
n = Network()
message = "get"

while run:
    try:
        game = n.send(message)
    except:
        run = False
        print("Couldn't get game")
        break
    message = input("-> ")

