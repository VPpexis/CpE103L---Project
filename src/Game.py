from src.cardDeck import cardDeck
from src.Player import Player
from src.Pile import Pile
from src.Card import Card

class Game:

	def play(self):

		cd = CardDeck()
		cd.fill()
		cd.shuffle()
		p1 = Player("Ernie")	#Data type is Player() object.
		p2 = Player("Burt")		#Data type is Player() object.

		while(cd.getSize() >=2):
			p1.collectCard(cd.deal())
			p2.collectCard(cd.deal())

		p1.useWonPile()
		p2.useWonPile()

		down = Pile()	#Pile for cards in a war

		for t in range(1,100):

			if !enoughCards(1):
				break

			#Data type is Card() object.
			c1 = p1.playCard()
			c2 = p2.playCard()

			print("\nTurn " + t + ": ")
			print(p1.getName() + ": " + c1 + " ")
			print(p2.getName() + ": " + c2 + " ")

			if (c1.)