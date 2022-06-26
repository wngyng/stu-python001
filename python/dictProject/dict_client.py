"""
dict 客户端
发起请求，展示结果
"""
import getpass
from socket import *

ADDR = ('192.168.200.135', 8000)
s = socket()
s.connect(ADDR)


def do_register():
    """注册
    """
    while True:  #输入密码错误循环
        name = input("User:")
        passwd = getpass.getpass("请输入密码")  #调用密码隐藏函数
        passwd1 = getpass("重复输入密码：")
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue

        msg = "R %s %s" % (name, passwd)
        #发送请求
        s.send(msg.encode())
        #接收反馈
        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功！")
        else:
            print("注册失败！")
        return


def main():
    """创建网络连接
    """
    while True:
        print("""
        =================Welcome==============
        1.注册           2.登录          3.退出
        ======================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            do_register()  #调用
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        else:
            print("请输入正确命令！")


if __name__ == '__main__':
    main()