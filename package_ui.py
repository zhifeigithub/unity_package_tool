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
        MainWindow.resize(450, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.test_play_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_play_button.setGeometry(QtCore.QRect(30, 20, 171, 71))
        self.test_play_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.test_play_button.setObjectName("test_play_button")
        self.package_play_button = QtWidgets.QPushButton(self.centralwidget)
        self.package_play_button.setGeometry(QtCore.QRect(30, 110, 171, 71))
        self.package_play_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.package_play_button.setObjectName("package_play_button")
        self.package_button = QtWidgets.QPushButton(self.centralwidget)
        self.package_button.setGeometry(QtCore.QRect(230, 110, 171, 71))
        self.package_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.package_button.setObjectName("package_button")
        self.instruction_button = QtWidgets.QPushButton(self.centralwidget)
        self.instruction_button.setGeometry(QtCore.QRect(30, 200, 171, 71))
        self.instruction_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.instruction_button.setObjectName("instruction_button")
        self.update_package_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_package_button.setGeometry(QtCore.QRect(30, 290, 250, 71))
        self.update_package_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.update_package_button.setObjectName("update_package_button")
        self.update_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_test_button.setGeometry(QtCore.QRect(30, 400, 250, 71))
        self.update_test_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.update_test_button.setObjectName("update_test_button")
        self.edit_config_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_config_button.setGeometry(QtCore.QRect(30, 490, 250, 71))
        self.edit_config_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.edit_config_button.setObjectName("edit_config_button")
        self.test_vs_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_vs_button.setGeometry(QtCore.QRect(30, 590, 250, 71))
        self.test_vs_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.test_vs_button.setObjectName("test_vs_button")
        self.package_vs_button = QtWidgets.QPushButton(self.centralwidget)
        self.package_vs_button.setGeometry(QtCore.QRect(30, 690, 250, 71))
        self.package_vs_button.setStyleSheet("font: 75 20pt \"Consolas\";")
        self.package_vs_button.setObjectName("package_vs_button")
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
        self.test_play_button.setText(_translate("MainWindow", "测试运行"))
        self.package_play_button.setText(_translate("MainWindow", "打包运行"))
        self.package_button.setText(_translate("MainWindow", "打新包"))
        self.instruction_button.setText(_translate("MainWindow", "更新日志"))
        self.update_package_button.setText(_translate("MainWindow", "更新打包文件夹"))
        self.update_test_button.setText(_translate("MainWindow", "更新测试文件夹"))
        self.edit_config_button.setText(_translate("MainWindow", "编辑配置文件"))
        self.test_vs_button.setText(_translate("MainWindow", "打开测试VS工程"))
        self.package_vs_button.setText(_translate("MainWindow", "打开打包VS工程"))

    def set_test_play_button_click(self, call_func):
        self.test_play_button.clicked.connect(call_func)

    def set_package_play_button_click(self, call_func):
        self.package_play_button.clicked.connect(call_func)

    def set_package_button_click(self, call_func):
        self.package_button.clicked.connect(call_func)

    def set_instruction_button_click(self, call_func):
        self.instruction_button.clicked.connect(call_func)

    def set_update_package_button_click(self, call_func):
        self.update_package_button.clicked.connect(call_func)

    def set_update_test_button_click(self, call_func):
        self.update_test_button.clicked.connect(call_func)

    def set_edit_config_button_click(self, call_func):
        self.edit_config_button.clicked.connect(call_func)

    def set_test_vs_button_click(self, call_func):
        self.test_vs_button.clicked.connect(call_func)

    def set_package_vs_button_click(self, call_func):
        self.package_vs_button.clicked.connect(call_func)

