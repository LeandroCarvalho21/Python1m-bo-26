def mostrar_menu():
    print("\n=======Opções=======\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair \n")

def somar(a,b):
    calculo = a+b
    return calculo

def sub(a,b):
    calculo = a-b
    return calculo

def mult(a,b):
    calculo = a*b
    return calculo

def div(a,b):
    calculo = a/b
    return calculo


def main():
    resposta = ''
    while resposta != '0':
        mostrar_menu()
        resposta = input("Escolha uma opção: ")
        if (resposta =='1' ):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado_da_calculadora = somar(num1,num2)
            print(F"A Adilção de {num1} + {num2} = {resultado_da_calculadora}")
            
        elif(resposta == '2'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado_da_calculadora = sub(num1,num2)
            print(F"A Subtração de {num1} - {num2} = {resultado_da_calculadora}")
            
        elif(resposta == '3'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado_da_calculadora = mult(num1,num2)
            print(F"A Multiplicação de {num1} * {num2} = {resultado_da_calculadora}")
            
        elif(resposta == '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado_da_calculadora = div(num1,num2)
            print(F"A Divisão de {num1} / {num2} = {resultado_da_calculadora}")
            
        elif(resposta == '0'):
            print(F"Saindo do sistema!")
            
        else:
            print ("Opção errada, tente novamente...")
   

main()