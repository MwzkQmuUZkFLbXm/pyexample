#!/usr/bin/env python
# -*- coding: utf-8 -*-
# numnote.pyt 

def numnote(lst):
    msg = []
    for num in lst:
        if num < 0:
            s = str(num) + ' is negative'
        elif 0 <= num <= 9:
            s = str(num) + ' is a digit'
        msg.append(s)
    return msg


if __name__ == "__main__":
    print('\n'.join(numnote([1,5,-6,22])))
