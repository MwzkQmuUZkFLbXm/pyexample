#!/usr/bin/env python
# -*- coding: utf-8 -*-
# convert_to_int.py 

def convert_to_int1(s,base):
    try:
        return int(s,base)
    except (ValueError, TypeError) as e:
        return e

def convert_to_int2(s, base):
    try:
        return int(s, base)
    except ValueError as e:
        return e
    except TypeError as e:
        return e

def convert_to_int3(s, base):
    try:
        return int(s, base)
    except:
        return 'error'

def convert_to_int4(s, base):
    try:
        return int(s, base)
    except TypeError as e:
        raise e
    except ValueError as e:
        raise e

if __name__ == '__main__':
    #print convert_to_int1('1100100',2)
    #print convert_to_int2('1000000000',2)
    #print convert_to_int3('1000000000',2)
    print convert_to_int4('1100100',2)
