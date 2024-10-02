import sys
from PyQt6 import uic
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QTextEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QTextEdit多行富文本框控件.ui")

    myTextEdit: QTextEdit = ui.textEdit
    myTextEdit.setTextColor(QtGui.QColor(255, 0, 0))  # 文本颜色
    myTextEdit.setTextBackgroundColor(QtGui.QColor(255, 250, 0))  # 背景颜色
    myTextEdit.setPlainText("Hello World, 这是纯文本")
    print(myTextEdit.toPlainText())

    myTextEdit_2: QTextEdit = ui.textEdit_2
    myTextEdit_2.setHtml("<font color='green'>学开源</font>，上<a href='http://www.github.com'>github</a>")
    print(myTextEdit_2.toHtml())

    ui.show()
    sys.exit(app.exec())