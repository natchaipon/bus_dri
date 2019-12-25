# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dri_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/Natchaipon/Desktop/smartbus_dri/953419.png"))
        self.bg.setObjectName("bg")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 40, 471, 211))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
# import bg_rc
