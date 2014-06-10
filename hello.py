#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# hello.py 

def say_hello_to(name):
    """Prints a hello message."""
    cap_name = name.capitalize()
    print('Hello ' + cap_name + ', how are you?')

def main():
    string = raw_input('Enter a string:>>>')
    return say_hello_to(string)

if __name__ == '__main__':
    print main()
