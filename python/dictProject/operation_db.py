"""
dict 项目用于处理数据
"""
import pymysql
import hashlib
import time


class Database:
    """编写一个功能类，提供给服务端使用
    Args:
    host='192.168.200.139',port=3306,user='pc',passwd='123123',
                 database='dict',charset='utf8') :   
    """

    def __init__(self, host='192.168.200.139',
                 port=3306, user='pc',
                 passwd='123123', database='dict',
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_db()  # 链接数据库

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
        # 创建游标
        self.cur = self.db.cursor()

    def close(self):
        """关闭数据库"""
        self.cur.close()
        self.db.close()

    def register(self, name: str, passwd):
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
        # 加密处理
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

    def login(self, name: str, passwd):
        """login MySQL 登录验证

        Args:
            name (str): _description_
            passwd (str): _description_

        Returns:
            布尔值: _description_
        """
        sql = "select * from user where name = %s and passwd = %s"
        hash = hashlib.md5((name + "the-sat").encode())
        hash.update(passwd.encode())
        self.cur.execute(sql, [name, hash.hexdigest()])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def insert_history(self, name: str, word: str):
        """插入历史记录

        Args:
            name (str): _description_
            word (str): _description_
        """
        tm = time.ctime()
        sql = "insert into hist(name,word,time) value (%s,%s,%s)"
        try:
            self.cur.execute(sql, [name, word, tm])
            self.db.commit()
        except Exception as e:
            self.db.rollback()

    def query(self, word: str):
        """查单词

        Args:
            word (str): _description_
        """
        print(word)
        sql = "select mean from words where word = '%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]
        else:
            return

    def hist(self, name):
        sql = "select name,word,time from hist \
            where name = '%s' order by id desc limit 10" % name
        self.cur.execute(sql)
        msg=self.cur.fetchall()
        return msg
