

id_atual = 1

banco_de_dados = [{
    "id": "0",
    "nome": "Leandro",
    "curso": "Python",
    "cpf": "39877475871"
}]



def buscar_alunos(cpf):
    for aluno in banco_de_dados:
        if aluno["id"] == cpf.strip():
            print(f"Deu certo {aluno}")
            return aluno

    return None

def listar_alunos():
    for alunos in banco_de_dados:
        print(alunos)


def cadastrar_aluno(nome , curso , cpf):
    global id_atual 
    novo_aluno ={
        "id":id_atual,
        "nome": nome,
        "curso": curso,
        "cpf": cpf,
    
    }
    
    banco_de_dados.append(novo_aluno)
    id_atual +=1
    for aluno in banco_de_dados: print(aluno)
    
    
    print("Função cadastrar ")
    
    