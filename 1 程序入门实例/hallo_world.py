from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建一个应用
# print(sys.argv)
# print(app.arguments())  # 获取参数

"""窗体的创建"""
window = QWidget()
window.setWindowTitle("窗体标题1")  # 设置标题
window.resize(100, 200)  # 窗口宽高设置
window.move(100, 200)  # 窗口位置设置
window.show()

"""标签的创建"""
label = QLabel()
label.setText("你好，python老爷")  # 设置标签内容
label.move(20, 30)  # 设置标签位置
label.resize(30, 10)  # 设置标签大小
label.setStyleSheet("background-color:blue;padding:10px")
label.setParent(window)  # 设置标签的父控件为窗体
label.show()

sys.exit(app.exec())  # 开始执行程序，并且进入消息循环等待
