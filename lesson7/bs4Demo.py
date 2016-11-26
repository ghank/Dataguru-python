#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: bs4Demo.py
@time: 2016/11/19 22:29
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

html = urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')
bsObj = BeautifulSoup(html, "lxml")
subjectList = bsObj.find_all("li",{"class":"subject-item"})
for subject in subjectList:
    print(subject)
