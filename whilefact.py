#!/usr/bin/env python
# -*- coding: utf-8 -*-
# whilefact.py 

n = int(raw_input("Enter an integer >= 0:-->"))
fact = 1
i = 2
while i <= n:
    fact *= i
    i +=1
print(str(n)+' factorial is '+str(fact))
