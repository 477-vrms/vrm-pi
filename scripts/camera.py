import socket
from time import sleep

f = open("img/pi.jpeg", "rb")
image: bytes = f.read()
f.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sock.sendto(image, ("127.0.0.1", 4200))
