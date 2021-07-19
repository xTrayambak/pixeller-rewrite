"""
Server backend.
"""

import socket
import _thread
import sys

from random import randrange

class Server():
    server = socket.gethostbyname(socket.gethostname())
    port = 5555
    max_connections = 2

    players = []

    socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    def bind(self):
        try:
            self.socket.bind(
                (
                    self.server,
                    self.port
                )
            )
        except Exception as e:
            print("[Server] An error occured while binding the socket to the server parameters.\n"+str(e))

    def listen(self):
        self.socket.listen(self.max_connections)
        print("[Server] Now listening for connections.")

    def thread_client_conn(self, conn):
        conn.send(
            str(
                [
                    str("Connected."),
                    str(self.players),
                    str(
                        str(randrange(0, 500))+","+str(randrange(0, 500))
                    )
                ]
            ).encode()
        )
        reply = ""
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")

                if not data:
                    print("[Server] A connection failed to deliver a packet to the server henceforth the connection was broken.")
                    break
                else:
                    print("Received packet. "+str(reply))

                conn.sendall(str.encode(reply))
            except Exception as e:
                print("[Client Connection Thread] "+str(e))
                break
        
        conn.close()

    def accept(self):
        while True:
            try:
                conn, addr = self.socket.accept()
                print("[Server] New connection from "+str(addr))

                _thread.start_new_thread(self.thread_client_conn, (conn,))
            except Exception as e:
                print("[Server] "+str(e))

if __name__ == "__main__":
    serv = Server()
    serv.bind()
    serv.listen()
    serv.accept()