#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Hank zhang
@contract:
@file: scrapyDemo5.py
@time: 2016/11/15 22:05
"""

import requests
import json, io
from HTMLParser import HTMLParser
import time
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


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
            #_download_poster_image(novel)
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
    with open('./pic/'+fname, 'wb') as f:
        f.write(r.content)
        novel['poster-path'] = fname


def showing_novels(url):
    #url-Agent:产生请求的浏览器类型
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/54.0'}
    #获取
    r = requests.get(url[0],headers=headers)
    parser = NovelParser()
    parser.feed(r.content.decode('utf-8'))

    with io.open('./text/'+url[1], 'w', encoding='utf-8') as f:
        try:
            f.write(unicode(json.dumps(parser.novels, ensure_ascii=False, indent=4)))
        except IOError, e:
            print 'f.write error',e

    return parser.novels


if __name__ == '__main__':
    import multiprocessing as multi
    from multiprocessing import Pool

    urls = []
    for i in xrange(4):
        http_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start="+str(20*i)+"&type=T"
        urls.append((http_url, str(i)))

    pool_num = 4
    pool = multi.Pool(pool_num)
    start = time.clock()
    pool.map(showing_novels, urls)
    end = time.clock()
    print "running time is %s s."%(end-start)




    # pool = Pool(4)
    # #检查
    # results = pool.map_async(showing_novels, [urls[0], urls[1], urls[2], urls[3]])
    # logging.debug(results.get(timeout=30))
    #
    # logging.debug(pool.map(showing_novels, urls))