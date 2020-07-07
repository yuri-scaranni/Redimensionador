import sys, os
from codigos.CaniveteImagens.interface import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class canivete(QMainWindow, Ui_Canivete):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_pesquisar.clicked.connect(self.abrirImagem)
        self.btn_redefinir.clicked.connect(self.redefinir)
        self.btn_salvar.clicked.connect(self.salvar)

    def abrirImagem(self):
        img_open, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            f'{os.getcwd()}'
        )
        self.label_pesquisa.setText(img_open)
        self.old_img = QPixmap(img_open)
        self.label_imagem.setPixmap(self.old_img)
        self.inserir_largura.setText(str(self.old_img.width()))
        self.inserir_altura.setText(str(self.old_img.height()))

    def redefinir(self):
        largura = int(self.inserir_largura.text())
        self.nova_imagem = self.old_img.scaledToWidth(largura)
        self.label_imagem.setPixmap(self.nova_imagem)
        self.inserir_largura.setText(str(self.nova_imagem.width()))
        self.inserir_altura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        img_open, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            f'{os.getcwd()}'
        )
        self.nova_imagem.save(img_open + ".png")

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    instancia_canivete = canivete()
    instancia_canivete.show()
    qt.exec_()