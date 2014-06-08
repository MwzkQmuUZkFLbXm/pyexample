#!/usr/bin/env python
# -*- coding: utf-8 -*-
# html.py 

import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()
