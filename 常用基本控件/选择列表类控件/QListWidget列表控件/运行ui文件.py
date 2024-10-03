import sys
from PyQt6.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PyQt6 import uic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QListWidget列表控件.ui")

    myListWidget: QListWidget = ui.listWidget

    item = QListWidgetItem()
    item.setText("这是文本")
    item.setToolTip("这是提示信息")

    myListWidget.addItem(item)

    ui.show()
    sys.exit(app.exec())