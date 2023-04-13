from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(90, 140, 621, 91))
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.splitter.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.splitter.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.splitter.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.splitter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.splitter.addWidget(self.pushButton_4)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(550, 420, 248, 197))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 229, 551, 391))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(549, 229, 251, 191))
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(-1, -1, 801, 141))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CPU\u6570\u636e\u901a\u8def", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"lw", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"beq", None))
    # retranslateUi

