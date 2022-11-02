# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generalZvQcfb.ui'
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
        MainWindow.resize(301, 170)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 10, 160, 112))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_ing_alumno = QPushButton(self.verticalLayoutWidget)
        self.bt_ing_alumno.setObjectName(u"bt_ing_alumno")

        self.verticalLayout.addWidget(self.bt_ing_alumno)

        self.bt_creargrup = QPushButton(self.verticalLayoutWidget)
        self.bt_creargrup.setObjectName(u"bt_creargrup")

        self.verticalLayout.addWidget(self.bt_creargrup)

        self.bt_list_alum = QPushButton(self.verticalLayoutWidget)
        self.bt_list_alum.setObjectName(u"bt_list_alum")

        self.verticalLayout.addWidget(self.bt_list_alum)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bt_ing_alumno.clicked.connect(MainWindow.ing_alum)
        self.bt_creargrup.clicked.connect(MainWindow.crea_grup)
        self.bt_list_alum.clicked.connect(MainWindow.lista_alum)
        self.pushButton_4.clicked.connect(MainWindow.salir)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_ing_alumno.setText(QCoreApplication.translate("MainWindow", u"Ingresar Alumno", None))
        self.bt_creargrup.setText(QCoreApplication.translate("MainWindow", u"Crear Grupo", None))
        self.bt_list_alum.setText(QCoreApplication.translate("MainWindow", u"Lista de Alumnos", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

