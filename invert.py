#!/usr/bin/env python
# -*- coding: utf-8 -*-
# invert.py 
from __future__ import print_function

def invert(x):
    try:
        return 1 / x
    except ZeroDivisionError as e:
        return e
    finally:
        print('invert(%s) done' % x)

def write_to_file(fname):
    try:
        num = 1
        with open(fname, 'r+') as f:
            for line in f:
                print('%d %s' %(num, line), end='')
                num = num + 1
    except IOError as e:
        return e 

if __name__ == '__main__':
    #print invert(0)
    print (write_to_file('story.txt'))
