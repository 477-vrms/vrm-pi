import sys
sys.path.insert(1, '../')
import os
from vrms.network.udp import Udp
import numpy as np
import cv2

u = Udp.load_udp()
out = None

temp = None
filename = "mwen.h264"

count = 0

while count < 200:
    if out is None:
        width  = 640 # float
        height = 480 # float

        fourcc = cv2.VideoWriter_fourcc(*'H264')
        out = cv2.VideoWriter(filename, fourcc, 30, (width, height))
    else:
        frame = u.get_frame()
        print(len(frame))
        if count == 0:
            f = open("temp.txt", "wb")
            f.write(frame)
            f.close()
        # out.write(y)
        count += 1

if out is not None:
    out.release()  
