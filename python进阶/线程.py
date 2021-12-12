import threading
import time


def func01():
    for i in range(1000):
        print(".")
        time.sleep(0.01)


def func02():
    for i in range(1000):
        print("*")
        time.sleep(0.01)


if __name__ == "__main__":
    th1 = threading.Thread(target=func01)
    th2 = threading.Thread(target=func02)
    # 线程守护：子线程跟随主线程结束而结束
    th1.setDaemon(True)
    th2.setDaemon(True)
    th1.start()
    th2.start()
    # 线程阻塞：主线程在子线程结束后才结束
    th1.join()
    th2.join()
    print("主线程跑路")
