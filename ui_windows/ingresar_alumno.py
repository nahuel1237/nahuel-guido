# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingresar_alumnoFMhWBz.ui'
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
        MainWindow.resize(334, 225)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 60, 211, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_nombre1 = QLineEdit(self.formLayoutWidget)
        self.le_nombre1.setObjectName(u"le_nombre1")
        self.le_nombre1.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nombre1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_apellido1 = QLineEdit(self.formLayoutWidget)
        self.le_apellido1.setObjectName(u"le_apellido1")
        self.le_apellido1.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_apellido1)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.le_DNI_1 = QLineEdit(self.formLayoutWidget)
        self.le_DNI_1.setObjectName(u"le_DNI_1")
        self.le_DNI_1.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_DNI_1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 140, 211, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bt_limp_1 = QPushButton(self.horizontalLayoutWidget)
        self.bt_limp_1.setObjectName(u"bt_limp_1")

        self.horizontalLayout_7.addWidget(self.bt_limp_1)

        self.bt_enviar_1 = QPushButton(self.horizontalLayoutWidget)
        self.bt_enviar_1.setObjectName(u"bt_enviar_1")

        self.horizontalLayout_7.addWidget(self.bt_enviar_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bt_limp_1.clicked.connect(MainWindow.limpiar_alum)
        self.bt_enviar_1.clicked.connect(MainWindow.enviar_alum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.le_DNI_1.setInputMask(QCoreApplication.translate("MainWindow", u"99.999.999", None))
        self.bt_limp_1.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.bt_enviar_1.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

