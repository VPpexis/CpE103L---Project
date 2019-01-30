# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Player(object):
    def setupUi(self, Player):
        Player.setObjectName("Player")
        Player.resize(636, 399)
        self.background = QtWidgets.QLabel(Player)
        self.background.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.background.setObjectName("background")
        self.versus = QtWidgets.QLabel(Player)
        self.versus.setGeometry(QtCore.QRect(200, 70, 201, 171))
        self.versus.setObjectName("versus")
        self.Player1box = QtWidgets.QTextEdit(Player)
        self.Player1box.setGeometry(QtCore.QRect(60, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Player1box.setFont(font)
        self.Player1box.setObjectName("Player1box")
        self.Player2box = QtWidgets.QTextEdit(Player)
        self.Player2box.setGeometry(QtCore.QRect(410, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Player2box.setFont(font)
        self.Player2box.setObjectName("Player2box")
        self.line = QtWidgets.QFrame(Player)
        self.line.setGeometry(QtCore.QRect(20, 190, 581, 31))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Player)
        self.line_2.setGeometry(QtCore.QRect(20, 100, 581, 31))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.enterNamesTxt = QtWidgets.QLabel(Player)
        self.enterNamesTxt.setGeometry(QtCore.QRect(210, 20, 251, 31))
        self.enterNamesTxt.setObjectName("enterNamesTxt")
        self.p1Label = QtWidgets.QLabel(Player)
        self.p1Label.setGeometry(QtCore.QRect(20, 130, 41, 51))
        self.p1Label.setObjectName("p1Label")
        self.p2Label = QtWidgets.QLabel(Player)
        self.p2Label.setGeometry(QtCore.QRect(580, 130, 41, 51))
        self.p2Label.setObjectName("p2Label")
        self.playerStart = QtWidgets.QPushButton(Player)
        self.playerStart.setGeometry(QtCore.QRect(230, 240, 171, 71))
        self.playerStart.setObjectName("playerStart")

        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        _translate = QtCore.QCoreApplication.translate
        Player.setWindowTitle(_translate("Player", "Please enter your names..."))
        self.background.setText(_translate("Player", "<html><head/><body><p><img src=\":/background/versus.jpg\"/></p></body></html>"))
        self.versus.setText(_translate("Player", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; font-style:italic; color:#000000;\">VS</span></p></body></html>"))
        self.enterNamesTxt.setText(_translate("Player", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Enter your names</span></p></body></html>"))
        self.p1Label.setText(_translate("Player", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">P1</span></p></body></html>"))
        self.p2Label.setText(_translate("Player", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">P2</span></p></body></html>"))
        self.playerStart.setText(_translate("Player", "START"))

import player_rc

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Player = QtWidgets.QWidget()
    ui = Ui_Player()
    ui.setupUi(Player)
    Player.show()
    sys.exit(app.exec_())

