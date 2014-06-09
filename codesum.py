#!/usr/bin/env python
# -*- coding: utf-8 -*-
# codesum.py 

def codesum(s):
    """Return the sums of the character codes of s"""
    total = 0
    for c in s:
        total = total + ord(c)
    return total 

if __name__ == '__main__':
    print codesum('Hi there!')
