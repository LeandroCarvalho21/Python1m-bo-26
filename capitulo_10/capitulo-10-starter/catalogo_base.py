import json

# Complete a leitura, alteração e gravação durante a prática.
novo_produto = {
    "nome": "Borracha",
    "categoria": "Papelaria",
    "preco": 2.50,
    "quantidade": 8,
}

with open (file="meu_arquivo.txt", mode="w", encoding="utf-8") as arq:
    arq.write("Escrevi e sai correndo!")
    print("oi")

with open (file="amigos.txt", mode="r", encoding="utf-8") as familia:
    nome_da_familia = familia.readlines()# le a primeira linha
    nome_da_familia = familia.read()# le a todas as linhas
    print(nome_da_familia)

# salvar um dicionario em um formato NÃO JSON,
#precisamos serializar o dicionario em um formato de texto
with open (file="produto.txt", mode="w", encoding="utf-8") as item:
    for chave, valor in novo_produto.items():
        item.write(f"{chave} {valor}\n")

#salvar um dicionario em JSON, toda serialização feita automaticamente
with open (file="produto.json", mode="w", encoding="utf-8") as item_json:
    json.dump(novo_produto, item_json, indent=4)
    
with open (file="capitulo_10/capitulo-10-starter/produtos.json", mode="r", encoding="utf-8") as ler_produtos:
    produtos = json.load(ler_produtos)
    print(produtos)

