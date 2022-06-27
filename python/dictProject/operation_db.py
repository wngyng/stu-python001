"""
dict 项目用于处理数据
"""
import pymysql
import hashlib


class Database:
    """编写一个功能类，提供给服务端使用
    Args:
    host='192.168.200.139',
                 port=3306,
                 user='pc',
                 passwd='123123',
                 database='dict',
                 charset='utf8') :   
    """

    def __init__(self,
                 host='192.168.200.139',
                 port=3306,
                 user='pc',
                 passwd='123123',
                 database='dict',
                 charset='utf8'):
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
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    def create_cursor(self):
        #创建游标
        self.cur = self.db.cursor()

    def close(self):
        """关闭数据库"""
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        """register 处理注册
        Args:
            name (_type_): 用户名
            passwd (_type_): 密码
        Returns:
            布尔值: 是否成功注册
        """
        sql = "select * from user where name ='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False
        #加密处理

        hash = hashlib.md5((name + "the-sat").encode())
        hash.update(passwd.encode())
        sql = "insert into user (name,passwd) values(%s,%s)"
        try:
            self.cur.execute(sql, [name, hash.hexdigest()])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            return False