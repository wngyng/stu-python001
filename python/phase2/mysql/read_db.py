"""
数据库读操作
select
"""
from turtle import onrelease
import pymysql

db = pymysql.connect(host='192.168.200.139',
                     user='pc',passwd='123123',
                     database='HonorKings',
                     charset='utf8')
#创建游标
cur = db.cursor()
sql = "select * from myclass where age=13;"
#执行语句，cur拥有查询结果
cur.execute(sql)

#获取查找结果的第一个
#one_row = cur.fetchone()
#print(one_row)

#获取从查找结果前2个
#many_row=cur.fetchmany(2)
#print(many_row)

#获取全部查询结果
all_row=cur.fetchall()
print(all_row)
cur.close
db.close

