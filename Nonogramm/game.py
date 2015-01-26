__author__ = 'ilendemli'

import sys
import random

import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem)

ui_class, base_class = uic.loadUiType("Nonogram.ui")


class LG():
    @staticmethod
    def calculate_list(tl):
        tlist = []

        for i in range(len(tl)):
            tcount = 0
            trow = tl[i]
            tocc = []

            for j in range(len(trow)):
                if trow[j] == 1:
                    tcount += 1

                elif trow[j] == 0 and tcount != 0:
                    tocc.append(tcount)
                    tcount = 0

            if tcount != 0:
                tocc.append(tcount)

            tlist.append(tocc)

        return tlist

    @staticmethod
    def rotate_list(tl):
        tlist = []

        for i in range(len(tl)):
            trow = []

            for j in range(len(tl[i])):
                trow.append(tl[j][i])

            tlist.append(trow)

        return tlist


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


class Nonogramm(QMainWindow):
    game = None
    clicked = None
    valid_fields = None

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = ui_class()
        self.ui.setupUi(self)

        self.ui.table_game.clicked.connect(self.handlespot)
        self.ui.button_newgame.clicked.connect(self.handlenewgame)
        self.ui.button_solution.clicked.connect(self.handlesolution)
        self.ui.combo_stage.activated.connect(self.handlestage)

    def handlespot(self):
        table = self.ui.table_game

        row = table.currentRow()
        column = table.currentColumn()

        titem = table.item(row, column)
        titem.toggle()

        if self.clicked[row][column] == 1:
            self.clicked[row][column] = 0
        else:
            self.clicked[row][column] = 1

        error = 0
        offset = 0
        for row in range(0, 15):
            for column in range(0, 15):
                if self.clicked[row][column] == 1:
                    if self.game[row][column] == 0:
                        error += 1

                    elif self.game[row][column] == 1:
                        offset += 1

        self.ui.label_left.setText("%i" % (self.valid_fields - offset))
        self.ui.label_wrong.setText("%i" % error)

        titem.setSelected(False)

        if ((self.valid_fields - offset) == 0) and error == 0:
            MessageBox(None, "Herzlichen glückwunsch!\nSie haben das Spiel geschafft!", "Nonogram", 0x40 | 0x0)

    def handlenewgame(self):
        self.clicked = [[0 for _ in range(15)] for _ in range(15)]
        self.handlestage()

        summe = 0
        for v in self.game:
            summe += sum(v)

        self.ui.label_left.setText("%i" % summe)
        self.ui.label_wrong.setText("0")

        self.valid_fields = summe

        list_rot = LG.rotate_list(self.game)

        list_hor = LG.calculate_list(self.game)
        list_ver = LG.calculate_list(list_rot)

        table_game = self.ui.table_game
        table_hor = self.ui.table_hor
        table_ver = self.ui.table_ver

        table_game.setRowCount(0)
        table_game.setColumnCount(0)

        table_hor.setRowCount(0)
        table_hor.setColumnCount(0)

        table_ver.setRowCount(0)
        table_ver.setColumnCount(0)

        table_game.setRowCount(15)
        table_game.setColumnCount(15)

        table_hor.setRowCount(15)
        table_hor.setColumnCount(7)

        table_ver.setRowCount(7)
        table_ver.setColumnCount(15)

        for row in range(len(self.game)):
            list_game_column = self.game[row]

            for column in range(len(list_game_column)):
                titem = CTableWidgetItem(row, column)

                table_game.setItem(row, column, titem)

        for row in range(len(list_hor)):
            list_hor_column = list_hor[row]

            for column in range(len(list_hor_column)):
                titem = QTableWidgetItem()
                titem.setTextAlignment(0x0004 | 0x0080)
                titem.setText("%i" % list_hor_column[column])

                table_hor.setItem(row, column, titem)

        for row in range(len(list_ver)):
            list_ver_column = list_ver[row]
            list_col_length = len(list_ver_column)

            for column in range(list_col_length):
                titem = QTableWidgetItem()
                titem.setTextAlignment(0x0004 | 0x0080)
                titem.setText("%i" % list_ver_column[column])

                table_ver.setItem(7 - list_col_length + column, row, titem)

        table_game.setEnabled(True)

    def handlesolution(self):
        table = self.ui.table_game

        for row in range(15):
            for column in range(15):
                titem = table.item(row, column)

                if self.game[row][column] == 1:
                    titem.setmarked(True)
                else:
                    titem.setmarked(False)

        table.setEnabled(False)

        self.ui.label_left.setText("0")
        self.ui.label_wrong.setText("0")

    def handlestage(self):
        index = self.ui.combo_stage.currentIndex()

        amount = 200

        if index == 1:
            amount = 150

        elif index == 2:
            amount = 125

        elif index == 3:
            amount = 90

        elif index == 4:
            amount = 50

        self.game = [[0 for _ in range(15)] for _ in range(15)]

        count = 0

        while count != amount:
            x = random.randint(0, 14)
            y = random.randint(0, 14)

            if self.game[x][y] == 0:
                self.game[x][y] = 1
                count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    nono = Nonogramm()

    nono.show()
    sys.exit(app.exec_())
