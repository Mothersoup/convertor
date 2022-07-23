from PyQt5 import QtCore, QtWidgets

import logic


def create_widget(widget, name, x, y, width, height):
    if name is not None:
        widget.setText(name)
    widget.setGeometry(QtCore.QRect(x, y, width, height))
    widget.setObjectName(name)
    return widget


class Ui_MainWindow(object):
    def __init__(self):
        self.pushButton = None
        self.octal = None
        self.octal_text = None
        self.base64 = None
        self.base64_text = None
        self.ascii = None
        self.ascii_text = None
        self.statusbar = None
        self.menubar = None
        self.output = None
        self.binary_text = None
        self.decimal_text = None
        self.ed_t = None
        self.pushButton = None
        self.centralwidget = None
        self.label = None
        self.haspmap = {}

    def create_button(self, name, x, y, width=200, height=200):
        return create_widget(QtWidgets.QPushButton(self.centralwidget), name, x, y, width, height)

    def create_text_input(self, name, convert, x, y, width, height):
        text_input_temp = create_widget(QtWidgets.QTextEdit(self.centralwidget), name, x, y, width, height)
        self.haspmap[text_input_temp] = convert
        return text_input_temp

    def create_label(self, name, x, y, width, height):
        return create_widget(QtWidgets.QLabel(self.centralwidget), name, x, y, width, height)

    def setupUi(self, main_window):
        main_window.setObjectName("Convertor")
        main_window.resize(840, 573)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setWindowTitle("Convertor")
        self.label = self.create_label(None, 0, 0, 421, 391)

        x = 520
        y = 50
        width = 172
        height = 80
        self.pushButton = self.create_button("convertor", x, y, width, height)

        x = 180
        y = 130
        width = 252
        height = 42
        y1 = 130 - 42
        # text decimal
        self.decimal_text = self.create_label("decimal", x, y1, width, height)
        self.ed_t = self.create_text_input(None, logic.trans_from_ascii, x, y, width, height)
        # binary
        self.binary_text = self.create_label("binary", x, y1 + 2 * height, width, height)
        self.output = self.create_text_input(None, logic.trans_from_binary, x, y + 2 * height, width, height)
        self.ascii_text = self.create_label("ascii", x, y1 + 4 * height, width, height)
        self.ascii = self.create_text_input(None, logic.trans_from_ascii, x, y + 4 * height, width, height)
        self.octal = self.create_text_input(None, logic.trans_from_octal, x, y + 6 * height, width, height)
        self.octal_text = self.create_label("octal", x, y1 + 6 * height, width, height)
        self.base64 = self.create_text_input(None, logic.trans_from_base64, x, y + 8 * height, width, height)
        self.base64_text = self.create_label("base64", x, y1 + 8 * height, width, height)

        main_window.setCentralWidget(self.centralwidget)

        self.menubar = create_widget(QtWidgets.QMenuBar(main_window), None, 0, 0, 840, 25)
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        main_window.setWindowTitle("Convertor")
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # deal with output section

    def set_final_text(self, text, trans_to_various, textinput):
        textinput.setText(trans_to_various(text))

    def output_final_text(self):
        print(self)
        print(self.haspmap)
        '''for di in self.haspmap:
            if di != "":
                all_text = self.haspmap[di](di)
                self.set_final_text(self.ascii.toPlainText, logic.ascii_trans, all_text)
                self.set_final_text(self.ed_t.toPlainText, logic.hex_trans, all_text)
                self.set_final_text(self.octal.toPlainText, logic.octal_trans, all_text)
                self.set_final_text(self.base64.toPlainText, logic.base64_trans, all_text)
                self.set_final_text(self.output.toPlainText, logic.binary_trans, all_text)
'''
# 1 QWidget()function creates the top level window   "relate with window "
# 2 QLabel( need input QWidget son class) could set a text in it   "relate with banner"
# 3 setGeometry()Define the size and position of window also could name a top banner beside cancel
# 4 sys.exit(app.exec_())  app.exec_() could let main window keep appearing like a loop
