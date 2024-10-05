from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QTreeView
from PyQt6 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('./QTreeView树视图.ui')

    myQTreeView: QTreeView = ui.treeView

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['分类', '名称', '作者', '价格'])

    """添加一级节点"""
    type1 = QStandardItem('Java')
    type2 = QStandardItem('Python')
    type3 = QStandardItem('C++')

    """添加二级节点"""
    type1.appendRow([QStandardItem(''), QStandardItem('Java入门到精通'), QStandardItem('xxx'), QStandardItem('180')])

    """添加到根节点"""
    model.appendRow(type1)
    model.appendRow(type2)
    model.appendRow(type3)

    myQTreeView.setModel(model)

    myQTreeView.expandAll()

    ui.show()
    sys.exit(app.exec())