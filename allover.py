#!/usr/bin/env python
# -*- coding: utf-8 -*-
# allover.py 

import re

def is_done1(value):
    return value == 'done' or value == 'quit'

if __name__ == '__main__':
    value = raw_input('Enter a value: ')
    is_done1(value)
