#!/usr/bin/env python
# -*- coding: utf-8 -*-
# forfact.py

n = int(raw_input('Enter an integer >= 0: '))
fact = 1
for i in range(2, n+1):
    fact = fact * i
print(str(n) + ' factorial is ' + str(fact))
