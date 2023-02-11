from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys
from datetime import datetime
import bd
from PyQt5.QtCore import *
from datetime import datetime
##    x = bd.nomes_alunos()
#### funções para salvar no banco
def salvar_aula():
    tela_aula.combo_instrumentos.addItems(bd.nomes_instrumentos()) 
    tela_aula.dateEdit.setMinimumDate(QDate.currentDate()) 
    tela_aula.combo_alunos.addItems(bd.nomes_alunos())
    instrumento = tela_aula.combo_instrumentos.currentText()
    data = tela_aula.dateEdit.text()
    aluno = tela_aula.combo_alunos.currentText()
    conteudo = tela_aula.textEditConteudo.toPlainText()
    print('Aluno: '+aluno+'Instrumento: '+
          instrumento+'Data: '+data+'Conteúdo: '+conteudo)
    if (instrumento == ''or data==''or instrumento==''or
        conteudo==''):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Falta dados suficientes para salvar aula")
        msgBox.setWindowTitle("Erro!")
        msgBox.exec()
    else:
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Dados Salvos!\nAluno: '+aluno+'\nInstrumento: '+
        instrumento+'\nData: '+data+'\nConteúdo: '+conteudo)
        msgBox.setWindowTitle("Registrando Aula")
        msgBox.exec()
        carregar_tabela_aulas()
        bd.registrar_aula(aluno, instrumento, conteudo)
        tela_aula.close()
    
def salvar_aluno():
    x = tela_registro_aluno.text_box_aluno.text()
    d = datetime.now().strftime("%d/%m/%Y")
    
    if (tela_registro_aluno.combo_instrumento == '' or
        x == ''):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Falta dados para salvar aluno")
        msgBox.setWindowTitle("Erro!")
        msgBox.exec()
    else:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Salvar "+x)
        msgBox.setWindowTitle("salvar")
        msgBox.exec()
        bd.cadastrar_aluno(x, d)
        tela_registro_aluno.close()
        
##def salvar_aula:
def salvar_instrumento():
    x = tela_instrumento.textbox.text()
    if (x == ''):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Não foi informado o nome do instrumento")
        msgBox.setWindowTitle("Erro Econtrado")
        msgBox.exec()
    else:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Salvo com sucesso: "+x)
        msgBox.setWindowTitle("Instrumento Cadastrado")
        msgBox.exec()
        bd.cadastrar_instrumento(x)
        tela_instrumento.close()
#### funções para excluir do banco
##def excluir_aluno:
##def excluir_aula:
##def excluir_instrumento:
def carregar_tabela_aulas():
    registro_aula = bd.buscar_registro_aulas()
    tela_aula.tableWidget.setRowCount(len(registro_aula))
    row = 0
    for x in registro_aula:
        tela_aula.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
        tela_aula.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
        tela_aula.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
        tela_aula.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
        row=row+1
def abrir_registro_aula():
    carregar_tabela_aulas()
    tela_aula.combo_instrumentos.addItems(bd.nomes_instrumentos()) 
    tela_aula.dateEdit.setMinimumDate(QDate.currentDate()) 
    tela_aula.combo_alunos.addItems(bd.nomes_alunos())
    tela_aula.show()
def abrir_tela_instrumentos():
    instrumento = tela_instrumento.textbox.text()
    tela_instrumento.show()
    print(instrumento)
def abrir_tela_registro_aluno():
    tela_registro_aluno.dateEdit.setMinimumDate(QDate.currentDate()) 
    tela_registro_aluno.combo_instrumento.addItems(bd.nomes_instrumentos())
    tela_registro_aluno.show()
def abrir_aulas_salvas():
    registro_aula = bd.buscar_registro_aulas()
    tela_aulas_salvas.tableWidget.setRowCount(len(registro_aula))
    row = 0
    for x in registro_aula:
        tela_aulas_salvas.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
        tela_aulas_salvas.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
        tela_aulas_salvas.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
        tela_aulas_salvas.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
        row=row+1
    tela_aulas_salvas.show()
app = QtWidgets.QApplication(sys.argv)
#tela menu
tela_menu = uic.loadUi('tela_menu.ui')
tela_menu.btn_registrar_aula.clicked.connect(abrir_registro_aula)
tela_menu.btn_instrumentos.clicked.connect(abrir_tela_instrumentos)
tela_menu.btn_registrar_aluno.clicked.connect(abrir_tela_registro_aluno)
tela_menu.btn_visualizar_registros.clicked.connect(abrir_aulas_salvas)
#tela instrumentos
tela_instrumento = uic.loadUi('tela_instrumento.ui')
##y = bd.nomes_instrumentos()
##z = bd.nomes_alunos()
tela_instrumento.btn_salvar.clicked.connect(salvar_instrumento)
#tela aula
tela_aula = uic.loadUi('tela_aula.ui')
tela_aula.btn_salvar.clicked.connect(salvar_aula)
#tela aulas salvas
tela_aulas_salvas = uic.loadUi('tela_aulas_salvas.ui')
#tela registro aluno
tela_registro_aluno = uic.loadUi('tela_registro_aluno.ui')
tela_registro_aluno.btn_salvar.clicked.connect(salvar_aluno)
#tela_menu.btn_visualizar_registros.clicked.connect(abrir_registros)
bd.conn.close
tela_menu.show()
app.exec_()

