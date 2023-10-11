from PyQt6 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle("About Qlabel")
form_width = 800
form_height = 600
Form.resize(form_width, form_height)
# 宣告Qlabel物件
label1 = QtWidgets.QLabel(Form)
# 設定標籤text
label1.setText("first Qlabel")

label2 = QtWidgets.QLabel(Form)
label2.setText("first Qlabel move(50, 50)")
# [Qlabel物件].move([x座標]: num, [y座標]: num)
label2.move(50, 50)

label3 = QtWidgets.QLabel(Form)
label3.setText("first Qlabel setGeometry()")
# [Qlabel物件].setGeometry([x座標]: num, [y座標]: num, [物件x大小限制]: num, [物件y大小限制]: num)
label3.setGeometry(50, 80, 100, 100)

label4 = QtWidgets.QLabel(Form)
label4.setText("label4 is toooooooooooooooooooooooooooooooooooooooooooo long")
# 設定是否可以換行
label4.setWordWrap(True)
# 設定對齊方式
label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

label5 = QtWidgets.QLabel(Form)
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
label5.setFont(font1)

Form.show()
sys.exit(app.exec())
