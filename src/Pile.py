from src.Card import Card

class Pile:
        pile=[Card()]
        front=1
        end=4
        card=Card()
        

        def clear(self):
                global front,end
                front=0
                end=0
                print("front",front,"end",end)

        def getSize(self):
                global front,end
                pileSize=end-front
                return pileSize

        def addCard(self):
                global end,pile,card
                pile[end]=card
                end+=1

        def addCards(self):
                while self.getSize()>0:
                        addCard(self.nextCard())

        def nextCard(self):
                global front,pile,card
                if front==end:
                        return "No cards Left boi."
                else:
                        pile[front]=card
                        front+=1
                        return c
        
        

        
