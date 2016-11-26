#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: homework4_ex.py
@time: 2016/10/25 18:19
"""
# 1、参考老师上传的资料的 2.1节内容，实现一个一维数组类，要支持下标操作符
# 2、继承 1的 数组类实现一个向量类，要求支持向量的加法、乘法运算。
# 详细见视频中的介绍。


import numpy as np
class ArrayObject(object):

    def __init__(self, data=None):
        self.value = np.array(data)

    def __get__(self, instance, owner):
        return self.data.get(instance, self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __repr__(self):
        return str(self.value)


from types import IntType
class VectorObject(ArrayObject):
    def __init__(self, data=None):
        super(VectorObject, self).__init__(data)

    def __add__(self, other):
        item = VectorObject()
        if isinstance(other, VectorObject):
            item.value = self.value + other.value
        else:
            return None
        return item

    def __mul__(self, other):
        item = VectorObject()
        #if type(other) is IntType:
        if isinstance(other, int) or isinstance(other, float):
            item.value = self.value*other
        elif isinstance(other, VectorObject):
            item.value = self.value * other.value
        else:
            return None
        return item

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

#class metacls(type):
#    def __new__(mcs, name, bases, dict):
#        dict['foo'] = 'metacls was here'
#        return type.__new__(mcs, name, bases, dict)


if __name__ == "__main__":
    a = VectorObject()
    a = VectorObject([1,2,3,4,5])
    b = VectorObject([6,7,8,9,10])
    print a[0]
    print a+b
    print a*b
    print a*6




