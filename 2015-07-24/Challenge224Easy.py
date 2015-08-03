import random

def shuffle(input):
	for i in range(0,len(input)-2):
		j = random.randint(i,len(input)-1)
		input[i],input[j] = input[j],input[i]
	return input

def runTest():
	inputs = [[1,2,3,4,5,6,7,8,9,10],['a','b','c','d','e','f'],["ABC","DEF","GHI","JKL","MNO","PQR"],["apple", "blackberry", "cherry", "dragonfruit", "grapefruit", "kumquat", "mango", "nectarine", "persimmon", "raspberry", "raspberry"]]
	for input in inputs:
		print("INPUT:  " + ', '.join(map(str, input)))
		print("OUTPUT: " + ', '.join(map(str, shuffle(input))))

runTest()
