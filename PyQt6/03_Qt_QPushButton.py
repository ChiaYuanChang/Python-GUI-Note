import sys
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle("About QPushButton")
form_width = 800
form_height = 600
Form.resize(form_width, form_height)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText("first button")

btn2 = QtWidgets.QPushButton(Form)
btn2.setText("button.move(50, 50)")
btn2.move(50, 50)

btn3 = QtWidgets.QPushButton(Form)
btn3.setText("button.setGeometry()")
btn3.setGeometry(50, 150, 50, 50)


Form.show()
sys.exit(app.exec())

