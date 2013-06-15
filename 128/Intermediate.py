def printMatrix(m):
    for i in m:
        for j in i:
            print j,
        print
def pave_over(m, paveme):
    p, which, i = paveme
    if which == 'r':
        for x in xrange(0,len(m)):
            m[i][x] = 1
    else:
        for x in xrange(0,len(m)):
            m[x][i] = 1
def countNZRow(m, i):
    return sum(1 if m[i][j] <= 0 else 0 for j in xrange(0, len(m)))
def countNZCol(m, j):
    return sum(1 if m[i][j] <= 0 else 0 for i in xrange(0, len(m)))
def finished(m):
    for i in m:
        for j in i:
            if j <= 0: return False
    return True


def pavement(m):
    from heapq import *
    num_paved = 0
    paved_rows, paved_cols = set(), set()
    paved_roads = {"r" : paved_rows, "c" : paved_cols}
    N = len(m)
    while num_paved < N :
        h = [] # (priority, row|col, index)
        unpaved_r, unpaved_c = 0, 0
        unpaved = N - num_paved
        # check rows
        if finished(m): break
        allrows_paved = True
        for i in xrange(0, N):
            temp = countNZRow(m, i)
            allrows_paved = allrows_paved and temp == 0
            if countNZRow(m, i) == unpaved:
                paved_rows.update([i])
                for x in xrange(0,N):
                    m[i][x] = 1
                num_paved += 1
                break
            elif temp > 0:
                heappush(h, (countNZRow(m, i), "r", i))
                unpaved_r += 1
            j = i
            temp = countNZCol(m, j)
            if countNZCol(m, j) == unpaved:
                paved_cols.update([j])
                for x in xrange(0,N):
                    m[x][j] = 1
                num_paved += 1
                break
            elif temp > 0:
                heappush(h, (countNZCol(m, i), "c", j))
                unpaved_c += 1
        if allrows_paved:
            break
        if unpaved != N - num_paved: # force to pave
            continue
        print h
        if unpaved_r > unpaved_c:
            h = [x for x in h if x[1] == 'r']
        else:
            h = [x for x in h if x[1] == 'c']
        h.sort()
        # print "unpaved_r", unpaved_r
        # print "unpaved_c", unpaved_c
        paveme = h.pop()
        paved_roads[paveme[1]].update([paveme[2]])
        pave_over(m, paveme)
        num_paved += 1
    print 'paved rows', paved_rows
    print 'paved cols', paved_cols
    print 'num paved', num_paved
    printMatrix(m)
    return
        # no for sures
        
    

def main():
    N = int(raw_input("Enter N rows/cols: "))
    m = []
    for i in xrange(0, N):
        a = raw_input("Enter row: " + str(i) + ": ")
        m.append( map(int, a.split()) )
    print ''
    pavement(m)
        
        
        

if __name__=="__main__":
    main()