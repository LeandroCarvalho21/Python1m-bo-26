def mostrarMenu():
    print ("**** CALCULADORA ****")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("3 - Divisão")
    print ("0 - Sair")

def somar(a, b):
    return a + b


def main():
    resposta = ''
    while resposta != '0':
        mostrarMenu()
        resposta = input ('Escolha uma opção: ')
        if resposta == '1':
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            resultado = somar(numero1, numero2)
            print (f"A soma dos números digitado é: {resultado}")
        elif resposta == '2':
            print ("Calculando uma subtração...")
        elif resposta == '3':
            print ("Calculando uma divisão...")
        elif resposta == '4':
            print ("Calculando uma multiplicação...")
        elif resposta == '0':
            print ("Saindo do sistema!")
        else:
            print ("Opção errada, tente novamente...")

main()