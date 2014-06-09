#!/usr/bin/env python
# -*- coding: utf-8 -*-
# players.py 

import random
import getpass

class Player(object):
    def __init__(self, name):
        self.__name = name
        self.__score = 0 

    def reset_score(self):
        self.__score = 0

    def incr_score(self):
        self.__score += 1

    def get_name(self):
        return self.__name

    def __str__(self):
        return "name = '%s', score = %s" % (self.__name, self.__score)

    def __repr__(self):
        return 'Player(%s)' % str(self)

class Human(Player):
    def __repr__(self):
        return 'Human(%s)' % str(self)

    def get_move(self):
        while True:
            try:
                #n = int(input('%s move (1 - 10): ' % self.get_name()))
                n = int(getpass.getpass('%s move (1 - 10): ' % self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print('Oops!')
            except:
                print('Oops!')

class Computer(Player):
    def __repr__(self):
        return 'Computer(%s)' % str(self)

    def get_move(self):
        return random.randint(1, 10)

def play_undercut(p1, p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    #if not isinstance(p1, Human):
    print("%s move: %s" % (p1.get_name(), m1))
    #if not isinstance(p2, Human)
    print("%s move: %s" % (p2.get_name(), m2))

    if m1-1 >= m2:
        p1.incr_score()
        return p1, p2, '%s wins!' % p1.get_name()
    elif m2-1 >= m1:
        p2.incr_score()
        return p1, p2, '%s wins!' % p2.get_name()
    else:
        return p1, p2, 'draw: no winner'
