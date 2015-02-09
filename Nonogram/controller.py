__author__ = 'ilendemli'

import random


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

    @staticmethod
    def create_new_game(index):

        amount = 200

        if index == 1:
            amount = 150

        elif index == 2:
            amount = 125

        elif index == 3:
            amount = 90

        elif index == 4:
            amount = 50

        temp_game = [[0 for _ in range(15)] for _ in range(15)]

        count = 0

        while count != amount:
            x = random.randint(0, 14)
            y = random.randint(0, 14)

            if temp_game[x][y] == 0:
                temp_game[x][y] = 1
                count += 1

        return temp_game

class TG():

    @staticmethod
    def recreate_tables(table_game, table_hor, table_ver):
        table_game.setRowCount(0)
        table_game.setColumnCount(0)

        table_hor.setRowCount(0)
        table_hor.setColumnCount(0)

        table_ver.setRowCount(0)
        table_ver.setColumnCount(0)

        table_game.setRowCount(15)
        table_game.setColumnCount(15)

        table_hor.setRowCount(15)
        table_hor.setColumnCount(8)

        table_ver.setRowCount(8)
        table_ver.setColumnCount(15)