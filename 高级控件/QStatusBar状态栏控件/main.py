from PyQt6.QtWidgets import QApplication, QStatusBar, QLabel
from PyQt6 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QStatusBar状态栏控件.ui")

    myQStatusBar:QStatusBar = ui.statusBar

    # myLabel = QLabel()
    # myLabel.setText("版权所有")
    #
    # myQStatusBar.addWidget(myLabel)

    myLabel_1 = QLabel()
    myLabel_1.setText("联系方式")

    myQStatusBar.addPermanentWidget(myLabel_1)

    myQStatusBar.showMessage("欢迎使用", 3000)


    ui.show()
    sys.exit(app.exec())