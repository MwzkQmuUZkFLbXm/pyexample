#!/usr/bin/env python
# -*- coding: utf-8 -*-
# eatvowels.py

def eat_vowels(s):
    """Removes the vowels from s."""

    return ' '.join(c for c in s if c.lower() not in 'aeiou')

if __name__ == '__main__':

    print eat_vowels('Apple Sauce')
