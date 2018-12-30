from src.Pile import Pile

class Player:

	playPile = Pile()
	wonPile = Pile()


	def player(self):
		name = input("Name: ")


	def playCard(self):
		global playPile, wonPile
		if player.playPile.getSize() == 0:
			useWonPile()
		elif player.playPile.getSize() > 0:
			return playPile.nextCard()


	def collectCard():
		global playPile, wonPile
		wonPile.addCard()

	def collectCard():
		global playPile, wonPile
		wonPile.addCards()

	def useWonPile(self):
		global playPile, wonPile
		playPile.clear()
		playPile.addCards(wonPile)
		wonPile.clear()

	def numCards(self):
		global playPile, wonPile
		remainingCards = playPile.getSize() + wonPile.getSize()
		print(remainingCards)



