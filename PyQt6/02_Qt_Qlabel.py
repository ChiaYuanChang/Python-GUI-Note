from PyQt6 import QtWidgets
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
Form.show()
sys.exit(app.exec())
