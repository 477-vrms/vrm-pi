import io
import random
import picamera
from PIL import Image

prior_image = None

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    stream = picamera.PiCameraCircularIO(camera, seconds=1)
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            camera.split_recording('after.h264')
            stream.copy_to('before.h264', seconds=1)
            stream.clear()
            camera.split_recording(stream)
            break
    finally:
        camera.stop_recording()