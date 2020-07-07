# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Canivete(object):
    def setupUi(self, Canivete):
        Canivete.setObjectName("Canivete")
        Canivete.resize(604, 480)
        self.centralwidget = QtWidgets.QWidget(Canivete)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.gridLayout.addWidget(self.btn_pesquisar, 1, 5, 1, 1)
        self.btn_redefinir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_redefinir.setObjectName("btn_redefinir")
        self.gridLayout.addWidget(self.btn_redefinir, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.inserir_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.inserir_altura.setObjectName("inserir_altura")
        self.gridLayout.addWidget(self.inserir_altura, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.btn_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salvar.setObjectName("btn_salvar")
        self.gridLayout.addWidget(self.btn_salvar, 2, 5, 1, 1)
        self.inserir_largura = QtWidgets.QLineEdit(self.centralwidget)
        self.inserir_largura.setObjectName("inserir_largura")
        self.gridLayout.addWidget(self.inserir_largura, 2, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 584, 402))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_imagem = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_imagem.setText("")
        self.label_imagem.setObjectName("label_imagem")
        self.gridLayout_2.addWidget(self.label_imagem, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 6)
        self.label_pesquisa = QtWidgets.QLineEdit(self.centralwidget)
        self.label_pesquisa.setObjectName("label_pesquisa")
        self.gridLayout.addWidget(self.label_pesquisa, 1, 0, 1, 5)
        Canivete.setCentralWidget(self.centralwidget)

        self.retranslateUi(Canivete)
        QtCore.QMetaObject.connectSlotsByName(Canivete)

    def retranslateUi(self, Canivete):
        _translate = QtCore.QCoreApplication.translate
        Canivete.setWindowTitle(_translate("Canivete", "Canivete"))
        self.btn_pesquisar.setText(_translate("Canivete", "Pesquisar"))
        self.btn_redefinir.setText(_translate("Canivete", "Redefinir"))
        self.label_2.setText(_translate("Canivete", "Altura"))
        self.label.setText(_translate("Canivete", "Largura"))
        self.btn_salvar.setText(_translate("Canivete", "Salvar"))
