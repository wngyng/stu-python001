"""
wait 处理僵尸进程
"""
import os

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process", os.getpid())
    os._exit(3)
else:
    # pid, status = os.wait()  # 等待僵尸进程结束
    pid, status = os.waitpid(-1, os.WNOHANG)  # 非阻塞状态
    print("pid:", pid)
    print("status:", os.WEXITSTATUS(status))
    while True:
        pass
