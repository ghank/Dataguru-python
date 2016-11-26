
#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: testdemo.py
@time: 2016/10/25 17:56
"""

class A(object):
    def __init__(self):
        pass

    def sayHi(self):
        print 'in A'

class B(A):
    def sayHi(self):
        # super(B, self).sayHi()
        super(B, self).sayHi()
        print 'in B'

class C(A):
    def sayHi(self):
        super(C, self).sayHi()
        print 'in C'

class D(B, C):
    def sayHi(self):
        super(D, self).sayHi()
        # B.sayHi(self)
        # C.sayHi(self)
        print 'in D'

# b = B()
# b.sayHi()
d = D()
d.sayHi()