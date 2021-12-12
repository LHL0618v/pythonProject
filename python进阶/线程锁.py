import threading
import time

# 线程锁可以解决共享全局变量时产生的数据冲突问题
lock = threading.Lock()
n = 0


def func():
    global n
    for i in range(1000):
        # 获取锁
        lock.acquire()
        n += 1
        n -= 1
        # 释放锁
        lock.release()
    print(n)


def func1():
    global n
    for i in range(1000):
        #  自动释放锁
        with lock:
            n += 1
            n -= 1
    print(n)


if __name__ == "__main__":
    start = time.time()
    th1 = threading.Thread(target=func1)
    th2 = threading.Thread(target=func1)
    # 线程守护：子线程跟随主线程结束而结束
    th1.setDaemon(True)
    th2.setDaemon(True)
    th1.start()
    th2.start()
    # 线程阻塞：主线程在子线程结束后才结束
    th1.join()
    th2.join()
    print(time.time() - start)
