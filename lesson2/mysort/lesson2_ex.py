#!/usr/bin/env python
# coding: utf-8
#
#  布置人:dasheng
# 1.自己实现一个排序算法，不能使用python内置的sorted和sort，具体哪种排序算法不限；
# 函数接口：mysort(data)
# 可选部分：【 对于有一定基础的同学，可以考虑扩展接口如下
#                mysort(data,key=somefunc,reveresed=True|False）
#                 支持自定义比较函数，比如按照sin(x)或者abs(x)结果排序这样；
#                 支持正序或者逆序排序；
# 】

# def mysort(data, key=somefunc, reveresed=True|False):
#
#     pass

def mysort(data):
    for j in xrange(len(data), -1, -1):
        for i in xrange(0, j-1, 1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
#
# elem = [7, 9, 8 ,19, 100, 76]
#
# mysort(elem)
# print elem

# 2.实现测试用例：

# 3.实现wordcount, 自己找一篇英文文章或者句子，统计每个单词出现次数，
# 并使用1中的排序算法输出排序后的结果。
# import re
# charector = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
# count = dict()
# text_list = []
# f = open('wordcount.txt', 'r')
# for eachline in f:
#     text_list.append(eachline.split(' '))
#
# print text_list
#
# # for elem in charector:
# #     count[elem] = 0
# #
# #     for ch in str:
# #         if ch == elem:
# #             count[elem] += 1
import re
text_list = []
wordpattern = r'\b[A-Za-z]+\b'
str = ''
f = open('wordcount.txt', 'r')

for eachline in f:
    str.join(eachline.split(' '))
print str
print re.findall(r'\b[A-Za-z]+\b', str)


