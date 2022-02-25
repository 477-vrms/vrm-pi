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


def uart_tx_rx() -> None:
    test_string = "Test serial port ...".encode('utf-8')
    port_list = ["/dev/ttyAMA1"]#,"/dev/ttyAMA1","/dev/ttyS0","/dev/ttyS"]
    while 1:
        try:
            serialPort = serial.Serial("/dev/ttyAMA1", 9600, timeout = 2)
            #print ("Serial port", "/dev/ttyAMA1", " ready for test :")
            bytes_sent = serialPort.write(test_string)
            #print ("Sended", bytes_sent, "byte")
            loopback = serialPort.read(bytes_sent)
            #print("Received ",len(loopback), "bytes. Port", "/dev/ttyAMA1")
            serialPort.close()
        except IOError:
            print("Error on", "/dev/ttyAMA1","\n")

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
