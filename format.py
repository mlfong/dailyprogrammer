#!/usr/local/bin/python

'''
formats program for /r/dailyprogrammer commenting
-> adds 4 spaces before each line
'''

import sys
if len(sys.argv) != 2:
  print 'Usage: format.py INPUT'
  sys.exit(2)
with open(sys.argv[1]) as f:
  for line in f:
    print " "*4+line,

