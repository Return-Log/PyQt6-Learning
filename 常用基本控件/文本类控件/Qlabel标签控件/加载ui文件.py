from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./Qlabel标签控件.ui")

    myLabel: QLabel = ui.label  # 使用 “: QLabel =” 可以获取用法提示
    print(myLabel.text())  # 获取标签的文本

    ui.show()
    sys.exit(app.exec())