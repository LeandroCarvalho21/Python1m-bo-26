import sqlite3

CAMINHO_BANCO = 'escola.db'

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def create_table():
    conexao = conectar()
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso TEXT NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()
    
create_table()        

def listar_alunos():
    conexao = conectar()
    alunos = conexao.execute('SELECT * FROM alunos').fetchall()
    conexao.close()
    print(f'{"ID":^5} | {"NOME":^15} | {"CURSO":^15} | {"NOTA 1":^15} | {"NOTA 2":^15}')
    print(76*'-')
    for aluno in alunos:
        print(f'{aluno["id"]:^5} | {aluno["nome"]:^15} | {aluno["curso"]:^15} | {aluno["nota1"]:^15} | {aluno["nota2"]:^15}')

def cadastrar_aluno(nome, curso, nota1 , nota2):
    conexao = conectar()
    conexao.execute('''
        INSERT INTO alunos (nome, curso, nota1, nota2)
        VALUES(?,?,?,?)
        ''', (nome, curso, nota1 , nota2))
    conexao.commit()
    conexao.close()
    
def buscar_aluno(id):
    conexao = conectar()
    aluno = conexao.execute('SELECT * FROM  alunos WHERE id= ?', id).fetchall()
    conexao.close()
    return aluno
   
def excluir(id):
    aluno_encontrado  = buscar_aluno(id)
    if aluno_encontrado:
        conexao = conectar()
        conexao.execute('DELETE FROM alunos WHERE id = ?', id)
        conexao.commit()
        conexao.close()
        print("Aluno excluido com sucesso!!!")
    else:
        print("Aluno não cadastrado!!!")
        
def atualizando_aluno(id_atual, nome, curso, nota1,nota2):
    conexao = conectar()
    conexao.execute('''
        UPDATE alunos
        SET nome = ?, curso = ?, nota1 = ?, nota2 = ? WHERE id = ?                   
        ''',(nome,curso,nota1,nota2,id_atual))
    conexao.commit()
    conexao.close()
    
def aprovados():
    # Puxando alunos aprovados com comando python.
    conexao = conectar()
    alunos = conexao.execute("SELECT * FROM alunos").fetchall()
    conexao.close()
    for aluno in alunos:
        media = (float(aluno["nota1"]) + float(aluno["nota2"]))/2
        if (media >= 5 ):
            print(f"{aluno['nome']} aprovado com média: {media} ")
   
    
    # Puxando alunos aprovados com comando SQL, execultando no servidor do DB
    
    # conexao = conectar()
    # alunos = conexao.execute('''
    #   SELECT nome, nota1, nota2, (nota1 + nota 2) / 2 AS media 
    #   FROM alunos 
    #   WHERE media >= 5
    #   OREDER BY media DESC
    #   ''').fetchall()
    # conexao.close()
    # for aluno in alunos:
    #     print("aluno['nome'], aluno [media]  ")
   
    
def reprovados():
    conexao = conectar()
    alunos = conexao.execute("SELECT * FROM alunos").fetchall()
    conexao.close()
    for aluno in alunos:
        media = (float(aluno["nota1"]) + float(aluno["nota2"]))/2
        if (media < 5):
            print(f"{aluno['nome']} reprovado com média: {media} ")

def situacao(nome):
    conexao = conectar()
    aluno = conexao.execute("SELECT * FROM ALUNOS WHERE nome = ? ",(nome,)).fetchone()
    conexao.close()
    print(f" Aluno: {aluno['nota1']}\n Curso: {aluno['curso']}\n ")
    
    
            

    
                        
        
            
              
                    
                    