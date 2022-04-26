import zmq
from zmq import Socket
import json

from vrms.network.udp import Udp
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
        self.arm = ArmHandler.load_arm()

    def handle_obj(self, obj):
        if obj["action"] == "move":
            self.arm.enqueue(obj)
        elif obj["action"] == "video_ready":
            udp = Udp.load_udp()
            udp.set_is_sent(1)
        elif obj["action"] == "video_start":
            udp = Udp.load_udp()
            udp.set_is_sent(2)
        elif obj["action"] == "video_end":
            udp = Udp.load_udp()
            udp.set_is_sent(0)
        elif obj["action"] == "buzzer":
            self.arm.activate_buzzer()

    def client(self, lock) -> None:
        udp = Udp.load_udp()
        udp.set_arm_handler(self.arm)
        while True:
            response = self.subscriber.recv()
            if response != b"vrms_pi":
                try:
                    str_json = response.decode("UTF-8")
                    obj = json.loads(str_json)
                    self.handle_obj(obj)
                except json.JSONDecodeError as e:
                    print(e)
                except Exception as e:
                    print("disconnected from the internet?")
                    print(e)
