from time import sleep
from picamera import PiCamera
import io

def get_camera_generator():
    camera = PiCamera()
    camera.resolution = (64 * 3, 48 * 3)
    camera.framerate = 30
    stream = io.BytesIO()

    for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
        stream.seek(0)
        yield stream.read()
        stream.seek(0)
        stream.truncate()

# camera.resolution = (1024, 768)
# camera.start_preview()
# # Camera warm-up time
# sleep(2)
# camera.capture('foo.jpg')
