from src.cardDeck import cardDeck
from src.Card import Card
from src.Pile import Pile

cd = cardDeck()
s = Card()
pl1 = Pile()
pl2 = Pile()

#Error: 'Card' object has no attribute 'r'

cd.fill()
print("Deck before deal")
cd.displayDeck()
print("\n\n\n\n")
print("Player 1 Pile")
pl1.addCard(cd.dealCard())
pl1.addCard(cd.dealCard())
pl1.addCard(cd.dealCard())

pl1.showCards()
    


