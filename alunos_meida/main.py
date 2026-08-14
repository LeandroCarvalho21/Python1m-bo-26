from alunos import *

def pause():
    input("precione o Enter para continuar...")

def mostrar_menus():
    print(" 1 - Listar alunos\n 2 - Cadastrar aluno\n 3 - Excluir aluno\n 4 - Atualizar aluno\n 5 - Alunos Aprovados\n 6 - Alunos Reprovados\n 0 - Sair ")
   
    
def main():
    mostrar_menus()
    opcao = input ("Digite uma opção: ")
    
    if (opcao == "1"):
        listar_alunos()

    elif (opcao == "2"):
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        cpf = input("Digite o cpf do aluno: ")
        cadastrar_aluno(nome , curso, cpf)

    
    
main()