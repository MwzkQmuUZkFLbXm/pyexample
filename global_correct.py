#!/usr/bin/env python
# -*- coding: utf-8 -*-
# global.py 

name = "Jack"
def say_hello(name):
    print('Hello ' + name + '!')
def change_name(new_name):
    global name
    name = new_name
    return name

print say_hello(name)
change_name('Piper')
print say_hello(name)

