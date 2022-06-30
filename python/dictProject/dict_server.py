"""
dict 服务端部分
处理请求逻辑
"""
from socket import *
from multiprocessing import Process
import signal
import sys
from time import sleep
from operation_db import *
# 全局变量
HOST = '0.0.0.0'
POST = 8000
ADDR = (HOST, POST)


def main():
    """创建数据库链接对象
    """
    db = Database()
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    # 等待客户端连接
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
        # 创建子进程
        p = Process(target=do_request, args=(c, db))
        p.daemon = True
        p.start()


def do_register(c: socket, db: Database, data: str):
    """
    处理用户数据库注册用户
    Args:
        c (socket): 套接字
        db (Database): 数据库
        data (str): 数据库数据
    """
    tmp = data.split(' ')  # 空格分割
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'FAIL')


def do_request(c: socket, db: Database):
    """
    接收并处理客户端请求
    """
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ':', data,)
        if not data or data[0] == 'E':  # 无数据或返回E，退出
            c.close()
            sys.exit("客户端退出")
        if data[0] == 'R':
            db.create_cursor()  # 创建游标db.cur
            do_register(c, db, data)
        if data[0] == 'L':
            db.create_cursor()  # 创建游标db.cur
            do_login(c, db, data)
        if data[0] == 'Q':
            db.create_cursor()  # 创建游标db.cur
            do_query(c, db, data)
        if data[0] == 'H':
            db.create_cursor()  # 创建游标db.cur
            do_hist(c, db, data)


def do_login(c: socket, db: Database, data: str):
    """do_login 处理登录

    Args:
        c (socket): _description_
        db (Database): _description_
        data (str): L name passwd
    """
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'FAIL')


def do_query(c: socket, db: Database, data: str):
    """查询操作

    Args:
        c (socket): _description_
        db (Database): _description_
        data (str): _description_
    """
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]
    db.insert_history(name, word)  # 插入历史记录
    mean = db.query(word)   # 查单词
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())


def do_hist(c: socket, db: Database, data):
    name = data.split(' ')[1]
    r = db.hist(name)
    print(r)
    if not r:
        c.send(b"Fail")
        return
    c.send(b'OK')
    for line in r:
        # line ==> word ,time
        msg = "%s    %s    %s" % line
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)
    c.send(b'##')


if __name__ == '__main__':
    main()
