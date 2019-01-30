from src.cardDeck import cardDeck
from src.Player import Player
from src.Pile import Pile
from src.Card import Card

class Game:

	def __init__(self):
		self.p1 = Player("P1")
		self.p2 = Player("P2")
		return

	def enoughCards(self, n):
		print("P1 Cards: " + str(self.p1.displayPlayerCards()))
		print("P2 Cards: " + str(self.p2.displayPlayerCards()))
		if isinstance(n, int):
			if (self.p1.numCards() < n or self.p2.numCards() < n):
				print("Return is False")
				return False
			print("Return is True")
			return True
		return True

	def play(self):

		cd = cardDeck()
		cd.fill()
		print(cd.getSize())
		#print("\n\n\n")
		cd.shuffleDeck()
		#cd.displayDeck()
		#print("\n\n\n")

		while(cd.getSize() >=2):
			#print(cd.getSize())
			self.p1.collectCard(cd.dealCard())
			self.p2.collectCard(cd.dealCard())

		#print("Player 1: " + str(self.p1.numCards()))
		#print("Player 2: " + str(self.p2.numCards()))
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
					if not(self.enoughCards(1)):
						done = False
						break

					num = c1.getCardRank()

					print("\nWar! Players put down " + str(num) + " card(s).")

					for m in range(0, num):
						if not self.enoughCards(1):
							break
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
						done = False
					elif (c1.compareTo(c2) < 0):
						print(c1.compareTo(c2))
						self.p2.collectCards(down)
						done = False
					elif (c1.compareTo(c2) == 0):
						done = True

					if not(self.enoughCards(1)):
						done = False
						break

			print(str(self.p1.numCards()) + " to " + str(self.p2.numCards()))
		return
		

	def getWinner(self):
		if(self.p1.numCards() > self.p2.numCards()):
			return "P1"
		elif(self.p2.numCards() > self.p1.numCards()):
			return "P2"
		else:
			return None
		return

	def check(self):
		print(1)
		return