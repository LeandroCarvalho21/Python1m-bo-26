# percorrer todos os produtos;
# exibir os campos principais;
# calcular o valor de cada item em estoque;
# classificar como esgotado, crítico ou adequado;
# somar o valor total do catálogo;
# contar quantos produtos exigem reposição.
import time

produtos = [
    {"nome": "Caderno", "categoria": "Papelaria", "preco": 8.50, "quantidade": 10, "estoque_minimo": 3},
    {"nome": "Caneta", "categoria": "Papelaria", "preco": 3.20, "quantidade": 0, "estoque_minimo": 5},
    {"nome": "Sabonete", "categoria": "Higiene", "preco": 4.00, "quantidade": 2, "estoque_minimo": 4},
    {"nome": "Café", "categoria": "Alimentos", "preco": 18.00, "quantidade": 6, "estoque_minimo": 2},
]

contador = 0
total = 0
produtos_reposicao = []

#Percorre todos os produtos
print(100*"=")
print("------------percorre todos os produtos------------")
for i in produtos:
    print(i)
    time.sleep(1)

#exibe os principais campos
print(80*"=")
print("------------exibe os principais campos------------")
for produto in produtos:
    nome = produto.get("nome")
    preco = produto.get("preco")
    quantidade = produto.get("quantidade")
    print(f"Nome: {nome} | preço: {preco} | quantidade: {quantidade}") 
  
# calcular o valor de cada item em estoque;
print(80*"=")
print("------------Valor total de cada produto------------")
for item in produtos:
    nome = item.get("nome")
    quantidade = item.get("quantidade")
    preco = item.get("preco")
    total_de_cada_produto = quantidade*preco
    print(f"Valor total do {nome} R$:{total_de_cada_produto}")

# classificar como esgotado, crítico ou adequado;
print(80*"=")
print("------------esgotado, crítico ou adequado------------")
for item in produtos:
    quantidade = item.get("quantidade")
    qtd_minimo = item.get("estoque_minimo")
    nome = item.get("nome")
        
    if(quantidade<=0):
        print(f"O produto {nome} está esgotado")
    elif(quantidade >= 1 and quantidade <= qtd_minimo):
        print(f"o estoque de {nome} está critico")
    else:
        print(f"o estoque de {nome} está adequado")
            
# somar o valor total do catálogo;
print(80*"=")
print("------------valor total do catálogo------------")
for item in produtos:
    total += item.get("quantidade")* item.get("preco")
print(f"Total R$:{total}")

# contar quantos produtos exigem reposição
print(80*"=")
print("------------contar quantos produtos exigem reposição------------")
for item in produtos:
    nome = item.get("nome")
    estoque_minimo = item.get("estoque_minimo")
    quantidade = item.get("quantidade")
    if (quantidade< estoque_minimo):
        contador +=1
        produtos_reposicao.append(nome)
      
print(f"Quantidade de produtos para repor: {contador} ")
print(80*"=")
print("------------Repor------------")
for reposicao in produtos_reposicao:
    print(f"repor o produto {reposicao}")


