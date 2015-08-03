
def sortWord(word):
	hasPeriod = (word.find(".") != -1) 
	hasComma = (word.find(",") != -1) 
	dashPos = word.find("-")
	aposPos = word.find("\'")

	#remove special characters
	word = word.replace(".","").replace(",","").replace("-","").replace("\'","")
	
	outword = ''.join(sorted(word))

	if dashPos != -1:
		outword = outword[:dashPos] + "-" + outword[dashPos:]
	if aposPos != -1:
		outword = outword[:aposPos] + "\'" + outword[aposPos:]
	if hasPeriod:
		outword = outword + "."
	if hasComma:
		outword = outword + ","

	return outword

def mangleSentence(input):
	words = input.split(" ")
	output = ""
	for word in words:
		isTitle = word.istitle()
		if isTitle:
			output += sortWord(word.lower()).title() + " "
		else:
			output += sortWord(word) + " "
	return output.rstrip()

def runTests():
	print("BASIC TESTS".center(25,'*'))
	inputs = ["This challenge doesn't seem so hard.","There are more things between heaven and earth, Horatio, than are dreamt of in your philosophy."]
	outputs = ["Hist aceeghlln denos't eems os adhr.","Eehrt aer emor ghinst beeentw aeehnv adn aehrt, Ahioort, ahnt aer ademrt fo in oruy hhilooppsy."]
	for x in range(0,len(inputs)):
		print(("TEST " + str(x)).center(20,'-'))
		print("Input: " + inputs[x])
		output = mangleSentence(inputs[x])
		print("Output: " + output)
		print("Expect: " + outputs[x])
		if (output == outputs[x]):
			print("PASS".center(20,'-'))
		else:
			print("FAIL".center(20,'-'))

def runChallenges():
	print("CHALLENGE TESTS".center(25,'*'))
	inputs = ["Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.","Adder's fork, and Blind-worm's sting, Lizard's leg, and Howlet's wing.","For a charm of powerful trouble, like a hell-broth boil and bubble."]
	for x in range(0,len(inputs)):
		print(("TEST " + str(x)).center(20,'-'))
		print("Input: " + inputs[x])
		output = mangleSentence(inputs[x])
		print("Output: " + output)

runTests()
runChallenges()
