import sys
import package_ui
import my_exception
from PyQt5 import QtCore, QtGui, QtWidgets

class my_start:
    def test_play(self):
        import test_play

    def package(self):
        import package

    def update_instruction(self):
        import instruction_file_updater


#f_handler = open('out.log', 'w+')
#sys.stdout = f_handler
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = package_ui.Ui_MainWindow()
ui.setupUi(MainWindow)

begin = my_start()
ui.set_test_play_button_click(begin.test_play)
ui.set_package_button_click(begin.package)
ui.set_instruction_button_click(begin.update_instruction)

icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("icon.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
MainWindow.setWindowIcon(icon)
MainWindow.setFixedSize(MainWindow.width(),MainWindow.height())

MainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print("完成！")

