"""
dict 服务端部分
处理请求逻辑
"""
from socket import *
from multiprocessing import Process
import signal
import sys
from operation_db import *
#全局变量
HOST = '0.0.0.0'
POST = 8000
ADDR = (HOST, POST)


def main():
    """创建数据库链接对象
    """
    db = Database()
    #创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    #处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    #等待客户端连接
    print("Listen the port 8000")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        #创建子进程
        p = Process(target=do_request, args=(c, db))
        p.daemon = True
        p.start()


def do_request(c: socket, db: Database):
    """
    处理客户端请求
    """
    while True:
        data = c.recv(1024).decode()
        print(data)


if __name__ == '__main__':
    main()