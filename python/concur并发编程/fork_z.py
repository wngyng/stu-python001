import os

pid = os.fork()
if pid < 0:
    pass
elif pid == 0:
    print("Child process:", os.getgid())
else:
    while True:
        pass
