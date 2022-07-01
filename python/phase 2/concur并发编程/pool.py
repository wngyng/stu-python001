"""
进程池原理示意
"""
from multiprocessing import Pool
from time import sleep, ctime

# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)

# 创建进程池
po = Pool(6)
# 向进程池添加事件
for i in range(20):
    msg = "Hello %d" % i
    po.apply_async(func=worker, args=(msg,))
# 关闭进程池
po.close()
# 回收进程池
po.join()
