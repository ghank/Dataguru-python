#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: processDemo.py
@time: 2016/11/21 21:37
"""
from multiprocessing import Process, current_process
import time

def worker():
    while True:
        print 'in worker %s', current_process()
        time.sleep(0.5)

if __name__=="__main__":
    ps = [Process(target=worker) for i in range(6)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()