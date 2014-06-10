#!/usr/bin/env python
# -*- coding: utf-8 -*-
# local.py 

import math
def dist(x, y, a, b):
    s = (x - a) ** 2 + (y - b) ** 2
    return math.sqrt(s)

def rect_area(x, y, a, b):
    width = abs(x - a)
    height = abs(y - b)
    return width * height

print dist(4,4,2,2)
print rect_area(4,4,2,2)
