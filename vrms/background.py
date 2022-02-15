from multiprocessing import Process
import os
from time import sleep
import datetime
import serial

from vrms.hardware.arm import ArmHandler
from vrms.network.mqtt import Mqtt
from vrms.network.udp import Udp



def example() -> None:
    count: int = 0
    while True:
        x = datetime.datetime.now()
        os.system(f'echo {count} >> logs.txt')
        count += 1
        sleep(3600)


def mqtt() -> None:
    a = ArmHandler()
    m = Mqtt(a)
    m.client()


def udp() -> None:
    u = Udp()
    u.client()


def arm() -> None:
    pass
    # a.client()


def uart_tx_rx() -> None:
    try:
        ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate
        while True:
            received_data = ser.read()  # read serial port
            sleep(0.03)
            data_left = ser.inWaiting()  # check for remaining byte
            received_data += ser.read(data_left)
            ser.write(received_data)  # transmit data serially
    except Exception as e:
        print(e)


class Background:

    def __init__(self):
        self.p1 = Process(target=example)
        self.p2 = Process(target=mqtt)
        self.p3 = Process(target=udp)
        self.p4 = Process(target=uart_tx_rx)

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
