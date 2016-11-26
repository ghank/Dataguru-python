#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: test_lesson5.py
@time: 2016/11/6 18:48
"""

import unittest
from lesson5.homework5_ex import queryIP
import struct
from socket import inet_ntoa
from time import clock

def long2ip(lint):
    #将无符号长整形转换为点分十进制 IP 地址形式
    return inet_ntoa(struct.pack("!I", lint))

class TestIPqueryMethods(unittest.TestCase):
    def test_ipquery(self):
        start = clock()
        ipList = [
            ('1.24.217.8', u'内蒙古巴彦淖尔市', u'联通'),
            ('1.27.100.128', u'内蒙古赤峰市', u'联通巴林左旗林东镇新城区BRAS数据机房[新骨干线路]'),
            ('61.184.172.237', u'湖北省咸宁市', u'温泉红蜘蛛网吧'),
            ('61.184.177.55', u'湖北省咸宁市', u'电信ADSL'),
            ('61.184.178.68', u'湖北省咸宁市赤壁市', u'电信')
        ]
        for elem in ipList:
            u1 = queryIP(elem[0])
            self.assertEqual(u1.country, elem[1])
            self.assertEqual(u1.telecom, elem[2])
            print "u1: iprange(%s---%s), %s %s <---> elem: %s %s %s " %(long2ip(u1.srcIP), \
                            long2ip(u1.destIP), u1.country, u1.telecom, elem[0], elem[1], elem[2])

        end = clock()
        print "running time is %s s." % (end - start)

if __name__ == '__main__':
    unittest.main()


