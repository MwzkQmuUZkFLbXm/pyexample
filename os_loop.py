#!/usr/bin/env python
# -*- coding: utf-8 -*-
# os_thread.py 

import time, threading

def loop():
    print 'thread %s is running...' % threading.currentThread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.currentThread().name, n)
        time.sleep(10)
    print 'thread %s ended.' % threading.currentThread().name

print 'thread %s is running...' % threading.currentThread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s end.' % threading.currentThread().name
