import os
import time
from typing import Optional


def on_retrieve_position(arm_json) -> None:
    latency = -1
    current = (time.time() % 10000000000)
    if "T" in arm_json:
        latency = current - float(arm_json["T"])
    os.system(f'echo "{arm_json}, {current}, {latency}" >> joint.csv')


class JsonData:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class ArmHandler:

    def __init__(self):
        self.queue: Optional[JsonData] = None
        self.tail: Optional[JsonData] = None

    def add_json(self, item):
        on_retrieve_position(arm_json=item)
        # it is buggy here, ignore
        # if self.tail:
        #     self.tail.next_node = JsonData(data=item)
        #     self.tail = self.tail.next_node
        # else:
        #     self.tail = JsonData(data=item)
        #     self.queue = self.tail
        #     print("queue is set")

    def client(self) -> None:
        # It is buggy here, ignore
        while True:
            pass
            # if self.queue is not None:
            #     print("Got to Here")
            #     head: JsonData = self.queue
            #     self.queue = self.queue.next_node
            #     self.tail = None if self.queue is None else self.tail
