n = int(raw_input())
for i in xrange(0, n):
  dic = {}
  for c in raw_input().lower():
    if ord('a') <= ord(c) <= ord('z'):
      if c in dic.keys():
        dic[c] += 1
      else:
        dic[c] = 1
  print len(dic.keys())==26, ", ".join(["%s: %s" % (key, dic[key]) for key in sorted(dic.iterkeys())])
