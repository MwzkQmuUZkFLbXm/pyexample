#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write.py 

from __future__ import print_function
import os

def make_story():
    if os.path.isfile('story.txt'):
        print('story.txt already exists.')
    else:
        f = open('story.txt','w')
        f.write('Mary had a little lamb,\n')
        f.write('and then she had some more.\n')

def add_to_story(line, fname='story.txt'):
    f = open(fname, 'a')
    f.write(line)

def insert_title(title, fname='story.txt'):
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp 
    f.seek(0)
    f.write(temp)

def is_gif(fname):
    f = open(fname, 'rb')
    first4 = tuple(f.read(4))
    return first4 == (0x47, 0x49, 0x46, 0x38)

if __name__ == '__main__':
    make_story()
