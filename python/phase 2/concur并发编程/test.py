import multiprocessing as mp
import time


# 计算密集型
def count(x, y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1


# io密集型
def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(1500000):
        f.write("hello world\n")
    f.close()


def read():
    f = open('test')
    lines = f.readline()
    f.close()


jobs = []
st = time.time()
for i in range(10):
    t = mp.Process(target=count,args=(1,1))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
print("Single CPU:", time.time() - st)
