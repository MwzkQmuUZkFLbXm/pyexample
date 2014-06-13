#!/usr/bin/env python
# -*- coding: utf-8 -*-
# remail.py 

import re

remail_c1 = re.compile(r'^(.+)@(.+)$')
remail_c2 = re.compile(r'^<(.+)>\s(.+)@(.+)$')

def remail_v1(email=None):
    if email == None:
        return "Please Enter an email"
    return remail_c1.match(email)

def remail_v2(email=None):
    if email == None:
        return False
    return remail_c2.match(email)
