import sys
sys.path.insert(1, '../')
import os
from vrms.hardware.camera import get_camera_generator

generator = get_camera_generator()
print(generator)

i = 0
for temp in generator:
    print(temp, i)
    if i >= 30:
        break
    i += 1