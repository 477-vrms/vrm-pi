import socket
from time import sleep


class Udp:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def server(self) -> None:
        count: int = 0
        while count < 10:
            print("sending message")
            self.s.sendto(b"What Up Matt Wen", ("34.132.95.250", 2002))
            sleep(1)
            count += 1

    def client(self) -> None:
        print("listening for messages")
        while True:
            data, addr = self.s.recvfrom(1024)
            print("received message: %s" % data)
