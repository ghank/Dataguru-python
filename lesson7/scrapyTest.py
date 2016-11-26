#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapyTest.py
@time: 2016/11/15 0:00
"""

from HTMLParser import HTMLParser

htmlcontent = '''
                <title>这是一个标题</title>
              '''
class myTestParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._tags = []

    def handle_starttag(self, tag, attrs):
        self._tags.append(tag)

    def handle_data(self, data):
        print '/'.join(self._tags)+'='+data

    def handle_endtag(self, tag):
        self._tags.pop()

if __name__ == '__main__':
    test = myTestParser()
    test.feed(htmlcontent)
