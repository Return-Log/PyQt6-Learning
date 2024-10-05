from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem
from PyQt6 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('QTreeWidget树控件.ui')

    myQTreeWidget: QTreeWidget = ui.treeWidget

    myQTreeWidget.setHeaderLabels(['分类', '名称', '作者', '价格'])

    # 添加一级节点
    type1 = QTreeWidgetItem(myQTreeWidget, ['Java'])
    type2 = QTreeWidgetItem(myQTreeWidget, ['Python'])
    type3 = QTreeWidgetItem(myQTreeWidget, ['PHP'])

    # 添加二级节点
    item1 = QTreeWidgetItem(type1, ['', 'Java基础', 'xx', '99'])
    item2 = QTreeWidgetItem(type1, ['', 'Java进阶', 'xx', '299'])
    item1.setIcon(2, QIcon('save.svg'))  # 设置图标
    item1.setCheckState(1, Qt.CheckState.Unchecked)  # 设置复选框状态

    myQTreeWidget.setAlternatingRowColors(True)  # 设置斑马纹

    myQTreeWidget.expandAll()

    ui.show()
    sys.exit(app.exec())
