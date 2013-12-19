N, M = map(int, raw_input().split())
matrix = [[0 for y in xrange(N)] for x in xrange(N)]
for y in xrange(M):
  line = raw_input()
  lhs = map(int, line[:line.find("->")].split())
  adjs = map(int, line[line.find("->")+2:].split())
  for row in lhs:
    for adj in adjs:
      matrix[row][adj] = 1
print "\n".join("".join(str(el) for el in row)for row in matrix)
