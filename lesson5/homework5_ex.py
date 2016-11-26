#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: sqlalchemy_ex.py
@time: 2016/11/1 11:04
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationships, backref
from time import clock
from socket import inet_aton, inet_ntoa
from codecs import decode
import struct
from sqlalchemy import and_

# 创建对象的基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'demo'

    id = Column(Integer, primary_key=True)
    srcIP = Column(Integer)
    destIP = Column(Integer)
    country = Column(String(100))
    telecom = Column(String(100))


#return filelist
def readfile(filename):
    data = []
    fp = open(filename, 'rb')
    for line in fp:
        if line.isspace():
            continue
        a = line.split()
        if len(a) == 4:
            data.append(a)
    fp.close()
    return data

def ip2long(ip):
    #将点分十进制 IP 地址转换成无符号的长整数
    return struct.unpack("!I", inet_aton(ip))[0]

def long2ip(lint):
    #将无符号长整形转换为点分十进制 IP 地址形式
    return inet_ntoa(struct.pack("!I", lint))

#获取对应ip所属的地址段
def queryIP(ip):
    # 初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine('mysql+mysqlconnector://root:000000@127.0.0.1:3306/test?charset=utf8', echo=False)
    Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        u1 = session.query(User).filter(and_(User.srcIP <= ip2long(ip), User.destIP >= ip2long(ip))).one()
    except Exception, e:
        session.close()
        return None

    session.close()
    return u1


if __name__ == '__main__':
    # 初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine('mysql+mysqlconnector://root:000000@127.0.0.1:3306/test?charset=utf8', echo=True)
    Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    #仅录入数据库时，使用
    # count = 0
    # index = 0
    # start = clock()
    # ipsList = readfile('2014ips.txt')
    # assert ipsList != None
    #
    # for elem in ipsList:
    #     if len(elem) != 4:
    #         continue
    #
    #     ipsInfo = User(id=index, srcIP=ip2long(elem[0]), destIP=ip2long(elem[1]), country=elem[2], telecom=elem[3])
    #     session.add(ipsInfo)
    #     count += 1
    #     index += 1
    #
    #     if count >= 10000:
    #         session.commit()
    #         count = 0
    # session.commit()
    # end = clock()
    # print "running time is ", end - start

    while True:
        startip = raw_input('start->:')
        endip = raw_input('end->:')
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        try:
            u1 = session.query(User).filter(and_(User.srcIP <= ip2long(startip), User.destIP >= ip2long(startip))).one()
            u2 = session.query(User).filter(and_(User.srcIP <= ip2long(endip), User.destIP >= ip2long(endip))).one()
        except Exception, e:
            print "ip: cann't find this info "
        finally:
            if u1 != None and u2 != None :
                u3 = session.query(User).filter(and_(User.id >= u1.id, User.id <= u2.id)).all()
                if u3 != []:
                    for e in u3:
                        print long2ip(e.srcIP), long2ip(e.destIP), e.country, e.telecom









