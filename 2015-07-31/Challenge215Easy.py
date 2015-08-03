def calcNextCycleNum(input,power):
	return sum(pow(int(x),int(power)) for x in str(input))

def runTests():
	numTests = 4
	for x in range(0,numTests):
		f = open("input"+str(x))
		base = f.readline().rstrip()
		n = f.readline().rstrip()
		expectedOutput = [int(n) for n in f.readline().rstrip().split(', ')]
		output = []
		done = False;
		num = n
		while not done:
			num = calcNextCycleNum(num,base)
			#print ("Num: " + str(num))
			if num not in output:
				output.append(num)
			else:
				output=output[output.index(num):]
				done=True	
			#print ("Output: ".format(str(output)))
		print (" -- TEST {0} --".format(x))
		print (" BASE: {0}      INPUT: {1}".format(base,n))
		print (" OUTPUT    : {0}".format(str(output)))
		print (" EXP OUTPUT: {0}".format(str(expectedOutput)))
		if output == expectedOutput:
			print (" -- PASS --")
		else:
			print (" -- FAIL --")

runTests()
		