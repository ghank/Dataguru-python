#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: test_weekday.py
@time: 2016/10/23 15:28
"""

# from weekdays.homework3_ex import sumWeekday
from lesson3.weekdays.homework3_better import sumWeekday
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_dict = {(2016, 10): u'星期一', (2016, 9): u'星期五', (2016, 8): u'星期三', (2016, 7): u'星期日',
                     (1988, 10): u'星期一', (1988, 9): u'星期五', (1988, 8): u'星期三', (1988, 7): u'星期日'}
        keys = test_dict.viewkeys()
        keyslist = list(keys)
        for i in range(0, 8):
            print keyslist[i][0], keyslist[i][1], test_dict[keyslist[i]], sumWeekday(keyslist[i][0], keyslist[i][1])
            self.assertEqual(sumWeekday(keyslist[i][0], keyslist[i][1]), test_dict[keyslist[i]])

if __name__ == '__main__':
    unittest.main()
