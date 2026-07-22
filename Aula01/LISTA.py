#Criando uma lista de modelos de carros 
carros = ["gol","corsa","parati","fit","asx","fox"]
print(f"Carro na primeira vaga: {carros[0]}")

#Trocar o elemento do indice 0 "gol" por "Gol AP"
carros[0]= "Gol AP"
print(f"Carro na primeira vaga: {carros[0]}")

#Munipulação de listas(aumentar ou diminuir ou zerar)
#o \n no final do input  serve para quebrar uma linha 
novo_carro= str(input("Qual carro você deseja por na garagem\n"))
carros.append(novo_carro)
print(f"seu novo carro é um: {novo_carro}")
print(carros)

remover_carro=input("Qual carro você quer tirar da garagem\n")
#se o carro não existir vai gerar erros 
#verificar se o carro esta na lista
if (remover_carro in carros):
    carros.remove(remover_carro)
    print(f"você removeu o carro: {remover_carro}")
    print(carros)

#verificar se o carro esta na lista
if ("parati" in carros):
    print("parati está na garagem.")
else:
    print("parati não esta na garagem.")