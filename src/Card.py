class Card:
	
	def _init__(self):
		return
	
	def setCard(self, r, s):
		self.r = r
		self.s = s
	
	def getCardRank(self):
		return self.r
	
	def getCardSuit(self):
		return self.s

	def toString(self):
		val = ""
		suitlist = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
		
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
	
	