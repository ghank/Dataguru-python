#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: homework8_ex.py
@time: 2016/11/23 21:37
"""

from HTMLParser import HTMLParser
import requests
import os
import logging
from threading import Thread, current_thread
from multiprocessing import Queue, Process
import time


logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s', \
                    datefmt='%a %d %b %Y %H:%M:%S')

_NOVEL_PATH = 'html/head/meta/meta/meta/link/link/body/div/div/div/div/div/div/div/div/ul/li'

class Novel(object):
    def __init__(self):
        self.attrs = []

    def __str__(self):
        content = []
        for k, v in self.attrs:
            #tuple类型
            line = '{0} = {1}'.format(k, v.encode('utf-8'))
            content.append(line)
        return '\r\n'.join(content)

    #图片下载
    def downloadImg(self, imgPath, headers):
        imgUrl = None
        #判定ImgUrl是否存在于attrs里
        for (k, v) in self.attrs:
            if k == 'novelImgUrl':
                imgUrl = v
        if imgUrl is None:
            return None
        logging.debug('%s download image' % (current_thread()))
        imgName = imgUrl.split('/')[-1]
        imgLocalPath = os.path.join(imgPath, imgName)
        img = requests.get(imgUrl, headers)
        with open(imgLocalPath, 'wb') as f:
            f.write(img.content)
        logging.debug('%s download image' % (imgLocalPath))
        #保存图片路径
        self.attrs.append(('novelImgLocalPath', imgLocalPath))
        return imgLocalPath

#html解析器
class DouBanNovelRankParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._tags_stack = []
        self.novels = []
        #解析路径
        self.comparePath = ''.join(_NOVEL_PATH)

    def reset(self):
        HTMLParser.reset(self)
        self._tags_stack = []
        self._new_novel = False
        self._next_url = False

    def handle_starttag(self, tag, attrs):
        def _getattr(attrName):
        # 匹配属性名，输出属性内容
            for attr in attrs:
                if attr[0] == attrName:
                    return attr[1]
            return None
        #保存标签
        self._tags_stack.append(tag)
        #标签的位置, tags之间用字符'/'相连
        path = '/'.join(self._tags_stack)
        #可以用下面代码检查感兴趣内容的路径

        #是否与预置的路径一致；是，则解析这个字段
        if path == self.comparePath:
            self._new_novel = True
            #存取了Novel对象
            self.novels.append(Novel())
        #获取url
        if self._new_novel == True and tag == 'a' and _getattr('title'):
            self.novels[-1].attrs.append(('novelUrl',_getattr('href')))
            self.novels[-1].attrs.append(('novelName', _getattr('title')))
        #提取图片url
        elif self._new_novel == True and tag == 'img':
            self.novels[-1].attrs.append(('novelImgUrl', _getattr('src')))

    def handle_endtag(self, tag):
        # 删除对应的起始tag
        self._tags_stack.pop()
        path = '/'.join(self._tags_stack)
        if path == self.comparePath:
            self._new_novel = False
            self.comparePath += '/li'

    def handle_data(self, data):
        path = '/'.join(self._tags_stack)
        #可以用下面代码检查感兴趣内容的路径
        # logging.debug(path, data)
        if self._new_novel == True and path.endswith('/p'):
            self.novels[-1].attrs.append(('novelIntro', data))

def getUrl(urlQueue, imgPath, header):
    while not urlQueue.empty():
        logging.debug('%s getUrl' % (current_thread()))
        x = requests.get(urlQueue.get(), headers=headers)
        novelParser = DouBanNovelRankParser()
        #x.content的str格式转化成unicode格式
        novelParser.feed(x.content.decode("utf-8"))
        for novel in novelParser.novels:
            print novel
            novel.downloadImg(imgPath, headers)
    logging.debug("getUrl func exit now.")


if __name__ == '__main__':
    queue = Queue()
    #当前目录
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    #图片路径
    imgPath = os.path.join(parent_dir, 'douBanNovelImg')
    #建立图片路径
    if not os.path.exists(imgPath):
        os.makedirs(imgPath)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/52.0.2840.71 Safari/537.36'
    }

    start = time.clock()

    for i in xrange(99):
        http_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start="+str(20*i)+"&type=T"
        queue.put(http_url)

    urlThreads = [Thread(target=getUrl, name="UrlThread", args=[queue, imgPath, headers,]) for i in range(16)]
    for t in urlThreads:
        t.start()
    for t in urlThreads:
        t.join()

    print "threads running time is %s s."%(time.clock()-start)

    #进程有自己独立的资源


