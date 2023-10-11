import sys
from PyQt6 import QtWidgets, QtGui, QtCore


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.setWindowTitle("About Qlabel class version")
        self.resize(800, 800)
        self.ui()

    def ui(self):
        # 在form裡面加入label
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("first Qlabel class version")
        self.label1.move(50, 50)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("label2")
        self.label2.setGeometry(50, 80, 100, 100)

        # 設定邊界
        self.label3.setContentsMargins(0, 0, 0, 0)
        # 設定可以換行
        self.label3.setWordWrap(True)
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label4 = QtWidgets.QLabel(self)
        # 字體設定
        ## 宣告字體物件
        font1 = QtGui.QFont()
        ## 設定字體
        font1.setFamily("System")
        ## 設定字體大小
        font1.setPointSize(20)
        ## 粗體
        font1.setBold(True)
        ## 斜體
        font1.setItalic(True)
        ## 刪除線
        font1.setStrikeOut(True)
        ## 底線
        font1.setUnderline(True)
        # 設定字體樣式
        self.label4.setFont(font1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())