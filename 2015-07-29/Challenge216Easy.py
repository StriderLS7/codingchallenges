from itertools import product
from random import shuffle

import collections

suits = ["Clubs","Diamonds","Hearts","Spades"]
values = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
cards = ["{0} of {1}".format(*card) for card in product(values,suits)]

#print (cards)

shuffle(cards)

#print (cards)
playerCount = 1

def deal(n):
	return list(map(lambda n: cards.pop(),range(0,n)))

def burn():
	deal(1)

while not str(playerCount).isnumeric() or (int(playerCount) < 2 or int(playerCount) > 8):
	playerCount = input("Enter # of players (2-8): ")

hands = collections.OrderedDict()
print ("")

hands["Player 1"] = "{0}".format(deal(2))
for player in range(1,int(playerCount)):
	hands ["CPU Player " + str(player)] =  "{0}".format(deal(2))

for player,hand in hands.items():
	print ("{0}: {1}".format(player,str(hand)))

print ("")
burn()
print ("Flop:  {0}".format(deal(3)))
burn()
print ("Turn:  {0}".format(deal(1)))
burn()
print ("River: {0}".format(deal(1)))
