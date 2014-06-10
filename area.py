#!/usr/bin/env python
# -*- coding: utf-8 -*-
# area.py 

import math
def area(radius):
    """Return the area of a circle with the given radius
    For example:
    >>> area(5.5)
    95.033177771091246"""

    return math.pi * radius ** 2

def main():
    print area(10)

if __name__ == '__main__':
    main()
