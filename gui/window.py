import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize, Qt

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "Game of War"
		self.left = 10
		self.top = 10
		self.width = 1280
		self.height = 960

		self.initUI()

		return

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.setAutoFillBackground(True)

		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.red)
		self.setPalette(p)

		button = QPushButton('Deal',self)
		button.setToolTip('Deal')
		button.resize(200, 64)
		button.move(600, 800)
		button.clicked.connect(self.on_click)

		label1 = QLabel(self)
		label2 = QLabel(self)
		label3 = QLabel(self)
		label4 = QLabel(self)
		label5 = QLabel(self)
		label6 = QLabel(self)
		pixmap = QPixmap("image.png")
		pixmap1 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap2 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap3 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap4 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap5 = pixmap.scaled(100,300, Qt.KeepAspectRatio)
		pixmap6 = pixmap.scaled(100,300, Qt.KeepAspectRatio)

		label1.move(650, 600)
		label1.setPixmap(pixmap1)
		label2.move(650, 10)
		label2.setPixmap(pixmap2)
		label3.move(650, 300)
		label3.setPixmap(pixmap3)
		label4.move(500, 300)
		label4.setPixmap(pixmap4)
		label5.move(500, 600)
		label5.setPixmap(pixmap5)
		label6.move(500, 10)
		label6.setPixmap(pixmap6)


		self.show()
		return

	@pyqtSlot()
	def on_click(self):
		print("Button clicked")
		return



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())