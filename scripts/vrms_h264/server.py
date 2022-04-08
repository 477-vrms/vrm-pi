import io
import itertools
import picamera
from multiprocessing import process

def buffer_generator():
    s = 0

    s1 = io.BytesIO()
    s2 = io.BytesIO()
    while True:
        if s == 0:
            yield s1
            s = 1
        else:
            yield s2
            s = 0

b_gen = buffer_generator()
camera = picamera.PiCamera()
generator = camera.record_sequence(b_gen)

def temp():
    analyse = next(generator)
    analyse.seek(0)
    temp = analyse.read()
    analyse.seek(0)
    analyse.truncate()
    return temp

count = 0
while count < 30:
    foo = temp()
    print(len(foo))
    count += 1
print("done")