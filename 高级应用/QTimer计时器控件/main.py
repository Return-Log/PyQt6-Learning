import sys

from PyQt6.QtCore import QTimer, QDateTime
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6 import uic

def start(timer, label):
    timer.start(1000)
    timer.timeout.connect(lambda : show(label))

def show(label: QLabel):
    time = QDateTime.currentDateTime()
    timeout = time.toString('yyyy-MM-dd hh:mm:ss')
    label.setText(timeout)

def stop(timer):
    timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("./QTimer计时器控件.ui")

    timer = QTimer(ui)

    pushButton: QPushButton = ui.pushButton
    pushButton_2: QPushButton = ui.pushButton_2
    label: QLabel = ui.label

    pushButton.clicked.connect(lambda: start(timer, label))
    pushButton_2.clicked.connect(lambda: stop(timer))

    ui.show()
    sys.exit(app.exec())