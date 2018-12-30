from src.Card import Card

class Pile:
        
        #Instance of the pile.
        def __init__(self):
            self.pile = [Card()]
            self.front = 0
            self.end = 0
            return
        
        #Clears data stored in object.
        def clear(self):
            self.front=0
            self.end=0
            #print("Pile is cleared...")
            return

        #Gets the sized of the Pile.
        def getSize(self):
            return (self.end - self.front)

        #The data type of c should be a Class Object
        def addCard(self, c):
            self.pile.append(c)
            self.end += 1
            return

        #The data type of p should be a Pile Object.
        def addCards(self, p):
            while p.getSize() > 0:
                addCard(p.nextCard())
            return

        #Goes to the next card in the pile.
        def nextCard(self):
            if front==end:
                return "No cards Left boi."
            else:
                self.pile[self.front]=card
                front += 1
                return c
            return
        
        #Returns the card stored in the object.
        def showCards(self):
            i = 0
            for x in range(1, self.end):
                print(str(self.pile[i].toString()))
                i += 1
            return
        
        def test(self):
            print("Test is successful...")
            return
        
        

        
