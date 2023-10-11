import sys
from PyQt6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Qlabel class version")
        self.resize(800, 800)

    def ui(self):
        # 在form裡面加入label
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("first Qlabel class version")
        self.label1.move(50, 50)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("label2")
        self.label2.setGeometry(50, 80, 100, 100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())