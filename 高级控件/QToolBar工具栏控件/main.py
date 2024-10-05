from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QToolBar
from PyQt6 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QToolBar工具栏控件.ui")

    myQToolBar:QToolBar = ui.toolBar
    myQToolBar.addAction(QIcon("add.svg"), "添加")

    myQToolBar.addSeparator()

    myQToolBar.addAction(QIcon("save.svg"), "保存")

    ui.show()
    sys.exit(app.exec())