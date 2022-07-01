"""
套接字非阻塞示例
"""
from socket import *
from time import sleep, ctime

# 日志文件
f = open('log.txt', 'a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('192.168.200.135', 8888))
sockfd.listen(3)
# 设置套接字为非阻塞
# sockfd.setblocking(False)
# 设置超时检测
sockfd.settimeout(3)
while True:
    print("Waiting for connect..")
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        # 每隔2秒写入一条日志
        sleep(5)
        f.write("%s: %s \n" % (ctime(), e))
        f.flush()
    else:
        data = connfd.recv(1024).decode()
        print(data)
