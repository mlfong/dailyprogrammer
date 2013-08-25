from random import choice
st, ed = map(int, raw_input().split())
expressions = ["+", "-", "*", "/"]
numbers = [str(i) for i in xrange(min(st,ed), max(st,ed)+1)]
while True:
  ans, problem = "",""
  try:
    values = [choice(numbers)]
    for i in range(3):
      values.append(choice(expressions))
      values.append(choice(numbers))
    problem = " ".join(v for v in values)
    ans = eval(problem)
  except:
    pass  
  print problem
  get = raw_input()
  if get.lower() == 'q': break
  else:
    print "Correct!" if get == str(ans) else "Incorrect..."
