import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

import ui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setScaledContents(True)

        # when push ascii button

        # self.ui.pushButton.clicked.connect(switch_not_empty())
        self.ui.pushButton.clicked.connect(ui.output_final_text)
        self.ui.clear.clicked.connect(ui.clear_all)

""""def change_to_ascii(self):
        ascii_text = logic.ascii_trans(self.ui.ed_t.toPlainText())
        return ascii_text
    def change_ascii_to_binary(self):
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
