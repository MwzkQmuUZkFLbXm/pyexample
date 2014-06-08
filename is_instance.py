#!/usr/bin/env python
# -*- coding: utf-8 -*-
# is_instance.py 

value = ['list','tuple','dict',['list','tuple','dict',['forg', 'dog','hamster',['green','blue','orange','white']]]]

def is_instance(value):
    if isinstance(value, list):
        for item in value:
            if isinstance(item, list):
                for i in item:
                    print i
            else:
                print item
    else:
        return False

def is_instance1(value):
    for i in value:
        if isinstance(i, list):
            is_instance1(i)
        else:
            print i

if __name__ == '__main__':
    is_instance1(value)
