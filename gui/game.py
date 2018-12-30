# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 1091, 631))
        self.background.setObjectName("background")
        self.P1ScoreNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.P1ScoreNum.setGeometry(QtCore.QRect(50, 50, 71, 31))
        self.P1ScoreNum.setObjectName("P1ScoreNum")
        self.P2ScoreNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.P2ScoreNum.setGeometry(QtCore.QRect(970, 50, 71, 31))
        self.P2ScoreNum.setObjectName("P2ScoreNum")
        self.referee = QtWidgets.QTextBrowser(self.centralwidget)
        self.referee.setGeometry(QtCore.QRect(480, 290, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.referee.setFont(font)
        self.referee.setObjectName("referee")
        self.P1NameBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.P1NameBox.setGeometry(QtCore.QRect(250, 70, 211, 31))
        self.P1NameBox.setObjectName("P1NameBox")
        self.P2NameBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.P2NameBox.setGeometry(QtCore.QRect(630, 70, 211, 31))
        self.P2NameBox.setObjectName("P2NameBox")
        self.P1MidCard = QtWidgets.QLabel(self.centralwidget)
        self.P1MidCard.setGeometry(QtCore.QRect(270, 180, 211, 281))
        self.P1MidCard.setObjectName("P1MidCard")
        self.P2MidCard = QtWidgets.QLabel(self.centralwidget)
        self.P2MidCard.setGeometry(QtCore.QRect(620, 180, 211, 281))
        self.P2MidCard.setObjectName("P2MidCard")
        self.P1TopCard = QtWidgets.QLabel(self.centralwidget)
        self.P1TopCard.setGeometry(QtCore.QRect(0, 350, 211, 271))
        self.P1TopCard.setObjectName("P1TopCard")
        self.P2TopCard = QtWidgets.QLabel(self.centralwidget)
        self.P2TopCard.setGeometry(QtCore.QRect(890, 350, 211, 271))
        self.P2TopCard.setObjectName("P2TopCard")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 21))
        self.menubar.setObjectName("menubar")
        self.mainMenu = QtWidgets.QMenu(self.menubar)
        self.mainMenu.setObjectName("mainMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewGame = QtWidgets.QAction(MainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
        self.actionQuitGame = QtWidgets.QAction(MainWindow)
        self.actionQuitGame.setObjectName("actionQuitGame")
        self.mainMenu.addAction(self.actionNewGame)
        self.mainMenu.addSeparator()
        self.mainMenu.addAction(self.actionQuitGame)
        self.menubar.addAction(self.mainMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game Of War"))
        self.background.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/table/tabletopgame.jpg\"/></p></body></html>"))
        self.P1MidCard.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/table/midcard.png\"/></p></body></html>"))
        self.P2MidCard.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/table/midcard.png\"/></p></body></html>"))
        self.P1TopCard.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/table/cardback.png\"/></p></body></html>"))
        self.P2TopCard.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/table/cardback.png\"/></p></body></html>"))
        self.mainMenu.setTitle(_translate("MainWindow", "Main Menu"))
        self.actionNewGame.setText(_translate("MainWindow", "New Game"))
        self.actionQuitGame.setText(_translate("MainWindow", "Quit Game"))

import game_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

