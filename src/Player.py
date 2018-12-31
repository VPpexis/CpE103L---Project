from src.Pile import Pile

class Player:

	#Instance of the object.
	def __init__(self, n):
		self.name = n
		self.playPile = Pile()
		self.wonPile = Pile()
		return

	#
	def playCard(self):
		if self.playPile.getSize() == 0:
			useWonPile()
		elif self.playPile.getSize() > 0:
			return playPile.nextCard()
		return

	#Returns the name of the player.
	def getName(self):
		return self.name

	#collects the card from the other player.
	def collectCard(self, c):
		wonPile.addCard(c)
		return

	#collect the cards from the other player.
	def collectCards(self, p):
		self.wonPile.addCards(p)
		return

	#Resets the pile back to 0.
	def useWonPile(self):
		self.playPile.clear()	#Resets front and end to 0
		self.playPile.addCards(wonPile)
		self.wonPile.clear()	#Resets front and end to 0
		return

	#Returns a value of the size of the playPile and wonPile.
	def numCards(self):
		return (self.playPile.getSize() + self.wonPile.getSize())

	#Used for debugging.
	def test(self):
		print("Test is sucessful...")
		return