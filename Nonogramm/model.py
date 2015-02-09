__author__ = 'ilendemli'

from PyQt5 import uic


class GUIModel(object):

    @classmethod
    def create(cls, parent):
        ui_class, base_class = uic.loadUiType("Nonogram.ui")

        uiobj = ui_class()
        uiobj.setupUi(parent)

        return uiobj