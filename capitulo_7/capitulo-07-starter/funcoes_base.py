# calcular_custo(quantidade, preco_unitario), que retorna o produto dos valores;
# classificar_estoque(quantidade, estoque_minimo), que retorna uma classificação;
# exibir_resumo(nome, quantidade, custo, situacao), que apresenta os dados;
# use os dados fornecidos no arquivo para chamar as três funções.
# Mantenha cálculo, decisão e apresentação em funções diferentes.

# Complete estas funções durante a prática acompanhada.
def calcular_custo(quantidade_produto : int, preco_produto: float):
    print(f"execultando a função com os valores {quantidade_produto } e {preco_produto}")
    return quantidade_produto *preco_produto

def classificar_estoque(quantidade_produto: int, minimo_produto:int):
    if (quantidade_produto<= minimo_produto):
        print("Estoque crintico")
        return "critico"
    else:
        print("Estoque normal")
        return "Normal"

def exibir_resumo(nome, quantidade, custo, situacao):
    print(f"Produto: {nome}")
    print(f"quantidade: {quantidade}")
    print(f"Custo total: {custo}")
    print(f"Situação do estoque: {situacao}")
#--------------------------------------------------------------------------------

nome_produto = "Caderno"
quantidade_produto = 3
preco_produto = 8.50
minimo_produto = 5

calcular_custo(quantidade_produto , preco_produto)
classificar_estoque(quantidade_produto, minimo_produto)
exibir_resumo(nome_produto, quantidade_produto, preco_produto, minimo_produto)
# Chame as funções e apresente o resumo.


# # função simples
# def exibir_cabecalho():
#     print(60*"=")
#     print("--------Bem vindo ao gerenciador de Estoque--------")
#     print(60*"=")


# exibir_cabecalho()
# #--------------------------------------------------------------------------------
# # função com parametro
# produtos = ["Copo","Prato","Travessa","Xícara"]
# produtos
# def exibir_produtos(nome):
#     if nome in produtos:
#         print(60*"=")
#         print("--------Bem vindo ao gerenciador de Estoque--------")
#         print(f"Esse é produto {nome.lower()} e tem as seguintes características:")
#         print(60*"=")
#     else:
#         print(60*"=")
#         print(f"Desculpe não temos {nome.lower()}")
#         print(60*"=")

# exibir_produtos("Prato")
# #--------------------------------------------------------------------------------
# # função com return
# def ficar_milionario():
#     return 1000000

# ficar_milionario ()
# saldo = ficar_milionario()

# print(f"Seu saldo agora é de R$: {saldo}")
# #--------------------------------------------------------------------------------
# # função com return
# def calcular_idade(ano_nascimento):
#     ano_atual = 2026
#     return ano_atual- ano_nascimento
    
# print(f"Você tem: {calcular_idade(1993)} anos")


