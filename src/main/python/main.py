from fbs_runtime.application_context import ApplicationContext
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from prefixcalculator_fun import calculate

# button function
def PButton(context, name, ssheet, connection, xs, ys, xp,yp):
    b = QPushButton(name, context)
    b.setStyleSheet(ssheet)
    b.clicked.connect(connection)
    b.resize(xs,ys)
    b.move(xp, yp)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(600, 250)
        self.setWindowTitle("Prefix Calculator")

        str1 = '{font-family: Courier;font-style: normal; font-size: 22pt;font-weight: bold;}'
        #str2 = '{font-family: Arial;font-style: normal;font-size: 13pt;}'
        str3 = '{color: gray; font-family: Arial;font-style: normal;font-size: 24pt;font-weight: bold;}'
        str4 = '{background-color: grey; color: white; font-family: Arial;font-style: normal;\
        font-size: 24pt;font-weight: bold;}'
        self.inputstring = ""

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Prefix Calculator')
        self.nameLabel.setStyleSheet('QLabel ' + str3)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.nameLabel.setFixedWidth(200)
        self.nameLabel.move(5, 220)

        #input 
        self.line = QLineEdit(self)
        self.line.setStyleSheet('QLineEdit ' + str1)
        self.line.move(100, 20)
        self.line.setFixedSize(390, 32)
        self.line.setAlignment(QtCore.Qt.AlignRight)
        self.line.textChanged.connect(self.textAdded) # keyboard and button inputs are sent 

        # result
        self.resline = QLineEdit(self)
        self.resline.setReadOnly(True)
        self.resline.setStyleSheet('QLineEdit ' + str1)
        self.resline.move(100, 60)
        self.resline.setFixedSize(390, 32)
        self.resline.setAlignment(QtCore.Qt.AlignRight)
        self.resline.setText('0')

        # button
        x = 102
        y = 105
        size = 34
        pitch = 39

        #calculator buttons
        strcal='QPushButton {background-color:green;color:white;font-family:Arial;font-style:normal; \
        font-size:40pt;font-weight:bold;}'
        compute = PButton(self, '=', strcal, self.compute, 64, 64, 510,22)
        b1 = PButton(self, '1', 'QPushButton '+ str4, self.one, size, size, x,y)
        b2 = PButton(self, '2', 'QPushButton '+ str4, self.two, size, size, x+pitch,y)
        b3 = PButton(self, '3', 'QPushButton '+ str4, self.three, size, size, x+2*pitch,y)
        b4 = PButton(self, '4', 'QPushButton '+ str4, self.four, size, size, x+3*pitch,y)
        b5 = PButton(self, '5', 'QPushButton '+ str4, self.five, size, size, x+4*pitch,y)
        b6 = PButton(self, '6', 'QPushButton '+ str4, self.six, size, size, x+5*pitch,y)
        b7 = PButton(self, '7', 'QPushButton '+ str4, self.seven, size, size, x+6*pitch,y)
        b8 = PButton(self, '8', 'QPushButton '+ str4, self.eight, size, size, x+7*pitch,y)
        b9 = PButton(self, '9', 'QPushButton '+ str4, self.nine, size, size, x+8*pitch,y)
        b0 = PButton(self, '0', 'QPushButton '+ str4, self.zero, size, size, x+9*pitch,y)
        y1 = y+pitch
        b11 = PButton(self, '+', 'QPushButton '+ str4, self.plus, size, size, x,y1)
        b12 = PButton(self, '-', 'QPushButton '+ str4, self.minus, size, size, x+1*pitch,y1)
        b13 = PButton(self, '*', 'QPushButton '+ str4, self.mult, size, size, x+2*pitch,y1)
        b14 = PButton(self, '/', 'QPushButton '+ str4, self.division, size, size, x+3*pitch,y1)
        b15 = PButton(self, '.', 'QPushButton '+ str4, self.decimal, size, size, x+4*pitch,y1)
        size2 = 2*pitch+size
        b16 = PButton(self, 'space', 'QPushButton '+ str4, self.space, size2, size, x+5*pitch,y1)
        x2 = x+5*pitch+size2+5
        strd='QPushButton {background-color:grey;color:white;font-family:Arial;font-style:normal; \
        font-size:18pt;font-weight:bold;}'
        b17 = PButton(self, 'del', strd, self.delete, size, size, x2,y1)
        b18 = PButton(self, 'AC', strd, self.ac, size, size, x2+pitch,y1)

    def compute(self):
        final_value = calculate(self.line.text()); self.resline.setText(str(final_value))
    def textAdded(self, text):
        self.inputstring = text
    def one(self):
        self.inputstring = self.inputstring + "1"; self.line.setText(self.inputstring)
    def two(self):
        self.inputstring = self.inputstring + "2"; self.line.setText(self.inputstring)
    def three(self):
        self.inputstring = self.inputstring + "3"; self.line.setText(self.inputstring)       
    def four(self):
        self.inputstring = self.inputstring + "4"; self.line.setText(self.inputstring)
    def five(self):
        self.inputstring = self.inputstring + "5"; self.line.setText(self.inputstring)    
    def six(self):
        self.inputstring = self.inputstring + "6"; self.line.setText(self.inputstring)
    def seven(self):
        self.inputstring = self.inputstring + "7"; self.line.setText(self.inputstring)
    def eight(self):
        self.inputstring = self.inputstring + "8"; self.line.setText(self.inputstring)   
    def nine(self):
        self.inputstring = self.inputstring + "9"; self.line.setText(self.inputstring)
    def zero(self):
        self.inputstring = self.inputstring + "0"; self.line.setText(self.inputstring)
    def decimal(self):
        self.inputstring = self.inputstring + "."; self.line.setText(self.inputstring)
    def plus(self):
        self.inputstring = self.inputstring + "+"; self.line.setText(self.inputstring)
    def minus(self):
        self.inputstring = self.inputstring + "-"; self.line.setText(self.inputstring)    
    def mult(self):
        self.inputstring = self.inputstring + "*"; self.line.setText(self.inputstring)
    def division(self):
        self.inputstring = self.inputstring + "/"; self.line.setText(self.inputstring)
    def space(self):
        self.inputstring =  self.inputstring + " "; self.line.setText(self.inputstring)
    def delete(self):
        self.inputstring =  self.inputstring[:-1]; self.line.setText(self.inputstring)
    def ac(self):
        self.inputstring =  ""; self.line.setText(self.inputstring); self.resline.setText('0')

#uses fbs to create installer etc https://build-system.fman.io/
if __name__ == "__main__":
    appctxt = ApplicationContext()
    mainWin = MainWindow()
    mainWin.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
