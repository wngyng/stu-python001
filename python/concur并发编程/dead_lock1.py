from threading import Thread, Lock, RLock
import time

num = 0  # 共享资源
# 重复载入锁（在一个线程内可以重复上锁，上几次解几次）
lock = RLock()


class MyThread(Thread):
    def fun1(self):
        global num
        with lock:  # 上锁
            num -= 1

    def fun2(self):
        global num
        if lock.acquire():  # 上锁
            num += 1
            if num > 5:
                # 打印到5就不打印了，因为fun1()重复上锁，所有暂停
                self.fun1()
            print(self.name, "Num = ", num)
            lock.release()

    def run(self):
        while True:
            time.sleep(2)
            self.fun2()


for i in range(10):
    t = MyThread()
    t.start()
