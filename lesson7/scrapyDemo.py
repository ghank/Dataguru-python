#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: scrapyDemo.py
@time: 2016/11/14 20:43
"""

# import requests
#
# url = 'https://movie.douban.com/chart'
# headers = {
#
# }
# response = requests.get(url)
# print response.status_code
# print response.text
#
# imgurl = "https://img1.doubanio.com/mpic/s27284878.jpg"
# response = requests.get(imgurl)
# f = open(imgurl.split('/')[-1], 'wb')
# f.write(response.content)
# f.close()

from __future__ import print_function
from HTMLParser import HTMLParser
import requests
import os

_MOVIE_PATH = 'html/head/meta/meta/meta/meta/meta/link/link/link/link/body/div/div/div/div/div/div/div/div/table'

class Movie(object):
    def __init__(self):
        self.attrs = []

    def __str__(self):
        #保存电影图片名称和链接
        content = []
        for k, v in self.attrs:
            #dict类型
            line = '{0} = {1}'.format(k, v)
            content.append(line)
        return '\r\n'.join(content)

    #影片图片下载
    def downloadImg(self, imgpath, headers):
        imgurl = None
        #判定Imgurl是否存在于attrs里
        for (k, v) in self.attrs:
            if k == 'movie_img_url':
                imgurl = v

        if imgurl is None:
            return None

        #取出影片名称
        imgname = imgurl.split('/')[-1]
        imglocalpath = os.path.join(imgpath, imgname)
        img = requests.get(imgurl, headers)
        with open(imglocalpath, 'wb') as f:
            f.write(img.content)
        #保存影片图片路径
        self.attrs.append(('movie_img_localpath', imglocalpath))
        return imglocalpath

#html解析器
class DouBanMovieRankParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._tags_stack = []
        self.movies = []
        self._new_movie = False

    def reset(self):
        HTMLParser.reset(self)
        self._tags_stack = []
        self._new_movie = False

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

        #可以用下面代码检查感兴趣内容的路径
        print (path)
        #是否与预置的电影路径一致；是，则解析这个字段
        if path == _MOVIE_PATH:
            self._new_movie = True
            #存取了Movie对象
            self.movies.append(Movie())
            print("movies.append")

        #获取电影url和title
        if self._new_movie == True and tag == 'a' and _getattr('class') == 'nbg':
            self.movies[-1].attrs.append(('movie_url',_getattr('href')))
            self.movies[-1].attrs.append(('movie_name', _getattr('title')))
        #提取图片url
        elif self._new_movie == True and tag == 'img':
            self.movies[-1].attrs.append(('movie_img_url', _getattr('src')))

    def handle_endtag(self, tag):
        path = '/'.join(self._tags_stack)
        if path == _MOVIE_PATH:
            self._new_movie = False
        #踢出倒数第一个元素
        self._tags_stack.pop()

    def handle_data(self, data):
        path = '/'.join(self._tags_stack)
        #可以用下面代码检查感兴趣内容的路径
        #print (path, data)

        if self._new_movie == True and path.endswith('/p'):
            self.movies[-1].attrs.append(('movie_intro', data))

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    x = requests.get('https://movie.douban.com/chart', headers=headers)
    movieparser = DouBanMovieRankParser()
    movieparser.feed(x.content)
    #当前目录
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    #图片路径
    imgpath = os.path.join(parent_dir, 'doubanmovieimg')
    #建立图片路径
    if not os.path.exists(imgpath):
        os.makedirs(imgpath)

    for movie in movieparser.movies:
        print(movie)
        movie.downloadImg(imgpath, headers)










