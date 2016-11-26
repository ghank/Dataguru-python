#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: sqlalchemy_ex.py
@time: 2016/11/1 11:04
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref


# 创建对象的基类:
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(100))

    books = relationship('Book')

    def __repr__(self):
        return "<User(id='%s', name='%s', address='%s', book='%s)>" %(self.id, self.name, self.address, self.books)

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(Integer, ForeignKey('user.id'))

class School(Base):
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:000000@127.0.0.1:3306/demo?charset=utf8', echo=True)
#3、映射实例化，创建数据库表 Base.metadata.create_all(engine) 来创建所有 Base 派生类所对应的数据表
Base.metadata.create_all(engine)

# 创建DBSession类型:
Session = sessionmaker(bind=engine)
# 创建session对象:
session = Session()

#5、操作数据库 (增删改查)
u1 = User(name='zhangsan', address='beijing')
b1 = Book(name='zhangsan', user_id=User.id)
# u2 = User(name='lisi', address='beijing')
# b1 = Book(name="zhangsan")
# b2 = Book(name="lisi")
session.add(u1)
session.add(b1)
#4.1、插入

# session.add(u1)
# session.add(u2)
# session.add(b1)
# session.add(b2)
session.commit()
# print u1.id
#
# us = [
#     ('list1', 'abc'),
#     ('list2', 'abc'),
#     ('list3', 'abc'),
#     ('list4', 'abc'),
#     ('list5', 'abc'),
#     ('list6', 'abc'),
# ]
# for u in us:
#     u2 = User(name=u[0], address=u[1])
#     session.add(u2)
#
# # session.commit()
#
# #4.2、查询
# u1 = session.query(User).filter(User.name.like('li%')).all()
# print u1
#
# u1 = session.query(User).filter(User.name == 'zhangsan').first()
# print u1
#
# #4.3、修改
# u1.address = 'jilin'
# session.commit()
#
# #4.4、删除
# session.delete(u1)
# session.commit()