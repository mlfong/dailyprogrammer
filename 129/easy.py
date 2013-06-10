def longest2charss(s, longest=""):
    print '\tlongest unique 2 char substrings:', list(set([s[i:1+j] if len(set(s[i:1+j])) < 3 and len(s[i:1+j]) >= len(longest) else longest for i in xrange(0, len(s)) for j in xrange(i, len(s))]))
    return longest
    
if __name__=="__main__":
    while longest2charss(raw_input('enter lowercase string: ')): pass