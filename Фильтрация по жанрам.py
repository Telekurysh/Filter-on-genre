import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sqlite3
from ui import Ui_Form


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("films.db")
        req = "SELECT id,title FROM genres"
        cur = self.con.cursor()
        self.data = cur.execute(req).fetchall()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        el = self.comboBox.currentText()
        if el != '-':
            for i in self.data:
                if el == i[1]:
                    index = i[0]
                    break
            req = "SELECT title FROM films WHERE genre = {}".format(index)
        else:
            req = "SELECT title FROM films"
        cur = self.con.cursor()
        data = cur.execute(req).fetchall()
        self.tablewidget.setRowCount(len(data))
        for i in range(len(data)):
            self.tablewidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
        self.tablewidget.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())
