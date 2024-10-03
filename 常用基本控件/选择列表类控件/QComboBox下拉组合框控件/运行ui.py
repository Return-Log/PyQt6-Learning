from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QComboBox
from PyQt6 import uic
import sys

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QComboBox下拉组合框控件.ui")

    myComboBox: QComboBox = ui.comboBox
    myComboBox.addItem("1")
    list = ["2", "3", "4"]
    myComboBox.addItems(list)
    myComboBox.addItem(QIcon("./agplv3-with-text-162x68.png"), "agplv3")
    print(myComboBox.currentText(), myComboBox.currentIndex())
    print(myComboBox.itemText(4), myComboBox.itemIcon(3))

    ui.show()
    sys.exit(app.exec())