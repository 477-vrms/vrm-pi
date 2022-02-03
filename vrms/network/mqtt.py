import zmq
from zmq import Socket
import json


class Mqtt:

    def __init__(self, arm_handler):
        self.ctx = zmq.Context()
        self.subscriber: Socket = self.ctx.socket(zmq.SUB)
        self.subscriber.connect("tcp://34.132.95.250:2001")
        self.subscriber.setsockopt(zmq.SUBSCRIBE, b"vrms_pi")
        self.arm_handler = arm_handler

    def client(self) -> None:
        while True:
            response = self.subscriber.recv()
            if response != b"vrms_pi":
                try:
                    str_json = response.decode("UTF-8")
                    obj = json.loads(str_json)
                    self.arm_handler.add_json(obj)
                except json.JSONDecodeError as e:
                    print(e)
