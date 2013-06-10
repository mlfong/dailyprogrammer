
from random import shuffle, randint

abc = "abcdefghijklmnopqrstuvwxyz"
words = open("enable-6.txt").read().splitlines()

def validate(newabc):
	global abc, words
	cipher = dict(zip(abc, newabc))
	count = 0
	for word in words:
	  nword = "".join(map(cipher.get, word))
	  if sorted(nword) == list(nword):
	    count += 1
	return count

def swapN(guess, N):
	guess2 = guess[:]
	for x in xrange(0, 10):
		a, b = randint(0, N-1), randint(0, N-1)
		temp = guess2[a]
		guess2[a] = guess2[b]
		guess2[b] = temp
	return guess2


def main():
	guess = [letter for letter in open('best.txt').readline()]
	best, best_t = guess, validate(guess)
	print "start", "".join(best), best_t
	for x in xrange(0,100):
		newGuess = swapN(best, 26)
		temp, temp_t = newGuess, validate(newGuess)
		if temp_t > best_t:
			best = temp
			best_t = temp_t
	print "best",
	print "".join(best), best_t
	f = open("best.txt", 'w')
	f.write("".join(best))
	f.close()
	pass

if __name__ == '__main__':
	main()










