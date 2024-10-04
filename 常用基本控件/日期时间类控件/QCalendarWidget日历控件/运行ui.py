import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QCalendarWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QCalendarWidget日历控件.ui")

    myCalendarWidget:QCalendarWidget = ui.calendarWidget
    print(myCalendarWidget.selectedDate().toString("yyyy-MM-dd"))

    ui.show()
    sys.exit(app.exec())