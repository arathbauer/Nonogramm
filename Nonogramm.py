# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GrundGeruestNono.ui'
#
# Created: Fri Jan 16 14:35:31 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 872)
        self.panel = QtWidgets.QWidget(MainWindow)
        self.panel.setObjectName("panel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.container = QtWidgets.QVBoxLayout()
        self.container.setSpacing(10)
        self.container.setContentsMargins(10, 10, 10, 10)
        self.container.setObjectName("container")
        self.oben = QtWidgets.QHBoxLayout()
        self.oben.setObjectName("oben")
        self.grid_vertikale = QtWidgets.QGridLayout()
        self.grid_vertikale.setObjectName("grid_vertikale")
        self.oben.addLayout(self.grid_vertikale)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.oben.addItem(spacerItem)
        self.oben.setStretch(0, 2)
        self.oben.setStretch(1, 1)
        self.container.addLayout(self.oben)
        self.mitte = QtWidgets.QHBoxLayout()
        self.mitte.setObjectName("mitte")
        self.grid_felder = QtWidgets.QGridLayout()
        self.grid_felder.setObjectName("grid_felder")
        self.mitte.addLayout(self.grid_felder)
        self.grid_horizontale = QtWidgets.QGridLayout()
        self.grid_horizontale.setObjectName("grid_horizontale")
        self.mitte.addLayout(self.grid_horizontale)
        self.mitte.setStretch(0, 2)
        self.mitte.setStretch(1, 1)
        self.container.addLayout(self.mitte)
        self.unten = QtWidgets.QHBoxLayout()
        self.unten.setObjectName("unten")
        self.label_offen = QtWidgets.QLabel(self.panel)
        self.label_offen.setEnabled(True)
        self.label_offen.setObjectName("label_offen")
        self.unten.addWidget(self.label_offen)
        self.edit_offen_zahl = QtWidgets.QLineEdit(self.panel)
        self.edit_offen_zahl.setEnabled(False)
        self.edit_offen_zahl.setMouseTracking(False)
        self.edit_offen_zahl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_offen_zahl.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_offen_zahl.setObjectName("edit_offen_zahl")
        self.unten.addWidget(self.edit_offen_zahl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.unten.addItem(spacerItem1)
        self.button_loesung = QtWidgets.QPushButton(self.panel)
        self.button_loesung.setObjectName("button_loesung")
        self.unten.addWidget(self.button_loesung)
        self.combobox_grad = QtWidgets.QComboBox(self.panel)
        self.combobox_grad.setObjectName("combobox_grad")
        self.combobox_grad.addItem("")
        self.combobox_grad.addItem("")
        self.combobox_grad.addItem("")
        self.combobox_grad.addItem("")
        self.combobox_grad.addItem("")
        self.unten.addWidget(self.combobox_grad)
        self.button_neustart = QtWidgets.QPushButton(self.panel)
        self.button_neustart.setObjectName("button_neustart")
        self.unten.addWidget(self.button_neustart)
        self.unten.setStretch(1, 1)
        self.unten.setStretch(2, 2)
        self.unten.setStretch(3, 1)
        self.unten.setStretch(4, 1)
        self.unten.setStretch(5, 1)
        self.container.addLayout(self.unten)
        self.container.setStretch(0, 1)
        self.container.setStretch(1, 2)
        self.verticalLayout.addLayout(self.container)
        MainWindow.setCentralWidget(self.panel)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionEasy = QtWidgets.QAction(MainWindow)
        self.actionEasy.setObjectName("actionEasy")
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setObjectName("actionMedium")
        self.actionHard = QtWidgets.QAction(MainWindow)
        self.actionHard.setObjectName("actionHard")
        self.actionExpert = QtWidgets.QAction(MainWindow)
        self.actionExpert.setObjectName("actionExpert")
        self.actionImpossible = QtWidgets.QAction(MainWindow)
        self.actionImpossible.setObjectName("actionImpossible")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionTeam = QtWidgets.QAction(MainWindow)
        self.actionTeam.setObjectName("actionTeam")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_offen.setText(_translate("MainWindow", "Felder offen:"))
        self.edit_offen_zahl.setText(_translate("MainWindow", "150"))
        self.button_loesung.setText(_translate("MainWindow", "Lösung"))
        self.combobox_grad.setItemText(0, _translate("MainWindow", "Easy"))
        self.combobox_grad.setItemText(1, _translate("MainWindow", "Medium"))
        self.combobox_grad.setItemText(2, _translate("MainWindow", "Hard"))
        self.combobox_grad.setItemText(3, _translate("MainWindow", "Expert"))
        self.combobox_grad.setItemText(4, _translate("MainWindow", "Impossible"))
        self.button_neustart.setText(_translate("MainWindow", "Neustart"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionHard.setText(_translate("MainWindow", "Hard"))
        self.actionExpert.setText(_translate("MainWindow", "Expert"))
        self.actionImpossible.setText(_translate("MainWindow", "Impossible"))
        self.actionExit.setText(_translate("MainWindow", "Solve Game"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionTeam.setText(_translate("MainWindow", "Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

