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
