#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fibonacci.py 

import time

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

aaa = time.time()
print fibonacci(35)
print time.time() - aaa

print '-' * 10

fib = lambda n:n if n < 2 else fib(n - 1)+fib(n - 2)
bbb = time.time()
print fib(35)
print time.time() - bbb

def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci1(n - 2) + fibonacci1(n - 1)

print '-' * 10
ccc = time.time()
print fibonacci1(35)
print time.time() - ccc
