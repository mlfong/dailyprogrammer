
        
    

def main():
    N = int(raw_input("Enter N rows/cols: "))
    m = []
    for i in xrange(0, N):
        a = raw_input("Enter row: " + str(i) + ": ")
        b = a.split()
        c = (b[1] if b[1] < b[2] else b[2], b[0])
        m.append( c )
    print ''
    m.sort()
    for i in m:
        print i[1],
    print
        
        
        

if __name__=="__main__":
    main()