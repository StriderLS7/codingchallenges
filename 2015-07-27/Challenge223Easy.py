import datetime

def getGarlandLength(input):
	done = False
	count = 0
	for i in range(0,len(input)):
		#print("Checking: " + input[:i] + " == " + input[-i:])
		if input[:i]==input[-i:]:
			count=i
	return count

def runTests():
	inputs = ["programmer","ceramic","onion","alfalfa"]
	outputs = [0,1,2,4]
	for i in range(0,len(inputs)):
		garland = getGarlandLength(inputs[i])
		print ("TEST: " + inputs[i] + " = " + str(garland) + " : " + str(garland == outputs[i]))

def findLargestWord():
	print ("Starting dictionary search: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
	f = open("enable1.txt","r")
	maxCount = -1
	bestWord = ""
	for line in f:
		line = line.strip()
		garland = getGarlandLength(line)
		#print ("Checking word: " + line + " -> " + str(garland))
		if garland > maxCount:
			maxCount = garland
			bestWord = line
	print ("Finished: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
	print("Best word: " + bestWord + " -> " + str(maxCount))

runTests()
print ("\n\n")
findLargestWord()