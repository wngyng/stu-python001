from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(esc, name):
    for i in range(3):
        sleep(esc)
        print("I'm %s" % name)
        print("I'm working...")


# 位置传参
# p = Process(target=worker, args=(2, "Baron"))
# 关键字传参
# p = Process(target=worker, kwargs={'name': "Abby", 'esc': 2})
p = Process(target=worker, args=(2,), kwargs={'name': "Abby"})
p.start()
p.join()
