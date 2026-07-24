# 1. Entrada de dados
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))
quantidade_por_caixa = int(input("Digite quantas unidades cabem em cada caixa: "))

# 2. Cálculos
custo_total = quantidade * preco_unitario
caixas_completas = quantidade // quantidade_por_caixa

# CORREÇÃO: O operador '%' pega o resto (as unidades que sobraram)
fora_da_caixa = quantidade % quantidade_por_caixa

# 3. Resumo Organizado
print("\n" + "="*30)
print(f" RESUMO DA COMPRA: {nome_produto.upper()} ")
print("="*30)
print(f"• Custo total: R$ {custo_total:.2f}")
print(f"• Caixas completas preenchidas: {caixas_completas}")
print(f"• Unidades que ficaram fora das caixas: {fora_da_caixa}")
print("="*30)
