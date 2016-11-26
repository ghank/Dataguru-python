#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapyDemo1.py
@time: 2016/11/14 23:40
"""

from HTMLParser import HTMLParser
from htmlentitydefs import  name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print 'handle_starttag:<%s>'%tag
        return attrs

    def handle_endtag(self, tag):
        print 'handle_endtag:<%s>'%tag

    def handle_startendtag(self, tag, attrs):
        print 'handle_startendtag:<%s>'%tag

    def handle_data(self, data):
        print 'data:'

    def handle_comment(self, data):
        print '<!-- -->'

    def handle_entityref(self, name):
        print 'handle_entityref:&%s:'%name

    def handle_charref(self, name):
        print 'handle_charref:&#%s:'%name

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')
b = parser.handle_starttag('a', [('href', 'http://www.cwi.nl/')])
print b