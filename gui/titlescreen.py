# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titlescreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import player as player

class Ui_TitleScreen(object):
    def setupUi(self, TitleScreen):
        TitleScreen.setObjectName("TitleScreen")
        TitleScreen.resize(602, 421)
        self.background = QtWidgets.QLabel(TitleScreen)
        self.background.setGeometry(QtCore.QRect(0, -20, 861, 461))
        self.background.setObjectName("background")
        self.handcards = QtWidgets.QLabel(TitleScreen)
        self.handcards.setGeometry(QtCore.QRect(210, 160, 471, 581))
        self.handcards.setObjectName("handcards")
        self.StartButton = QtWidgets.QPushButton(TitleScreen)
        self.StartButton.setGeometry(QtCore.QRect(320, 130, 111, 41))
        self.StartButton.setIconSize(QtCore.QSize(16, 16))
        self.StartButton.setObjectName("StartButton")
        self.StartButton.clicked.connect(self.on_click())
        self.QuitButton = QtWidgets.QPushButton(TitleScreen)
        self.QuitButton.setGeometry(QtCore.QRect(440, 130, 111, 41))
        self.QuitButton.setObjectName("QuitButton")

        self.retranslateUi(TitleScreen)
        QtCore.QMetaObject.connectSlotsByName(TitleScreen)

    def retranslateUi(self, TitleScreen):
        _translate = QtCore.QCoreApplication.translate
        TitleScreen.setWindowTitle(_translate("TitleScreen", "Game of War"))
        self.background.setText(_translate("TitleScreen", "<html><head/><body><p><img src=\":/background1/Game_of_War_Fire_Age.jpg\"/></p></body></html>"))
        self.handcards.setText(_translate("TitleScreen", "<html><head/><body><p><img src=\":/cards/handcards.png\"/></p></body></html>"))
        self.StartButton.setText(_translate("TitleScreen", "Start Game"))
        self.QuitButton.setText(_translate("TitleScreen", "Quit Game"))

    def on_click(self):
        player.main()
        print(1)
        return

import titlebackground_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TitleScreen = QtWidgets.QDialog()
    ui = Ui_TitleScreen()
    ui.setupUi(TitleScreen)
    TitleScreen.show()
    sys.exit(app.exec_())

