from multiprocessing import Process
import os
from time import sleep
import datetime

from vrms import Mqtt, Udp


def example() -> None:
    count: int = 0
    while True:
        x = datetime.datetime.now()
        print(f'Hello World: {x}')
        os.system(f'echo {count} >> logs.txt')
        count += 1
        sleep(3600)


def mqtt() -> None:
    m = Mqtt()
    m.client()


def udp() -> None:
    u = Udp()
    u.client()


class Background:

    def __init__(self):
        self.p1 = Process(target=example)
        self.p2 = Process(target=mqtt)
        self.p3 = Process(target=udp)

    def listen(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()

    def close(self):
        self.p1.join()
        self.p2.join()
        self.p3.join()