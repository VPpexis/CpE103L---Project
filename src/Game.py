from src.cardDeck import cardDeck
from src.Player import Player
from src.Pile import Pile
from src.Card import Card

class Game:

	def __init__(self):
		self.p1 = Player("Ernie")
		self.p2 = Player("Burt")
		return

	def enoughCards(self, n):
		if isinstance(n, int):
			if (self.p1.numCards() < n or self.p2.numCards() < n):
				return False
		return True

	def play(self):

		cd = cardDeck()
		cd.fill()
		#cd.displayDeck()
		print("\n\n\n")
		cd.shuffleDeck()
		#cd.displayDeck()
		print("\n\n\n")

		while(cd.getSize() >=2):
			#print(cd.getSize())
			self.p1.collectCard(cd.dealCard())
			self.p2.collectCard(cd.dealCard())

		print("\n\n\n")
		print(self.p1.numCards())
		#print(self.p2.numCards())
		#print("Player 1 Pile: ")
		#self.p1.displayPlayerCards()
		#print("\n\n\nPlayer 2 Pile: ")
		#self.p2.displayPlayerCards()
		self.p1.useWonPile()
		self.p2.useWonPile()

		down = Pile()	#Pile for cards in a war

		
		for t in range(1,100):
			if not self.enoughCards(1):
				break

			#Data type is Card() object.
			c1 = self.p1.playCard()
			c2 = self.p2.playCard()

			print("\nTurn " + str(t) + ": ")
			print(self.p1.getName() + ": " + str(c1.toString()) + " ")
			print(self.p2.getName() + ": " + str(c2.toString()) + " ")

			if (c1.compareTo(c2) > 0):
				self.p1.collectCard(c1)
				self.p1.collectCard(c2)
			elif (c1.compareTo(c2) < 0):
				self.p2.collectCard(c1)
				self.p2.collectCard(c2)
			else:
				down.clear()
				down.addCard(c1)
				down.addCard(c2)
				done = True
				while done:
					num = c1.getCardRank()
					if not(self.enoughCards(num)):
						break
					print("\nWar! Players put down " + str(num) + " card(s).")

					for m in range(1, num):
						c1 = self.p1.playCard()
						c2 = self.p2.playCard()
						down.addCard(c1)
						down.addCard(c2)

					print(self.p1.getName() + ": " + c1.toString() + " ")
					print(self.p2.getName() + ": " + c2.toString() + " ")

					done = False

					if (c1.compareTo(c2) > 0):
						print(c1.compareTo(c2))
						self.p1.collectCards(down)
						done = True
					elif (c1.compareTo(c2) < 0):
						print(c1.compareTo(c2))
						self.p2.collectCards(down)
						done = True
					else:
						done = False
			print(str(self.p1.numCards()) + " to " + str(self.p2.numCards()))
		return
		

	def getWinner():
		if(self.p1.numCards() > self.p2.numCards()):
			return p1
		elif(self.p2.numCards() > self.p1.numCards()):
			return self.p2
		else:
			return null
		return

	def check(self):
		print(1)
		return