import serial

def uart_tx_rx(self) -> None:
    j_str = (str(self.j1)+":"+str(self.j2)+":"+str(self.j3)+":"+str(self.j4)+":"+str(self.j5)+":"+str(self.j6)+":"+str(self.j7)+":"+str(self.j8)+"$").encode('utf-8')
    print(j_str)
    serialPort = serial.Serial("/dev/ttyAMA1", 9600, timeout = 2)
    bytes_sent = serialPort.write(j_str)
    #print("SENT: ")
    #print(bytes_sent)
    #loopback = serialPort.read(bytes_sent)
    #print("Received")
    #print(loopback)

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


class ArmHandler:

    def __init__(self):
        self.j1 = 1500
        self.j2 = 1500
        self.j3 = 1500
        self.j4 = 1500
        self.j5 = 1500
        self.j6 = 1500
        self.j7 = 1500
        self.j8 = 1500
        pass

    def add_json(self, item):
        on_retrieve_position(self,arm_json=item)
        uart_tx_rx(self)
