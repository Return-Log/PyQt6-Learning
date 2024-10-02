from PyQt6.QtGui import QValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QLineEdit
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QlineEdit单行文本框.ui")

    myLineEdit: QLineEdit = ui.lineEdit
    print(myLineEdit.text())  # 获取标签的文本

    print(QValidator.__subclasses__())
    myLineEdit.setValidator(QIntValidator())  # 限制输入类型为整数


    myLineEdit_2: QLineEdit = ui.lineEdit_2
    myLineEdit_2.setFocus()  # 获取焦点

    ui.show()
    sys.exit(app.exec())