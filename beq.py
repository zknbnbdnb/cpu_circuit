from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 1080, 600))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(960, 680, 111, 51))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 680, 111, 51))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(750, 680, 111, 51))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 680, 111, 51))
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(540, 680, 111, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u6682\u505c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u51cf\u901f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u52a0\u901f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u8fd8\u539f\u901f\u5ea6", None))
    # retranslateUi

