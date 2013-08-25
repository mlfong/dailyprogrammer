N, M = map(int, raw_input().split(" "))
grid = [] # print N, M
for i in xrange(M):
	grid.append(raw_input())
X, Y, R = map(float, raw_input().split(" "))


point_in = set()
points = set()
for i in xrange(len(grid)):
  row = grid[i]
  for j in xrange(len(row)):
    if row[j] == 'x':
      point_in.add((i, j))
      point_in.add((i+1, j))
      point_in.add((i, j+1))
      point_in.add((i+1, j+1))
      points.add((i,j))
print X, Y, R


for row in grid:
  print row

import math
X2 = math.cos(R)
Y2 = math.sin(R)

y_del = Y2 - 0
x_del = X2 - 0
slope = y_del / x_del
# y = mx + b
m = slope
b = Y
x = X

x22 = x + 0.001
y22 = m * x22

print 'slope', slope

print "deltas", x_del, y_del
while True:
  tryall = [(math.floor(X), math.floor(Y)), (math.floor(X), math.ceil(Y)), (math.ceil(X), math.floor(Y)), (math.ceil(X), math.ceil(Y))]
  allin = (math.floor(X), math.floor(Y)) in points
  for t in tryall:
    allin &= t in point_in
  if allin:
    break
  else:
    # X -= 0.001
    # Y = m * X + b
    X -= x_del
    Y -= y_del
print X, Y



