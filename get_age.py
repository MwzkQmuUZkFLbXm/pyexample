#!/usr/bin/env python
# -*- coding: utf-8 -*-
# get_age.py 

def get_age():
    while True:
        try:
            n = int(raw_input('How old are you?'))
            return n
        except ValueError:
            print('Please enter an integer value.')


if __name__ == '__main__':
    print get_age()
