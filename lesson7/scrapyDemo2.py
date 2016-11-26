#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapyDemo2.py
@time: 2016/11/15 20:01
"""


import requests
import json
from HTMLParser import HTMLParser

#解析器
class MovieParser(HTMLParser):
    #初始化
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    #处理起始标签
    def handle_starttag(self, tag, attrs):
        #匹配属性名，输出属性内容
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        #标签匹配  匹配以li为起始标签，包含data-title属性，同时data-category的属性内容等于nowplaying
        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs, 'data-category') == 'nowplaying':
            #创建一个movie的字典，并提取影片信息保存在movie字典里
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            #打印movie内容
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)
            self.in_movies = True

        #在匹配上合适的电影后，匹配电影的图片
        if tag == 'img' and self.in_movies:
            self.in_movies = False
            #获取图片链接
            src = _attr(attrs, 'src')
            #从movies链表中获取最后加入的movie对象
            movie = self.movies[len(self.movies) - 1]
            #将图片链接保存到movie对应的poster-url节点
            movie['poster-url'] = src
            #获取该
            _download_poster_image(movie)

def _download_poster_image(movie):
    src = movie['poster-url']
    #提交链接，接受响应数据
    r = requests.get(src)
    #获取图片的名称
    fname = src.split('/')[-1]
    #创建对应名称的文件，并在movie对应poster-path保存图片路径
    with open(fname, 'wb') as f:
        f.write(r.content)
        movie['poster-path'] = fname


def nowplaying_movies(url):
    #url-Agent:产生请求的浏览器类型
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    #获取
    r = requests.get(url,headers=headers)
    parser = MovieParser()
    parser.feed(r.content)
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/xiamen/'
    #含有影片信息的链表
    movies = nowplaying_movies(url)
    #含有影片信息的链表转换成json格式信息，sort_keys对dict排序，indent=4表示存储格式缩进4个字符
    #separators分割符，对数据进行压缩
    print('%s' % (json.dumps(movies, sort_keys=True, indent=4, separators=(',', ':'))) )