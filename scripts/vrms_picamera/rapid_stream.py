import sys
sys.path.insert(1, '../../')
import os
from vrms.hardware.camera import get_camera_generator, get_video_generator

generator = get_video_generator()

i = 0
for temp in generator:
    print(len(temp))
    if i >= 30:
        break
    i += 1
print("error")