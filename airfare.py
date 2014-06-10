#!/usr/bin/env python
# -*- coding: utf-8 -*-
# arefare.py 

age = int(raw_input("How old are you?-->"))
if age <= 2:
    print('Free')
elif 2 < age < 13:
    print('Child fare.')
else:
    print('Adult fare.')
