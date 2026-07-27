produtos = ["Caderno", "Caneta", "Borracha", "Lápis"]
quantidades = [10, 0, 3, 5]
estoque_minimo = 3

# Crie acumuladores antes do laço.

# Percorra os índices e produza o relatório.

#loop for 

#temos uma coleção (Produtos)
#Vamos agir em um item  da coleção 



for produto in produtos:
    print(f"No estoque existe um: {produto}")
    


# quero exibir números de 1 até 100 com range
for numero in range (0,101):
    print(f"Números: {numero}")


# conjunto de movimentações de pix
movimentos = [-300, 1500, -600, 400]
entradas = 0
saidas = 0
 
# contar trasações do tipo SAIDA e ENTRADA.
for movimento in movimentos:
    if (movimento > 0):
        print(f"Transação de ENTRADA: R$: {movimento}")
        entradas += 1
    else:
        print(f"Transação de saida: R$: {movimento}")
        saidas += 1
print(f"Total de entradas: {entradas}")
print(f"Total de saidas: {saidas}")


# cursos do  senai
cursos = ["excel", "python", "power Bi"]
carga_horaria = [80,60,24] #Representa horas

for i in range(len(cursos)):
    print(f"O curso: {cursos[i]}, tem uma duração de {carga_horaria[i]} horas ")