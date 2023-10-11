import sys
from PyQt6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("first Qlabel class version")
        self.resize(800, 800)
        self.setStyleSheet("background:fcc;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
