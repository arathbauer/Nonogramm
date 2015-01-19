import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QLabel)

ui_class, base_class = uic.loadUiType("Nono.ui")

class CPushButton(QPushButton):
    def __init__(self, rowIndex, columnIndex):
        QPushButton.__init__(self)

        self.rowIndex = rowIndex
        self.columnIndex = columnIndex

    def getRowIndex(self):
        return self.rowIndex

    def getColumnIndex(self):
        return self.columnIndex

class Nono(QMainWindow):
    game = None
    verticals = None
    horizontals = None
    clicked = None
    valid_fields = 0

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = ui_class()
        self.ui.setupUi(self)

        self.ui.button_neustart.clicked.connect(self.handleNeustart)
        self.ui.button_loesung.clicked.connect(self.handleLoesung)
        self.ui.combobox_grad.activated.connect(self.handleGrad)

    def setGame(self, game):
        self.game = game

    def setHorizontals(self, horizontals):
        self.horizontals = horizontals

    def setVerticals(self, verticals):
        self.verticals = verticals

    def handleLoesung(self):
        felder = self.ui.grid_felder

        for row in range(0, 15):
            for column in range (0, 15):
                t_button = felder.itemAtPosition(row, column).widget()
                t_button.__class__ = CPushButton

                if self.game[row][column] == 1:
                    t_button.setStyleSheet('background-color: black; border: 2px solid black; border-radius: 3px')
                else:
                    t_button.setStyleSheet('background-color: lightgray; border: 2px solid gray; border-radius: 3px')

    def calculate_list(self, tl):
        t_list = []

        t_count = 0

        for i in range(0, len(tl)):
            t_row = tl[i]
            t_arr = []

            for j in range(0, len(t_row)):
                if t_row[j] == 1:
                    t_count += 1

                elif t_row[j] == 0 and t_count != 0:
                    t_arr.append(t_count)
                    t_count = 0

            t_list.append(t_arr)

        return t_list

    def rotate_list(self, tl):
        t_list = []

        for i in range(0, len(tl)):
            t_row = []

            for j in range(0, len(tl[i])):
                t_row.append(tl[j][i])

            t_list.append(t_row)

        return t_list

    def handleNeustart(self):
        self.clicked = [[0 for _ in range(15)] for _ in range(15)]

        tl = [[random.choice([0, 1]) for _ in range(15)] for _ in range(15)]

        hor = self.calculate_list(tl)
        ver = self.calculate_list(self.rotate_list(tl))

        self.setGame(tl)
        self.setHorizontals(hor)
        self.setVerticals(ver)

        horizontale = self.ui.grid_horizontale
        vertikale = self.ui.grid_vertikale
        felder = self.ui.grid_felder

        t_row = 0
        for row in self.horizontals:
            t_col = 0
            if len(row) > 0:
                for t_v in row:
                    t_label = QPushButton()
                    t_label.setEnabled(False);
                    t_label.setText("%i" % t_v)
                    t_label.setStyleSheet('background-color: none; border: 2px solid none;')
                    horizontale.addWidget(t_label, t_row, t_col)

                    t_col += 1
            else:
                t_label = QPushButton()
                t_label.setEnabled(False);
                t_label.setText("0")
                t_label.setStyleSheet('background-color: none; border: 2px solid none;')
                horizontale.addWidget(t_label, t_row, t_col)

            t_row += 1

        t_col = 0
        for col in self.verticals:
            t_row = 0
            if len(col) > 0:
                for t_v in col:
                    t_label = QPushButton()
                    t_label.setEnabled(False);
                    t_label.setText("%i" % t_v)
                    t_label.setStyleSheet('background-color: none; border: 2px solid none;')
                    vertikale.addWidget(t_label, t_row, t_col)

                    t_row += 1
            else:
                t_label = QPushButton()
                t_label.setEnabled(False);
                t_label.setText("0")
                t_label.setStyleSheet('background-color: none; border: 2px solid none;')
                vertikale.addWidget(t_label, t_row, t_col)

            t_col += 1

        summe = 0
        for v in self.verticals:
            summe += sum(v)

        self.ui.edit_offen_zahl.setText("%i" % summe)
        self.ui.edit_fehler_zahl.setText("0")

        self.valid_fields = summe

        for row in range(0, 15):
            for column in range (0, 15):
                t_button = None

                try:
                    t_button = felder.itemAtPosition(row, column).widget()

                except AttributeError:
                    t_button = CPushButton(row, column)
                    t_button.clicked.connect(self.handleSpot)
                    felder.addWidget(t_button, row, column)

                t_button.setStyleSheet('background-color: lightgray; border: 2px solid gray; border-radius: 3px')

    def handleSpot(self):
        felder = self.ui.grid_felder

        clickedButton = self.sender()

        row = clickedButton.getRowIndex()
        column = clickedButton.getColumnIndex()

        if self.clicked[row][column] == 1:
            self.clicked[row][column] = 0
            clickedButton.setStyleSheet('background-color: lightgray; border: 2px solid gray; border-radius: 3px')
        else:
            self.clicked[row][column] = 1
            clickedButton.setStyleSheet('background-color: black; border: 2px solid black; border-radius: 3px')

        error = 0
        offset = 0
        for row in range(0, 15):
            for column in range(0, 15):
                if self.clicked[row][column] == 1:
                    if self.game[row][column] == 0:
                        error += 1

                    elif self.game[row][column] == 1:
                        offset += 1

        self.ui.edit_offen_zahl.setText("%i" % (self.valid_fields - offset))
        self.ui.edit_fehler_zahl.setText("%i" % error)

    def handleGrad(self):
        index = self.ui.combobox_grad.currentIndex()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    nono = Nono()

    nono.show()
    sys.exit(app.exec_())
