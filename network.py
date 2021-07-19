import socket
from _thread import start_new_thread

class Network:
    def __init__(self):
        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.data = self.connect() #start_new_thread(self.connect, ())

    def getPos(self):
        return self.data["position"]
    
    def getPlayers(self):
        return self.data["players"]

    def getResult(self):
        return self.data["result"]
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print("[Network] "+str(e))

    def connect(self):
        try:
            print("[Network] Now connecting to a server and receiving first bits of data.")

            self.client.connect(self.addr)
            data = self.client.recv(2048).decode()
            list(data)

            print(data)

            print("length of data is "+str(len(data)))
            print("type of data is "+str(type(data)))

            # Converting string to list
            res = data.strip('][').split(', ')


            print("[Network] Received tuple data.")

            print("[Network] Extracted tuple data.")

            result, playerList, position = res

            print("[Network] Success!")

            plrListRes = playerList.strip('][').split(', ')

            return {
                'result': result,
                'players': plrListRes,
                'position': list(eval(position))
            }

        except Exception as e:
            print("[Network] An error occured while receiving first bits of data. \n"+str(e))

"""n = Network()
print(n.send("Hello from the client!"))
print(n.send("Hey server, what's up?"))
"""