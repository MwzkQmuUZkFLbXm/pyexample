#!/usr/bin/env python
# -*- coding: utf-8 -*-
# list.py 

from __future__ import print_function
import os 

def list_cwd():
    return os.listdir(os.getcwd())

def files_cwd():
    return [p for p in list_cwd() if os.path.isfile(p)]

def folders_cwd():
    return [p for p in list_cwd() if os.path.isdir(p)]

def list_py(path=None):
    if path==None:
        path = os.getcwd()
        return [fname for fname in os.listdir(path) if os.path.isfile(fname) if fname.endswith('.py')]

def size_of_bytes(fname):
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    return sum(size_of_bytes(f) for f in files_cwd())

if __name__ == '__main__':
    print('\n'.join(list_cwd()))
    print()
    print('\n'.join(files_cwd()))
    print()
    print('\n'.join(folders_cwd()))
    print()
    print('\n'.join(list_py()))
    print()
    print(cwd_size_in_bytes())
