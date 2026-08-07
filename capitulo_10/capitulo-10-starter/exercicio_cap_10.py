# carregar a lista existente;
# receber nome, categoria, preço e quantidade;
# criar um dicionário;
# acrescentá-lo à lista;
# gravar a lista inteira no mesmo JSON;
# exibir quantos produtos estão cadastrados;
# encerrar sem menu e sem repetição de cadastro.

import json

# 1. CORREÇÃO: Usar barras normais (/) no caminho do arquivo
CAMINHO_JSON = "capitulo_10/capitulo-10-starter/pecas.json"

def acrecenta_produtos():
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria: ")
    preco = float(input("Digite o preço: "))
    qtd = int(input("Digite a quantidade: "))
    
    # CORREÇÃO: Corrigido o erro de digitação "categotia" para "categoria"
    novo_item = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": qtd
    }
    return novo_item

# 2. CORREÇÃO: Tenta abrir o arquivo existente. Se não existir, cria uma lista vazia.
try:
    with open(file=CAMINHO_JSON, mode="r", encoding="utf-8") as arquivo:
        hardware = json.load(arquivo)
        print("Arquivo carregado com sucesso.")
except (FileNotFoundError, json.JSONDecodeError):
    hardware = []
    print("Arquivo não encontrado ou vazio. Criando nova lista.")

# 3. CORREÇÃO: Pega o produto digitado pelo usuário APENAS UMA VEZ
novo_produto = acrecenta_produtos()

# 4. CORREÇÃO: Adiciona o novo produto à lista que veio do arquivo JSON
hardware.append(novo_produto)

# 5. CORREÇÃO: Salva a lista completa (com o novo item) de volta no arquivo
with open(file=CAMINHO_JSON, mode="w", encoding="utf-8") as arquivo:
    json.dump(hardware, arquivo, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso no arquivo JSON!")
