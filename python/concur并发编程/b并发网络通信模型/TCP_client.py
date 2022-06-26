"""
TCP 套接字客户端
重点代码
"""
from socket import *

# 创建套接字
sockfd = socket()
# 发起连接
server_addr = ('192.168.200.135', 8888)
sockfd.connect(server_addr)
# 收发消息
sockfd.send('来自客户端的消息'.encode())
data = sockfd.recv(1024)
print("From server:", data)
# 关闭
sockfd.close()
