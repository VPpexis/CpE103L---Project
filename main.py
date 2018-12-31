from src.cardDeck import cardDeck
from src.Card import Card
from src.Pile import Pile
from src.cardSlot import cardSlot
from src.Player import Player

cd = cardDeck()
s = Card()
pl1 = Pile()
pl2 = Pile()
player1 = Player("Van")
player2 = Player("Ria")

'''
----------------------------------------------------------------
As of 31/12/18	by: Panugan.
----------------------------------------------------------------
pileDeck.dealCard() Error: 'Card' object has no attribute 'r'
Player class is created but not tested.
Card.py is not finish. Problems encountered in understanding
	java code lines.
Game.py is created but some codes are not finished due to the
	unability of converting java to python code in some parts.
Added test() module to test class if it would initially work.

p.s. Label accoridngly with comments to avoid confussions and
	do not remove anything important in the main class.
p.s.s PLS post updateds or changes that you have done here by
	copying the format here and do it below Update Post.
'''
#################################################################

'''
cd.fill()
print("Deck before deal")
cd.displayDeck()
#cd.countDeck()
print("\n\n\n\n")
print("Player 1 Pile")

#################################################################

pl1.addCard(cd.dealCard())
#pl1.showCards() 
'''
#################################################################

cd.fill()
cardSlot(cd.dealCard())

#################################################################

#player1.test()
#player2.test()
#print(player1.getName())
#print(player2.getName())