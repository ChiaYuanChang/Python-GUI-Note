from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle("About QPushButton")
form_width = 800
form_height = 600
Form.resize(form_width, form_height)
Form.show()
sys.exit(app.exec())

