"""
select函数讲解
"""
from socket import *
from select import select

# 做几个IO用于监控
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)
fd=open('log.txt','a+')
print("开始提交监控IO")
rs, ws, xs = select([s], [fd], [])
print("rs:", rs)
print("ws:", ws)
print("xs:", xs)
