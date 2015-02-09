__author__ = 'ilendemli'

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QTableWidgetItem)


class CTableWidgetItem(QTableWidgetItem):
    marked = False

    def __init__(self, row, column):
        QTableWidgetItem.__init__(self)

        self.row = row
        self.column = column

    def toggle(self):
        if self.marked:
            self.marked = False
        else:
            self.marked = True

        self.refresh()

    def refresh(self):
        if self.marked:
            self.setBackground(QColor(100, 100, 150))
        else:
            self.setBackground(QColor(255, 255, 255))

    def setmarked(self, marked):
        self.marked = marked
        self.refresh()