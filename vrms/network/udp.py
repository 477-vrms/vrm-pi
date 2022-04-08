import json
import socket
from time import sleep
import base64
import random

from vrms.hardware.camera import get_camera_generator

packet_size = 25000
header_size = 10
data_packet_size = packet_size - header_size

def split_image(data):
    photo_size = len(data)
    num_packets = (photo_size // data_packet_size)

    if (photo_size % data_packet_size != 0):
        num_packets += 1

    photo_size_bytes = photo_size.to_bytes(4, 'little')
    num_packets_bytes = num_packets.to_bytes(1, 'little')

    photo_id = random.randint(0, 2147483647)
    photo_id_bytes = photo_id.to_bytes(4, 'little')

    start, end = 0, data_packet_size

    for i in range(num_packets):
        # print(f"photo id: {photo_id}, i: {i}, num_packets: {num_packets}, photo size: {photo_size}")
        packet_id = i.to_bytes(1, 'little')
        yield photo_id_bytes + packet_id + num_packets_bytes + photo_size_bytes + data[start:end]
        start += data_packet_size
        end += data_packet_size

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
        for packet in split_image(frame):
            self.send_response(packet)
    
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
