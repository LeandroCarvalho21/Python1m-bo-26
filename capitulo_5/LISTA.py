# #Criando uma lista de modelos de carros 
# carros = ["gol","corsa","parati","fit","asx","fox"]
# print(f"Carro na primeira vaga: {carros[0]}")

# #Trocar o elemento do indice 0 "gol" por "Gol AP"
# carros[0]= "Gol AP"
# print(f"Carro na primeira vaga: {carros[0]}")

# #Munipulação de listas(aumentar ou diminuir ou zerar)
# #o \n no final do input  serve para quebrar uma linha 
# novo_carro= str(input("Qual carro você deseja por na garagem\n"))
# carros.append(novo_carro)
# print(f"seu novo carro é um: {novo_carro}")
# print(carros)

# remover_carro=input("Qual carro você quer tirar da garagem\n")
# #se o carro não existir vai gerar erros 
# #verificar se o carro esta na lista
# if (remover_carro in carros):
#     carros.remove(remover_carro)
#     print(f"você removeu o carro: {remover_carro}")
#     print(carros)

# #verificar se o carro esta na lista
# if ("parati" in carros):
#     print("parati está na garagem.")
# else:
#     print("parati não esta na garagem.")

playlist = ["Vídeo de marcenaria ", "Vídeo de culinaria ", "Vídeo de programação"]
print(playlist)
playlist.sort()
print(playlist)
print("="*100)


material_escolar = ["Caderno"]
print(f"material escolar: {material_escolar}")
print("="*80)
print(""*80)

material = input("Digite o nome do material escolar: ")
material_escolar.append(material)
print(f"material escolar adicionado a lista: {material_escolar}")
print("="*80)
print(""*80)

material_escolar.insert(1,"lapis")
print(f"lapis no indice 1: {material_escolar}")
print("="*80)
print(""*80)

material_escolar[0]= "Caderno universitário"
print(f"Alterando nome indice 0: {material_escolar}")
print("="*80)
print(""*80)

if "Caneta" in material_escolar:
    material_escolar.remove("Caneta")
    print(f"Item removido da lista")
else:
    print(f"Não, possui o item Caneta na lista de material")

material_escolar.sort
print(f"Organizando: {material_escolar}")

print(f"Exibindo o primeiro item da lista e o ultimo e a coleção final: {material_escolar[0], material_escolar[-1], material_escolar}")

