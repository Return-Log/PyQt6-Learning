from PyQt6.QtWidgets import QApplication, QLineEdit, QInputDialog
from PyQt6 import uic
import sys

def get_name(formLayout, input_name):
    name,result = QInputDialog.getText(formLayout, "输入对话框", "请输入你的名字:", QLineEdit.EchoMode.Normal, "名字")
    if result:
        input_name.setText(name)
        print(name)
    else:
        print("取消输入")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("QInputDialog输入对话框控件.ui")

    formLayout = ui.formLayoutWidget
    input_name: QLineEdit = ui.lineEdit
    input_name.returnPressed.connect(lambda: get_name(formLayout, input_name))

    ui.show()
    sys.exit(app.exec())