#!/usr/bin/env python
# -*- coding: utf-8 -*-
# person.py 

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    def __str__(self):
        return "%s" % self._x

    def __repr__(self):
        return str(self)

class Person(object):
    """Class to represent a person."""

    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self.__age = age

    def __str__(self):
        return "Person('%s', %s)" % (self.__name, self.__age)

    def __repr__(self):
        return str(self)
