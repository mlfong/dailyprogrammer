# avoids print as it always puts a space after
# runs in O(2n)->O(n) and does not have a last row of just spaces
from sys import stdout
n = int(raw_input())
words = [raw_input() for x in xrange(n)]
limit = max([len(word) for word in words])
for i in xrange(0, limit):
  for word in words:
    stdout.write(word[i] if i < len(word) else " ")
  print 
