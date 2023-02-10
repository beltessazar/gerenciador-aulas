import mysql.connector
import sqlite3
import datetime
try:
        conn = sqlite3.connect('gerenciador_aulas.bd')
except Error as e:
        print(e)
cursor = conn.cursor()
##iniciando tabelas caso não existam
cursor.execute ('''CREATE TABLE IF NOT EXISTS aluno
                        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_registro DATE)
                ''')
cursor.execute ('''CREATE TABLE IF NOT EXISTS instrumento
                        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL)
                ''')
cursor.execute ('''CREATE TABLE IF NOT EXISTS registro_aula
                        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome_aluno TEXT NOT NULL,
                        instrumento TEXT NOT NULL,
                        descricao_aula TEXT NOT NULL,
                        data DATE)
                ''')

print(conn)
print(cursor)


## inserts
def cadastrar_instrumento(x):
        cursor.execute("INSERT INTO instrumento (nome) VALUES (?)", (x,))
        conn.commit()
def registrar_aula(nome, instrumento, descricao):
        cursor.execute("""INSERT INTO registro_aula(nome_aluno,instrumento, descricao_aula) VALUES (?, ?, ?)""", (nome, instrumento, descricao,))
        conn.commit()
def cadastrar_aluno(nome, data):
        cursor.execute("INSERT INTO aluno (nome, data_registro) VALUES (?, ?)", (
                nome, data))
        conn.commit()
## selects
def buscar_alunos():
    return tuple(cursor.execute("""
    SELECT * FROM aluno;
    """))
def buscar_instrumentos():
    return tuple(cursor.execute("""
    SELECT * FROM instrumento;
    """))
def buscar_registro_aulas():
    return tuple(cursor.execute("""
    SELECT * FROM registro_aula;
    """))
def nomes_instrumentos():
    lista = []
    x  = tuple(cursor.execute("""
    SELECT nome FROM instrumento;
    """))
    for i in range(len(x)):
        lista.append(x[i][0])
    return lista
def nomes_alunos():
    lista = []
    x  = tuple(cursor.execute("""
    SELECT nome FROM aluno;
    """))
    for i in range(len(x)):
        lista.append(x[i][0])
    return lista
##print(type(nomes_instrumentos()))
##print(nomes_instrumentos())
##print(nomes_alunos())
##cadastrar_instrumento('Cavaco')
##y = buscar_alunos()
##registrar_aula("João", "Cavaquinho", "Ler livro 1", '05-05-1990')
##print(buscar_instrumentos())
##z = buscar_registro_aulas()
##print(buscar_registro_aulas())

#conn.close()
##try:
##    mydb = mysql.connector.connect(
##        host="69.49.241.17",
##        user="mont4629",
##        password="u560u5PsUu",
##        database="mont4629_stm"
##    )
##
##    mycursor = mydb.cursor()
##
##    def inserir(tipo_servico, valor_servico, data_servico):
##        sql_insert = """INSERT INTO servicos (id, tipo_servico, valor, data)
##                        VALUES (%s,%s,%s,%s)"""
##        val = (0, tipo_servico, valor_servico, data_servico)
##        mycursor.execute(sql_insert, val)
##        return val
##    def select_all():
##        mycursor.execute("SELECT * FROM servicos")
##        resultado = mycursor.fetchall()
##        return resultado
##
##    mydb.commit()
##
##    # print(inserir(1, 666, "2020-05-05"))
##    # print(select_all())
##    # print(mycursor.rowcount, "OK")
##    # print("Executado antes")
##except:
##    print("SERVIDOR DESLIGADO! :(")
x = datetime.datetime.now().strftime("%d/%m/%Y")
print(x)

