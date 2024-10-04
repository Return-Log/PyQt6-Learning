from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6 import uic
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QTabWidget选项卡控件.ui")

    myQTabWidget: QTabWidget = ui.tabWidget

    tab = QWidget()
    myQTabWidget.addTab(tab, "添加标签")

    print(myQTabWidget.tabText(2))

    ui.show()
    sys.exit(app.exec())