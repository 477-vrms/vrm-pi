import zmq
from zmq import Socket
import json

from vrms.hardware.arm import ArmHandler
from vrms.network.udp import Udp


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

    def handle_obj(self, obj):
        print("msg: ", obj)
        if obj["action"] == "move":
            self.arm_handler.enqueue(obj)
        elif obj["action"] == "video_ready":
            udp = Udp.load_udp()
            udp.start_sending()
        elif obj["action"] == "video_start":
            udp = Udp.load_udp()
            udp.set_is_sent(True)
        elif obj["action"] == "video_end":
            udp = Udp.load_udp()
            udp.stop_sending()

    def client(self, lock) -> None:
        while True:
            response = self.subscriber.recv()
            if response != b"vrms_pi":
                try:
                    str_json = response.decode("UTF-8")
                    obj = json.loads(str_json)
                    lock.acquire()
                    try:
                        self.handle_obj(obj)
                    finally:
                        lock.release()
                except json.JSONDecodeError as e:
                    print(e)
