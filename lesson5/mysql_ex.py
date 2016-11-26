#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: mysql_ex.py
@time: 2016/11/1 10:07
"""

from mysql import connector
#1、创建链接
params = dict(host='localhost', port=3306, user='root', password='000000', database='test')
conn = connector.connect(**params)

#2、创建游标
cursor = conn.cursor()

# #3、执行SQL语句
# ddl = '''
#     create table users(id integer, name varchar(40), address varchar(100))
# '''
#
# #需增加try...catch...语句
# cursor.execute(ddl)
sqltext = '''
    insert into users(name, address) values('zhangsan', 'beijing')
    '''
cursor.execute(sqltext)
conn.commit()

sqltext = '''
    select * from users
    '''
cursor.execute(sqltext)
for row in cursor:
    print row

sqltemplate = '''
    insert into users(name, address) values(%s, %s)
'''
u1 = ('lisi', 'abc')

cursor.execute(sqltemplate, u1)
conn.commit()

us = [
    ('lisi', 'abc'),
    ('lisi', 'abc'),
    ('lisi', 'abc'),
    ('lisi', 'abc'),
    ('lisi', 'abc'),
    ('lisi', 'abc'),
]
cursor.executemany(sqltemplate, us)
conn.commit()


