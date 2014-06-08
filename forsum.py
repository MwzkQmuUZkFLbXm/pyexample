#!/usr/bin/evn python
# -*- coding: utf-8 -*-
#forsum.py

n = int(raw_input('How many numbers to sum?'))
total = 0
for i in range(n):
    s = raw_input('Enter number ' + str(i+1) + ': ')
    total = total + int(s)
print('The sum is ' + str(total))
