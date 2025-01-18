# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'default.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)


class Ui_Default(object):
    def setupUi(self, Default):
        if not Default.objectName():
            Default.setObjectName(u"Default")
        Default.resize(400, 150)
        Default.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: #ededed;\n"
"}\n"
"\n"
"QLabel, QPushButton, QComboBox, QLineEdit, QRadioButton, QCheckBox {\n"
"    font-family: \"Open Sans\", serif;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton, QLineEdit {\n"
"    background-color: #ededed;\n"
"    color: #121212;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 20pt;\n"
"	font-weight: 800;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c000c0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f;\n"
"}\n"
"\n"
"QComboBox {\n"
"	color: black;\n"
"    background-color: #c000c0;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 15px;\n"
"    /*border-left: 1px solid #121212;*/\n"
"	border: none\n"
"}\n"
"\n"
"QLineEdit {background: white}\n"
"\n"
"QRadioButton {font-size: 12pt}\n"
"\n"
"QC"
                        "heckBox {font-size: 10pt}")
        self.label = QLabel(Default)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 71))
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_yes = QPushButton(Default)
        self.btn_yes.setObjectName(u"btn_yes")
        self.btn_yes.setGeometry(QRect(5, 100, 151, 41))
        self.btn_no = QPushButton(Default)
        self.btn_no.setObjectName(u"btn_no")
        self.btn_no.setGeometry(QRect(245, 100, 151, 41))

        self.retranslateUi(Default)

        QMetaObject.connectSlotsByName(Default)
    # setupUi

    def retranslateUi(self, Default):
        Default.setWindowTitle(QCoreApplication.translate("Default", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Default", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b, \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u0431\u0440\u043e\u0441\u0438\u0442\u044c \n"
"\u0432\u0441\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0434\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \n"
"\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e?", None))
        self.btn_yes.setText(QCoreApplication.translate("Default", u"\u0414\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Default", u"\u041d\u0435\u0442", None))
    # retranslateUi

