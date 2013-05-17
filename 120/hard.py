def machine1(n):
	return [n/2, n/3, n/4]
    
def machine2(n, p):
    assert p > 0
    return n+1
    
def findJumps():
    lim = 577 # 577 b/c naive sol finds 576
    coc = 0 # currOneCoin
    jump = []
    for i in xrange(1, 577):
        next = getNumOneCoins(i)
        if coc + 2 <= next:
            jump.append(i-1)
        coc = next
    return jump

def getNumOneCoins(n2):
    n2list = machine1(n2)
    oneCount = 0
    while n2list:
        n2listnew = []
        for v in n2list:
            if v == 1:
                oneCount += 1
                continue
            for t in machine1(v):
                if t != 0:
                    n2listnew.append(t)
        n2list = n2listnew
    return oneCount

def optimalSplit(n, n2, jump, oneCountOrig):
    n2list = machine1(n2)
    oneCount = oneCountOrig
    while n2list:
        print n2list
        n2listnew = []
        for v in n2list:
            # if v == 11: print v, oneCount
            if v == 1:
                oneCount += 1
                continue
            if v in jump and oneCount:
                v, oneCount = v + 1, oneCount - 1
            for t in machine1(v):
                if t != 0:
                    n2listnew.insert(0,t)
                    # n2listnew.append(t)
        n2list = n2listnew
    return oneCount - oneCountOrig
    
def BytelandianExchange3(n, l, jump):
    n1, n2, n3 = machine1(n)
    # n1c = getNumOneCoins(n1)
    # n2c = getNumOneCoins(n2)
    # n3c = getNumOneCoins(n3)
    n1c = optimalSplit(n, n1, jump, 0)
    n2c = optimalSplit(n, n2, jump, 0)
    n3c = optimalSplit(n, n3, jump, 0)
    # print n2c , n3c
    # print 'sum', n1+n2c+n3c
    if n+1 <= n1 + n2c + n3c or \
        n+1 <= n1c + n2 + n3c or \
        n+1 <= n1c + n2c + n3:
        print n
        return True
    

        
    
jump = findJumps()
# for i in xrange(1, 577):
    # if BytelandianExchange3(i, [], jump):
        # break
        
print getNumOneCoins(33)
print machine1(33)
print optimalSplit(0, 33, jump, 0)