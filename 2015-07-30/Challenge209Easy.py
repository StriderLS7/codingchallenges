
def calculateFlair(input):
	flair = {}
	currentTime = 0
	for player,time in input:
		flair[player] = int((60+currentTime)-time)
		currentTime = time
	#	print ("Calculated flair for player {0} = {1}".format(player,flair[player]))
	return flair


def runTests():

	inputFiles = ["input1","input2"]

	for inputFile in inputFiles:
		print("Input: " + inputFile)
		input = open(inputFile,"r")
		players = {}
		playerCnt = int(input.readline())
		print ("Players: " + str(playerCnt))
		for i in range(0,playerCnt):
			line = input.readline().strip()
			players[line[:line.find(':')]] = float(line[line.find(':')+1:].strip())
		players = sorted(players.items(),key=lambda player: player[1])
		flair = calculateFlair(players)
		for player,time in players:
			print("{0}: clicked at {1} => flair = {2}".format(player,time,flair[player]))
		print("")

runTests()