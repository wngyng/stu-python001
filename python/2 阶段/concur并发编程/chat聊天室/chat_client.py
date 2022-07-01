"""
搭建数据报套接字
"""
import os
import sys
from socket import *

# 服务器地址
ADDR = ('192.168.200.135', 8888)


def send_msg(s, name):
    # 发送消息
    while True:
        try:
            text = input("发言：")
        except KeyboardInterrupt:
            text = 'quit'
        # 退出聊天室
        if text == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


def recv_msg(s, name):
    # 接收消息
    while True:
        data, addr = s.recvfrom(2048)
        # 服务端发送EXIT表示让客户端退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + "\n发言：", end='')


def main():
    # 创建网络连接
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 等待回应
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    pid = os.fork()
    if pid < 0:
        sys.exit("Error！")
    elif pid == 0:
        send_msg(s, name)
    else:
        recv_msg(s, name)


if __name__ == "__main__":
    main()
