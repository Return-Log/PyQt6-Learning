import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox
from PyQt6 import uic

def show_info():
    QMessageBox.information(None, '标题', '内容', QMessageBox.StandardButton.Ok)

def show_critical():
    QMessageBox.critical(None, '标题', '内容', QMessageBox.StandardButton.Ok)

def show_question():
    QMessageBox.question(None, '标题', '内容', QMessageBox.StandardButton.Ok)

def show_about():
    QMessageBox.about(None, '标题', '内容')

def show_warning():
    result = QMessageBox.warning(None, '标题', '内容', QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)
    if result == QMessageBox.StandardButton.Ok:
        print('点击了确定')
    elif result == QMessageBox.StandardButton.No:
        print('点击了取消')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('QMessageBox对话框控件.ui')

    info_btn: QPushButton = ui.pushButton_5
    info_btn.clicked.connect(show_info)

    critical_btn: QPushButton = ui.pushButton_4
    critical_btn.clicked.connect(show_critical)

    question_btn: QPushButton = ui.pushButton_3
    question_btn.clicked.connect(show_question)

    about_btn: QPushButton = ui.pushButton_2
    about_btn.clicked.connect(show_about)

    warning_btn: QPushButton = ui.pushButton
    warning_btn.clicked.connect(show_warning)

    ui.show()
    sys.exit(app.exec())