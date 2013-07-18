import random
E, V, R, I, O = map(int, raw_input().split())
minrands = [I for i in xrange(V)]
lines = []
for i in xrange(E*2):
  v = random.randint(0,V-1) # which visitor
  r = random.randint(1,R) # room number
  in_time = random.randint(minrands[v],O)
  out_time = random.randint(minrands[v]+1, \
    min(minrands[v]+((O-I)/(1+(E/2))),O)) # some pseudo-random time interval
  minrands[v] = out_time+1
  lines.append(map(str, [v, r, "I", in_time]))
  lines.append(map(str, [v, r, "O", out_time]))
random.shuffle(lines)
print E*2
for line in lines:
  print " ".join(line)


