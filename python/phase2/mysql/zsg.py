"""
MySQL语句传参练习
"""
from os import curdir
import pymysql
#df
db = pymysql.connect(host='192.168.200.139',
                     user='pc',
                     passwd='123123',
                     database='HonorKings',
                     charset='utf8')
#创建游标
cur = db.cursor()
while True:
    name = input('Name:')
    age = input("Age:")
    gender = input("m or w:")
    score = input("Score:")
    #sql = "insert into myclass(name,age,gender,score)\
    # values('%s',%d,'%s',%f);" % (name, age, gender, score)
    sql = "insert into myclass(name,age,gender,score)\
         values(%s,%s,%s,%f);"

    try:
        #以列表中元素全是字符串，执行语句，会自动识别类型
        cur.execute(sql, [name, age, gender, score])
        db.commit()
        print("已经提交记录。")
    except Exception as e:
        db.rollback()  #失败回滚到操作之前的状态
        print("Faild:", e)
cur.close()
db.close()