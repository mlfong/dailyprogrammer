N, M = map(int, raw_input().split())
contestants = raw_input().split()
voters = [[map(int, raw_input().split()), 0] for i in xrange(N)]
current = 0
losers = set()
while True:
  has_tie = False
  counts = [[0, contestants[i]] for i in xrange(M)]
  for voter in voters:
    i = voter[1] # store which vote voter should use
    for i in xrange(len(voter)):
      if voter[0][i] not in losers:
        break
    curr_vote = voter[0][i]
    counts[curr_vote][0] += 1
  ranked_contestants = []
  for i in xrange(0, M):
    val = counts[i]
    percent = 100*(val[0])/float(len(voters))
    person = val[1]
    ranked_contestants.append((percent,person, i))
  ranked_contestants.sort(reverse=True)
  # print "ranked", ranked_contestants
  highest = ranked_contestants[0][0]
  lowest = set()
  i = 1
  lowest.add(ranked_contestants[-1][0])
  while ranked_contestants[-i][0] == 0:
    lowest.add(ranked_contestants[-i][0])
    i += 1

  print "lowest", lowest
  count_highest = 0
  for x in ranked_contestants:
    if x[0] == highest:
      count_highest += 1
    if x[0] in lowest:
      losers.add(x[2])
  print "losers", losers
  for i in xrange(N):
    voter = voters[i]
    votes = voter[0]
    while votes[voter[1]] in losers: 
      # print votes[voter[1]]
      voter[1] += 1
  
  print "Round %d:" % (current+1), ", ".join([ str(round(x[0],1))+"% " + x[1] for x in ranked_contestants if x[0] > 0])
  if count_highest == 100/highest: # ex. if 2 ppl have 50%, we have draw
    print "Draw Detected"
    break
  elif ranked_contestants[0][0] > 50.0:
    print ranked_contestants[0][1], "is the winner"
    break
  current += 1
  # break







