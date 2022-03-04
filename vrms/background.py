from threading import Thread

from vrms.hardware.arm import ArmHandler
from vrms.network.mqtt import Mqtt
from vrms.network.udp import Udp


def arm() -> None:
    a = ArmHandler.load_arm()
    a.client()


def mqtt() -> None:
    m = Mqtt.load_mqtt()
    m.client()


def udp() -> None:
    u = Udp.load_udp()
    u.client()


class Background:

    def __init__(self):
        self.p1 = Thread(target=arm)
        self.p2 = Thread(target=mqtt)
        self.p3 = Thread(target=udp)

    def listen(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()

    def close(self):
        self.p1.join()
        self.p2.join()
        self.p3.join()
