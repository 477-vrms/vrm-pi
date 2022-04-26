import serial
import time
'''
def uart_tx_rx(self) -> None:
    j_str = (str(self.j1)+":"+str(self.j2)+":"+str(self.j3)+":"+str(self.j4)+":"+str(self.j5)+":"+str(self.j6)+":"+str(self.j7)+":"+str(self.j8)+"$").encode('utf-8')
    print(j_str)
    serialPort = serial.Serial("/dev/ttyAMA1", 9600, timeout = 2)
    bytes_sent = serialPort.write(j_str)
    print("SENT: ")
    print(bytes_sent)
    loopback = serialPort.read(bytes_sent)
    print("Received")
    print(loopback)

def on_retrieve_position(self,arm_json) -> None:
    print(arm_json)
    self.j1 = arm_json["J1"]
    self.j2 = arm_json["J2"]
    self.j3 = arm_json["J3"]
    self.j4 = arm_json["J4"]
    self.j5 = arm_json["J5"]
    self.j6 = arm_json["J6"]
    self.j7 = arm_json["J7"]
    self.j8 = arm_json["J8"]
'''
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

    def activate_buzzer(self):
        self.enqueue({
            "J1": "*",
            "J2": "*",
            "J3": "*",
            "J4": "*",
            "J5": "*",
            "J6": "*",
            "J7": "*",
            "J8": "*",
        })

    def enqueue(self, item):
        n = Node(item)
        self.queue_head = n

    def dequeue(self):
        if self.queue_head is None:
            return None
        new_head = self.queue_head.next
        item = self.queue_head.item
        self.queue_head = new_head
        return item

    def client(self, lock):
        while True:
            item = self.dequeue()
            if item is not None:
                #print("i")
                #print(item)
                self.on_retrieve_position(arm_json=item)
                self.uart_tx_rx()

    def uart_tx_rx(self) -> None:
        j_str = (str(self.j1) + ":" + str(self.j2) + ":" + str(self.j3) + ":" + str(self.j4) + ":" + str(
            self.j5) + ":" + str(self.j6) + ":" + str(self.j7) + ":" + str(self.j8))
        j_str_encode = (j_str + "$"*(96-len(j_str))).encode('utf-8')
        #print(j_str_encode)
        serialPort = serial.Serial("/dev/ttyAMA0", 9600, parity=serial.PARITY_NONE,timeout=0.2)
        #print(serialPort)
        bytes_sent = serialPort.write(j_str_encode)
        #print("SENT: ")
        #print(bytes_sent)
        loopback = serialPort.read(bytes_sent)
        #print("Received")
        #print(loopback)

    def on_retrieve_position(self, arm_json) -> None:
        # print(arm_json)
        self.j1 = arm_json["J1"]
        self.j2 = arm_json["J2"]
        self.j3 = arm_json["J3"]
        self.j4 = arm_json["J4"]
        self.j5 = arm_json["J5"]
        self.j6 = arm_json["J6"]
        self.j7 = arm_json["J7"]
        self.j8 = arm_json["J8"]
        
# if __name__ == "__main__":
#         serialPort = serial.Serial("/dev/ttyAMA0", 9600, parity=serial.PARITY_NONE,timeout=0.2)
#         #print(serialPort)
#         while(1):
#             bytes_sent = serialPort.write("118".encode('utf-8'))
#         #print("SENT: ")
#         #print(bytes_sent)
#             loopback = serialPort.read(bytes_sent)
