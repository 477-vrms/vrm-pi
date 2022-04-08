from time import sleep
from picamera import PiCamera
import io
import itertools
import picamera

def get_camera_generator():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    stream = io.BytesIO()

    for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
        stream.seek(0)
        yield stream.read()
        stream.seek(0)
        stream.truncate()
