import zmq
from zmq import Socket
import json

from vrms.hardware.arm import ArmHandler


class Mqtt:

    default = None

    @classmethod
    def load_mqtt(cls):
        if cls.default is None:
            cls.default = Mqtt()
        return cls.default

    def __init__(self):
        self.ctx = zmq.Context()
        self.subscriber: Socket = self.ctx.socket(zmq.SUB)
        self.subscriber.connect("tcp://34.132.95.250:2001")
        self.subscriber.setsockopt(zmq.SUBSCRIBE, b"vrms_pi")
        self.arm_handler = ArmHandler.load_arm()

    def client(self, lock) -> None:
        while True:
            response = self.subscriber.recv()
            if response != b"vrms_pi":
                try:
                    str_json = response.decode("UTF-8")
                    #print(str_json)
                    obj = json.loads(str_json)
                    lock.acquire()
                    try:
                        self.arm_handler.enqueue(obj)
                    finally:
                        lock.release()
                except json.JSONDecodeError as e:
                    print(e)
