import threading
from threading import Thread

from vrms.hardware.arm import ArmHandler
from vrms.network.mqtt import Mqtt
from vrms.network.udp import Udp


def arm(lock) -> None:
    a = ArmHandler.load_arm()
    a.client(lock)


def mqtt(lock) -> None:
    m = Mqtt.load_mqtt()
    m.client(lock)


def udp(lock) -> None:
    pass
    # u = Udp.load_udp()
    # u.client(lock)


class Background:

    def __init__(self):
        lock = threading.Lock()

        self.p1 = Thread(target=arm, args=(lock,))
        self.p2 = Thread(target=mqtt, args=(lock,))
        self.p3 = Thread(target=udp, args=(lock,))

    def listen(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()

    def close(self):
        self.p1.join()
        self.p2.join()
        self.p3.join()
