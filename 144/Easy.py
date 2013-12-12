n = int(raw_input())
d = {x[0]: int(x[1]) for i in xrange(n) for x in [raw_input().split()] }
d = {x[0]: d[x[0]]-int(x[1]) for i in xrange(n) for x in [raw_input().split()] }
print "\n".join(k+" "+str(v) for k,v in d.items() if v != 0)
