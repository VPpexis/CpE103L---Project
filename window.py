import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import pyqtSlot, QSize, Qt, QCoreApplication
from src.cardDeck import cardDeck
from src.Player import Player
from src.Pile import Pile
from src.Card import Card
import time

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "Game of War"
		self.left = 10
		self.top = 10
		self.width = 1280
		self.height = 960
		self.t = 1
		self.p1RCard = 0
		self.p1SCard = 0
		self.p2RCard = 0
		self.p2SCard = 0
		self.forTextStat = ""
		
		self.label3 = QLabel(self)
		self.label4 = QLabel(self)

		self.textLabel1 = QLabel(self)
		self.textLabel2 = QLabel(self)
		self.textLabel3 = QLabel(self)
		self.textLabel4 = QLabel(self)
		self.textLabel5 = QLabel(self)
		self.textLabel6 = QLabel(self)
		self.textStatus = QLabel(self)

		self.p1 = Player("P1")
		self.p2 = Player("P2")

		self.cd = cardDeck()
		self.cd.fill()
		self.cd.shuffleDeck()

		while(self.cd.getSize() >=2):
			self.p1.collectCard(self.cd.dealCard())
			self.p2.collectCard(self.cd.dealCard())

		self.p1.useWonPile()
		self.p2.useWonPile()
		self.down = Pile()

		self.initUI()
		return

	def enoughCards(self, n):
		print("P1 Cards: " + str(self.p1.displayPlayerCards()))
		print("P2 Cards: " + str(self.p2.displayPlayerCards()))
		if isinstance(n, int):
			if (self.p1.numCards() < n or self.p2.numCards() < n):
				print("Return is False")
				self.w = MyPopup()
				self.w.setGeometry(100, 100, 400, 200)
				self.w.show()
				return False
			print("Return is True")
		return True

	def updateImage(self):
		img1 = QPixmap("resources/cards/png/"+ str(self.p1SCard) + "_" + str(self.p1RCard) + ".jpg")
		img2 = QPixmap("resources/cards/png/"+ str(self.p2SCard) + "_" + str(self.p2RCard) + ".jpg")
		pixmap1 = img1.scaled(100,300, Qt.KeepAspectRatio)
		pixmap2 = img2.scaled(100,300, Qt.KeepAspectRatio)

		self.label3.move(650, 300)
		self.label3.setPixmap(pixmap1)
		self.label4.move(500, 300)
		self.label4.setPixmap(pixmap2)

		p1WonPile, p1PlayPile = self.p1.displayPlayerCards()
		p2WonPile, p2PlayPile = self.p2.displayPlayerCards()

		self.textLabel1.setText("Pl_1 Playpile: " + str(p1PlayPile))
		self.textLabel2.setText("Pl_1 WonPile: " + str(p1WonPile))
		self.textLabel3.setText("Pl_2 PlayPile: " + str(p2PlayPile))
		self.textLabel4.setText("Pl_2 WonPile: " + str(p2WonPile))
		#self.textStatus.setText(self.forTextStat)

		self.label3.show
		self.label4.show
		self.textStatus.show
		return

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.setAutoFillBackground(True)

		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.darkGreen)
		self.setPalette(p)

		button = QPushButton('Deal',self)
		button.setToolTip('Deal')
		button.resize(200, 64)
		button.move(600, 800)
		button.clicked.connect(self.dealGame)

		label1 = QLabel(self)
		label2 = QLabel(self)
		label5 = QLabel(self)
		label6 = QLabel(self)
		pixmap = QPixmap("image.png")
		pixmap1 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap2 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap3 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap4 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap5 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap6 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		self.textLabel1.setText("000000000000000000")
		self.textLabel2.setText("000000000000000000")
		self.textLabel3.setText("000000000000000000")
		self.textLabel4.setText("000000000000000000")
		self.textStatus.setText("00000000000000000000000000000000000000000000000000000000000")
		self.textLabel5.setText("Player 1 Down Pile")
		self.textLabel6.setText("Player 2 Down Pile")

		label1.move(650, 600)
		self.textLabel1.move(650, 580)
		label1.setPixmap(pixmap1)
		label2.move(650, 10)
		self.textLabel3.move(650, 170)
		label2.setPixmap(pixmap2)
		self.label3.move(650, 300)
		self.label3.setPixmap(pixmap3)
		self.textLabel5.move(640, 460)
		self.label4.move(500, 300)
		self.label4.setPixmap(pixmap4)
		self.textStatus.move(500, 270)
		self.textLabel6.move(490, 460)
		label5.move(500, 600)
		self.textLabel2.move(500, 580)
		label5.setPixmap(pixmap5)
		label6.move(500, 10)
		self.textLabel4.move(500, 170)
		label6.setPixmap(pixmap6)

		self.w = MyPopup("Player1")
		self.w.setGeometry(100, 100, 400, 200)
		self.w.show()

		self.show()
		return

	@pyqtSlot()
	def dealGame(self):
		if not self.enoughCards(1):
			return

		#Data type is Card() object.
		c1 = self.p1.playCard()
		c2 = self.p2.playCard()
		
		self.p1RCard = c1.getCardRank()
		self.p1SCard = c1.getCardSuit()
		self.p2RCard = c2.getCardRank()
		self.p2SCard = c2.getCardSuit()
		self.updateImage()

		print("P1Card: " + str(c1.getCardRank()) + str(c1.getCardSuit()))
		print("P2Card: " + str(c2.getCardRank())+ str(c2.getCardSuit()))

		print("\nTurn " + str(self.t) + ": ")
		self.textStatus.setText("Turn " + str(self.t) + ": ")
		self.textStatus.show

		self.t = self.t + 1

		print(self.p1.getName() + ": " + str(c1.toString()) + " ")
		print(self.p2.getName() + ": " + str(c2.toString()) + " ")

		if (c1.compareTo(c2) > 0):
			self.p1.collectCard(c1)
			self.p1.collectCard(c2)
		elif (c1.compareTo(c2) < 0):
			self.p2.collectCard(c1)
			self.p2.collectCard(c2)
		else:
			self.down.clear()
			self.down.addCard(c1)
			self.down.addCard(c2)
			done = True
			num = c1.getCardRank()
			self.textStatus.setText("War! " + str(num) + " card(s) were taken. The last card are shown.")
			self.textStatus.show
			
			while done:
				if not(self.enoughCards(1)):
					done = False
					break

				print("\nWar! Players put down " + str(num) + " card(s).")
				
				for m in range(0, num):
					if not self.enoughCards(1):
						break
					c1 = self.p1.playCard()
					c2 = self.p2.playCard()
					self.down.addCard(c1)
					self.down.addCard(c2)

				self.p1RCard = c1.getCardRank()
				self.p1SCard = c1.getCardSuit()
				self.p2RCard = c2.getCardRank()
				self.p2SCard = c2.getCardSuit()
				self.updateImage()

				print(self.p1.getName() + ": " + c1.toString() + " ")
				print(self.p2.getName() + ": " + c2.toString() + " ")

				done = False

				if (c1.compareTo(c2) > 0):
					print(c1.compareTo(c2))
					self.p1.collectCards(self.down)
					done = False
				elif (c1.compareTo(c2) < 0):
					print(c1.compareTo(c2))
					self.p2.collectCards(self.down)
					done = False
				elif (c1.compareTo(c2) == 0):
					done = True

				if not(self.enoughCards(1)):
					done = False
					break

			print(str(self.p1.numCards()) + " to " + str(self.p2.numCards()))
		return

class MyPopup(QWidget):
    def __init__(self, winner):
    	QWidget.__init__(self)
    	self.winner = winner
    	self.UI()
    	return

    def UI(self):
    	_translate = QCoreApplication.translate
    	self.setWindowTitle("Game Over!!!!")
    	label1 =  QLabel(self)
    	#label1.setText("Winner is " + str(self.winner))
    	#label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    	label1.setText(_translate("Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">Gameover</span></body></html>"))
    	#label1.setAlignment(Qt.Qt.AlignCenter)
    	label1.show
    	return


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())