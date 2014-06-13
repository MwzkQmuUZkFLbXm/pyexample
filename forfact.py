#!/usr/bin/env python
# -*- coding: utf-8 -*-
# forfact.py

n = int(raw_input('Enter an integer >= 0: '))
fact = 1
for i in range(2, n+1):
    fact = fact * i
print(str(n) + ' factorial is ' + str(fact))

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

print '*'*10
print fact(0)
print fact(1)
print fact(5)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)

def fact1(n):
    return fact_iter(1, 1, n)
print '*'*10
print fact1(100)
