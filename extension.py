#!/usr/bin/env python
# -*- coding: utf-8 -*-
# extension.py

def get_ext(fname):
    """Return the extension of file fname."""
    dot = fname.rfind('.')
    if dot == -1:
        return None
    else:
        return fname[dot+1:] 

if __name__ == '__main__':
    print get_ext('hello.txt')
