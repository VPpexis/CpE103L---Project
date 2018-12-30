from src.Card import Card
from array import *
import random

class cardDeck:
	
	#Instance of the carrDeck.
	def __init__(self):
            self.numCards = 0
            self.deck = [Card()]
            return
		
	#Fills the deck with 52 cards.
	def fill(self):
            index = 0
            for s in range(0,52):
                self.deck.append(Card())
            for r in range(1,14):
                for s in range(1,5):
                    self.deck[index].setCard(r,s)
                    index += 1
            self.numCards = 52
            return
	
	#Shows the Deck
	def displayDeck(self):
            for i in range(0, self.numCards):
                print(str(self.deck[i].toString()))
            return
			
	#Shuffled the cards in the deck
	def shuffleDeck(self):
	    random.shuffle(self.deck)
	    return
		
	#Deal the card to the pile
	def dealCard(self):
            if(self.numCards == 0):
                return 0
            else:
                return self.deck[self.numCards]
	
	#Test if cardDeck is working.
	def test(self):
            print("Test is successful...")
            return
   
