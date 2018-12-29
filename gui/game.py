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
        MainWindow.resize(1090, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1091, 631))
        self.background.setObjectName("background")
        self.P1ScoreNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.P1ScoreNum.setGeometry(QtCore.QRect(50, 50, 71, 31))
        self.P1ScoreNum.setObjectName("P1ScoreNum")
        self.P2ScoreNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.P2ScoreNum.setGeometry(QtCore.QRect(970, 50, 71, 31))
        self.P2ScoreNum.setObjectName("P2ScoreNum")
        self.referee = QtWidgets.QTextBrowser(self.centralwidget)
        self.referee.setGeometry(QtCore.QRect(480, 290, 141, 71))
        self.referee.setObjectName("referee")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
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

