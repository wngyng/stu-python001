"""
写数据库练习
增删改
"""
from os import curdir
import pymysql

db = pymysql.connect(host='192.168.200.139',
                     user='pc',
                     passwd='123123',
                     database='HonorKings',
                     charset='utf8')
#创建游标
cur = db.cursor()
try:
    #插入操作
    sql = "insert into interest values\
         (1,'Alex','sing','A',6354,'凑合吧');"
    cur.execute(sql)
    #修改操作
    sql = "update interest set price=6666 where name='Abby';"
    cur.execute(sql)
    #删除操作    
    sql = "delete from myclass where score < 88;"
    cur.execute(sql)
    db.commit()
    print('上传成功！')
except Exception as e:
    db.rollback()
    print("错误",e)
cur.close
db.close