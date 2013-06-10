#!/usr/bin/ruby


# from math import sqrt
# 	for i in xrange(2, 1+int(sqrt(N))):
# 		s, c = 1, 0
# 		while s < N and s != N:
# 			s, c = s * i, c + 1
# 		if s == N: 
# 			print('%d, (%d^%d)' % (c, i, c))
# 			return
# 	print('%d, (%d^%d)' % (1, N, 1))

def highestPrimeP(n)
	for i in 2...Math.sqrt(n)
		$s, $c = 1, 0
		while $s <= n do
			$s *= i
			$c += 1
		end
		puts "#$s"
		if $s == n
			puts "#$c, (#{i}^#$c)"
			return
		end
	end
end


highestPrimeP(100)