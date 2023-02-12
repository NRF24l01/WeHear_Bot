from multiprocessing import Process
import time

def voice():
    print(231)
    while True:
        print("sad")
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=voice)
    p.start()
    while True:
        print(214)
        time.sleep(1)