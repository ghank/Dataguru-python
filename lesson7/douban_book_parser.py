#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os
from HTMLParser import HTMLParser


class DoubanBookParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.book = []
        self.in_book = False
        self.in_pics = False
        self.in_reviews = False

    # handler to process "start tag"
    def handle_starttag(self, tag, attrs):

        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'class') == 'subject-item':
            book = {}
            self.book.append(book)
            self.in_book = True

        if tag == 'img' and self.in_book:
            self.in_book = False

            src = _attr(attrs, 'src')
            book = self.book[len(self.book) - 1]
            book['poster-url'] = src

            download_poster_image(book)
            self.in_pics = True

        if tag == 'p' and _attr(attrs, 'reviews') and self.in_reviews:
            reviews = _attr(attrs, 'reviews')
            book = self.book[len(self.book) - 1]
            book['reviews'] = reviews
            self.in_reviews = False

        if tag == 'a' and _attr(attrs, 'title') and self.in_pics:
            title = _attr(attrs, 'title')
            book = self.book[len(self.book) - 1]
            book['title'] = title
            self.in_pics = False
            #print('%(title)s | %(poster-url)s' % book)
            print('%(title)s | %(poster-url)s | %(reviews)s' % book)


# function to download the book's poster image
def download_poster_image(book):
    src = book['poster-url']

    r = requests.get(src)

    fname = src.split('/')[-1]
    with open('./pic/' + fname, 'wb') as f:
        f.write(r.content)
        book['poster-path'] = fname


# function to parse a single book
def download_book_info(book_url):
    # url-Agent:mockup the browser header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/54.0'}

    # pass the headers to the request so the website will think this is from a browser instead of from a program
    r = requests.get(book_url[0], headers=headers)

    # define the parser object
    parser = DoubanBookParser()
    parser.feed(r.content.decode('utf-8'))

    with os.open('./text/' + book_url[1], 'w', encoding='utf-8') as f:
        try:
            f.write(unicode(json.dumps(parser.book, ensure_ascii=False, indent=4)))
        except IOError, e:
            print 'f.write error', e

    return bookparser.book


if __name__ == '__main__':

    target_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/54.0'}

    x = requests.get(target_url, headers=headers)
    bookparser = DoubanBookParser()
    bookparser.feed(x.content)

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    imgpath = os.path.join(parent_dir, 'doubanbookimg')

    if not os.path.exists(imgpath):
        os.makedirs(imgpath)

    for b in bookparser.book:
        b.download_poster_image(imgpath, headers)
        # b.download_book_info()
        print(b)


        # print "running time is %s s."%(end-start)
