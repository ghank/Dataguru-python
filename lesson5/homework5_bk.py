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

# 创建对象的基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    srcIP = Column(String(40))
    destIP = Column(String(40))
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
    return inet_aton(struct.pack("!I", lint))

if __name__ == '__main__':
    # 初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine('mysql+mysqlconnector://root:000000@127.0.0.1:3306/test?charset=utf8', echo=True)
    Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    count = 0
    index = 0

    # start = clock()
    # ipsList = readfile('2014ips.txt')
    # assert ipsList != None
    #
    # for elem in ipsList:
    #     if len(elem) != 4:
    #         continue
    #
    #     ipsInfo = User(id=index, srcIP=elem[0], destIP=elem[1], country=elem[2], telecom=elem[3])
    #     session.add(ipsInfo)
    #     count += 1
    #     index += 1
    #     session.commit()
    #     # if count >= 10000:
    #     #     session.commit()
    #     #     count = 0
    # session.commit()
    # end = clock()
    # print "running time is ", end - start

    while True:
        u1 = []
        ip = raw_input('--->ip:')
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        print ip2long(ip)
        try:
            u1 = session.query(User).filter(ip2long(ip) <= ip2long(User.destIP)).all()
        # except Exception, e:
        #     print "ip: cann't find this info "
        finally:
            if u1 != []:
                for elem in u1:
                    print elem.country, elem.telecom








