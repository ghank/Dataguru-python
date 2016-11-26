#!/usr/bin/env python
# encoding: utf-8
"""
@author:revised from scrapyDemo.py
@contract:
@file: doubanbookspider.py
@time: 2016/11/19 20:43
"""
from __future__ import print_function
from HTMLParser import HTMLParser
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


_BOOK_PATH =  'html/head/meta/meta/meta/link/link/body/div/div/div/div/div/div/div/div/ul/li'

class Book(object):
    def __init__(self):
        #定义一个属性集合
        self.attrs = []

    def __str__(self):
        #保存图书图片名称和链接
        content = []
        for k, v in self.attrs:
            #dict类型
            line = '{0} = {1}'.format(k, v)
            content.append(line)
        return '\r\n'.join(content)

    #图书图片下载
    def downloadImg(self, imgpath, headers):
        imgurl = None
        #判定Imgurl是否存在于attrs里
        for (k, v) in self.attrs:
            if k == 'book_img_url':
                imgurl = v

        if imgurl is None:
            return None

        #取出图书名称
        imgname = imgurl.split('/')[-1]
        imglocalpath = os.path.join(imgpath, imgname)
        img = requests.get(imgurl, headers)
        with open(imglocalpath, 'wb') as f:
            f.write(img.content)
        #保存图书图片路径
        self.attrs.append(('book_img_localpath', imglocalpath))
        return imglocalpath

#html解析器
class DouBanBookRankParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._tags_stack = []
        self.books = []
        self._new_book = False
        self.comparePath = ''.join(_BOOK_PATH)

    def reset(self):
        HTMLParser.reset(self)
        self._tags_stack = []
        self._new_book = False

    def handle_starttag(self, tag, attrs):
        def _getattr(attrname):
        # 匹配属性名，输出属性内容
            for attr in attrs:
                if attr[0] == attrname:
                    return attr[1]
            return None
        #保存标签
        self._tags_stack.append(tag)
        #标签的位置, tags之间用字符'/'相连
        path = '/'.join(self._tags_stack)

        #检查是否与预置的解析路径一致；若是，则解析这个字段
        if path == self.comparePath :
            self._new_book = True

            #存取Book对象
            self.books.append(Book())

        #获取图书url
        # if self._new_book == True and tag == 'li' and _getattr('class') == 'subject-item':
        if self._new_book == True and tag == 'a' and _getattr('title'):
            self.books[-1].attrs.append(('book_url',_getattr('href')))

        #self._new_book = False
        #
        #提取图片url
        elif self._new_book == True and tag == 'img':
            # self._tags_stack.pop()
            self.books[-1].attrs.append(('book_img_url', _getattr('src')))

    def handle_endtag(self, tag):
        #踢出倒数第一个tag
        self._tags_stack.pop()

        path = '/'.join(self._tags_stack)
        if path == self.comparePath:
            self._new_book = False
            self.comparePath += '/li'


    def handle_data(self, data):
        path = '/'.join(self._tags_stack)
        #可以用下面代码检查感兴趣内容的路径，第一次的时候使用，找出欲抓取的内容块的定位后就要disable掉，否则总打印一堆东西没用了
        #print (path, data)

        if self._new_book == True and path.endswith('/p'):
            self.books[-1].attrs.append(('book_intro', data))

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    x = requests.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', headers=headers)
    bookparser = DouBanBookRankParser()
    bookparser.feed(x.content)

    #当前目录
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    #图片路径
    imgpath = os.path.join(parent_dir, 'doubanbookimg')
    #建立图片路径
    if not os.path.exists(imgpath):
        os.makedirs(imgpath)

    for book in bookparser.books:
        print(book)
        #book.downloadImg(imgpath, headers)










