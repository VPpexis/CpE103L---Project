from src.Card import Card

class Pile:
        
        #Instance of the pile.
        def __init__(self):
            self.pile = []
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
            val = self.end - self.front
            return val

        #The data type of c should be a Class Object
        def addCard(self, c):
            self.pile.append(c)
            self.end += 1
            return

        #The data type of p should be a Pile Object.
        def addCards(self, p):
            while p.getSize() > 0:
                self.addCard(p.nextCard())
            return

        #Goes to the next card in the pile.
        def nextCard(self):
            if self.front==self.end:
                return "No cards Left boi."
            else:
                c = self.pile[self.front]
                self.front += 1
                return c
            return
        
        #Returns the card stored in the object.
        def showCards(self):
            i = 1
            for x in range(0, self.end):
                print(str(self.pile[i].toString()))
                i += 1
            return
        
        def test(self):
            print("Test is successful...")
            return
        
        

        
