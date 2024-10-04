import sys
from PyQt6.QtWidgets import QApplication, QDateTimeEdit
from PyQt6 import uic
from PyQt6 import QtCore


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QDateTimeEdit日期时间控件.ui")

    myDateTimeEdit: QDateTimeEdit = ui.dateTimeEdit

    myDateTimeEdit.setDate(QtCore.QDate(2022, 5, 5))
    myDateTimeEdit.setTime(QtCore.QTime(12, 12, 12))

    print(myDateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss"))

    ui.show()
    sys.exit(app.exec())