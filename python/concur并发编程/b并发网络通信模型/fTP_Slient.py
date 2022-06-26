
import time
from socket import *
import sys


# 具体功能
class FtpClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        # ok表示请求成功
        if data == 'OK':
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):  # 退出
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(('G ' + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            #
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    def do_put(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print("没有该文件")
            return
            # 接收请求
        filename = filename.split('/')[-1]
        self.sockfd.send(('P ' + filename).encode())
        # 等待回复
        data = self.sockfd.recv(120).decode()
        if data == 'OK':
            while True:
                data=f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    print("上传完成")
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


# 发起请求
def request(sockfd):
    ftp = FtpClient(sockfd)
    while True:
        print("""
============== 命令选项 ==============
***************list******************
************** get file *************
************** put file *************
*************** quit ****************
=====================================""")
        cmd = input("输入命令：")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)


# 网络链接
def main():
    # 服务器地址
    ADDR = ('192.168.200.135', 8080)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("链接服务器失败")
        return
    else:
        print("""
        *********************************
           Data       File         Image
        *********************************""")
        cls = input("输入想要的文件类别：")
        if cls not in ['Data', 'File', 'Image']:
            print("Sorry input Error!")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)  # 发送具体请求


if __name__ == '__main__':
    main()
