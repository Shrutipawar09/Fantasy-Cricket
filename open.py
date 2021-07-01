# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
MyCricket=sqlite3.connect('Database_cricket.db')
curs=MyCricket.cursor()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(19, 29, 361, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_team = QtWidgets.QLabel(self.frame)
        self.label_team.setGeometry(QtCore.QRect(60, 50, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_team.setFont(font)
        self.label_team.setObjectName("label_team")
        self.combo_name = QtWidgets.QComboBox(self.frame)
        self.combo_name.setGeometry(QtCore.QRect(60, 81, 161, 31))
        self.combo_name.setObjectName("combo_name")
        self.btn_open = QtWidgets.QPushButton(self.frame)
        self.btn_open.setGeometry(QtCore.QRect(90, 140, 93, 28))
        self.btn_open.setObjectName("btn_open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        curs.execute("SELECT DISTINCT name FROM teams;")
        result=curs.fetchall()
        for i in result:
            self.combo_name.addItem(i[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_team.setText(_translate("Dialog", "Select team name"))
        self.btn_open.setText(_translate("Dialog", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())