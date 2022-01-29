# https://github.com/pika/pika
import os
import socket
from time import sleep
import datetime
from multiprocessing import Process
import pika

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def server() -> None:
    count: int = 0
    while count < 10:
        print("sending message")
        s.sendto(b"What Up Matt Wen", ("localhost", 8002))
        sleep(1)
        count += 1


def example() -> None:
    count: int = 0
    while True:
        x = datetime.datetime.now()
        print(f'Hello World: {x}')
        os.system(f'echo {count} >> logs.txt')
        count += 1
        sleep(3600)


def client() -> None:
    print("listening for messages")
    while True:
        data, addr = s.recvfrom(1024)
        print("received message: %s" % data)


def main() -> None:
    p1 = Process(target=client)
    p2 = Process(target=server)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
