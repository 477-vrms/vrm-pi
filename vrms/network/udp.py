import json
import socket
from time import sleep


class Udp:
    default = None

    @classmethod
    def load_udp(cls):
        if cls.default is None:
            cls.default = Udp()
        return cls.default

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.c.bind(("127.0.0.1", 4200))

        self.is_sending = 0

    def send_response(self, response):
        self.s.sendto(response, ("34.132.95.250", 2002))

    def set_is_sent(self, is_sent):
        self.is_sending = is_sent

    def send_frame(self):
        frame = self.c.recvfrom(1024 * 65)
        self.send_response(frame[0])

    def client(self, lock) -> None:
        init = {
            "id": "vrms-pi",
            "password": "FAKEPASSWORD"
        }
        response = json.dumps(init).encode('utf-8')
        while True:
            if self.is_sending == 1:
                self.send_response(response)
            if self.is_sending == 2:
                self.send_frame()
            else:
                sleep(1)
