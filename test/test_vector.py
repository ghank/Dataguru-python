#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: test_vector.py
@time: 2016/10/28 17:34
"""
import unittest
from lesson4.vector.homework4_ex import ArrayObject
from lesson4.vector.homework4_ex import VectorObject

class TestVectorMethods(unittest.TestCase):
    def test_Array(self):
        a = ArrayObject([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(a[0], 1)
        self.assertEqual(a[6], 7)

    def test_Vector(self):
        b = VectorObject([6, 7, 8, 9, 10])
        c = VectorObject([1, 2, 3, 4, 5])

        d = b+c
        self.assertEqual((b+c).getValue(), d.getValue())

        d = b*c
        self.assertEqual((b*c).getValue(), d.getValue())

        d = c*2
        self.assertEqual((c*2).getValue(), d.getValue())


if __name__ == '__main__':
    unittest.main()


