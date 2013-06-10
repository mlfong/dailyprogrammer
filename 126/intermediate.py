#!/usr/bin/python

import sys
from math import sqrt

def primeP(N, m=[]):
	for i in xrange(2, 1+int(sqrt(N))):
		s, c = 1, 0
		while s < N and s != N:
			s, c = s * i, c + 1
		if s == N: m.append(str(i) + '^' + str(c))
	if m: print 'N: ', N ,'\n', m
	pass

def highestPrimeP(N):
	from math import sqrt
	for i in xrange(2, 1+int(sqrt(N))):
		s, c = 1, 0
		while s < N and s != N:
			s, c = s * i, c + 1
		if s == N: 
			print('%d, (%d^%d)' % (c, i, c))
			return
	print('%d, (%d^%d)' % (1, N, 1))

def main():
	if len(sys.argv) != 2:
		print 'Usage: python intermediate.py N'
		return
	N = int(sys.argv[1])
	highestPrimeP(N)
	pass


if __name__ == '__main__':
	main()