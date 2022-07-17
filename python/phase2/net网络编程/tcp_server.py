"""
TCP 套接字服务端
"""
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
sockfd.bind(('192.168.0.176', 8888))
# 设置监听
sockfd.listen(5)
# 等待处理客户端链接
print("waiting for connect....")
connfd, addr = sockfd.accept()
# 收发消息
data = connfd.recv(1024)
print("接收到的消息：", data)
n = connfd.send(b'Receive your message')
print("发送了%d个字节数据" % n)
# 关闭套接字
connfd.close()
sockfd.close()