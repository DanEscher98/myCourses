import math
import os
from concurrent.futures import ThreadPoolExecutor as Executor
from threading import Thread
from time import sleep


def worker(data):
    data += data
    print(data)


with Executor(max_workers=10) as exe:
    future = exe.submit(worker, "data")


threads = [Thread(target=lambda: sleep(50)) for i in range(10000)]

[t.start() for t in threads]
print(f"PID = {os.getpid()}")
[t.join() for t in threads]
