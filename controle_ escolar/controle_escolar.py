from colorama import init, Fore
init(autoreset=True)
import os
from alunos import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(f"{Fore.MAGENTA}======Controle Escolar======")
    print(f"{Fore.YELLOW} 1 - Listar Alunos \n 2 - Cadastrar Alunos \n 3 - Excluir Alunos \n 4 - Atualizar Alunos\n 5 - Alunos Aprovados\n 6 - Alunos Reprovados\n 0 - Sair \n ")
 
def pause():
    input(f"{Fore.YELLOW}ENTER para continuar...") 
  

def main():
    mostrar_menu()
    opcao = input("Digite uma opção: ")
    
    
    if (opcao == "1"):
        listar_alunos()
        pause()
                  
    elif (opcao == "2"):
        cadastrar = input("Digite seu Nome: ")
        curso = input("Digite seu curso: ")
        nota1 = input("Digite a Nota 1: ")
        nota2 = input("Digite a Nota 2: ")
        cadastrar_aluno(cadastrar,curso, nota1 , nota2)
        print("Aluno cadastrado com sucesso")
        pause()
       
    elif (opcao == "3"):
        id_atual = input("Digite o id do aluno para excluir: ")
        excluir_aluno(id_atual)
        pause()
       
    elif (opcao == "4"):
        id_atual = input("Digite o id do aluno para atualizar: ")
        nome_aluno = input("Digite o nome do aluno atualizado: ")
        atualizando_aluno(id_atual, nome_aluno)
        pause()
    elif (opcao == "5"):
        aprovados()
        pause()
    elif (opcao == "6"):
        reprovado()
        pause()

        
    elif (opcao == "0"):
        print(f"opção {opcao} Saindo do sistema\n")
        exit(0)
         
    else:
        print(f"{Fore.RED}Opção errada, tente novamente...\n")
    
            
        
    main()
main()