# "short" version
import random; m = map(int, raw_input("enter NdM: ").split("d")); print " ".join( [str(random.randint(1, m[1])) for i in xrange(0, m[0]) ] ) 

# long, normal version
from random import randint
N, M = map(int, raw_input("enter NdM: ").split("d"));
from random import randint
for i in xrange(0, N):
  print randint(1, M),
print 

