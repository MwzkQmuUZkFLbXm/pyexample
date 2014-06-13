#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multi_processing.py 
from multiprocessing import Process
import os

print '*'* 20
print 'Process %s start...' % os.getpid()
print '*'*20 
pid = os.fork()
if pid == 0:
    print 'I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just create a child process (%s).' % (os.getpid(), pid)
