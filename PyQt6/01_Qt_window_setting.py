import sys
from PyQt6 import QtWidgets


app = QtWidgets.QApplication(sys.argv)
# 建立視窗元件
Form = QtWidgets.QWidget()
# 設定視窗標題
Form.setWindowTitle("this is title")
# 設定視窗尺寸
form_width = 800
form_height = 600
Form.resize(form_width, form_height)
# 使用css樣式設定背景
Form.setStyleSheet("background:#fcc;")
# 顯示視窗
Form.show()
sys.exit(app.exec())
