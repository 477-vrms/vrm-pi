# https://github.com/pika/pika
import os
from time import sleep
import datetime
import pika


def main() -> None:
    count: int = 0
    while True:
        x = datetime.datetime.now()
        print(f'Hello World: {x}')
        os.system(f'echo {count} >> logs.txt')
        count += 1
        sleep(3600)


if __name__ == "__main__":
    main()
