import json
import socket
from time import sleep
import base64

from vrms.hardware.camera import get_camera_generator

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

        self.c = get_camera_generator()

        self.is_sending = 0
        self.count = 0

    def send_response(self, response):
        self.s.sendto(response, ("34.132.95.250", 2002))

    def set_is_sent(self, is_sent):
        self.count = 0
        self.is_sending = is_sent

    def send_frame(self):
        frame = next(self.c)
        # print("len: ", len(frame))
        # if self.count <= 0:
        #     print(frame)
        #     self.count += 1
        self.send_response(frame)
    
    def client(self, lock) -> None:
        init = {
            "id": "vrms_pi",
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
