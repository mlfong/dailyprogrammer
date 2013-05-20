#!/usr/local/bin/python

'''
formats program for /r/dailyprogrammer commenting
-> adds 4 spaces before each line
'''

import sys, os
if __name__=='__main__':
    if len(sys.argv) != 3: 
        print 'Usage: format.py [transcript]\nUse - for stdout.'
        sys.exit(2)
    if sys.argv[2] != '-': sys.stdout = file(sys.argv[2], 'w')
    f = open(sys.argv[1])
    for line in f:
        print "    "+line,
    f.close()
