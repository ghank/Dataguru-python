#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: threadDemo.py
@time: 2016/11/21 21:16
"""

from threading import Thread, current_thread, Lock
import time

# def worker(lock):
#     while True:
#         lock.acquire()
#         print 'in worker %s' %current_thread()
#         lock.release()
#         time.sleep(0.5)

def worker():
    while True:
        print 'in worker %s' %current_thread()
        time.sleep(0.5)

class MyThread(Thread):
    def __init__(self, lock):
        Thread.__init__(self)
        self._lock = lock

    def run(self):
        while True:
            self._lock.acquire()
            print 'in worker %s' %current_thread()
            self._lock.release()
            time.sleep(0.5)


if __name__ == '__main__':
    l = Lock()
    print 'in main %s' %current_thread()
    # threads = [Thread(target=worker, args=[l]) for i in range(5)]
    threads = [MyThread(l) for i in range(5)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()