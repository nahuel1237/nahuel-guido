# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grupoPVhKvQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(264, 171)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 30, 160, 51))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_nombre_2 = QLineEdit(self.formLayoutWidget)
        self.le_nombre_2.setObjectName(u"le_nombre_2")
        self.le_nombre_2.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nombre_2)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_descrip_2 = QLineEdit(self.formLayoutWidget)
        self.le_descrip_2.setObjectName(u"le_descrip_2")
        self.le_descrip_2.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_descrip_2)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 80, 160, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_limpiar_2 = QPushButton(self.horizontalLayoutWidget)
        self.bt_limpiar_2.setObjectName(u"bt_limpiar_2")

        self.horizontalLayout_2.addWidget(self.bt_limpiar_2)

        self.bt_enviar_2 = QPushButton(self.horizontalLayoutWidget)
        self.bt_enviar_2.setObjectName(u"bt_enviar_2")

        self.horizontalLayout_2.addWidget(self.bt_enviar_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 264, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bt_limpiar_2.clicked.connect(MainWindow.limpiar_grup)
        self.bt_enviar_2.clicked.connect(MainWindow.enviar_grup)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.bt_limpiar_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar ", None))
        self.bt_enviar_2.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

