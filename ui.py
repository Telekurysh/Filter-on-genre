from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 321)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 471, 26))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 0, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.tablewidget = QtWidgets.QTableWidget(Form)
        self.tablewidget.setGeometry(QtCore.QRect(10, 50, 571, 261))
        self.tablewidget.setObjectName("tablewidget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(translate("Form", "Каталог фильмов"))
        self.pushButton.setText(translate("Form", "Поиск"))
        self.comboBox.addItem(translate("Form", '-'))
        for id, title in self.data:
            self.comboBox.addItem(translate("Form", title))
        req = "SELECT title FROM films"
        cur = self.con.cursor()
        data = cur.execute(req).fetchall()
        self.tablewidget.setColumnCount(1)
        self.tablewidget.setRowCount(len(data))
        self.tablewidget.setHorizontalHeaderLabels(["Фильм"])
        for i in range(len(data)):
            self.tablewidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
        self.tablewidget.resizeColumnsToContents()
