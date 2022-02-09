from multiprocessing import Process
import os
import serial
from time import sleep
import datetime
import wiringpi

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

def uart_tx_rx() -> None: 
    wiringpi.wiringPiSetup()
    serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
    print(serial)
    while True:
        print(wiringpi.serialDataAvail(serial))

class Background:

    def __init__(self):
        self.p1 = Process(target=example)
        self.p2 = Process(target=mqtt)
        #self.p3 = Process(target=udp)
        self.p3 = Process(target=uart_tx_rx)

    def listen(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()

    def close(self):
        self.p1.join()
        self.p2.join()
        self.p3.join()
