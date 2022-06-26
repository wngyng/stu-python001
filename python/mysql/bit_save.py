"""
二进制文件存储
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
#取出文件
sql = "select * from Images where filename='mv3.jpg'"
cur.execute(sql)
image = cur.fetchone()
with open(image[1], 'wb') as fd:
    fd.write(image[2])

cur.close()
db.close()
