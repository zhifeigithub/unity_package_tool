# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SzoFiel\Desktop\打包自动化\PyCharmPrj\PyQt\package_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.test_play_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_play_button.setGeometry(QtCore.QRect(30, 20, 171, 71))
        self.test_play_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.test_play_button.setObjectName("test_play_button")
        self.package_button = QtWidgets.QPushButton(self.centralwidget)
        self.package_button.setGeometry(QtCore.QRect(240, 20, 171, 71))
        self.package_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.package_button.setObjectName("package_button")
        self.instruction_button = QtWidgets.QPushButton(self.centralwidget)
        self.instruction_button.setGeometry(QtCore.QRect(450, 20, 171, 71))
        self.instruction_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.instruction_button.setObjectName("instruction_button")
        self.update_package_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_package_button.setGeometry(QtCore.QRect(660, 20, 171, 71))
        self.update_package_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.update_package_button.setObjectName("update_package_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 23))
        self.menubar.setObjectName("menubar")
        self.menuD = QtWidgets.QMenu(self.menubar)
        self.menuD.setTitle("")
        self.menuD.setObjectName("menuD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unity_Package_Tool"))
        self.test_play_button.setText(_translate("MainWindow", "Test"))
        self.package_button.setText(_translate("MainWindow", "Package"))
        self.instruction_button.setText(_translate("MainWindow", "UpdateLog"))
        self.update_package_button.setText(_translate("MainWindow", "UpdatePackageProj"))

    def set_test_play_button_click(self, call_func):
        self.test_play_button.clicked.connect(call_func)

    def set_package_button_click(self, call_func):
        self.package_button.clicked.connect(call_func)

    def set_instruction_button_click(self, call_func):
        self.instruction_button.clicked.connect(call_func)

    def set_update_package_button_click(self, call_func):
        self.update_package_button.clicked.connect(call_func)