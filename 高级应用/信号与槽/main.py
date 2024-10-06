import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton
from PyQt6 import uic

def cal(a: int, b: int, lineEdit_3:QLineEdit):
    lineEdit_3.setText(str(a+b))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./加法器.ui")

    lineEdit: QLineEdit = ui.lineEdit
    lineEdit_2: QLineEdit = ui.lineEdit_2
    lineEdit_3: QLineEdit = ui.lineEdit_3
    pushButton: QPushButton = ui.pushButton

    pushButton.clicked.connect(lambda: cal(int(lineEdit.text()), int(lineEdit_2.text()), lineEdit_3))

    lineEdit_3.setReadOnly(True)
    lineEdit_3.setHidden(True)


    ui.show()
    sys.exit(app.exec())