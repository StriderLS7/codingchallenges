def isPalindrome(input):
	input = str(input)
	mid = int(len(input)/2)
	#print ("Checking input [" + input + "]: mid=" + str(mid))
	if len(input) % 2 == 0:
		#print ("Case 1: " + str(input[:mid]) + " compared to " + str(input[len(input):mid-1:-1]))
		return input[:mid] == input[len(input):mid-1:-1]
	else:
		#print ("Case 2: " + str(input[:mid]) + " compared to " + str(input[len(input):(mid):-1]))
		return input[:mid] == input[len(input):(mid):-1]
	

def runPalidromicTests():
	inputs = [11,1101,11011,11111,111111,1221,12221,12312]
	for input in inputs:
		print(str(input) + ": " + str(isPalindrome(input)))

def makeStep(input):
	input = str(input)
	return int(input) + int(input[::-1])

def runTests():
	inputs = [11,68,123,286,196196871]
	outputs = [11,1111,444,8813200023188,4478555400006996000045558744]
	steps = [0,3,1,23,45]

	for i in range(0,len(inputs)):
		input = inputs[i]
		count = 0
		while not isPalindrome(input):
			count = count + 1
			input = makeStep(input)
		print ("Input [" + str(inputs[i]) + "] => " + str(count) + " steps = " + str(input))
		if input == outputs[i] and count == steps[i]:
			print ("PASS")
		else:
			print ("FAIL")

runTests()