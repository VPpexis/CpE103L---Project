from src.Card import Card
from array import *
import random

class cardDeck:
	numCards = 0
	deck = [Card()]
	def __init__(self):
		i = 0
		
	def fill(self):
		index = 0
		
		for s in range(1,52):
			cardDeck.deck.append(Card())
		
		for r in range(1,14):
			for s in range(1,5):
				cardDeck.deck[index].setCard(r,s)
				index += 1
				
			cardDeck.numCards = 52;
			
	def displayDeck(self):
		for i in range(0, cardDeck.numCards):
			print(str(cardDeck.deck[i].toString()))
			
		
	def shuffleDeck(self):
		random.shuffle(cardDeck.deck)
		
	def dealCard():
		if(cardDeck.numCards == 0):
			return 0
		else:
			return deck[cardDeck.numCards]
   
