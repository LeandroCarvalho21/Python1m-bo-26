# Crie resumo_produto.py com as funções:

# calcular_valor_estoque(quantidade, preco): retorna o valor total;
# classificar_estoque(quantidade, minimo): retorna inválido, esgotado, crítico ou adequado;
# exibir_resumo(nome, quantidade, valor, situacao): apresenta os dados.
# Depois:

# receba nome, quantidade, preço e mínimo;
# chame as funções;
# apresente o resumo;
# teste os quatro caminhos da classificação.
# Não use módulos, dicionários ou inteligência artificial.

def calcular_valor_estoque(quantidade, preco):
    total = quantidade*preco
    print(f"Valor do estoque: {total}")
    return total

def classificar_estoque(quantidade, minimo):
    if (quantidade > 5 and quantidade <=10):
        print(f"Estoque adequador: {quantidade}")
        return "adequado"
    elif(quantidade >= 1 and quantidade<=5):
        print(f"Estoque critico: {quantidade}")
        return "critico"
    elif(quantidade < minimo):
        print(f"Estoque esgotado: {quantidade}")
        return "esgotado"
    else:
        print("Estoque invalido")
        return "invalido"


def exibir_resulmo (nome, qtd, valor , situacao):
    print(80*"=")
    print(f"Nome do produto: {nome}")
    print(f"quantidade: {qtd}")
    print(f"Valor do produto: {valor}")
    print(f"Situação do estoque: {situacao}")
    print(80*"=")
    

produto = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))
qtd_minima = 1

valor_total_estoque = calcular_valor_estoque(qtd,preco)
situacao = classificar_estoque(qtd,qtd_minima)
exibir_resulmo(produto,qtd,valor_total_estoque, situacao)

