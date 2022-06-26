"""
IO多路复用select实现多客户端通信
重点代码
"""
from socket import *
from select import select

# 设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)
# 设置关注IO
rlist = [s]
wlist = []
xlist = []
while True:
    # 监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历三个返回值列表，判断哪个IO发生
    for r in rs:
        # 如果是套接字就绪则处理链接
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)

    for w in ws:
        pass
    for x in xs:
        pass
