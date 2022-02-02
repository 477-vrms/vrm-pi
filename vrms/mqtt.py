import os
import zmq
from zmq import Socket
import json


class Mqtt:

    def __init__(self):
        self.ctx = zmq.Context()
        self.subscriber: Socket = self.ctx.socket(zmq.SUB)
        self.subscriber.connect("tcp://34.132.95.250:2001")
        self.subscriber.setsockopt(zmq.SUBSCRIBE, b"vrms_pi")

    def client(self) -> None:
        while True:
            response = self.subscriber.recv()
            if response != b"vrms_pi":
                try:
                    str_json = response.decode("UTF-8")
                    obj = json.loads(str_json)
                    print("received message: %s" % str_json)
                    os.system(f'echo "{obj}" >> joint.txt')
                except json.JSONDecodeError as e:
                    print(e)
