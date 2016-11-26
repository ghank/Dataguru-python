#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Hank zhang
@contract:
@file: scrapyDemo4.py
@time: 2016/11/15 22:05
"""

import requests
import json
from HTMLParser import HTMLParser

#解析器
class NovelParser(HTMLParser):
    #初始化
    def __init__(self):
        HTMLParser.__init__(self)
        self.novels = []
        self.in_novels = False
        self.in_pics = False

    #处理起始标签
    def handle_starttag(self, tag, attrs):
        #匹配属性名，输出属性内容
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        #标签匹配
        if tag == 'li' and _attr(attrs, 'class') == 'subject-item':
            novel = {}
            self.novels.append(novel)
            self.in_novels = True

        if tag =='img' and self.in_novels:
            self.in_novels = False
            #获取图片链接
            src = _attr(attrs, 'src')
            novel = self.novels[len(self.novels) - 1]
            novel['poster-url'] = src

            #获取该
            _download_poster_image(novel)
            self.in_pics = True

        if tag == 'a' and _attr(attrs, 'title') and self.in_pics:
            self.in_pics = False
            title = _attr(attrs, 'title')
            novel = self.novels[len(self.novels) - 1]
            novel['title'] = title
            print('%(title)s | %(poster-url)s' % novel)


def _download_poster_image(novel):
    src = novel['poster-url']
    #提交链接，接受响应数据
    r = requests.get(src)
    #获取图片的名称
    fname = src.split('/')[-1]
    #创建对应名称的文件，并在movie对应poster-path保存图片路径
    with open('./pic/'+fname, 'wb') as f:
        f.write(r.content)
        novel['poster-path'] = fname


def showing_novels(url):
    #url-Agent:产生请求的浏览器类型
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    #获取
    r = requests.get(url,headers=headers)
    parser = NovelParser()
    parser.feed(r.content.decode('utf-8'))
    # parser.feed(r.content)
    return parser.novels

if __name__ == '__main__':
    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
    novels = showing_novels(url)
    print('%s' % (json.dumps(novels, sort_keys=True, indent=4, separators=(',', ':'))) )