import pandas as pd

from database import Database
import sys
import pyqtgraph as pg
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QFont, QTextCharFormat
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QWidget, QApplication
db = Database("ADAMS")

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.preds_table = QtWidgets.QTableWidget(self.centralwidget)
        self.c_name = QtWidgets.QTextEdit(self.centralwidget)
        self.graphWidget = pg.PlotWidget(self.centralwidget)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("PredStocks")
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        MainWindow.setObjectName("main_window")
        MainWindow.setGeometry(0, 0, 1150, 600)
        stylesheet = (
             "background-color: #ADC9EC"
             )
        MainWindow.setStyleSheet(stylesheet)




        self.centralwidget.setObjectName("centralwidget")
        self.header()
        self.predictions()
        self.company_info()
        self.graph()


    def header(self):
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 801, 110))
        self.textEdit.setObjectName("textEdit")

    def predictions(self):

        self.preds_table.setGeometry(QtCore.QRect(540, 280, 557, 62))
        self.preds_table.setObjectName("preds_table")
        self.preds_table.setColumnCount(5)
        self.preds_table.setRowCount(2)
        self.preds_table.verticalHeader().setVisible(False)
        self.preds_table.horizontalHeader().setVisible(False)
        prediction_data = db.fetch_preds_from_db()
        prediction_data = list(prediction_data[0])

        for i in range(5):
            self.preds_table.setColumnWidth(i,111)
            self.preds_table.setItem(0,i, QTableWidgetItem(col_names[i]))
            self.preds_table.setItem(1, i, QTableWidgetItem(str(prediction_data[i])))
        self.preds_table.setStyleSheet("font-size:18px;")

        return self.preds_table


    def company_info(self):

        self.c_name.setGeometry(QtCore.QRect(30, 200, 330, 50))
        self.c_name.setPlainText("Adam Sugar Mills Limited")
        self.c_name.setStyleSheet("font-size:18px; margin-top:10px; color:#1073F4;")
        self.c_name.setReadOnly(True)
        self.c_name.setObjectName("c_name")


    def graph(self):

        self.graphWidget.setGeometry(QtCore.QRect(30, 280, 500, 320))
        self.graphWidget.setBackground("#376773")
        self.graphWidget.setObjectName("graphWidget")

        actual_data , prediction_data= db.fetch_ploting_data()

        prediction_data[1] = prediction_data[1].replace(",","")
        # Create a PlotItem in the PlotWidget
        plot_item = ui.graphWidget.plotItem


        # Plot data with different colors
        pen_colors = [Qt.GlobalColor.blue, Qt.GlobalColor.red]
        plot_item.plot(prediction_data[5], pen=QPen(Qt.GlobalColor.blue))
        plot_item.plot(actual_data[5], pen=QPen(pen_colors[1]))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PredStocks"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#1073F4;\">Welcome to PredStocks</span></p>\n"
                                         ))




if __name__ == "__main__":
    prediction_data = None
    actual_data = None
    col_names = ['Date', 'Open', 'High', 'Low', 'Close']

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec())
