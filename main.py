from PyQt5 import QtWidgets, uic
import sys
from datetime import datetime
import bd
from PyQt5.QtCore import *
from datetime import datetime
##    x = bd.nomes_alunos()
## carregamento de nomes dos instrumentos

def abrir_registro_aula():
    tela_aula.dateEdit.setMinimumDate(QDate.currentDate()) 
    tela_aula.combo_alunos.addItems(bd.nomes_alunos())
    tela_aula.show()
def abrir_tela_instrumentos():
    instrumento = tela_instrumento.textbox.text()
    tela_instrumento.show()
    print(instrumento)
def abrir_tela_registro_aluno():
    tela_registro_aluno.dateEdit.setMinimumDate(QDate.currentDate()) 
    tela_registro_aluno.combo_instrumento.addItems(y)
    tela_registro_aluno.show()


app = QtWidgets.QApplication(sys.argv)

tela_menu = uic.loadUi('tela_menu.ui')
#tela instrumentos
tela_instrumento = uic.loadUi('tela_instrumento.ui')
tela_aula = uic.loadUi('tela_aula.ui')
tela_registro_aluno = uic.loadUi('tela_registro_aluno.ui')
y = bd.nomes_instrumentos()
tela_aula.combo_instrumentos.addItems(y)
tela_menu.btn_registrar_aula.clicked.connect(abrir_registro_aula)
tela_menu.btn_instrumentos.clicked.connect(abrir_tela_instrumentos)
tela_menu.btn_registrar_aluno.clicked.connect(abrir_tela_registro_aluno)
#tela_menu.btn_visualizar_registros.clicked.connect(abrir_registros)
bd.conn.close
tela_menu.show()
app.exec_()
