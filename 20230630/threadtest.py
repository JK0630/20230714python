import threading
import time

def func():
    while True:
        time.sleep(1)
        print("sub thread")

t = threading.Thread(target=func)
t.start()

while True:
    time.sleep(2)
    print("main thread")