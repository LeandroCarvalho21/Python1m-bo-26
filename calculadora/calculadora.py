#importando o modulo matematica com todas as funções
from matematica import *
import os
from colorama import init, Fore,Style

init(autoreset=True)

#importando modulo matematica e para usar preciso colocar matematica.nome_da_função 
#exemplo matematica.soma(num1, num2)
# import matematica

def mostrar_menu():
    print(f"\n {Fore.GREEN} =======Opções=======\n{Fore.RED} 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Pares\n 6 - impares \n 0 - Sair \n ")
    
def pedir_numeros():    
    num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: ")) 
    return num1, num2

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

def pause():
    input(f"{Fore.YELLOW}ENTER para continuar...")


def main():
    resposta = ''
    while resposta != '0':
        mostrar_menu()
        resposta = input("Escolha uma opção: ")
        if (resposta =='1' ):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = somar(num1,num2)
            limpar_tela()   
            print(F"{Style.BRIGHT} A Adilção de {num1} + {num2} = {resultado_da_calculadora}")
            pause()
        elif(resposta == '2'):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = sub(num1,num2)
            limpar_tela()   
            print(F"A Subtração de {num1} - {num2} = {resultado_da_calculadora}")
            pause()
            
        elif(resposta == '3'):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = mult(num1,num2)
            limpar_tela()   
            print(F"A Multiplicação de {num1} * {num2} = {resultado_da_calculadora}")
            pause()
            
        elif(resposta == '4'):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = div(num1,num2)
            limpar_tela()   
            print(F"A Divisão de {num1} / {num2} = {resultado_da_calculadora}")
            pause()
            
        elif(resposta == '5'):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = pares(num1,num2)
            limpar_tela()   
            for i in resultado_da_calculadora:
                print(f"Número par: {Fore.GREEN} {i}")
            pause()
            
        elif(resposta == '6'):
            num1,num2 = pedir_numeros()
            resultado_da_calculadora = impar(num1,num2)
            limpar_tela()
            for i in resultado_da_calculadora:
                print(f"Número impar:{Fore.RED} {i}")   
            pause()
            
        elif(resposta == '0'):
            print(F"Saindo do sistema!")
            
        else:
            print ("Opção errada, tente novamente...")
            pause()
main()