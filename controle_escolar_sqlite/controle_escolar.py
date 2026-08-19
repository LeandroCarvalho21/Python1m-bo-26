from colorama import init, Fore
init(autoreset=True)
import os
from alunos import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(f"{Fore.MAGENTA}======Controle Escolar======")
    print(f"{Fore.YELLOW} 1 - Listar Alunos \n 2 - Cadastrar Alunos \n 3 - Excluir Alunos \n 4 - Atualizar Alunos\n 5 - Alunos Aprovados\n 6 - Alunos Reprovados\n 7 - Situação do aluno\n 0 - Sair \n ")
 
def pause():
    input(f"{Fore.YELLOW}ENTER para continuar...") 
  

def main():
    mostrar_menu()
    opcao = input("Digite uma opção: ").strip()
      
    if (opcao == "1"):
        listar_alunos()
        pause()
                  
    elif (opcao == "2"):
        nome = input("Digite seu Nome: ").upper()
        curso = input("Digite seu curso: ").upper()
        nota1 = input("Digite a Nota 1: ")
        nota2 = input("Digite a Nota 2: ")
        # if (nota1 <= 10 and nota2 <= 10)  
        cadastrar_aluno(nome,curso, nota1 , nota2)
        print("Aluno cadastrado com sucesso")
        pause()
       
    elif (opcao == "3"):
        id_atual = input("Digite o id do aluno para excluir: ").strip()
        excluir(id_atual)
        pause()
       
    elif (opcao == "4"):
        id_atual = input("Digite o id do aluno para atualizar: ").strip()
        aluno_encontrado= buscar_aluno(id_atual)
        if aluno_encontrado:
            nome = input("Digite o nome do aluno atualizado: ").strip().upper()
            curso = input("Digite seu curso: ").strip().upper()
            nota1 = input("Digite a Nota 1: ").strip()
            nota2 = input("Digite a Nota 2: ").strip()
            atualizando_aluno(id_atual, nome, curso, nota1,nota2)
            print("Aluno atualizado com sucesso!!!")
        else:
            print("Aluno não encontrado!!!")
            
        pause()
          
    elif (opcao == "5"):
        aprovados()
        pause()
    elif (opcao == "6"):
        reprovados()
        pause()
    
    elif (opcao == "7"):
        nome = input("Digite o nome do aluno: ").upper()
        situacao(nome)
        pause()

        
    elif (opcao == "0"):
        print(f"opção {opcao} Saindo do sistema\n")
        exit(0)
         
    else:
        print(f"{Fore.RED}Opção errada, tente novamente...\n")
    
            
        
    main()
main()