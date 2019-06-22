# -*- coding: utf-8 -*-


#
# Created by: @ArianQaragozlou
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn import tree 

data = open("data" , "r").read()
data = data.split()
y = []
x = []
for i in data[4:]:
    d = i.split(",")
    y.append(d[1])
    x.append([float(d[5]) , float(d[2]) ])
clf = tree.DecisionTreeClassifier()
clf.fit(x,y)
def status(x1, x2) :
    return clf.predict([[x1 ,x2]])

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 429)
        self.widget = QtWidgets.QWidget(mainWindow)
        self.widget.setObjectName("widget")
        self.log = QtWidgets.QTextEdit(self.widget)
        self.log.setGeometry(QtCore.QRect(0, 280, 641, 101))
        self.log.setObjectName("log")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 80, 141, 29))
        self.lineEdit.setObjectName("lineEdit")
        self.button = QtWidgets.QPushButton(self.widget)
        self.button.setGeometry(QtCore.QRect(60, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.text = QtWidgets.QTextEdit(self.widget)
        self.text.setGeometry(QtCore.QRect(260, 40, 371, 231))
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 60, 241, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 371, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 150, 141, 29))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 241, 20))
        self.label_3.setObjectName("label_3")
        mainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.button.clicked.connect(self.chek)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.log.append("starting \n")
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Diagnosing the Breast cancer condition with Machine Leaning"))
        mainWindow.setAccessibleName(_translate("mainWindow", "Diagnosis of Breast Cancer Status"))
        self.button.setText(_translate("mainWindow", "Survey "))
        self.label.setText(_translate("mainWindow", "Area mean of Breast Cancer Tumor"))
        self.label_2.setText(_translate("mainWindow", "The result of the diagnosis of cancer status  :‌"))
        self.label_3.setText(_translate("mainWindow", "Radius mean of Breast Cancer Tumor"))
    def chek(self):
        x1 = self.lineEdit.text()
        x2 = self.lineEdit_2.text()
        self.log.append("Diagnosing the cancer condition ")
        y = status(float(x1) , float(x2) )
        if y[0] == "B":
            self.text.append("area mean and radius mean : "+x1+","+x2+" > This cancer is Benign")
        else :
            self.text.append("area mean and radius mean : "+x1+","+x2+" > This cancer is Malignant")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

