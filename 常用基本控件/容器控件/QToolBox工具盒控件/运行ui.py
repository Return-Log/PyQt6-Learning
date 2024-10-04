import sys
from PyQt6.QtWidgets import QApplication, QToolBox, QWidget
from PyQt6 import uic
from Tools.scripts.stable_abi import itemclass

if __name__=='__main__':
    app=QApplication(sys.argv)
    ui = uic.loadUi('./QToolBox工具盒控件.ui')

    myToolBox: QToolBox = ui.toolBox

    item = QWidget()
    myToolBox.addItem(item, "item1")
    print(myToolBox.currentIndex())

    ui.show()
    sys.exit(app.exec())