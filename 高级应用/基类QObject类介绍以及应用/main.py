from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6 import uic
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 加载qss样式
    with open('label.qss', 'r') as f:
        app.setStyleSheet(f.read())

    ui = uic.loadUi('基类QObject类介绍以及应用.ui')

    label_1: QLabel = ui.label
    label_2: QLabel = ui.label_2
    label_1.setProperty("level", "1")
    label_2.setProperty("level", "2")

    ui.show()
    sys.exit(app.exec())
