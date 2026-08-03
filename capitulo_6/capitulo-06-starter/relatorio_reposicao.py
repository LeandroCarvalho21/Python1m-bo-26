# ========Requisitos=============
# O programa deverá:

# exibir cada produto e sua quantidade;
# classificar cada item como esgotado, crítico ou adequado;
# somar todas as unidades;
# contar itens esgotados, críticos e adequados;
# exibir o resumo somente depois do laço.

import streamlit as st

st.title("Olá, Mundo!")
st.write("Meu primeiro aplicativo com Streamlit funcionando.")







produtos = ["Caderno", "Caneta", "Borracha", "Lápis", "Régua"]
quantidades = [10, 0, 3, 7, 1]
estoque_minimo = 3

item_adequado = 0
item_criticos = 0
item_esgotados = 0

soma_adequado= 0
produtos_escola={"material", "quantidade"}

for i in range (len(produtos)):
    print(f"Produto {produtos[i]} Quantidade: {quantidades[i]}")
    print(30*("="))

    if quantidades[i]>= 7 and quantidades[i]<=10:
        print(f"{produtos[i]}: {quantidades[i]} - adequado")
        print(30*("*"))
        item_adequado +=1
        # soma_adequado = int(soma_adequado + produtos[i])
        # produtos_escola.update(produtos[i], quantidades[i])
             
    elif quantidades[i]>=1 and quantidades[i]<=3:
        print(f"{produtos[i]}: {quantidades[i]} - critico")
        print(30*("*"))
        item_criticos +=1
    elif quantidades[i] <=0:
        print(f"{produtos[i]}: {quantidades[i]} - esgotago")
        print(30*("*"))
        item_esgotados +=1


# print(f"soma {soma_adequado}")
# print(f"dici {produtos_escola}")

print(40*("+"))
print(f"Quantidade de produtos adeguados:{item_adequado}")
print(f"Quantidade de produtos cristicos:{item_criticos}")
print(f"Quantidade de produtos esgotados:{item_esgotados}")
print(40*("+"))
# print(adequado)



# Caderno: 10 — adequado
# Caneta: 0 — esgotado
# Borracha: 3 — crítico
# Lápis: 7 — adequado
# Régua: 1 — crítico
# Total de unidades: 21
# Esgotados: 1
# Críticos: 2
# Adequados: 2