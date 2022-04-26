import importlib
import io
spam_spec = importlib.util.find_spec("picamera")
if spam_spec:
    from picamera import PiCamera

def get_camera_generator():
    if spam_spec:
        camera = PiCamera()
        # camera.resolution = (1920, 1080)
        camera.resolution = (68 * 3, 48 * 3)
        camera.framerate = 30
        stream = io.BytesIO()

        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield stream.read()
            stream.seek(0)
            stream.truncate()
    else:
        while True:
            yield "Debugging on Non Raspberry Pi"
