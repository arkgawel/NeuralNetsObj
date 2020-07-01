# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Preprocessing.Analize_and_Evaluate import Analize
from Preprocessing.DataLoader import DataLoader
from Preprocessing.Preprocess import Preprocess


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.cmatrix='empty'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textPath = QtWidgets.QTextEdit(self.centralwidget)
        self.textPath.setGeometry(QtCore.QRect(60, 40, 301, 31))
        self.textPath.setObjectName("textPath")


        self.textSep = QtWidgets.QTextEdit(self.centralwidget)
        self.textSep.setGeometry(QtCore.QRect(390, 40, 51, 31))
        self.textSep.setObjectName("textSep")

        self.textDec = QtWidgets.QTextEdit(self.centralwidget)
        self.textDec.setGeometry(QtCore.QRect(470, 40, 51, 31))
        self.textDec.setObjectName("textDec")


        self.textDefX = QtWidgets.QTextEdit(self.centralwidget)
        self.textDefX.setGeometry(QtCore.QRect(60, 170, 211, 31))
        self.textDefX.setObjectName("textDefX")


        self.textDefY = QtWidgets.QTextEdit(self.centralwidget)
        self.textDefY.setGeometry(QtCore.QRect(210, 170, 104, 31))
        self.textDefY.setObjectName("textDefY")


        self.pushNNet = QtWidgets.QPushButton(self.centralwidget)
        self.pushNNet.setGeometry(QtCore.QRect(60, 290, 101, 41))
        self.pushNNet.setObjectName("pushNNet")
        self.pushNNet.clicked.connect(self.onButtonClicked)

        self.pushButTest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButTest.setGeometry(QtCore.QRect(210, 290, 101, 41))
        self.pushButTest.clicked.connect(self.onButtonTestClicked)



        self.pushButTest.setObjectName("pushButTest")
        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setGeometry(QtCore.QRect(90, 20, 261, 16))


        self.labelPath.setObjectName("labelPath")
        self.labelSep = QtWidgets.QLabel(self.centralwidget)
        self.labelSep.setGeometry(QtCore.QRect(400, 20, 47, 13))
        self.labelSep.setObjectName("labelSep")
        self.labelDec = QtWidgets.QLabel(self.centralwidget)
        self.labelDec.setGeometry(QtCore.QRect(480, 20, 47, 13))
        self.labelDec.setObjectName("labelDec")
        self.labelDefX = QtWidgets.QLabel(self.centralwidget)
        self.labelDefX.setGeometry(QtCore.QRect(70, 150, 101, 16))
        self.labelDefX.setObjectName("labelDefX")
        self.labelDefY = QtWidgets.QLabel(self.centralwidget)
        self.labelDefY.setGeometry(QtCore.QRect(220, 150, 71, 16))
        self.labelDefY.setObjectName("labelDefY")
        self.textResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.textResult.setGeometry(QtCore.QRect(330, 160, 256, 192))
        self.textResult.setObjectName("textResult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 140, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())


        self.textPath.setText('./forestfires.csv')
        self.textSep.setText(";")
        self.textDec.setText(",")
        self.textDefX.setText("'temp','RH', 'wind','rain'")
        self.textDefY.setText("'fire'")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Prediction model", "Prediction model"))
        self.pushNNet.setText(_translate("MainWindow", "Build NNet"))
        
        self.pushButTest.setText(_translate("MainWindow", "Test Net"))
        self.labelPath.setText(_translate("MainWindow", "Define path: C:/.csv "))
        self.labelSep.setText(_translate("MainWindow", "Sep"))
        self.labelDec.setText(_translate("MainWindow", "Dec"))
        self.labelDefX.setText(_translate("MainWindow", "Define var X: a, b"))
        self.labelDefY.setText(_translate("MainWindow", "Define Y: a"))
        self.label.setText(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    def onButtonClicked(self):
        if (self.textPath.toPlainText() == '' or
            self.textDec.toPlainText() == '' or
            self.textSep.toPlainText() == '' or
            self.textDefX.toPlainText() == '' or
            self.textDefY.toPlainText() == '' ):

            print("fill all fields")
        else:
            try:
                vpath = self.textPath.toPlainText()
                vdecimal = self.textDec.toPlainText()
                vseparator = self.textSep.toPlainText()
                vx = self.textDefX.toPlainText()
                vy = self.textDefY.toPlainText()
                vx = eval('[' + vx + ']')
                vy = eval('[' + vy + ']')

                file = DataLoader(vpath, vseparator, vdecimal).read_file()
                X_train, X_test, y_train, y_test = Preprocess().scale_and_split(vx, vy, file)
                analize = Analize(len(vx))
                self.cmatrix = analize.evaluate_model(X_train, y_train, X_test, y_test)
                dialog = QMessageBox()
                dialog.setText("Model built")
                dialog.setWindowTitle("Model was built")
                dialog.addButton(QMessageBox.Ok)
                dialog.exec()
            except:
                dialog = QMessageBox()
                dialog.setText("Something is wrong! Check all inputs")
                dialog.setWindowTitle("Error")
                dialog.addButton(QMessageBox.Ok)
                dialog.exec()





    def onButtonTestClicked(self):
            self.textResult.setText(str(self.cmatrix))
            #self.print(tex)



if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())





