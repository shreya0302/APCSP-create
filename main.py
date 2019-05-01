from fbs_runtime.application_context import ApplicationContext
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from prefixcalculator import calculate

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(600, 250)
        self.setWindowTitle("Prefix Calculator")

        str1 = '{font-family: Courier;font-style: normal;font-size: 22pt;font-weight: bold;}'
        #str2 = '{font-family: Arial;font-style: normal;font-size: 13pt;}'
        str3 = '{color: gray; font-family: Arial;font-style: normal;font-size: 24pt;font-weight: bold;}'
        str4 = '{background-color: grey; color: white; font-family: Arial;font-style: normal;font-size: 24pt;font-weight: bold;}'
        self.inputstring = ""

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Prefix Calculator')
        self.nameLabel.setStyleSheet('QLabel ' + str3)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.nameLabel.setFixedWidth(200)
        self.nameLabel.move(5, 220)

        self.line = QLineEdit(self)
        self.line.setStyleSheet('QLineEdit ' + str1)
        self.line.move(100, 20)
        self.line.setFixedSize(390, 32)
        self.line.setAlignment(QtCore.Qt.AlignRight)
        self.line.textChanged.connect(self.textAdded)

        compute = QPushButton('=', self)
        compute.setStyleSheet('QPushButton {background-color: green; color: white; font-family: Arial;font-style: normal;font-size: 40pt;font-weight: bold;}')
        compute.clicked.connect(self.compute)
        compute.resize(64,64)
        compute.move(510, 22)

        self.resline = QLineEdit(self)
        self.resline.setReadOnly(True)
        self.resline.setStyleSheet('QLineEdit ' + str1)
        self.resline.move(100, 60)
        self.resline.setFixedSize(390, 32)
        self.resline.setAlignment(QtCore.Qt.AlignRight)
        self.resline.setText('0')

        # self.instruction = QPlainTextEdit(self)
        # self.instruction.setReadOnly(True)
        # self.instruction.setStyleSheet('QPlainTextEdit ' + str2)
        # self.instruction.move(150, 150)
        # self.instruction.setFixedSize(300, 100)
        # self.instruction.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        # self.instruction.setPlainText('Instruction:\nOnly +, -, *, / and numbers are allowed. Each terms are separated by one space. For example: \n  + / * 2 50 20 - 4 -2.5  =  11.5 \n  * 10 * 10 * 10 * 10 * 10 10  =  1000000 \n  / * 75 12 11  =  81.81818181818181')

        x = 102
        y = 105
        size = 34
        pitch = 39

        b1 = QPushButton('1', self)
        b1.setStyleSheet('QPushButton '+ str4)
        b1.clicked.connect(self.one)
        b1.resize(size,size)
        b1.move(x, y)

        b2 = QPushButton('2', self)
        b2.setStyleSheet('QPushButton '+ str4)
        b2.clicked.connect(self.two)
        b2.resize(size,size)
        b2.move(x+pitch, y)

        b3 = QPushButton('3', self)
        b3.setStyleSheet('QPushButton '+ str4)
        b3.clicked.connect(self.three)
        b3.resize(size,size)
        b3.move(x+2*pitch, y)

        b4 = QPushButton('4', self)
        b4.setStyleSheet('QPushButton '+ str4)
        b4.clicked.connect(self.four)
        b4.resize(size,size)
        b4.move(x+3*pitch, y)

        b5 = QPushButton('5', self)
        b5.setStyleSheet('QPushButton '+ str4)
        b5.clicked.connect(self.five)
        b5.resize(size,size)
        b5.move(x+4*pitch, y)

        b6 = QPushButton('6', self)
        b6.setStyleSheet('QPushButton '+ str4)
        b6.clicked.connect(self.six)
        b6.resize(size,size)
        b6.move(x+5*pitch, y)

        b7 = QPushButton('7', self)
        b7.setStyleSheet('QPushButton '+ str4)
        b7.clicked.connect(self.seven)
        b7.resize(size,size)
        b7.move(x+6*pitch, y)

        b8 = QPushButton('8', self)
        b8.setStyleSheet('QPushButton '+ str4)
        b8.clicked.connect(self.eight)
        b8.resize(size,size)
        b8.move(x+7*pitch, y)

        b9 = QPushButton('9', self)
        b9.setStyleSheet('QPushButton '+ str4)
        b9.clicked.connect(self.nine)
        b9.resize(size,size)
        b9.move(x+8*pitch, y)

        b0 = QPushButton('0', self)
        b0.setStyleSheet('QPushButton '+ str4)
        b0.clicked.connect(self.zero)
        b0.resize(size,size)
        b0.move(x+9*pitch, y)

        b11 = QPushButton('+', self)
        b11.setStyleSheet('QPushButton '+ str4)
        b11.clicked.connect(self.plus)
        b11.resize(size,size)
        b11.move(x, y+pitch)

        b12 = QPushButton('-', self)
        b12.setStyleSheet('QPushButton '+ str4)
        b12.clicked.connect(self.minus)
        b12.resize(size,size)
        b12.move(x+1*pitch, y+pitch)

        b13 = QPushButton('*', self)
        b13.setStyleSheet('QPushButton '+ str4)
        b13.clicked.connect(self.mult)
        b13.resize(size,size)
        b13.move(x+2*pitch, y+pitch)

        b14 = QPushButton('/', self)
        b14.setStyleSheet('QPushButton '+ str4)
        b14.clicked.connect(self.division)
        b14.resize(size,size)
        b14.move(x+3*pitch, y+pitch)

        b15 = QPushButton('.', self)
        b15.setStyleSheet('QPushButton '+ str4)
        b15.clicked.connect(self.decimal)
        b15.resize(size,size)
        b15.move(x+4*pitch, y+pitch)

        size2 = 2*pitch+size
        b16 = QPushButton('space', self)
        b16.setStyleSheet('QPushButton '+ str4)
        b16.clicked.connect(self.space)
        b16.resize(size2,size)
        b16.move(x+5*pitch, y+pitch)

        x2 = x+5*pitch+size2+5
        b17 = QPushButton('del', self)
        b17.setStyleSheet('QPushButton {background-color: grey; color: white; font-family: Arial;font-style: normal;font-size: 18pt;font-weight: bold;}')
        b17.clicked.connect(self.delete)
        b17.resize(size,size)
        b17.move(x2, y+pitch)

        b18 = QPushButton('AC', self)
        b18.setStyleSheet('QPushButton {background-color: grey; color: white; font-family: Arial;font-style: normal;font-size: 18pt;font-weight: bold;}')
        b18.clicked.connect(self.ac)
        b18.resize(size,size)
        b18.move(x2+pitch, y+pitch)


    def compute(self):
        final_value = calculate(self.line.text())
        #print(final_value)
        self.resline.setText(str(final_value))

    def textAdded(self, text):
        self.inputstring = text

    def one(self):
        self.inputstring = self.inputstring + "1"
        self.line.setText(self.inputstring)

    def two(self):
        self.inputstring = self.inputstring + "2"
        self.line.setText(self.inputstring)
    
    def three(self):
        self.inputstring = self.inputstring + "3"
        self.line.setText(self.inputstring)
        
    def four(self):
        self.inputstring = self.inputstring + "4"
        self.line.setText(self.inputstring)

    def five(self):
        self.inputstring = self.inputstring + "5"
        self.line.setText(self.inputstring)
    
    def six(self):
        self.inputstring = self.inputstring + "6"
        self.line.setText(self.inputstring)

    def seven(self):
        self.inputstring = self.inputstring + "7"
        self.line.setText(self.inputstring)

    def eight(self):
        self.inputstring = self.inputstring + "8"
        self.line.setText(self.inputstring)
    
    def nine(self):
        self.inputstring = self.inputstring + "9"
        self.line.setText(self.inputstring)

    def zero(self):
        self.inputstring = self.inputstring + "0"
        self.line.setText(self.inputstring)

    def decimal(self):
        self.inputstring = self.inputstring + "."
        self.line.setText(self.inputstring)

    def plus(self):
        self.inputstring = self.inputstring + "+"
        self.line.setText(self.inputstring)

    def minus(self):
        self.inputstring = self.inputstring + "-"
        self.line.setText(self.inputstring)
    
    def mult(self):
        self.inputstring = self.inputstring + "*"
        self.line.setText(self.inputstring)

    def division(self):
        self.inputstring = self.inputstring + "/"
        self.line.setText(self.inputstring)

    def space(self):
        self.inputstring =  self.inputstring + " "
        self.line.setText(self.inputstring)

    def delete(self):
        self.inputstring =  self.inputstring[:-1]
        self.line.setText(self.inputstring)

    def ac(self):
        self.inputstring =  ""
        self.line.setText(self.inputstring)
        self.resline.setText('0')

if __name__ == "__main__":
    appctxt = ApplicationContext()
    mainWin = MainWindow()
    mainWin.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
