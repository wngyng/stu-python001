"""
dict 项目用于处理数据
"""
import pymysql


class Database:
    """ 
    编写一个功能类，提供给服务端使用
    """

    def __init__(self,
                 host='192.168.200.139',
                 port='3306',
                 user='pc',
                 passwd='123123',
                 database='dict',
                 charset='utf8') -> None:
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_db()  #链接数据库

    def connect_db(self):
        """连接MySQL
        """
        self.db = pymysql.connect(self.host, self.port, self.user, self.passwd,
                                  self.database, self.charset)

    def create_cursor(self):
        """创建游标
        """
        self.cur = self.db.cursor()

    def close(self):
        """关闭数据库"""
        self.cur.close()
        self.db.close()