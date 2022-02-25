import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print(f"PrintThread -> {n}")


print(threading.main_thread().name)

pt = PrintThread()
pt.start()

for n in range(1, 11):
    print(f"MainThread -> {n}")


def print_numbers():
    for n in range(1, 11):
        print(f"NewThread -> {n}")


nt = Thread(target=print_numbers)
nt.start()
