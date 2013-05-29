def mccarthy91(N):
	if not N: return
	if N == 91:
		print "91"
	elif N > 100:
		print "M("+str(N-10)+") since " + str(N) + " > 100"
		mccarthy91(N-10)
	elif N <= 100:
		print "M(M("+str(N+11)+")) since " + str(N) + " <= 100"
		mccarthy91(mccarthy91(N+11))
	return


def main():
	import sys
	if len(sys.argv) != 2:
		print "Usage: python Easy.py N"
		return
	N = int(sys.argv[1])
	mccarthy91(N)

if __name__ == "__main__":
	main()
