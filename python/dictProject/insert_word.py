"""
将单词插入mysql
"""

import pymysql
import re

f = open('dict.txt')
db = pymysql.connect(host='192.168.200.139',
                     user='pc',
                     passwd='123123',
                     database='dict')
cur = db.cursor()
data = f.readline()
#word,mean = re.findall(r'(\w+)\s+(.+)', data)[0]
#print(word,'========',mean)
sql = 'insert into words(word,mean) values (%s,%s)'
for line in f:
    #获取匹配内容元祖（word,mean）
    tup = re.findall(r'(\w+)\s+(.*)', line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
f.close
cur.close
db.close
