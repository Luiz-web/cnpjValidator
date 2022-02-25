import sys
from gerando_cnpj import validando , formata
from PyQt5.QtWidgets import QApplication, QMainWindow


import design

class TrueCnpj(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGenerate.clicked.connect(self.formata)
        self.btnValidate.clicked.connect(self.validando)

    def formata(self):
         self.inputGenerate.setText(
             formata()
         )
   
    def validando(self):
        cnpj = self.inputValidate.text()
        self.labelReturn.setText(
            validando(cnpj)
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    true_cnpj = TrueCnpj()
    true_cnpj.show()
    qt.exec_()