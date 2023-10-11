import sys
from PyQt6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.btn1 = None
        self.setWindowTitle("About QPushButton class version")
        self.resize(800, 600)
        self.ui()

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("first button")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
