from multiprocessing import Process
import os
from time import sleep
import datetime

from vrms.hardware.arm import ArmHandler
from vrms.network.mqtt import Mqtt
from vrms.network.udp import Udp

a = ArmHandler()
m = Mqtt(a)
u = Udp()


def example() -> None:
    count: int = 0
    while True:
        x = datetime.datetime.now()
        os.system(f'echo {count} >> logs.txt')
        count += 1
        sleep(3600)


def mqtt() -> None:
    m.client()


def udp() -> None:
    u.client()


def arm() -> None:
    a.client()


class Background:

    def __init__(self):
        self.p1 = Process(target=example)
        self.p2 = Process(target=mqtt)
        self.p3 = Process(target=udp)
        self.p4 = Process(target=arm)

    def listen(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()
        self.p4.start()

    def close(self):
        self.p1.join()
        self.p2.join()
        self.p3.join()
        self.p4.join()
