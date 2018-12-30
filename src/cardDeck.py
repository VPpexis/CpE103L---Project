from src.Card import Card
from array import *
import random

class cardDeck:

    deck = [Card()]
	
	#Instance of the carrDeck.
    def __init__(self):
            self.numCards = 0
            return
		
	#Fills the deck with 52 cards.
    def fill(self):
            index = 0
            for s in range(0,52):
                cardDeck.deck.append(Card())
            for r in range(1,14):
                for s in range(1,5):
                    cardDeck.deck[index].setCard(r,s)
                    index += 1
            self.numCards = 52
            return
	
	#Shows the Deck
    def displayDeck(self):
            for i in range(0, self.numCards):
                print(str(cardDeck.deck[i].toString()))
            return
			
	#Shuffled the cards in the deck
    def shuffleDeck(self):
	    random.shuffle(cardDeck.deck)
	    return
		
	#Deal the card to the pile
    def dealCard(self):
            if(self.numCards == 0):
                return 0
            else:
                return cardDeck.deck[self.numCards]
	
	#Used for debugging. Test if cardDeck is working.
    def test(self):
            print("Test is successful...")
            return
   
   #Used for debugging. Count how many cards in the deck.
    def countDeck(self):
            print(len(cardDeck.deck))
