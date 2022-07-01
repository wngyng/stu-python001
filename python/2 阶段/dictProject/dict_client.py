"""
dict 客户端
发起请求，展示结果
"""
from getpass import getpass
from socket import *
ADDR = ('192.168.200.135', 8000)
s = socket()
s.connect(ADDR)


def do_register():  # 注册
    while True:  # 输入密码错误循环
        name = input("User:")
        passwd = getpass("请输入密码")  # 调用密码隐藏函数
        passwd1 = getpass("重复输入密码：")
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s" % (name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 接收反馈
        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功！")
        else:
            print("注册失败！")
        return


def do_login():  # do_login 登录处理
    name = input("User:")
    passwd = getpass()
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())
    # 等待反馈
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功！")
        login(name)
    else:
        print("登录失败！")


def login(name):  # login 二级界面
    while True:
        print("""
        ================Query=================
        1.查单词       2.历史记录          3.注销
        ======================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确命令！")


def do_query(name: str):
    """查单词

    Args:
        name (str): _description_
    """
    while True:
        word = input("单词：")
        if word == '##':  # 结束单词查询
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        data = s.recv(1024).decode()  # 等待回复
        print(data)


def do_hist(name: str):
    """查询历史记录

    Args:
        name (str): _description_
    """
    msg = "H %s" % name
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("还没有历史记录！")


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
            do_register()  # 调用
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            print("谢谢使用！")
            return
        else:
            print("请输入正确命令！")


if __name__ == '__main__':
    main()
