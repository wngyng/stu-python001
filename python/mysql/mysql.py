"""
pymysql 基本流程演示
"""
import pymysql

db = pymysql.connect(host='192.168.200.139',
                     port=3306,
                     user='pc',
                     passwd='123123',
                     database='HonorKings',
                     charset='utf8')
#创建游标对象
cur = db.cursor()
#shujucaozuosd
cur.execute("insert into myclass values(8,'Levi',13,'m',89.5)")

db.commit()
#closesdf
cur.close
db.close