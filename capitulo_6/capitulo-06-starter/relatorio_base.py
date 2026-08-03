
# # Crie acumuladores antes do laço.
# # Percorra os índices e produza o relatório.
# #loop for 
# #temos uma coleção (Produtos)
# #Vamos agir em um item  da coleção 



# # for produto in produtos:
# #     print(f"No estoque existe um: {produto}")
    


# # quero exibir números de 1 até 100 com range
# for numero in range (0,101):
#     print(f"Números: {numero}")


# # conjunto de movimentações de pix
# movimentos = [-300, 1500, -600, 400]
# entradas = 0
# saidas = 0
 
# # contar trasações do tipo SAIDA e ENTRADA.
# for movimento in movimentos:
#     if (movimento > 0):
#         print(f"Transação de ENTRADA: R$: {movimento}")
#         entradas += 1
#     else:
#         print(f"Transação de saida: R$: {movimento}")
#         saidas += 1
# print(f"Total de entradas: {entradas}")
# print(f"Total de saidas: {saidas}")


# # cursos do  senai
# cursos = ["excel", "python", "power Bi"]
# carga_horaria = [80,60,24] #Representa horas

# for i in range(len(cursos)):
#     print(f"O curso: {cursos[i]}, tem uma duração de {carga_horaria[i]} horas ")

# #loop while => enquanto a condição for verdadeira, faça:

# execultando = True
# while execultando == True :
#     escolha = input("Digite o nome do melhor jogador do mundo para sair: ").strip().lower()
#     if (escolha == "casemiro"):
#         execultando = False
    
# print(f"saimos do loop, pois a condições virou FALSE!") 


# exiba o nome e a quantidade de cada produto;
# some todas as unidades;
# conte quantos produtos estão esgotados;
# conte quantos possuem quantidade entre 1 e o estoque mínimo;
# ao final, apresente os três totais.

produtos = ["Caderno", "Caneta", "Borracha", "Lápis"]
quantidades = [10, 0, 3, 5]
estoque_minimo = 3

contador = 0 
# produtos = len(produtos)
# print(produtos)
print("==== controle de estoque ====")
for i in range (len(produtos)):
    print(f"produto: {produtos[i]} quantidade: {quantidades[i]}")
    print(30*"-")

total = 0 

for i in quantidades:
    total+=i
    print(total)

#esgotado
esgotados = 0

for i in range(len(produtos)):
    print(f"Verificando o item: {produtos[i]}...")
    print(f"quantidade: {quantidades[i]}")
    if(quantidades[i] <= 0):
        esgotados+=1
        print(30*"=")
        print(f"{produtos[i]} Está esgotado")
        print(f"temos {esgotados} produto(s) esgotado(s)")

        print(30*"=")
    elif (quantidades[i]>= 10):
        print(f"{produtos[i]} Estoque muito alto")
        print(30*"=")

    elif(quantidades[i]>0 and quantidades[i]<=3):
        print(30*"=")
        print(f"Estoque critico de {produtos[i]} quantidade: {quantidades[i]}")
        print(30*"=")

    else:
        print("dentro da média")
        print(30*"=")

# quantidades = len(quantidades)
# while quantidades < quantidades:
#     total = quantidades
#     print(quantidades)