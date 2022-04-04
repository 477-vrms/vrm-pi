import sys
sys.path.insert(1, '../')
import os
from vrms.network.udp import Udp
import numpy as np
import cv2

cam = cv2.VideoCapture(0)