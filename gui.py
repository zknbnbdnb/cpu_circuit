from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
from main import Ui_MainWindow
from r import Ui_Dialog1
from lw import Ui_Dialog2
from sw import Ui_Dialog3
from beq import Ui_Dialog4
from functools import partial


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)


class r(QDialog):
    def __init__(self):
        super().__init__()
        self.r = Ui_Dialog1()
        self.r.setupUi(self)
        self.gif = QMovie('r.gif')
        self.r.label.setMovie(self.gif)

        self.r.pushButton.clicked.connect(self.gif.start)
        self.r.pushButton_2.clicked.connect(partial(self.gif.setSpeed, 350))
        self.r.pushButton_3.clicked.connect(partial(self.gif.setSpeed, 50))
        self.r.pushButton_4.clicked.connect(self.gif.stop)
        self.r.pushButton_5.clicked.connect(partial(self.gif.setSpeed, 100))


class lw(QDialog):
    def __init__(self):
        super().__init__()
        self.lw = Ui_Dialog2()
        self.lw.setupUi(self)
        self.gif = QMovie('lw.gif')
        self.lw.label.setMovie(self.gif)

        self.lw.pushButton.clicked.connect(self.gif.start)
        self.lw.pushButton_2.clicked.connect(partial(self.gif.setSpeed, 350))
        self.lw.pushButton_3.clicked.connect(partial(self.gif.setSpeed, 50))
        self.lw.pushButton_4.clicked.connect(self.gif.stop)
        self.lw.pushButton_5.clicked.connect(partial(self.gif.setSpeed, 100))


class sw(QDialog):
    def __init__(self):
        super().__init__()
        self.sw = Ui_Dialog3()
        self.sw.setupUi(self)
        self.gif = QMovie('sw.gif')
        self.sw.label.setMovie(self.gif)

        self.sw.pushButton.clicked.connect(self.gif.start)
        self.sw.pushButton_2.clicked.connect(partial(self.gif.setSpeed, 350))
        self.sw.pushButton_3.clicked.connect(partial(self.gif.setSpeed, 50))
        self.sw.pushButton_4.clicked.connect(self.gif.stop)
        self.sw.pushButton_5.clicked.connect(partial(self.gif.setSpeed, 100))


class beq(QDialog):
    def __init__(self):
        super().__init__()
        self.beq = Ui_Dialog4()
        self.beq.setupUi(self)
        self.gif = QMovie('beq.gif')
        self.beq.label.setMovie(self.gif)

        self.beq.pushButton.clicked.connect(self.gif.start)
        self.beq.pushButton_2.clicked.connect(partial(self.gif.setSpeed, 350))
        self.beq.pushButton_3.clicked.connect(partial(self.gif.setSpeed, 50))
        self.beq.pushButton_4.clicked.connect(self.gif.stop)
        self.beq.pushButton_5.clicked.connect(partial(self.gif.setSpeed, 100))


app = QApplication([])

window = main()

i = 100

r = r()
lw = lw()
sw = sw()
beq = beq()
window.show()

btn1 = window.main.pushButton
btn2 = window.main.pushButton_2
btn3 = window.main.pushButton_3
btn4 = window.main.pushButton_4

btn1.clicked.connect(r.show)
btn2.clicked.connect(lw.show)
btn3.clicked.connect(sw.show)
btn4.clicked.connect(beq.show)


app.exec_()
