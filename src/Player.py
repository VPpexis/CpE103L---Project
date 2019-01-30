from src.Pile import Pile
from src.Card import Card

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
			self.useWonPile()
			return self.playPile.nextCard()
		elif self.playPile.getSize() > 0:
			return self.playPile.nextCard()
		else:
			print("No card is returned")
		return

	#Returns the name of the player.
	def getName(self):
		return self.name

	#collects the card from the other player.
	def collectCard(self, c):
		if isinstance(c, Card):
			self.wonPile.addCard(c)
		else:
			print("Error")
		return

	#collect the cards from the other player.
	def collectCards(self, p):
		if isinstance(p, Pile):
			self.wonPile.addCards(p)
		else:
			print("Error")
		return

	#Resets the pile back to 0.
	def useWonPile(self):
		self.playPile.clear()	#Resets front and end to 0
		self.playPile.addCards(self.wonPile)
		self.wonPile.clear()	#Resets front and end to 0
		return

	#Returns a value of the size of the playPile and wonPile.
	def numCards(self):
		return (self.playPile.getSize() + self.wonPile.getSize())

	#Used for debugging.
	def test(self):
		print("Test is sucessful...")
		return

	#Used for debugging.
	def displayPlayerCards(self):
		return self.wonPile.getSize(), self.playPile.getSize()