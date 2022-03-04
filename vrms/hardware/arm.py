import json

import serial


class Node:

    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node


class ArmHandler:
    default = None

    @classmethod
    def load_arm(cls):
        if cls.default is None:
            cls.default = ArmHandler()
        return cls.default

    def __init__(self):
        self.j1 = 1500
        self.j2 = 1500
        self.j3 = 1500
        self.j4 = 1500
        self.j5 = 1500
        self.j6 = 1500
        self.j7 = 1500
        self.j8 = 1500

        self.queue_head = None
        self.queue_tail = None
        self.size = 0

    def enqueue(self, item):
        n = Node(item)
        if self.queue_head is None:
            self.queue_head = n
        else:
            self.queue_tail.next = n
        self.queue_tail = n
        self.size += 1

    def dequeue(self):
        if self.queue_head is None:
            return None
        new_head = self.queue_head.next
        if new_head is None:
            self.queue_tail = None
        item = self.queue_head.item
        self.queue_head = new_head
        self.size -= 1
        return item

    def client(self):
        while True:
            item = self.dequeue()
            if item is not None:
                print(f"size: {self.size}")
                # self.on_retrieve_position(arm_json=item)
                # self.uart_tx_rx()

    def uart_tx_rx(self) -> None:
        j_str = (str(self.j1) + ":" + str(self.j2) + ":" + str(self.j3) + ":" + str(self.j4) + ":" + str(
            self.j5) + ":" + str(self.j6) + ":" + str(self.j7) + ":" + str(self.j8) + "$").encode('utf-8')
        print(j_str)
        serialPort = serial.Serial("/dev/ttyAMA1", 9600, timeout=2)
        bytes_sent = serialPort.write(j_str)
        print("SENT: ")
        print(bytes_sent)
        loopback = serialPort.read(bytes_sent)
        print("Received")
        print(loopback)

    def on_retrieve_position(self, arm_json) -> None:
        print(arm_json)
        self.j1 = arm_json["J1"]
        self.j2 = arm_json["J2"]
        self.j3 = arm_json["J3"]
        self.j4 = arm_json["J4"]
        self.j5 = arm_json["J5"]
        self.j6 = arm_json["J6"]
        self.j7 = arm_json["J7"]
        self.j8 = arm_json["J8"]
