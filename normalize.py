#!/usr/bin/env python
# -*- coding: utf-8 -*-
# normalize.python

keep = ['a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z', ' ', '-', "'",'\n']

def normalize(s):
    """Convert s to normalized string."""
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result

def make_freq_dict(s):
    """Returns a dictionary whose keys are the words s, 
    and whose values are the counts of those words"""

    s = normalize(s)
    r = s.replace('\n', ' ')
    words = r.split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

#t = 'a long time ago in a galaxy far far away.'
#s = "I'd like to copy!"

def file_stats(fname):
    """Print statistics for the given file."""
    try:
        with open(fname, 'r') as f:
            s = f.read()
    except IOError as e:
            return e

    num_chars = len(s)
    num_lines = s.count('\n')
    d = make_freq_dict(s)
    print d
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()

    num_words = sum(d[w] for w in d)

    print("The file '%s' has:" % fname)
    print("%s characters" % num_chars)
    print("%s lines" % num_lines)
    print("%s words" % num_words)

    print("\nThe top 10 most frequent words are:")
    i = 1
    for count, word in lst[:10]:
        print('%2s. %4s %s' %(i, count, word))
        i += 1

def main():
    file_stats('bill.txt')

if __name__ == '__main__':
    main()
