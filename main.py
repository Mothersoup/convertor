import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import logic

import ui



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setScaledContents(True)
        for boo in self.ui.input_list:
            if boo !="":


        # when push ascii button
      #  self.ui.pushButton.clicked.connect(switch_not_empty())
    """ self.ui.pushButton_to_ascii.clicked.connect(self.change_to_ascii)
        self.ui.pushButton_to_base64.clicked.connect(self.change_to_ascii)"""

""""def change_to_ascii(self):
        ascii_text = logic.ascii_trans(self.ui.ed_t.toPlainText())
        return ascii_text
    def change_to_binary(self):
        binary_text = logic.binary_trans(self.ui.ed_t.toPlainText())"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
