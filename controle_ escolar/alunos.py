from colorama import init, Fore
init(autoreset=True)

    # "nota1": 5,
    # "nota2": 5},
id_atual= 5

banco_de_dados= [
    {
    'id': '1',
    'nome': 'ana',
    'curso': 'python',
    'nota1': 5,
    'nota2': 7
    },
    
    {
    'id': '2',
    'nome': 'hugo',
    'curso': 'js',
    'nota1': 10,
    'nota2': 7
    }
    
    ]
 
def buscar_aluno_id(id):
    for aluno in banco_de_dados:
        if aluno ['id'] == id.strip():
            return aluno
    return None
            
def listar_alunos():
    print(f"{Fore.GREEN}{'===Lista de Alunos===':^40}\n")
    print(f" {Fore.CYAN}  {'ID' :^10} | {'NOME':^10} | {'CURSO':^10} | {'Nota 1':^10} | {'Nota 2':^10}")
    print(40*"=")
    for aluno in banco_de_dados:
        print(f"{aluno['id'] :^10} | {aluno['nome']:^10} | {aluno['curso']:^10} | {'Nota 1':^10} | {'Nota 2':^10}")
        print(40*"-")
    
def cadastrar_aluno(nome , curso , nota1 , nota2):
    print(f"{Fore.GREEN}===Cadastrar Aluno===")
    global id_atual
    novo_aluno = {
        'id': id_atual,
        'nome': nome,
        'curso': curso,
        'nota1': nota1,
        'nota2': nota2
         }
    banco_de_dados.append(novo_aluno)
    id_atual += 1
    for aluno in banco_de_dados: print(aluno)
          
def excluir_aluno(id):
    print(f"{Fore.GREEN}===Excluir Aluno===")
    aluno_encontrado = buscar_aluno_id(id)
    if aluno_encontrado:
        banco_de_dados.remove(aluno_encontrado)
    else:
        print("Aluno nãocadastrado!!!")

def atualizando_aluno(id,nome):
    print(f"{Fore.GREEN}===Atualizar Aluno===")
    aluno_encontrado = buscar_aluno_id(id)
    novo_dado = {'nome': nome}
    if aluno_encontrado:
        aluno_encontrado.update(novo_dado)
    else:
        print("Aluno não cadastrado")
        
def aprovados():
    for aluno in banco_de_dados:
        media = (float(aluno ['nota1'])+ float(aluno ['nota2'])) / 2
        if media >= 5:
            return aluno , media
            # print(f"{aluno['nome']} Média: {media}")
       
        
def reprovado():
    for aluno in banco_de_dados:
        media = (float(aluno ['nota1'])+ float(aluno ['nota2'])) / 2
        if media < 5:
            print(f"{aluno ['nome']} Média: {media}")
        