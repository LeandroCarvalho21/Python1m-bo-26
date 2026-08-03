produto = {
    "nome": "Caderno",
    "preco": 8.50,
    "quantidade": 12,
    "ativo": True,
    "categoria":["Material escolar"],
    "fornecedor": {"nome": "Carvalho papeis"
                   ,"cidade": "Aluminio"}
}

# Consulte, altere e complete o registro durante a prática.
print(produto.get("nome"))
print(produto.get("preco"))
print(f"o poduto é: {produto.get('nome')} e o preço é: {produto.get('preco')}")

#alterando qual quer valor do dicionario 
produto["preco"] = 16
produto["desconto"] = 0,17 # porcetagem 
print(produto)


#zerar tudo 
# produto.clear

#remove uma chave do dicionario 
# del produto["categoria"]

for chave, valor in produto.items():
    print(80*"=")
    print(f"a chave é: {chave} e o valor é: {valor}")
    
print(produto["fornecedor"]["nome"])
print(produto.get("fornecedor").get("nome"))
#keys() => apenas chaves
#values() => apenas valores
#items() => tudo, porém precisa de duas variaveis 


garagem = [
    {"modelo":"jetta",
     "cor": "preta",
     "km": 22000},

     {"modelo": "kombi",
      "cor": "Verde abacate",
      "km": 70000},
    
     {"modelo": "gol",
      "cor": "azul",
      "km": 200000},
]

frutas =["banana", "chocolate", "goiaba"]

print(garagem[0])
print(garagem[1])
print(garagem[2].get("modelo"))

print(80*"=")


for carro in garagem:
    print(carro.get("modelo"))


# for i in produto:
#     print(f"key: {i} e valeu: {i}" )
    

