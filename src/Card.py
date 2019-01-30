class Card:
	
	#Instance of the object.
	def __init__(self):
		self.r = 0
		self.s = 0
		return
	
	#Set the values of the card.
	def setCard(self, r, s):
		self.r = r
		self.s = s
	
	#Returns to card rank.
	def getCardRank(self):
		return self.r
	
	#Returns to card suit.
	def getCardSuit(self):
		return self.s

	#Converts r & s to String value.
	def toString(self):
		val = ""
		suitlist = ["Error", "Clubs", "Diamonds", "Hearts", "Spades"]
		
		if(self.r == 1):
			val = "Ace"
		elif(self.r == 11):
			val = "Jack"
		elif(self.r == 12):
			val = "Queen"
		elif(self.r == 13):
			val = "King"
		else:
			val = str(self.r)
			
		return val + " of " + suitlist[self.s]

	#Compares the other card with the current card.
	def compareTo(self, ob):
		thisRank = self.getCardRank()
		otherRank = ob.getCardRank()

		if thisRank == 1:
			thisRank = 14
		if otherRank == 1:
			otherRank =14

		return (thisRank - otherRank)

	#Checks if cards are equal.
	def equals(self, ob):
		if isinstance(ob, Card()):
			return #value==other.value && suit==other.suit;
		else:

			return False
