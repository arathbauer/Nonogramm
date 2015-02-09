__author__ = 'ilendemli'

import sys
import ctypes

from model import GUIModel
from view import CTableWidgetItem
from controller import (LG, TG)

from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem)

MessageBox = ctypes.windll.user32.MessageBoxW


class Nonogramm(QMainWindow):
    game = None
    clicked = None
    valid_fields = None

    red = 255
    green = 255
    blue = 255

    def __init__(self):
        QMainWindow.__init__(self, parent=None)

        self.ui = GUIModel.create(self)

        self.ui.table_game.clicked.connect(self.handlespot)
        self.ui.button_newgame.clicked.connect(self.handlenewgame)
        self.ui.button_solution.clicked.connect(self.handlesolution)
        self.ui.combo_stage.activated.connect(self.handlestage)

        self.ui.slider_red.valueChanged.connect(self.handleslider)
        self.ui.slider_green.valueChanged.connect(self.handleslider)
        self.ui.slider_blue.valueChanged.connect(self.handleslider)


    def handleslider(self):
        sender = self.sender()

        if sender == self.ui.slider_red:
            self.red = self.ui.slider_red.value()

        elif sender == self.ui.slider_green:
            self.green = self.ui.slider_green.value()

        elif sender == self.ui.slider_blue:
            self.blue = self.ui.slider_blue.value()

        self.setStyleSheet("background-color: rgb(%i, %i, %i);" % (self.red, self.green, self.blue))

    def handlespot(self):
        table_game = self.ui.table_game

        row = table_game.currentRow()
        column = table_game.currentColumn()

        titem = table_game.item(row, column)
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
            self.game = None
            table_game.setEnabled(False)
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

        TG.recreate_tables(table_game, table_hor, table_ver)

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

                table_ver.setItem(8 - list_col_length + column, row, titem)

        table_game.setEnabled(True)

    def handlesolution(self):
        if self.game:
            table_game = self.ui.table_game

            for row in range(15):
                for column in range(15):
                    titem = table_game.item(row, column)

                    if self.game[row][column] == 1:
                        titem.setmarked(True)
                    else:
                        titem.setmarked(False)

            table_game.setEnabled(False)

            self.ui.label_left.setText("0")
            self.ui.label_wrong.setText("0")

            self.game = None

        else:
            MessageBox(None, "Es wurde kein Spiel gestartet!", "Nonogram", 0x40 | 0x0)

    def handlestage(self):
        index = self.ui.combo_stage.currentIndex()

        self.game = LG.create_new_game(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    nono = Nonogramm()
    nono.show()
    sys.exit(app.exec_())
