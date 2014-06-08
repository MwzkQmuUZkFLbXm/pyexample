#!/usr/bin/env python
# -*- coding: utf-8 -*-
# printfile.py 
from __future__ import print_function

def print_file1(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end='')
    f.close()

def print_file2(fname):
    f = open(fname, 'r')
    print(f.read())
    f.close()

if __name__ == '__main__':
    print_file1('printfile.py')
    print()
    print_file2('list.py')
