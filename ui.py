from PyQt5 import QtCore, QtWidgets

import logic


def create_widget(widget, name, x, y, width, height):
    if name is not None:
        widget.setText(name)
    widget.setGeometry(QtCore.QRect(x, y, width, height))
    widget.setObjectName(name)
    return widget


toText = {}
fromText = {}


def output_final_text():
    for di in toText:
        text = di.toPlainText()
        if len(text) > 0:
            try:
                text = toText[di](text)
            except:
                break
            for field in fromText:
                if field != di:
                    try:
                        set_final_text(field, fromText[field](text))
                    except:
                        set_final_text(field, "error")
            break


def clear_all():
    for di in toText:
        for field in fromText:
            set_final_text(field, "")


asc2 = None
ed_t = None
octal = None
Base64 = None
output = None
text = None
Hex = None


def set_final_text(text_field, out_text):
    text_field.setText(str(out_text))


class Ui_MainWindow(object):
    def __init__(self):
        self.pushButton = None
        self.clear = None
        self.original_text = None
        self.hex_text = None
        self.octal_text = None
        self.Base64_text = None
        self.ascii_text = None
        self.statusbar = None
        self.menubar = None
        self.binary_text = None
        self.decimal_text = None
        self.pushButton = None
        self.centralwidget = None
        self.label = None

    def create_button(self, name, x, y, width=200, height=200):
        return create_widget(QtWidgets.QPushButton(self.centralwidget), name, x, y, width, height)

    def create_text_input(self, name, from_text, to_text, x, y, width, height):
        if from_text is None:
            from_text = logic.identity
        if to_text is None:
            to_text = logic.identity
        text_input_temp = create_widget(QtWidgets.QTextEdit(self.centralwidget), name, x, y, width, height)
        toText[text_input_temp] = to_text
        fromText[text_input_temp] = from_text
        return text_input_temp

    def create_label(self, name, x, y, width, height):
        return create_widget(QtWidgets.QLabel(self.centralwidget), name, x, y, width, height)

    def setupUi(self, main_window):
        global asc2, ed_t, octal, Base64, output, text, Base64, Hex
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
        self.clear = self.create_button("clear", x, 3 * y, width, height)

        x = 180
        y = 60
        width = 252
        height = 42
        y1 = y - 42
        # text decimal
        self.decimal_text = self.create_label("decimal", x, y1, width, height)
        ed_t = self.create_text_input(None, logic.ascii_to_decimal, logic.decimal_to_ascii, x, y, width, height)
        # binary
        self.binary_text = self.create_label("binary", x, y1 + 2 * height, width, height)
        output = self.create_text_input(None, logic.ascii_to_binary, logic.binary_to_ascii, x, y + 2 * height, width,
                                        height)

        self.ascii_text = self.create_label("ascii", x, y1 + 4 * height, width, height)
        asc2 = self.create_text_input(None, None, None , x, y + 4 * height, width, height)
        octal = self.create_text_input(None, logic.ascii_to_octal, logic.octal_to_ascii, x, y + 6 * height, width, height)

        self.octal_text = self.create_label("octal", x, y1 + 6 * height, width, height)
        Base64 = self.create_text_input(None,  logic.ascii_to_base64, logic.ascii_from_base64, x, y + 8 * height, width, height)

        self.base64_text = self.create_label("base64", x, y1 + 8 * height, width, height)

        self.original_text = self.create_label("text", x, y1 + 10 * height, width, height)
        text = self.create_text_input(None,  logic.all_ascii,  logic.to_ascii, x, y + 10 * height, width, height)

        self.hex_text = self.create_label("hex", 2.75 * x, y1 + 10 * height, width, height)
        Hex = self.create_text_input(None, logic.ascii_to_hex,  logic.hex_to_ascii, 2.75 * x, y + 10 * height, width, height)

        main_window.setCentralWidget(self.centralwidget)

        self.menubar = create_widget(QtWidgets.QMenuBar(main_window), None, 0, 0, 840, 25)
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        main_window.setWindowTitle("Convertor")
        QtCore.QMetaObject.connectSlotsByName(main_window)
        # deal with output section

# 1 QWidget()function creates the top level window   "relate with window "
# 2 QLabel( need input QWidget son class) could set a text in it   "relate with banner"
# 3 setGeometry()Define the size and position of window also could name a top banner beside cancel
# 4 sys.exit(app.exec_())  app.exec_() could let main window keep appearing like a loop
