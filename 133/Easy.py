import collections, math
N, visitors, roomavgs = int(raw_input()), {}, {}
for i in xrange(N):
  person, room_num, inout, walltime = raw_input().split()
  key = (room_num, person)
  if key not in visitors.keys():
    visitors[key] = (inout, int(walltime))
  else:
    room_num = int(room_num)
    if room_num not in roomavgs.keys():
      roomavgs[room_num] = []
    roomavgs[room_num].append(math.fabs(visitors[key][1]-int(walltime)))
roomavgs = collections.OrderedDict(sorted(roomavgs.items()))
for room in roomavgs.keys():
  print "Room", room, ",", sum(roomavgs[room])/len(roomavgs[room]), "minute average visit,", len(roomavgs[room]), "visitor(s) total"