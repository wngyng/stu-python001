import pymysql
from login import Login

user = Login(database='user',
             host='192.168.200.139',
             user='pc',
             passwd='123123',
             table='login')


#成功返回True，失败返回false
def do_login():
    name = input("User:")
    passwd = input("Passwd:")
    return user.login(name, passwd)


def do_register():
    name = input("User")
    passwd = input("Passwd")
    return user.register(name, passwd)


while True:
    print("""
    =======================
    **       login       **
    **     register      **
    =======================""")
    cmd = input("Cmd:")
    if cmd == 'login':
        if do_login():
            print("登录成功！")
        else:
            print("登录失败！")
            break
    elif cmd == 'register':
        if do_register():
            print("登录成功！")
        else:
            print("登录失败！")
            break
    else:
        print("请重新输入")
user.close_db
