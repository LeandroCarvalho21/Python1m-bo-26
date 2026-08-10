# def calculadora(opcao):
#     if (opcao >=0 and opcao<=4):
#         num1 = int(input("Digite o primeiro número: "))
#         num2 = int(input("Digite o segundo número: "))
#         if (opcao ==1 ):
#             calculo = num1+num2
#             print(F"A Adilção de {num1} + {num2} = {calculo}")
#         elif(opcao == 2):
#             calculo= num1-num2
#             print(F"A Subtração de {num1} - {num2} = {calculo}")
#         elif(opcao == 3):
#             calculo = num1*num2
#             print(F"A Multiplicação de {num1} * {num2} = {calculo}")
#         elif(opcao == 4):
#             calculo = num1/num2 
#             print(F"A Divisão de {num1} / {num2} = {calculo}")
#         else:
#             print(f"o número {opcao} é invalido ")
#     else:
#         print("Digite um número valido \n")

# print("=======Opções=======\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")
# opcao = int(input("Digite qual opção "))
# calculadora(opcao)

def mostrar_menu():
    print("\n=======Opções=======\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair ")

def somar(a,b):
    calculo = a+b
    return calculo

def main():
    resposta = ''
    mostrar_menu()
    while resposta != '0':
        resposta = input("Escolha uma opção: ")
        if resposta >='0' and resposta<='4':
            if (resposta =='1' ):
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                somar(num1,num2)
                # calculo = num1+num2
                print(F"A Adilção de {num1} + {num2} = {calculo}")
            elif(resposta == '2'):
                calculo= num1-num2
                print(F"A Subtração de {num1} - {num2} = {calculo}")
            elif(resposta == '3'):
                calculo = num1*num2
                print(F"A Multiplicação de {num1} * {num2} = {calculo}")
            elif(resposta == '4'):
                calculo = num1/num2 
                print(F"A Divisão de {num1} / {num2} = {calculo}")
            elif(resposta == '0'):
                print(F"Saindo do sistema!")
        else:
            print(f"Opção errada tente novamente")
    

main()