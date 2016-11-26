#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: homework6_ex.py
@time: 2016/11/10 13:03
"""

from time import clock
from pymongo import MongoClient
import json
import struct
from socket import inet_aton
import re

#用于计算时间消耗的装饰器
def time_cost(f):
    def _f(*arg, **kwarg):
        start = clock()
        a=f(*arg,**kwarg)
        end = clock()
        print f.__name__,"run cost time is %s s."%(str(end-start))
        return a
    return _f


#return filelist
@time_cost
def readfile(filename):
    data = []
    fp = open(filename, 'rb')
    for line in fp:
        if line.isspace():
            continue
        a = line.split()
        data.append(a)
    fp.close()
    return data

#return filelist
@time_cost
def readfile1(filename):
    data = []
    fp = open(filename, 'rb')
    for line in fp:
        a = re.split('\s+', line)
        data.append(a)
    fp.close()
    return data

def ip2long(ip):
    #将点分十进制 IP 地址转换成无符号的长整数
    return struct.unpack("!I", inet_aton(ip))[0]

#将文件录入到mongoDB数据库中
@time_cost
def writeDB(filename):
    conn = MongoClient('localhost')
    db = conn.test
    db.documents.remove(None)
    index = 1
    vars = []

    ipsList = readfile(filename)
    assert ipsList != None

    for elem in ipsList:
        if len(elem) >= 3:
            doc = { '_id' : index, 'srcIP' : elem[0], 'srcIPint' : ip2long(elem[0]), \
                    'destIP' : elem[1], 'destIPint' : ip2long(elem[1]), 'country' : elem[2], 'telecom' : ''.join(elem[3:]) }
        index += 1
        vars.append(doc)

    db.documents.insert(vars)
    return


#获取两个ip之间的地址段信息
@time_cost
def ipsRange(startip, endip):
    conn = MongoClient('localhost')
    db = conn.test

    startipInt = ip2long(startip)
    endipInt = ip2long(endip)

    cur1 = db.documents.aggregate(
        [
            {   '$match': {
                '$or': [ { 'srcIPint': {'$lte': startipInt}, 'destIPint': {'$gte': startipInt} },
                         {'srcIPint': {'$lte': endipInt}, 'destIPint': {'$gte': endipInt}}
                        ]
                }
                # '$group': {
                #     'ns' : 'documents',
                #     'key': {'_id':True},
                #     'condition': {''}
                # }
            }
        ]
    )
    print u"ip所对应的国家和运营商："
    for doc in cur1:
        print doc['srcIP'], doc['destIP'], doc['country'], doc['telecom']

    cur2 = db.documents.aggregate(
        [
            {   '$match': {
                '$or': [ { 'srcIPint': {'$lte': startipInt}, 'destIPint': {'$gte': startipInt} },
                         {'srcIPint': {'$gt': startipInt}, 'destIPint': {'$lt': endipInt}},
                         {'srcIPint': {'$lte': endipInt}, 'destIPint': {'$gte': endipInt}}
                        ]
                }
            }
        ]
    )
    print u"ip对应的地址段："
    for doc in cur2:
        print doc['srcIP'], doc['destIP'], doc['country'], doc['telecom']
    return

if __name__ == "__main__":
    #将文件录入mongoDB数据库
    #writeDB("2014ips.txt")
    ipsRange('6.6.6.6', '9.8.8.8')
    ipsRange('222.178.179.58', '222.178.179.58')

