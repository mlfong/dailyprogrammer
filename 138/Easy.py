from math import sqrt
m1, x1, y1 = map(float, raw_input().split(" "))
m2, x2, y2 = map(float, raw_input().split(" "))
dX, dY = x1 - x2, y1 - y2
dist = sqrt(dX**2 + dY**2)
print (m1*m2)/(dist**2)